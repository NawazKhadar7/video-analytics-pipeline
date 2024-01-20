# bursty-seven

Ingest an unpaced burst across seven streams.

The bounded queue backpressures without losing frames.

Family: bursty. Size: 7. Deterministic seed: 911109.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case bursty-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| produced | equals 84 |
| processed | equals 84 |
| dropped | equals 0 |
| detections | equals 84 |
| accounted | equals true |
| queue_capacity | equals 4 |

Scope: Synthetic boxes and bounded asynchronous queues.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
