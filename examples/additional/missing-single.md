# missing-single

Process periodic missing detections.

Nine detections remain while all twelve frames are processed.

Family: missing. Size: 1. Deterministic seed: 911105.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case missing-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 12 |
| processed | equals 12 |
| dropped | equals 0 |
| detections | equals 9 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
