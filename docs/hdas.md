# HDAs

## Nimbus (OBJ)
- Scene/project metadata
- Env path mapping: `USD`, `CACHE`, `REVIEW`
- Exposes `scene`, `project`, `seq`, `shot`, `artist`

## Nimbus I/O ROP (SOP)
- Extensions: `bgeo.sc`, `vdb`, `abc`, `usd`
- Auto‑version + dropdown sync
- "Save to Disk" and "Submit to Farm"
- Post‑cache hooks

## ROP NimbusCache (/out)
- Orchestrates multi‑stage caches
- Pre/Post scripts (backup hip, email, flipbook, ShotGrid)
- Switch logic driven by SOP extension
