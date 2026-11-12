# Repository overlay installation (manual / safer)

**Only after repositories are initialized/scaffolded:** Copy from `repo_overlays/angular-admin/` into Angular Admin repo root; from `repo_overlays/flutter-mobile/` into Flutter repo root; from `repo_overlays/aspnet-backend/` into Backend repo root. Include the `docs/second-brain/ACTIVE_RULES.md` file in every repository.

**Important:** If `AGENTS.md`, `docs/second-brain/ACTIVE_RULES.md` or `docs/second-brain/CONTEXT.md` already exists, compare and merge changes instead of overwrite. Commit only after reviewing and choosing a feature branch. Source PDFs are bundled in the hub `sources/`; no need to commit all PDFs to each code repo.

To inspect actual code after cloning:

```powershell
python tools/scan_local_repos.py --admin "C:\\path\\admin" --flutter "C:\\path\\flutter" --backend "C:\\path\\backend" > verified-code-inventory.md
```

The scanner is read-only and does not call the internet. The repository links may remain private.
