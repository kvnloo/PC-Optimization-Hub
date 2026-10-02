# End-to-end gaming latency lab

This branch treats gaming optimization as a measurement problem, not a tweak list.

## Pipeline

`mouse -> OS/input API -> simulation -> render submit -> GPU -> compositor -> scanout`

Each experiment must isolate one boundary and retain enough raw data to falsify the conclusion.

## Required outputs

- machine/config fingerprint
- workload + exact test duration
- raw trace or CSV
- p50 / p95 / p99 / max
- repeated-run variance
- relevant queue depth / utilization where available
- experiment receipt containing every changed variable

## Work lanes

| Lane | Upstream | First experiment | Promotion |
| --- | --- | --- | --- |
| ETL determinism | `GameTechDev/PresentMon#605` | live capture -> ETL replay -> golden summary | allowed after reproduction |
| metric cross-check | `CXWorld/CapFrameX#367` | CapFrameX vs raw PresentMon under FSO on/off | allowed after reproduction |
| compositor pacing | `ValveSoftware/gamescope#2412` | 144/240/360/480 Hz pacing matrix | downstream only pending AI policy |
| limiter pacing | `flightlessmango/MangoHud#1713` | early/late vs DXVK limiter | downstream only pending AI policy |
| mouse packetization | `RawAccelOfficial/rawaccel#294` | 1/2/4/8 kHz deterministic trace replay | downstream only pending AI policy |
| queue control | `ishitatsuyuki/LatencyFleX` | baseline vs adaptive safety margin | downstream only pending AI policy |
| D3D/Vulkan pacing | `doitsujin/dxvk` | limiter x refresh x VRR matrix | downstream only pending AI policy |
| scheduler effects | `FeralInteractive/gamemode` | baseline vs governor/renice/pinning | downstream only pending AI policy |
| aim workload | `mjohns/FpsAimForge` | event -> simulation -> present markers | downstream only pending AI policy |

## Explicit no-AI upstream lanes

Do not submit AI-assisted issues, comments, code, or pull requests to:

- `libsdl-org/SDL`
- `ppy/osu`

Godot allows restricted AI assistance with disclosure but prohibits fully AI-produced contributions. Treat Godot work from this lab as research-only unless a human independently authors and validates the contribution.

## Experimental rules

1. Change one variable at a time.
2. Warm up before capture.
3. Use repeated A/B/A or A/B/B/A runs when practical.
4. Keep average FPS separate from latency distributions.
5. Never call a software timestamp "input-to-photon" without external display validation.
6. Report regressions even when average FPS improves.
