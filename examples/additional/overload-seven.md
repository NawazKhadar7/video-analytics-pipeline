# overload-seven

Overload the drop-enabled four-frame queue.

Four frames are admitted and eighty are explicitly dropped.

Family: overload. Size: 7. Deterministic seed: 911110.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case overload-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 84 |
| processed | equals 4 |
| dropped | equals 80 |
| detections | equals 4 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
