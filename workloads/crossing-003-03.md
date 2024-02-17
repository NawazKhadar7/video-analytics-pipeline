# crossing-003-03

Track two moving objects on separate lanes.

Input scale: 3; deterministic random seed: 134.
Run `python scripts/demo.py --case workloads/crossing-003-03.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
