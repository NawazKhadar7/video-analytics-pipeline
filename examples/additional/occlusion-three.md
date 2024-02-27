# occlusion-three

Process three streams with synthetic occlusion gaps.

Missing boxes must not become dropped frames.

Family: occlusion. Size: 3. Deterministic seed: 911107.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case occlusion-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 36 |
| processed | equals 36 |
| dropped | equals 0 |
| detections | equals 27 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
