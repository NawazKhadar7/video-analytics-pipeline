# missing-seven

Process seven streams with periodic missing detections.

Sixty-three boxes remain across eighty-four frames.

Family: missing. Size: 7. Deterministic seed: 911106.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case missing-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 84 |
| processed | equals 84 |
| dropped | equals 0 |
| detections | equals 63 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
