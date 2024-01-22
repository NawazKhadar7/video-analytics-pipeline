# bursty-004-04

Exercise queue backpressure with a dense producer burst.

Input scale: 4; deterministic random seed: 228.
Run `python scripts/demo.py --case workloads/bursty-004-04.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
