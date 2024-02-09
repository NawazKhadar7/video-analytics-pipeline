# crossing-seven

Track crossing boxes across seven streams.

All 168 detections are accounted for.

Family: crossing. Size: 7. Deterministic seed: 911104.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case crossing-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 84 |
| processed | equals 84 |
| dropped | equals 0 |
| detections | equals 168 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
