# overload-005-05

Use drop-newest admission and reconcile dropped frames.

Input scale: 5; deterministic random seed: 167.
Run `python scripts/demo.py --case workloads/overload-005-05.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
