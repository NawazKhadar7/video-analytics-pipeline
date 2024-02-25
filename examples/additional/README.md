# Additional scenarios for video-analytics-pipeline

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case steady-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| steady-single | steady | 1 | Process twelve frames from one stream. |
| steady-seven | steady | 7 | Process seven streams with a four-frame queue. |
| crossing-single | crossing | 1 | Track two boxes in one stream. |
| crossing-seven | crossing | 7 | Track crossing boxes across seven streams. |
| missing-single | missing | 1 | Process periodic missing detections. |
| missing-seven | missing | 7 | Process seven streams with periodic missing detections. |
| occlusion-three | occlusion | 3 | Process three streams with synthetic occlusion gaps. |
| bursty-single | bursty | 1 | Ingest one stream without pacing. |
| bursty-seven | bursty | 7 | Ingest an unpaced burst across seven streams. |
| overload-seven | overload | 7 | Overload the drop-enabled four-frame queue. |

Scope: Synthetic boxes and bounded asynchronous queues.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
