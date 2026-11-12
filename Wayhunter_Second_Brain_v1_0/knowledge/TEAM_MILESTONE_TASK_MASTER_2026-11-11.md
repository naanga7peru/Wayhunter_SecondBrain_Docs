# WAYHUNTER — Second Brain: Member-wise Milestones & Tasks (2026-11-11)

**Purpose:** 7 full-stack module owners; 3 shared GitHub repositories. Separate **Milestones (outcomes)** from **Tasks (actions)** and map every original tracker row. This is a **planning rebaseline for team review**, not a rewrite of business requirements and not evidence of working code.

**Verified input counts:** 70 original milestones, 490 legacy tasks. Updated proposed plan: **70 member-specific milestones (10 each)** and **523 detailed tasks = 490 preserved legacy + 33 new tasks derived from explicitly documented rules**. Original task ID, status, evidence and original deadline remain visible; new task IDs are used for regrouping. Tasks moved between owners are **reassigned in this proposed plan only**, not edited in the original tracker.

**Rules priority:** Read `knowledge/LATEST_APPROVED_2026-11-11.md` before older BRD/architecture/tracker. When uncertain label `DECISION_REQUIRED`, do not invent a rule. Existing 5 PDFs are not modified.

**Completion state:** The original tracker has 484 `Not Started` and 6 `Demo - Verify` tasks, with **0 accepted**; none has been promoted to complete. New plan milestone status is `Planning / Unverified`, regardless of original milestone flags. Member assignments are suggested for team approval. Sprint Day slots are suggestions, not verified deadlines.

**Team ownership:**

| Member | Complete full-stack module | Admin modules | Mapped tasks |
|---|---|---|---:|
| M1 | Identity, Profile, Friends & Settings | ADM-01, ADM-03, ADM-17 | 106 |
| M2 | Traveler Planning, Maps & AI | ADM-07 | 59 |
| M3 | Active Trip, Safety & Notifications | ADM-08, ADM-09, ADM-16 | 69 |
| M4 | Hunter & Places | ADM-04, ADM-06 | 73 |
| M5 | Games, Anti-Cheat & Leaderboard | ADM-10 | 74 |
| M6 | Coins, Wallet & Vouchers | ADM-11, ADM-12, ADM-13 | 75 |
| M7 | Home, Ads, Campaigns & Analytics | ADM-02, ADM-05, ADM-14, ADM-15 | 67 |

**Technology per member:** Flutter screens/services/tests + ASP.NET Core APIs/domain/application + EF Core/SQL entities/migrations + Angular admin module + unit/integration/device/permission tests + GitHub PR proof. M7 may coordinate shared scaffolding/deployment but does **not** own everybody's business logic.

**Read next:** `planning/WAYHUNTER_70_MILESTONES.md` for outcomes and acceptance, then `planning/WAYHUNTER_523_TASKS.md` for detailed actions. Every member also has one standalone `planning/member_briefs/Mx_FULLSTACK_MILESTONES_TASKS.md`. Workbook is `planning/Wayhunter_70_Milestones_523_Tasks_Aligned.xlsx`.

**Required inter-owner contracts:**
- M1 account verification → M6 welcome +100; M1 does not mutate Coins.
- M1 friends & invitations ≠ M3 GPS group sharing consent.
- M2 trip draft, saved routes, place picker and AI → M3 live sessions and hazard matching; M2 reads M4 approved places.
- M3 safety notifications/events are used by other modules; users outside 1-km planned route get no hazard warning. Show hazard photo timestamp; 24h expiry.
- M4 approved Hunter evidence event → M6 +200 only once, after Admin decision.
- M5 Admin-approved Game creator +100 and only one Admin-verified winner +100 → M6 ledger once each. Creator cannot win; game expires 720h after Admin approval and is archived, not deleted.
- M6 10,000 Coin academic voucher requires >=10,100 spendable, Pending reserves, Admin Approve debits once, QR issued after approval; no cash-out, no mandatory voucher intake OCR.
- M7 home navigation `Home / Selected Module / Contextual Leaderboard / Profile`; dashboards use actual events. Each Angular feature still follows its designated ADM owner.

**Repository naming (planned; code status unverified):**
- `Wayhunter_mobile_application_frontend_flutter`: features owned by module.
- `Wayhunter_mobile_application_Backend`: 7 application/domain modules, shared contracts reviewed.
- `Wayhunter_mobile_application_admindashboard_angular`: 17 Admin features, each with one primary member.

**Sources inside original Second Brain:**  
- `knowledge/LATEST_APPROVED_2026-11-11.md` (latest overriding only explicit decisions)
- `knowledge/TEAM_GIT_WORKFLOW.md` (7 full-stack ownership)
- `knowledge/PROJECT_RULES.md` and `knowledge/ADMIN_17_MODULES.md`
- `sources/01_Master_BRD_v2.1.pdf`, `sources/03_Flutter_Architecture_v2.1.pdf`, `sources/04_Angular_Admin_Architecture_v3.1.pdf`
- `Wayhunter_7_Member_Work_Tracker_Dec01_2026.xlsx` (70 historic milestones, 490 tasks)
