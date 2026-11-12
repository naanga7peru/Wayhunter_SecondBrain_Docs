# WAYHUNTER — Second Brain Rules-Only Fix Report (2026-11-11)

**Scope:** Documents and Codex instructions only. No Flutter/Angular/C#/SQL folder creation, no commits, no migration, no application code execution and no business feature changes beyond the user's explicit **Game Archive** clarification.

## Owner decisions now synchronized
| Rule | Authoritative wording | Where corrected |
|---|---|---|
| GAME-DEC-02 | Admin approval → exactly 30 days → remove from public/play; retain Expired/Archived record and creator My Games (no physical deletion) | Latest, PROJECT_RULES, DECISIONS, WORKFLOWS, TESTS, START HERE, 3 repo instructions |
| GAME-DEC-01 | Exactly one verified winner; +100 Coins once | Active Rules, tests, repo instructions |
| VCH-DEC-01 | Pending: reserve 10,000; Admin Approve: debit 10,000 once; reject: release | 3 repo AGENTS/CONTEXT, tests, starter prompt |
| CO-DEC-01 | Requires >=10,100 **spendable** before request, leaves >=100 | Active Rules, tests, repo instructions |
| HAZARD | Only eligible route within 1 km; show photo capture timestamp; active 24h | Active Rules, tests, repo instructions |
| NAV | Home / dynamic selected module / contextual Leaderboard / Profile | Active Rules, tests, repo instructions |
| Voucher | Sample image + unique code + QR **output**; OCR/barcode **intake optional** | Active Rules, demo scope, acceptance tests |

## Other audit gaps addressed without changing logic
- No development/scaffolding yet: documented as **owner-reported**, not verified GitHub fact.
- M1–M7 full-stack responsibilities and ADM-01..17 ownership recorded as **team plan**.
- Display vs backend states described in a **non-binding proposed status map**.
- Voucher issue failure: no double debit, maintain Approved/Unissued for idempotent retry, no automatic refund promise.
- Original five PDFs remain byte-identical as historical/reference sources; active owner rules override specifically noted conflicts.
- Replicated `ACTIVE_RULES.md` in all 3 overlays so Codex does not require a separate Obsidian folder just to see today's owner decisions. `verify_rules_pack.py` checks rules drift and source hashes.

## Still NOT claimed
- No assurance actual repositories contain folders/controllers/DTOs; no tests were executed on project code.
- No new exact admin-role matrix, hazard cooldown seconds or payout mechanism has been invented.
- Archive clarification is the **one direct owner adjustment** to the previous physical-deletion note; all unrelated requirements stay as agreed.

## For the user
1. Unzip and open `SecundBrain/READ_THIS_FIRST_LATEST_2026-11-11.md`.
2. Open `Wayhunter_Second_Brain_v1_0/knowledge/LATEST_APPROVED_2026-11-11.md` (read first).
3. When ready to start repositories, copy each repo's `AGENTS.md`, `CONTEXT.md`, `ACTIVE_RULES.md` into that respective repository.
4. Run `python Wayhunter_Second_Brain_v1_0/tools/verify_rules_pack.py` after future manual edits.
