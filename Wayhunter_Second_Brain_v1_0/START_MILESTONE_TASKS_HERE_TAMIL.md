# Wayhunter — 70 Milestones + 523 Tasks / Second Brain Add-On (Tamil + Tanglish)

**Date:** 11 November 2026. **Status:** team-planning rebaseline, not approved/implemented code.

## Files you should read in order

1. `knowledge/LATEST_APPROVED_2026-11-11.md` — latest approved game, hazard, Coins and navigation rules (already in original ZIP).
2. `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md` — new 7-member full-stack ownership + how milestone and task status work.
3. `planning/WAYHUNTER_70_MILESTONES.md` — **70 complete milestone descriptions and exit conditions** with original ID mappings.
4. `planning/WAYHUNTER_523_TASKS.md` — **523 line-by-line task actions**, source original task ID, original status, acceptance, original due/estimate, and new owner.
5. `planning/member_briefs/M1_FULLSTACK_MILESTONES_TASKS.md` ... `M7_FULLSTACK_MILESTONES_TASKS.md` — give the relevant member their own file in their own ChatGPT chat.
6. `planning/Wayhunter_70_Milestones_523_Tasks_Aligned.xlsx` — editable team tracking workbook, separate Milestones, Tasks, legacy map, 17 Admin modules, dependencies and decision audit.

## What changed, what did not change?

- The original workbook has **70 legacy milestones, 490 legacy tasks**, **484 Not Started**, **6 Demo - Verify**, **0 accepted**.
- Full-stack modules (M1 identity/social, M2 planning/maps/AI, M3 live/safety/notifications, M4 Hunter/Places, M5 Games, M6 Coins, M7 Home/Ads) were used to reassign **148 of 490 legacy tasks** to a different member. A task with an `M2-...` old ID can now belong to M1 or M3; look at new owner, not original ID.
- A **new 70 milestone baseline** (10 for each member) groups all source tasks. **33 implementation tasks** added to ensure explicit latest rules are fully testable. Total **523 planned tasks**.
- **No original BRD, ERD, architecture PDF, original Excel tracker, source status, or accepted evidence is changed.**
- The original 70 milestone descriptions, prerequisites, status, exit criteria, source references and dates are preserved in the new milestone document/workbook.
- The 20-day slot is **suggested sequencing only**; cross-team contracts and actual ownership should be reviewed; work volume is not equal by task count.
- No assumption that GitHub repositories are built, running or passing tests.

## Directly insert into original Second Brain ZIP

This add-on has the same relative root path:
`SecundBrain/Wayhunter_Second_Brain_v1_0/`

Method A (easy): use `SecundBrain_With_Aligned_Milestone_Tasks_2026-11-11.zip`, which contains the untouched original ZIP entries plus these **new paths**.

Method B (preserve your own local Second Brain changes): extract `Wayhunter_SecondBrain_Milestone_Task_AddOn_2026-11-11.zip`, then **copy only its new files** into the matching folder of your current extracted Second Brain. Don't overwrite any original BRD/PDF/tracker.

## 3-repo workflow

Members work in **3 shared repositories**, not 7 independent repos:
- Flutter: their `lib/features/` implementation and `test/` suite.
- ASP.NET Core Backend + SQL Server EF Core: their module's APIs, entities, migrations and backend tests.
- Angular: their ADM module and Angular tests.

Use `feature/m1-*` through `feature/m7-*` branches and Pull Requests; cross-member API/ledger/auth/safety shared files require affected-owner review. Root scaffolding is team-wide and must not be interpreted as M7 owning business rules.

## Acceptance and status policy

A milestone is **complete only if** all essential full-stack tasks have recorded evidence (tests and PR references), are peer reviewed, and pass acceptance. `Not Started`, `Demo - Verify`, `In Review` or `In Progress` are not Accepted. Never auto-set completion based on source status. Re-baselining the old tracker itself requires member approval. Use `DECISION_REQUIRED` for unresolved product or implementation decisions.

## Important current rules

- Game: one verified winner; +100 Coins winner; +100 approved creator; no creator-self-win; archive when 720h after Admin approval, not delete.
- Hunter: current district + mandatory live 360 and normal photo; Admin approve -> publish; M6 +200 once.
- Hazard: only planned-route within 1 km, active for 24h from server report timestamp, show captured-photo timestamp.
- Coins: 100 welcome; 10,000-Coin sample voucher requires >=10,100 spendable; Pending reserve, Admin Approve debit once; sample voucher QR/code; OCR intake optional.
- Navigation: Home / Selected Module / Contextual Leaderboard / Profile.
- Contract ownership: only M6 changes Coins balances; M3 GPS consent distinct from M1 friendships; M7 doesn't invent KPI source totals.
