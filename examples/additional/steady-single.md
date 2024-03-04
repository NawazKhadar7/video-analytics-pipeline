# steady-single

Process twelve frames from one stream.

The paced producer preserves every frame.

Family: steady. Size: 1. Deterministic seed: 911101.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case steady-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 12 |
| processed | equals 12 |
| dropped | equals 0 |
| detections | equals 12 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
