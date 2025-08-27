# Contributing to Nimbus

Thanks for your interest!

## Dev setup
1. Clone the repo.
2. Duplicate `houdini/packages/nimbus.json.example` → `nimbus.json` and point `path_root` to your local clone.
3. Launch Houdini; you should see a **Nimbus** shelf.

## Code style
- Python: PEP8 (with pragmatic exceptions for Houdini)
- HDA changes: bump version in `CHANGELOG.md` and include a small GIF/screenshot when possible.
- Keep UI strings user‑friendly; long technical notes go in tooltips or docs.

## Submitting a PR
- Describe the problem and solution clearly.
- Add repro steps and test notes.
- For HDA binary updates, include a small demo scene if feasible.
