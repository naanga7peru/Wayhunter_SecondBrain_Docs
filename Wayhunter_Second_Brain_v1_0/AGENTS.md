# Wayhunter Second Brain — AI / Codex instructions

Read **`knowledge/LATEST_APPROVED_2026-11-11.md` FIRST**, then `START_HERE_TAMIL.md`, `knowledge/SOURCE_OF_TRUTH.md`, `knowledge/PROJECT_RULES.md`, `knowledge/DECISIONS_PENDING.md`, `knowledge/STATUS_DICTIONARY.md`, `knowledge/TEAM_GIT_WORKFLOW.md`, `knowledge/IMPLEMENTATION_STATUS.md`; consult Architecture PDFs afterward. Current owner instruction: Game expiry **archives**, not physical deletion. This is an academic demo before scaffolding/coding.

- Do **not** assume proposed Architecture/ERD tables are implemented. GitHub code must be inspected separately.
- Treat `sources/01_Master_BRD_v2.1.pdf` as the *draft* product baseline; changes require explicit product-owner approval.
- Coins-only system. Never reintroduce HP, RC, XP, or exchange logic.
- Every Hunter new place and Game creation has manual Admin approval; Game player completion reward requires verification.
- Wallet redeem request requires >=10,100 spendable Coins, reserves 10,000; Admin approval deducts 10,000 exactly once, rejection releases hold. See `knowledge/LATEST_APPROVED_2026-11-11.md`.
- Voucher OCR/QR/barcode intake is proposed, not a current confirmed release feature. Manual review and protected source image/PDF intake are documented.
- Preserve the agreed UI flow/design references during future code integration unless requested; no actual new repository UI/files have yet been verified or scaffolded.
- Never leak secrets, private GPS, contacts, unissued voucher codes, or authentication tokens.
- When asked to change code: first identify actual repo/branch/path/line and tests, then propose a minimal patch. Never infer file structure from mockups.
- Maintain evidence states: `SOURCE`, `PROPOSAL`, `CODE_VERIFIED`, `DECISION_REQUIRED`. Always label claims accordingly.
- Avoid direct edits to `main`; work on a feature branch and PR after user authorization.
