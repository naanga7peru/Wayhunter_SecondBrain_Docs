# Second Brain changelog

## v1.0 — 2026-11-11
- Captured three new `naanga7peru` GitHub URLs supplied by the project owner.
- GitHub access check returned 404 for each; code status marked UNVERIFIED, not empty.
- Bundled five existing current documentation references (BRD v2.1, Admin working process v1.1, Flutter architecture v2.1, Angular admin architecture v3.1, ERD v1.1).
- Created repository-specific `AGENTS.md` and context overlays for future Codex usage.
- At initial v1.0 creation these decisions were unresolved: voucher debit, Game winner/expiry, threshold/payout and safety parameters. **Historical log only**; newer resolutions are documented below and in current Rules.
- No GitHub modifications, SQL migrations, API integrations, code execution or production changes performed.

## Rules-only coherence patch — 2026-11-11
- Owner clarified **Game expiry = Expired/Archived**, retained in creator My Games and database; public/playable removed after approval + 30 days. All unrelated Game rules unchanged.
- Resolved stale VCH-DEC-01 instructions across root/hub and three repo overlays: **Admin Approval debits 10,000 once** with **10,100 minimum** and 100 remaining.
- Synchronized portable `ACTIVE_RULES.md` in each repo overlay, added explicit status mapping, new test checklist and 7-member ownership.
- Academic demo scope documented; optional OCR intake distinguished from required demo voucher QR issue.
- Source PDFs preserved byte-for-byte; all three GitHub repos remain unmodified and code remains unverified/not yet developed.
