# Seven members — full-stack module ownership (planning allocation)

**Scope:** Academic Final Project; folder structure and coding have **not started**. This is assignment/coordination, not a business rule or verified implementation. Each member owns Flutter + ASP.NET API + Angular Admin + SQL/EF design + tests for their module. Three separate GitHub repos; no commits are asserted.

| Owner | End-to-end module                       | Admin Module Ownership         | Shared interfaces                                                               |
| ----- | --------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------- |
| M1    | Identity, Profile, Friends              | ADM-01, ADM-03, ADM-17         | UserId, auth/roles, social, audit permissions                                   |
| M2    | Traveler Planning, Maps, AI Trip        | ADM-07                         | Trip drafts, places/routing, historical reuse, Traveler ranking data            |
| M3    | Active Trip, Safety, Notifications      | ADM-08, ADM-09, ADM-16         | Start/Finish sessions, group GPS consent, hazard routes, notifications          |
| M4    | Hunter & Places                         | ADM-04, ADM-06                 | Live 360/photo evidence, duplicate candidates, approval; emits eligible rewards |
| M5    | Games & Leaderboard UI                  | ADM-10                         | Game create/proof, single winner, 30-day archive; ranking display contracts     |
| M6    | Coins, Wallet, Vouchers                 | ADM-11, ADM-12, ADM-13         | Authoritative Coins ledger, holds, approval debit, demo voucher                 |
| M7    | Home, Advertising, Campaigns, Analytics | ADM-02, ADM-05, ADM-14, ADM-15 | Dashboard aggregates, ads/campaigns and reports                                 |

## Cross-module boundaries
- M1 owns identity/auth conventions; no member duplicates token or Admin-role logic.
- M2 owns trip planning; M3 owns live sessions/hazard and safety. They should use separate domain files/subfeatures even if a Flutter `traveller/` area is shared.
- M4 and M5 emit **eligible approved event IDs**; only M6's shared backend Coins service finalizes rewards. Idempotency and one winner rule stay server-authoritative.
- M3 provides notification delivery for other modules. Notification failure does not reverse a committed approval/Coins event.
- M7 displays aggregate source records; it does not hardcode fake business totals as actual data.
- M5 provides common Leaderboard UI contract; M2/M4/M5 own their respective ranking sources.
- Cross-module API contracts must be reviewed by the affected owner(s) before merging.

## Git coordination — proposed, not yet configured
- Initial scaffolding happens **after** agreeing folder structure; do not assume existing routes, controllers or migrations.
- `main` stable; an optional team-selected `develop` branch; isolated `feature/m1-...` to `feature/m7-...` branches; PR review before integration.
- Each PR: requirement ID, feature description, modified files, screenshots when relevant, expected result, tests and known gaps. No secrets in Git.
- Shared 20-day timeline is a **demo target**, not a production delivery guarantee. Avoid unnecessary bank/cash payout, real merchant settlement, mandatory OCR, or enterprise-scale infrastructure.

## Codex prompt pattern
> Read AGENTS.md, docs/second-brain/ACTIVE_RULES.md and CONTEXT.md. Confirm whether repo has any code yet. Propose folders/API contracts for this member and cross-team dependencies before creating code. Do not invent already implemented endpoints.
