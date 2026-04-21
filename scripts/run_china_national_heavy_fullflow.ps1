param(
    [string]$RootDir = $(Join-Path 'C:\temp\arcgis_benchmark_data' ("national_heavy_full_{0}" -f (Get-Date -Format 'yyyyMMdd_HHmmss')))
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$py2 = 'C:\Python27\ArcGIS10.8\python.exe'
$py3 = 'C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe'
$analysis = Join-Path $repoRoot 'analyze_results_3way.py'
$runBench = Join-Path $repoRoot 'run_benchmarks.py'
$reportDir = Join-Path $RootDir 'report'

New-Item -ItemType Directory -Path $RootDir -Force | Out-Null
New-Item -ItemType Directory -Path $reportDir -Force | Out-Null

function Invoke-BenchmarkStack {
    param(
        [string]$Name,
        [string]$PythonExe,
        [string[]]$ArgumentList,
        [string]$OutputDir,
        [string]$StdoutLog,
        [string]$StderrLog
    )

    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
    Write-Host ("[{0}] starting..." -f $Name)

    $proc = Start-Process -FilePath $PythonExe `
        -ArgumentList $ArgumentList `
        -WorkingDirectory $repoRoot `
        -RedirectStandardOutput $StdoutLog `
        -RedirectStandardError $StderrLog `
        -PassThru

    $proc.WaitForExit()
    if ($proc.ExitCode -ne 0) {
        throw ("{0} failed with exit code {1}" -f $Name, $proc.ExitCode)
    }

    $resultFile = Get-ChildItem -Path $OutputDir -File -Filter 'benchmark_results*.json' |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $resultFile) {
        throw ("{0} finished but no benchmark_results JSON was found in {1}" -f $Name, $OutputDir)
    }

    return $resultFile.FullName
}

$commonArgs = @(
    $runBench,
    '--region', 'china',
    '--scale', 'national_heavy',
    '--runs', '3',
    '--warmup', '1',
    '--generate-data',
    '--complexity', 'simple'
)

$stackJobs = @(
    @{
        Name = 'py3'
        Python = $py3
        Args = @('-u', $runBench, '--region', 'china', '--scale', 'national_heavy', '--runs', '3', '--warmup', '1', '--generate-data', '--stack', 'arcpy_pro', '--format', 'GDB', '--complexity', 'simple')
    },
    @{
        Name = 'py2'
        Python = $py2
        Args = @('-u', $runBench, '--region', 'china', '--scale', 'national_heavy', '--runs', '3', '--warmup', '1', '--generate-data', '--stack', 'arcpy_desktop', '--format', 'GDB', '--complexity', 'simple')
    },
    @{
        Name = 'os'
        Python = $py3
        Args = @('-u', $runBench, '--region', 'china', '--scale', 'national_heavy', '--runs', '3', '--warmup', '1', '--generate-data', '--stack', 'oss', '--format', 'GPKG', '--complexity', 'simple')
    }
)

foreach ($job in $stackJobs) {
    $stackDir = Join-Path $RootDir $job.Name
    $stdout = Join-Path $stackDir ('{0}.stdout.log' -f $job.Name)
    $stderr = Join-Path $stackDir ('{0}.stderr.log' -f $job.Name)
    $resultFile = Invoke-BenchmarkStack `
        -Name $job.Name `
        -PythonExe $job.Python `
        -ArgumentList $job.Args `
        -OutputDir $stackDir `
        -StdoutLog $stdout `
        -StderrLog $stderr

    $targetName = if ($job.Name -eq 'os') { 'benchmark_results_os.json' } elseif ($job.Name -eq 'py2') { 'benchmark_results_py2.json' } else { 'benchmark_results_py3.json' }
    Copy-Item -LiteralPath $resultFile -Destination (Join-Path $RootDir $targetName) -Force
}

Write-Host '[analysis] generating 3-way report...'
& $py3 -u -X utf8 $analysis --results-dir $RootDir --output-dir $reportDir

Write-Host ('[done] report directory: {0}' -f $reportDir)
