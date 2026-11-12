# M7 — Home, Ads, Campaigns & Analytics: 10 milestones & 67 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-02, ADM-05, ADM-14, ADM-15. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

### M7-MS01 — Home cinematic UI, three cards and dynamic navigation

**Milestone deliverable:** Home image/navigation work across device sizes
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 6 (5 legacy / 1 new).
**Original milestone references:** M1-MS05, M7-MS04 | **Original target weeks:** 2

- [ ] **M7-MS01-T01** [Mobile] Flutter shared theme மற்றும் responsive shell உருவாக்கு
  - **Acceptance:** Traveler blue, Hunter gold, Game purple styles ஒரே component system-ல் இருக்கும்.
  - **Trace:** `M1-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS01-T02** [Mobile] Home greeting, avatar, search மற்றும் module cards இணை
  - **Acceptance:** Backend user data மற்றும் approved navigation routes காட்டப்படும்.
  - **Trace:** `M1-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS01-T03** [Mobile] Global leaderboard visibility rules செயல் படுத்து
  - **Acceptance:** Home/Profile/Friends/Wallet-ல் shortcut மறைக்கப்படும்; module boards accessible.
  - **Trace:** `M1-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M7-MS01-T04** [QA] Small-screen, denied, empty மற்றும் retry நிலைகள் சோதனை
  - **Acceptance:** மூன்று மொழிகளிலும் Home/navigation acceptance screenshots இருக்கும்.
  - **Trace:** `M1-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS01-T05** [Mobile] Live banner rotation/refresh, visibility மற்றும் disposal சரிபார்
  - **Acceptance:** Baseline 3s rotation/15s refresh configurable ஆகும். Hidden tab/rebuild extra impression அனுப்பாது; timers dispose ஆகும்; pause/archive மற்றும் provider failure reflect ஆகும்.
  - **Trace:** `M7-MS04-T04` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.1,3,5: LiveAdvertisementBanner exists in
Home. Background visibility future work. M1 owns Home
shell/fallback; M7 owns widget behavior and required
module placements.
- [ ] **M7-MS01-T06** [Mobile] Enforce Home / Selected Module / Contextual Leaderboard / Profile navigation
  - **Acceptance:** Second tab reflects selected Traveler/Hunter/Game; context leaderboard changes
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M7-MS02 — Advertisement CMS, home banner and AdMob demo adapter

**Milestone deliverable:** 3-second ad banner, safe URLs, admin upload, refresh validated
**Proposed sprint days:** 03-04 | **Dependencies:** M7-MS01; M1-MS04 | **Task count:** 7 (6 legacy / 1 new).
**Original milestone references:** M1-MS05, M7-MS04 | **Original target weeks:** 2

- [ ] **M7-MS02-T01** [Mobile] Existing live Home banner-ஐ verify செய்து fallback இணை
  - **Acceptance:** Active ads Home-ல் load ஆகும். API/image failure navigation-ஐ தடுக்காது; empty/retry states மற்றும் sponsor label சோதிக்கப்படும்.
  - **Trace:** `M1-MS05-T06` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.1,3: Home live widget, 3s rotation, 15s
refresh reported. Source branch run செய்யவில்லை;
M7-MS04-T04 உடன் verify செய்யவும்.
- [ ] **M7-MS02-T02** [Data] Demo JSON ads data-ஐ SQL Server / EF Core-க்கு மாற்று
  - **Acceptance:** Ads, placements, schedules, status, counters மற்றும் image references SQL-ல் persist ஆகும். Restart மற்றும் migration/seed checks pass ஆகும்.
  - **Trace:** `M7-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.3-5: local JSON + uploads only. SQL
migration புதிய வேலை; source commits demo
records/images கொண்டிருக்கவில்லை.
- [ ] **M7-MS02-T03** [API] Existing Ads API-ஐ verify செய்து JWT/RBAC மற்றும் safe URLs இணை
  - **Acceptance:** Admin create/edit/status/upload writes unauthorized users-க்கு மறுக்கப்படும். Active query dates/district/placement validate செய்யும்; unsafe ad URLs reject ஆகும்.
  - **Trace:** `M7-MS04-T02` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.3-5: list/active/create/status/upload
endpoints reported; production auth இல்லை. Edit
behavior, targeting, allowed URLs மற்றும் roles-ஐ
நிறைவு செய்யவும்.
- [ ] **M7-MS02-T04** [Admin] Admin Ads flow-ஐ verify செய்து secure Cloudinary upload இணை
  - **Acceptance:** Create/edit/preview, sponsor, dates/district, Activate/Pause/Archive வேலை செய்யும். Authorized signed Cloudinary upload type/content/size checks pass ஆகும்.
  - **Trace:** `M7-MS04-T03` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide p.3: Admin create/upload/status/metrics;
zoneless markForCheck fix reported. JPEG/PNG/WebP <=5
MB local upload only; Cloudinary, validation
hardening மற்றும் secret handling மீதம்.
- [ ] **M7-MS02-T05** [Ops] AdMob test adapter மற்றும் provider readiness தனியாகப் பதிவு செய்
  - **Acceptance:** D16 approval/access கிடைத்தால் test adapter மற்றும் consent validate செய்யப்படும். Custom sponsored banner demo-ஐ AdMob integration எனக் குறிக்கக்கூடாது.
  - **Trace:** `M7-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide custom sponsor Ads API-ஐ மட்டுமே
விவரிக்கிறது. AdMob access/integration/earnings இதில்
உறுதிப்படுத்தப்படவில்லை; original planned task
தொடர்கிறது.
- [ ] **M7-MS02-T06** [QA] Fresh clone மற்றும் Ads end-to-end regression சோதனை செய்
  - **Acceptance:** New ad/image create → activate → Home rotate → counts → pause/archive pass. Expiry, invalid upload, outage, unauthorized write மற்றும் hidden-tab cases evidence உடன் pass ஆகும்.
  - **Trace:** `M7-MS04-T07` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.2,4-5: local end-to-end test reported.
Fresh clone-ல் old demo records/images வராது;
fixtures recreate செய்யவும். Full regression/peer
review இன்னும் தேவை.
- [ ] **M7-MS02-T07** [QA] Validate 3-second banner rotation, disposal and empty-campaign fallback
  - **Acceptance:** Home remains functional without active ads or network connectivity
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M7-MS03 — Campaign CRUD, district targeting and lifecycle

**Milestone deliverable:** Campaign schedule/district/availability policy consistently applied
**Proposed sprint days:** 05-06 | **Dependencies:** M7-MS02; M1-MS04 | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M7-MS05 | **Original target weeks:** 2

- [ ] **M7-MS03-T01** [Data] Campaign type, sponsor, audience மற்றும் budget schema உருவாக்கு
  - **Acceptance:** Sponsored game/place/mission/district-pass configuration references இருக்கும்.
  - **Trace:** `M7-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M7-MS03-T02** [API] Campaign draft/schedule/publish/archive endpoints உருவாக்கு
  - **Acceptance:** Invalid dates, budget மற்றும் unauthorized state changes மறுக்கப்படும்.
  - **Trace:** `M7-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS03-T03** [Admin] Campaign editor மற்றும் sponsor/content preview உருவாக்கு
  - **Acceptance:** Dates, audience, Coins budget மற்றும் disclosure காட்டப்படும்.
  - **Trace:** `M7-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS03-T04** [API] Budget cap மற்றும் duplicate reward-source prevention செய்
  - **Acceptance:** Sponsored attribution கூடுதல் duplicate Coin credit உருவாக்காது.
  - **Trace:** `M7-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS03-T05** [Admin] Campaign performance மற்றும் status monitor உருவாக்கு
  - **Acceptance:** Actual views/actions/spend totals மற்றும் archive controls இருக்கும்.
  - **Trace:** `M7-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M7-MS03-T06** [QA] Expired campaign மற்றும் reward-budget edge tests செய்
  - **Acceptance:** Over-budget/disabled content campaign-ல் active ஆகாது.
  - **Trace:** `M7-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.

### M7-MS04 — Admin dashboard KPI cards and authoritative aggregates

**Milestone deliverable:** Dashboard figures reconcile with source service records
**Proposed sprint days:** 07-08 | **Dependencies:** M7-MS03 | **Task count:** 8 (8 legacy / 0 new).
**Original milestone references:** M7-MS03, M7-MS07 | **Original target weeks:** 2, 3

- [ ] **M7-MS04-T01** [API] Users/places/games/trips count contracts இணை
  - **Acceptance:** Each domain aggregate definition மற்றும் status eligibility documented.
  - **Trace:** `M7-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T02** [API] Pending Hunter/Game/Coins queues aggregate உருவாக்கு
  - **Acceptance:** Queue counts matching domain list queries-க்கு பொருந்தும்.
  - **Trace:** `M7-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T03** [API] Coins balance/liability and stock summary adapter இணை
  - **Acceptance:** Authoritative ledger values; arbitrary manual balance editing இல்லை.
  - **Trace:** `M7-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T04** [Admin] Dashboard cards மற்றும் pending queue shortcuts உருவாக்கு
  - **Acceptance:** Click correct filtered queue-க்கு செல்லும்; no misleading mock live values.
  - **Trace:** `M7-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T05** [Admin] Activity map மற்றும் district/time filters உருவாக்கு
  - **Acceptance:** Aggregated privacy-safe location data மட்டும் காட்டப்படும்.
  - **Trace:** `M7-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T06** [Admin] Loading/empty/error/last-refresh states செய்
  - **Acceptance:** API failure zero activity என்று தவறாகக் காட்டப்படாது.
  - **Trace:** `M7-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M7-MS04-T07** [QA] Seeded records மற்றும் dashboard reconciliations சோதனை
  - **Acceptance:** Known seed totals, zero data மற்றும் failed provider cases evidence இருக்கும்.
  - **Trace:** `M7-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS04-T08** [API] Ledger/approval/activity aggregates domain owners-இடம் இணை
  - **Acceptance:** Reward liability, reserved/debited மற்றும் pending counts consistent ஆகும்.
  - **Trace:** `M7-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.

### M7-MS05 — Admin Reports, analytics, safe CSV/PDF export

**Milestone deliverable:** Date/district role-based reports; export injection safe
**Proposed sprint days:** 09-10 | **Dependencies:** M7-MS04 | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M7-MS07 | **Original target weeks:** 3

- [ ] **M7-MS05-T01** [API] Date/district/status analytics filters மற்றும் metric definitions உருவாக்கு
  - **Acceptance:** Completed trips, approved hunts/games, Coins மற்றும் hazards definitions documented.
  - **Trace:** `M7-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS05-T02** [Admin] Report charts, tables மற்றும் drilldown உருவாக்கு
  - **Acceptance:** Summary total-இலிருந்து authorized source records திறக்க முடியும்.
  - **Trace:** `M7-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS05-T03** [API] CSV export மற்றும் formula-injection escaping செய்
  - **Acceptance:** User-entered formula-like text executable spreadsheet formula ஆக export ஆகாது.
  - **Trace:** `M7-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS05-T04** [API] PDF report export மற்றும் role-filtered fields அமை
  - **Acceptance:** Selected filters reflected; private GPS/OTP/secrets export ஆகாது.
  - **Trace:** `M7-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS05-T05** [Admin] Report period, empty/error மற்றும் export feedback செய்
  - **Acceptance:** No-data மற்றும் failed query வேறுபட்டு தெரியும்; dates/timezone labelled.
  - **Trace:** `M7-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M7-MS05-T06** [QA] Aggregate totals மற்றும் export permission tests செய்
  - **Acceptance:** Known ledger/trip records-க்கு totals reconcile; wrong role export reject.
  - **Trace:** `M7-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.

### M7-MS06 — Sponsored Places/POIs and map-ad integration

**Milestone deliverable:** Sponsored POI integrates with M2 without corrupting place results
**Proposed sprint days:** 11-12 | **Dependencies:** M7-MS02; M2-MS03; M4-MS08 | **Task count:** 4 (1 legacy / 3 new).
**Original milestone references:** M7-MS05 | **Original target weeks:** 2

- [ ] **M7-MS06-T01** [API] Linked game/place eligibility checks இணை
  - **Acceptance:** Campaign publication Hunter/Game manual approval-ஐ bypass செய்யாது.
  - **Trace:** `M7-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS06-T02** [Mobile] Add route-time/district campaign filter to sponsored POIs without automatic suggestion changes
  - **Acceptance:** Only active eligible targeted sponsored cards shown; no fake provider locations
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M7-MS06-T03** [API] Integrate M7 sponsored placement records into M2 place/map cards with visible sponsorship labels
  - **Acceptance:** Sponsored locations are labeled; source approved-place records remain unchanged
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M7-MS06-T04** [QA] Test expired, deleted, or unpublished ad-to-place references
  - **Acceptance:** Unavailable campaigns/places cannot be promoted
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M7-MS07 — Impression/click events and reporting reconciliation

**Milestone deliverable:** Views/clicks dedupe and trend checks pass source totals
**Proposed sprint days:** 13-14 | **Dependencies:** M7-MS02; M7-MS04 | **Task count:** 4 (1 legacy / 3 new).
**Original milestone references:** M7-MS04 | **Original target weeks:** 2

- [ ] **M7-MS07-T01** [API] Impression/click counters-க்கு dedup, rate limits மற்றும் aggregation சேர்
  - **Acceptance:** Retry/replayed events counters inflate செய்யாது. Rate limits tested; aggregated counts reconcile. Views = impressions என்று label செய்யப்படும்; unique users எனக் காட்டாது.
  - **Trace:** `M7-MS04-T05` | Original status: `Demo - Verify` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.3-5: visible/rotated ad and tap POST
counters; consecutive same-ad refresh dedup only.
Cross-event dedup, abuse control மற்றும் analytics
aggregation மீதம்.
- [ ] **M7-MS07-T02** [API] Keep view and click events independently deduplicated for reporting
  - **Acceptance:** Ad dashboard counts reconcile with accepted source events
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M7-MS07-T03** [Data] Provide source event ID and campaign ID for audit/report drilldown
  - **Acceptance:** Metrics auditable to campaign/impression/click records
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M7-MS07-T04** [QA] Test district-targeted ad analytics and denied-location fallback
  - **Acceptance:** Unknown district not guessed; targeting rules clearly applied
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M7-MS08 — Admin shell, shared widgets and cross-owner integration

**Milestone deliverable:** 17 admin routes reachable with M1 RBAC; shared components reused
**Proposed sprint days:** 15-16 | **Dependencies:** M1-MS04; M7-MS09 | **Task count:** 4 (2 legacy / 2 new).
**Original milestone references:** M7-MS02 | **Original target weeks:** 1

- [ ] **M7-MS08-T01** [Admin] Angular sidebar/layout மற்றும் module routes உருவாக்கு
  - **Acceptance:** 17 admin areas owner stubs/routes documented; responsive shell இருக்கும்.
  - **Trace:** `M7-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS08-T02** [Admin] Shared table/filter/dialog/approval components உருவாக்கு
  - **Acceptance:** UserId/name, reference, reason மற்றும் status pattern reusable ஆகும்.
  - **Trace:** `M7-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS08-T03** [Ops] Define shared Angular shell route and widget ownership before feature module merges
  - **Acceptance:** Every feature module compiles under stable shell and role guards
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M7-MS08-T04** [QA] Run M1 auth / M7 navigation / 17 admin routes integration smoke tests
  - **Acceptance:** Routes protected; each owned module reachable for correct roles
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M7-MS09 — Shared repo scaffolding, CI and staging coordination

**Milestone deliverable:** Three repos build/test on clean checkout; no API secrets committed
**Proposed sprint days:** 17-18 | **Dependencies:** M1-MS01 | **Task count:** 15 (15 legacy / 0 new).
**Original milestone references:** M7-MS01, M7-MS08, M7-MS09 | **Original target weeks:** 1, 3

- [ ] **M7-MS09-T01** [Ops] Current repository/folder structure மற்றும் demo inventory பதிவு செய்
  - **Acceptance:** Actual Flutter/Angular/API paths மற்றும் demo-vs-complete inventory documented.
  - **Trace:** `M7-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.1-2: three feature/live-advertisements
branches; Flutter 3d67c29, Admin fb1426e, API
618a9f0. PDF-reported refs only. Existing tracker
baseline inventory-ல் இவற்றை verify செய்து
சேர்க்கவும்; no PR/merge reported.
- [ ] **M7-MS09-T02** [Ops] Git develop/feature workflow மற்றும் PR ownership அமை
  - **Acceptance:** Each module owner, reviewer, branch naming மற்றும் merge checks agreed.
  - **Trace:** `M7-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T03** [Data] SQL/EF migration coordination மற்றும் seed strategy அமை
  - **Acceptance:** Per-module migration ownership மற்றும் conflict-free integration order documented.
  - **Trace:** `M7-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T04** [Ops] Local environment templates மற்றும் health checks உருவாக்கு
  - **Acceptance:** Secrets இன்றி env examples; Flutter/Admin/API health smoke run pass.
  - **Trace:** `M7-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T05** [API] Shared media, event/outbox மற்றும் config interfaces ஒப்பந்தம் செய்
  - **Acceptance:** M2/M4/M5/M6 contracts implement செய்யக்கூடிய reference interfaces கிடைக்கும்.
  - **Trace:** `M7-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T06** [Ops] CI build/lint/test baseline மற்றும் branch checks அமை
  - **Acceptance:** Pull request-ல் three-project builds/required checks இயங்கும்.
  - **Trace:** `M7-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T07** [Ops] Provider health, quota/budget மற்றும் error monitoring அமை
  - **Acceptance:** Maps/AI/media/OTP/FCM health failures visible; secrets redacted.
  - **Trace:** `M7-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide p.5 future work: Ads API failures,
rate-limit counters, suspicious event spikes, upload
failures மற்றும் production hosting health-ஐ
monitoring-ல் சேர்க்கவும்.
- [ ] **M7-MS09-T08** [Ops] Log retention, secret rotation மற்றும் incident steps எழுது
  - **Acceptance:** Role access, retention durations மற்றும் recovery owners documented.
  - **Trace:** `M7-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T09** [Ops] Staging environment மற்றும் HTTPS configuration அமை
  - **Acceptance:** Flutter/Admin/API approved environment-ல் correct base URLs பயன்படுத்தும்.
  - **Trace:** `M7-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T10** [Ops] Build pipeline மற்றும் migration deployment sequence அமை
  - **Acceptance:** Reproducible artifact, migration check மற்றும் version metadata இருக்கும்.
  - **Trace:** `M7-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T11** [Ops] Secrets store, CORS மற்றும் restricted key setup சோதனை
  - **Acceptance:** Wildly permissive production config இல்லை; secrets bundles/logs-ல் இல்லை.
  - **Trace:** `M7-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T12** [Ops] SQL backup மற்றும் protected media retention workflow அமை
  - **Acceptance:** Backup access/retention owner-defined; recovery inputs documented.
  - **Trace:** `M7-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T13** [Ops] Isolated restore rehearsal மற்றும் rollback plan நடத்து
  - **Acceptance:** Restored DB counts/ledger references match; rollback steps evidence இருக்கும்.
  - **Trace:** `M7-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.
- [ ] **M7-MS09-T14** [QA] Staging smoke, performance baseline மற்றும் provider outage check செய்
  - **Acceptance:** Measured timings/limits recorded; agreed release target unmet என்றால் open issue இருக்கும்.
  - **Trace:** `M7-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS09-T15** [Ops] Ads branch setup உட்பட local/staging run guide புதுப்பி
  - **Acceptance:** Three branch clones, API 5055/Admin 4200/Flutter 5500 run order, new demo data seed மற்றும் LAN/HTTPS/CORS/firewall setup reproduce செய்யப்படும்.
  - **Trace:** `M7-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide pp.1-2,4-5: branch code only; demo
JSON/images not committed. Another phone/PC
localhost-ஐ host ஆக பயன்படுத்த முடியாது. Angular path
command copy செய்யும்போது admin_dash path-ஐ
சரிபார்க்கவும்.

### M7-MS10 — Seven-module integration, 17-admin UAT and demo handover

**Milestone deliverable:** Cross-owner UAT, blockers, tests and supervisor evidence archived
**Proposed sprint days:** 19-20 | **Dependencies:** M1-MS10; M2-MS10; M3-MS10; M4-MS10; M5-MS10; M6-MS10; M7-MS08 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M7-MS10 | **Original target weeks:** 3

- [ ] **M7-MS10-T01** [QA] Shared UAT matrix மற்றும் seven-module integration run நடத்து
  - **Acceptance:** AT-REG/FRI/TRA/HUN/GAM/LEA/WAL/ADM cases result/evidence recorded.
  - **Trace:** `M7-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M7-MS10-T02** [QA] Cross-module reward/privacy/idempotency regression நடத்தி பதிவு செய்
  - **Acceptance:** Approval→Coins→profile/rank மற்றும் revoke→sharing cleanup pass ஆகும்.
  - **Trace:** `M7-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M7-MS10-T03** [QA] All 17 admin modules role/route coverage சோதனை
  - **Acceptance:** Each required module accessible to allowed role; denied roles tested.
  - **Trace:** `M7-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS10-T04** [Ops] Open decisions, API/partner readiness மற்றும் release scope review செய்
  - **Acceptance:** Unresolved items மற்றும் unavailable production integrations explicit ஆக இருக்கும்.
  - **Trace:** `M7-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS10-T05** [QA] Critical defect triage மற்றும் owner retest coordination செய்
  - **Acceptance:** Severity/owner/evidence tracked; release blocker unresolved என்றால் visible.
  - **Trace:** `M7-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS10-T06** [Ops] Demo accounts, scenario script மற்றும் supervisor evidence pack தயார் செய்
  - **Acceptance:** 7 owners தங்கள் module working result காட்டும் repeatable demo sequence இருக்கும்.
  - **Trace:** `M7-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M7-MS10-T07** [QA] Supervisor review record மற்றும் final handover பதிவு செய்
  - **Acceptance:** Actual review decision/date/remaining actions மட்டும் பதிவு; fabricated sign-off இல்லை.
  - **Trace:** `M7-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
