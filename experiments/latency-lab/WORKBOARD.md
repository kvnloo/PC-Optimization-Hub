# Gaming latency contribution workboard

Checked 2026-10-01. "Downstream" means experimentation is allowed in our fork/lab, but no upstream AI-assisted issue, comment, code, or PR is posted until the repository policy is explicitly safe.

| Priority | Target | Work item | Status | AI upstream gate |
| --- | --- | --- | --- | --- |
| P0 | FpsAimForge | Mouse event -> dispatch -> update -> GPU submit instrumentation | draft in `kvnloo/FpsAimForge#1` | downstream only; no explicit upstream policy found |
| P0 | PresentMon | P02 full-trace paced-polling determinism reproducer for #662 | draft in `kvnloo/PresentMon#1` | green: repo ships agent guidance |
| P0 | CapFrameX | Optional `MsPCLatency` parser/layout regression baseline | draft in `kvnloo/CapFrameX#1` | green: repo ships `AGENTS.md`, `CLAUDE.md`, MCP/Claude support |
| P0 | threejs-game-skills | Deterministic browser aim-latency profiler + summarizer | draft in `kvnloo/threejs-game-skills#1` | downstream; upstream promotion not yet checked |
| P1 | SparkEngine | Verify real-Present benchmark semantics and exact-SHA replay for #576 | upstream qualification comment posted; code fork still needed | green: project explicitly documents AI-assisted development |
| P1 | gamescope | 144/240/360/480 Hz frame-pacing matrix for #2412 | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | RawAccel | 1/2/4/8 kHz deterministic packetization replay for #294 | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | MangoHud | limiter early/late vs DXVK + metric provenance | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | DXVK | limiter x refresh x VRR pacing matrix | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | LatencyFleX | fixed vs adaptive queue-safety controller | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | GameMode | governor/renice/pinning latency distributions | experiment spec ready | gated: no explicit AI policy confirmed |
| P1 | Unreal_mcp | deterministic input-to-present experiment orchestration | draft in `kvnloo/Unreal_mcp#1` | downstream |
| P1 | GamingPCSetup | reproducible A/B latency baseline protocol | draft in `kvnloo/GamingPCSetup#1` | downstream |
| P1 | FPSWarpDemo | late-warp vs no-warp deterministic experiment | draft in `kvnloo/FPSWarpDemo#1` | downstream |
| P2 | SDL | local 1/2/4/8 kHz relative-mouse timing study | research only | **red: no AI-assisted upstream contributions** |
| P2 | osu! | local input/backend timing study | research only | **red: AI/LLM-aided contributions typically closed/locked** |
| P2 | Godot | frame-pacing/XR evidence collection | research/manual only | restricted: limited disclosed AI assistance; no fully AI-authored contribution |

## Promotion rule

A lane becomes upstream-eligible only when all are true:

1. the repository explicitly permits the assistance mode being used;
2. the result is reproduced, not merely reasoned from code;
3. the smallest relevant test passes;
4. claims distinguish software timing from physical input-to-photon latency;
5. the patch matches the repository's current contribution and test conventions.

"No AI rule found" is not treated as permission.
