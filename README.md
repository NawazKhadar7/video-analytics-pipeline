# Real-Time Multimodal Video Analytics Pipeline

A bounded asynchronous ingestion and tracking reference with explicit overload accounting and event extraction.

## 1. Overview

Video pipelines must account for frames when producers outpace consumers. This reference isolates queue behavior, tracking and alert generation using synthetic bounding boxes, making overload and missing detections easy to reproduce.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Bounded ingestion:** Keeps the frame queue finite and makes backpressure or dropping explicit.
- **Per-camera tracking:** Associates bounding boxes with track IDs using greedy intersection-over-union matching.
- **Event extraction:** Emits synthetic line-region events from tracked object positions.
- **Workload accounting:** Reports produced, processed and dropped frames across steady, crossing, overload and occlusion scenarios.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Execution | Python 3.10+, asyncio queues | Runnable synthetic pipeline |
| Tracking | Bounding-box metadata and IoU matching | Runnable; no trained detector required |
| Optional adapter | OpenCV frame-count adapter | Separate optional path; not a full detection pipeline |

### How the components fit together

Synthetic frame metadata enters a bounded asyncio queue. A metadata detector passes boxes to camera-local trackers; tracked positions produce event JSON. The dashboard displays workload results and accounting metrics.

| Component | Responsibility |
| --- | --- |
| [src/syslab/ingestion.py](src/syslab/ingestion.py) | Producer pacing, bounded queues and drop behavior. |
| [src/syslab/detection.py](src/syslab/detection.py) | Extraction of synthetic detection metadata. |
| [src/syslab/tracker.py](src/syslab/tracker.py) | Camera-local IoU association and track state. |
| [src/syslab/core.py](src/syslab/core.py) | Workload orchestration and event accounting. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Default frames contain synthetic boxes, not images, audio or pretrained detections. There is no YOLO, INT8 inference, Kafka, WebSocket transport or GPU validation. Steady producers yield between frames; burst producers push until backpressure blocks them. IoU matching is greedy and cannot reliably resolve severe occlusion. A finite queue must backpressure or drop under overload.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `video-analytics-pipeline` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **22 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "steady",
  "id": "steady-001-01",
  "seed": 101,
  "size": 1
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/steady-001-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accounted": true,
    "alerts": 1,
    "detections": 12,
    "dropped": 0,
    "processed": 12,
    "produced": 12,
    "queue_capacity": 4
  }
}
```

The one-stream steady case produces and processes 12 frames, drops none and emits one line-region event. The input is synthetic box metadata; this result does not measure real image or audio understanding.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=steady-001-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Bounded ingestion | [src/syslab/ingestion.py](src/syslab/ingestion.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects computer-vision system design with streaming, scheduling and observability. Its useful research angle is the behavior of a pipeline under load, rather than the accuracy of a pretrained detector.

**A question to investigate:** How do dropping and backpressure policies change frame coverage, event continuity and queue behavior during bursts?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
