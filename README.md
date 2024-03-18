# Real-Time Multimodal Video Analytics Pipeline

A bounded asynchronous ingestion and tracking reference with explicit overload accounting and event extraction.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Bounded frame queue, backpressure/drop policies, IoU association, per-camera tracking, synthetic line alerts and an optional OpenCV frame-count adapter.

## Limits and optional runtimes

Default frames contain synthetic boxes, not images, audio or pretrained detections. There is no YOLO, INT8 inference, Kafka, WebSocket transport or GPU validation. Steady producers yield between frames; burst producers push until backpressure blocks them. IoU matching is greedy and cannot reliably resolve severe occlusion. A finite queue must backpressure or drop under overload.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
