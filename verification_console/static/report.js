(function () {
  "use strict";

  var state = {
    report: null,
    tasks: [],
    filtered: [],
    category: "all",
    focus: "all",
    search: "",
    selected: null,
  };

  var order = {
    V1_CreateFishnet: 10,
    V2_CreateRandomPoints: 20,
    V3_Buffer: 30,
    V4_Intersect: 40,
    V5_SpatialJoin: 50,
    R1_CreateConstantRaster: 60,
    R2_Resample: 70,
    R3_Clip: 80,
    M1_PolygonToRaster: 90,
    M2_RasterToPoint: 100,
  };

  var categoryLabelMap = {
    vector: "矢量",
    raster: "栅格",
    mixed: "混合",
  };

  var categoryOptions = [
    { key: "all", label: "全部" },
    { key: "vector", label: "矢量" },
    { key: "raster", label: "栅格" },
    { key: "mixed", label: "混合" },
  ];

  var focusOptions = [
    { key: "all", label: "全部库" },
    { key: "py2", label: "Py2" },
    { key: "py3", label: "Py3" },
    { key: "os", label: "OSS" },
  ];

  var els = {
    statusPill: document.getElementById("status-pill"),
    heroTotalTests: document.getElementById("hero-total-tests"),
    heroPassRate: document.getElementById("hero-pass-rate"),
    heroGenerated: document.getElementById("hero-generated"),
    statPy2Fast: document.getElementById("stat-py2-fast"),
    statPy3Fast: document.getElementById("stat-py3-fast"),
    statOsFast: document.getElementById("stat-os-fast"),
    statPy3VsPy2: document.getElementById("stat-py3-vs-py2"),
    statOsVsPy2: document.getElementById("stat-os-vs-py2"),
    taskSearch: document.getElementById("task-search"),
    categoryFilters: document.getElementById("category-filters"),
    stackFocus: document.getElementById("stack-focus"),
    tbody: document.getElementById("task-tbody"),
    detailTitle: document.getElementById("detail-title"),
    detailMeta: document.getElementById("detail-meta"),
    detailPy2: document.getElementById("detail-py2"),
    detailPy3: document.getElementById("detail-py3"),
    detailOs: document.getElementById("detail-os"),
    detailFastest: document.getElementById("detail-fastest"),
    detailConclusion: document.getElementById("detail-conclusion"),
    fastestBars: document.getElementById("fastest-bars"),
  };

  function apiGet(path) {
    return fetch(path, { cache: "no-store" }).then(function (res) {
      if (!res.ok) {
        throw new Error("GET " + path + " failed: " + res.status);
      }
      return res.json();
    });
  }

  function formatSeconds(value) {
    if (typeof value !== "number" || isNaN(value)) {
      return "-";
    }
    return value.toFixed(2) + " s";
  }

  function formatRatio(value) {
    if (typeof value !== "number" || !isFinite(value)) {
      return "-";
    }
    return value.toFixed(2) + "x";
  }

  function formatDate(value) {
    if (!value) {
      return "-";
    }
    try {
      return new Date(value).toLocaleString("zh-CN", { hour12: false });
    } catch (err) {
      return value;
    }
  }

  function categoryLabel(value) {
    return categoryLabelMap[value] || value;
  }

  function sortTasks(items) {
    return items.slice().sort(function (a, b) {
      var pa = order[a.test_name] || 9999;
      var pb = order[b.test_name] || 9999;
      if (pa !== pb) {
        return pa - pb;
      }
      return String(a.test_name).localeCompare(String(b.test_name));
    });
  }

  function fastestBadge(task) {
    var fastest = task.fastest || "";
    if (fastest.indexOf("Open") === 0) {
      return '<span class="badge badge-os">Open-Source</span>';
    }
    if (fastest.indexOf("Python 3") === 0 || fastest === "Python 3.x") {
      return '<span class="badge badge-py3">Py3</span>';
    }
    if (fastest.indexOf("Python 2") === 0 || fastest === "Python 2.7") {
      return '<span class="badge badge-py2">Py2</span>';
    }
    return '<span class="badge badge-fast">' + fastest + "</span>";
  }

  function buildFilters() {
    els.categoryFilters.innerHTML = "";
    categoryOptions.forEach(function (option) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "pill" + (state.category === option.key ? " active" : "");
      button.textContent = option.label;
      button.dataset.category = option.key;
      button.addEventListener("click", function () {
        state.category = option.key;
        render();
      });
      els.categoryFilters.appendChild(button);
    });

    els.stackFocus.innerHTML = "";
    focusOptions.forEach(function (option) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "toggle" + (state.focus === option.key ? " active" : "");
      button.textContent = option.label;
      button.dataset.focus = option.key;
      button.addEventListener("click", function () {
        state.focus = option.key;
        render();
      });
      els.stackFocus.appendChild(button);
    });
  }

  function matches(task) {
    var byCategory = state.category === "all" || task.category === state.category;
    var q = state.search.trim().toLowerCase();
    var bySearch = !q || String(task.test_name).toLowerCase().indexOf(q) >= 0 || String(task.category).toLowerCase().indexOf(q) >= 0;
    return byCategory && bySearch;
  }

  function computeTotals(tasks) {
    var totals = {
      py2: 0,
      py3: 0,
      os: 0,
      count: tasks.length,
      passed: 0,
      fastest: { py2: 0, py3: 0, os: 0 },
    };

    tasks.forEach(function (task) {
      totals.py2 += task.py2_time || 0;
      totals.py3 += task.py3_time || 0;
      totals.os += task.os_time || 0;
      if (task.py2_success && task.py3_success && task.os_success) {
        totals.passed += 1;
      }
      var fastest = task.fastest || "";
      if (fastest.indexOf("Open") === 0) {
        totals.fastest.os += 1;
      } else if (fastest.indexOf("Python 3") === 0) {
        totals.fastest.py3 += 1;
      } else {
        totals.fastest.py2 += 1;
      }
    });

    return totals;
  }

  function taskSummary(task) {
    var pieces = [];
    pieces.push("Py2 " + formatSeconds(task.py2_time) + " / Py3 " + formatSeconds(task.py3_time) + " / OSS " + formatSeconds(task.os_time));
    pieces.push("Py3 vs Py2 " + formatRatio(task.py3_speedup));
    pieces.push("OSS vs Py2 " + formatRatio(task.os_speedup));
    return pieces.join(" · ");
  }

  function renderRows(tasks) {
    els.tbody.innerHTML = "";
    tasks.forEach(function (task) {
      var tr = document.createElement("tr");
      tr.dataset.testName = task.test_name;
      tr.className = state.selected && state.selected.test_name === task.test_name ? "selected" : "";
      tr.innerHTML = [
        '<td><div class="task-name"><strong>' + task.test_name + '</strong><span>' + categoryLabel(task.category) + '</span></div></td>',
        '<td>' + categoryLabel(task.category) + "</td>",
        '<td class="num col-py2">' + formatSeconds(task.py2_time) + '</td>',
        '<td class="num col-py3">' + formatSeconds(task.py3_time) + '</td>',
        '<td class="num col-os">' + formatSeconds(task.os_time) + '</td>',
        '<td>' + fastestBadge(task) + '</td>',
        '<td class="num">' + formatRatio(task.py3_speedup) + '</td>',
        '<td class="num">' + formatRatio(task.os_speedup) + '</td>',
      ].join("");
      tr.addEventListener("click", function () {
        state.selected = task;
        renderSelection();
      });
      els.tbody.appendChild(tr);
    });
  }

  function renderSelection() {
    var rows = els.tbody.querySelectorAll("tr");
    Array.prototype.forEach.call(rows, function (row) {
      row.classList.toggle("selected", state.selected && row.dataset.testName === state.selected.test_name);
    });

    if (!state.selected) {
      return;
    }

    var task = state.selected;
    els.detailTitle.textContent = task.test_name;
    els.detailMeta.textContent = categoryLabel(task.category) + " · 通过: " + [task.py2_success, task.py3_success, task.os_success].filter(Boolean).length + "/3 · " + taskSummary(task);
    els.detailPy2.textContent = formatSeconds(task.py2_time) + " / σ " + formatSeconds(task.py2_std);
    els.detailPy3.textContent = formatSeconds(task.py3_time) + " / σ " + formatSeconds(task.py3_std);
    els.detailOs.textContent = formatSeconds(task.os_time) + " / σ " + formatSeconds(task.os_std);
    els.detailFastest.textContent = fastestLabel(task.fastest);
    els.detailConclusion.textContent = buildConclusion(task);
  }

  function fastestLabel(value) {
    if (!value) {
      return "-";
    }
    if (value.indexOf("Open") === 0) {
      return "Open-Source";
    }
    if (value.indexOf("Python 3") === 0) {
      return "Py3";
    }
    if (value.indexOf("Python 2") === 0) {
      return "Py2";
    }
    return value;
  }

  function buildConclusion(task) {
    var fastest = fastestLabel(task.fastest);
    var winnerTime = task.os_time;
    if (fastest === "Py2") {
      winnerTime = task.py2_time;
    } else if (fastest === "Py3") {
      winnerTime = task.py3_time;
    }

    return fastest + " 在这个任务里最快，用时 " + formatSeconds(winnerTime) + "。Py3 相比 Py2 是 " + formatRatio(task.py3_speedup) + "，OSS 相比 Py2 是 " + formatRatio(task.os_speedup) + "。";
  }

  function renderBars(stats) {
    var total = stats.total_tests || 1;
    var items = [
      { key: "py2", label: "Py2", value: stats.py2_faster || 0, className: "py2" },
      { key: "py3", label: "Py3", value: stats.py3_faster || 0, className: "py3" },
      { key: "os", label: "Open-Source", value: stats.os_faster || 0, className: "os" },
    ];

    els.fastestBars.innerHTML = "";
    items.forEach(function (item) {
      var row = document.createElement("div");
      row.className = "bar-row";
      row.innerHTML = [
        '<div class="bar-row-head"><span>' + item.label + '</span><strong>' + item.value + "/" + total + "</strong></div>",
        '<div class="bar-track"><div class="bar-fill ' + item.className + '" style="width: 0%"></div></div>',
      ].join("");
      els.fastestBars.appendChild(row);
      requestAnimationFrame(function () {
        var fill = row.querySelector(".bar-fill");
        if (fill) {
          fill.style.width = Math.max(6, (item.value / total) * 100) + "%";
        }
      });
    });
  }

  function renderStats(report) {
    var stats = report.statistics || {};
    var tasks = state.tasks;
    var totals = computeTotals(tasks);
    var successRate = totals.count ? Math.round((totals.passed / totals.count) * 100) : 0;

    els.statusPill.textContent = successRate === 100 ? "10/10 全绿" : successRate + "% 通过";
    els.heroTotalTests.textContent = stats.total_tests || tasks.length || "-";
    els.heroPassRate.textContent = successRate + "%";
    els.heroGenerated.textContent = formatDate(report.generated);
    els.statPy2Fast.textContent = (stats.py2_faster || 0) + " 项";
    els.statPy3Fast.textContent = (stats.py3_faster || 0) + " 项";
    els.statOsFast.textContent = (stats.os_faster || 0) + " 项";
    els.statPy3VsPy2.textContent = formatRatio(stats.py3_vs_py2_avg);
    els.statOsVsPy2.textContent = formatRatio(stats.os_vs_py2_avg);

    document.title = "中国 OSM 全国包三方性能报告 - " + stats.total_tests + " 项";
    renderBars(stats);
  }

  function render() {
    if (!state.report) {
      return;
    }

    buildFilters();

    var tasks = sortTasks(state.report.comparison || []).filter(matches);
    state.filtered = tasks;

    if (!state.selected || tasks.indexOf(state.selected) === -1) {
      state.selected = tasks.length ? tasks[0] : null;
    }

    els.tbody.parentNode.parentNode.className = "panel main-panel " + (state.focus === "all" ? "" : "focus-" + state.focus);
    renderRows(tasks);
    renderSelection();
    renderStats(state.report);
  }

  function bindEvents() {
    els.taskSearch.addEventListener("input", function (event) {
      state.search = event.target.value || "";
      render();
    });
  }

  function init(report) {
    state.report = report;
    state.tasks = sortTasks(report.comparison || []);
    bindEvents();
    render();
  }

  function showError(err) {
    els.statusPill.textContent = "加载失败";
    els.heroPassRate.textContent = "-";
    els.heroGenerated.textContent = "-";
    els.heroTotalTests.textContent = "-";
    els.taskSearch.disabled = true;
    els.tbody.innerHTML = '<tr><td colspan="8">无法加载报告数据：' + (err && err.message ? err.message : String(err)) + "</td></tr>";
    els.detailTitle.textContent = "报告未加载";
    els.detailMeta.textContent = "请确认 /api/report 可正常访问。";
    els.detailConclusion.textContent = "报告数据加载失败。";
  }

  apiGet("/api/report").then(function (payload) {
    if (!payload || !payload.ok || !payload.report) {
      throw new Error((payload && payload.error) || "Invalid report payload");
    }
    init(payload.report);
  }).catch(showError);
})();
