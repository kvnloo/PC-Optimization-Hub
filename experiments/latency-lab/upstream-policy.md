# Upstream AI contribution gate

Checked 2026-10-01.

## Green: AI tooling is explicitly represented in-repo

### PresentMon

`GameTechDev/PresentMon` contains `AGENTS.md` with coding and testing instructions for agents. Contributions still require normal validation and DCO sign-off.

### CapFrameX

`CXWorld/CapFrameX` contains `AGENTS.md`, `CLAUDE.md`, and first-class MCP/Claude integration in its README.

## Red: do not submit AI-assisted upstream contributions

### SDL

`libsdl-org/SDL/AGENTS.md` explicitly says generative AI must not be used to generate code for contributions and asks contributors not to submit AI-generated comments or code.

### osu!

`ppy/osu/CONTRIBUTING.md` says contributions created, documented, or aided by AI/LLMs will typically be closed and locked.

## Restricted

### Godot

Godot discourages AI assistance, prohibits contributions made entirely by AI, requires understanding/review, and requires disclosure when AI assists a contribution. AI-written proposals are not allowed.

## Unknown / downstream-only

No explicit project-level permission was found during the policy scan for:

- `ValveSoftware/gamescope`
- `flightlessmango/MangoHud`
- `RawAccelOfficial/rawaccel`
- `ishitatsuyuki/LatencyFleX`
- `doitsujin/dxvk`
- `FeralInteractive/gamemode`
- `mjohns/FpsAimForge`

Absence of a ban is not treated as permission. Research may proceed in this fork, but upstream posting is gated on a clear maintainer-safe policy.
