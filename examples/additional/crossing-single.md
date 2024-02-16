# crossing-single

Track two boxes in one stream.

Twelve frames contain twenty-four detections.

Family: crossing. Size: 1. Deterministic seed: 911103.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case crossing-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 12 |
| processed | equals 12 |
| dropped | equals 0 |
| detections | equals 24 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
