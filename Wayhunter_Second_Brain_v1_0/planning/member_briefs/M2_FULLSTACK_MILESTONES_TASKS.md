# M2 — Traveler Planning, Maps & AI: 10 milestones & 59 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-07. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

### M2-MS01 — Travel planning contracts and external-provider adapters

**Milestone deliverable:** Trip/AI/Maps/Weather adapter contracts and inputs documented
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M3-MS01, M3-MS03 | **Original target weeks:** 1, 2

- [ ] **M2-MS01-T01** [Design] T-01 முதல் T-15 வரை user journey map செய்
  - **Acceptance:** Create, start, finish மற்றும் leaderboard paths தனித்தனியாக இருக்கும்.
  - **Trace:** `M3-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS01-T02** [Design] Maps/Places/Routes/Weather adapter responsibilities பிரி
  - **Acceptance:** Provider failures fake route/weather உருவாக்கக் கூடாது என்று cases இருக்கும்.
  - **Trace:** `M3-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS01-T03** [Design] Historical route eligibility மற்றும் privacy rules எழுது
  - **Acceptance:** Completed authorized same-trip consecutive segments மட்டும் eligible.
  - **Trace:** `M3-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS01-T04** [Design] AI plan validation மற்றும் estimate labels வரையறு
  - **Acceptance:** Generated stops/costs editable estimates; proprietary AI model scope இல்லை.
  - **Trace:** `M3-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS01-T05** [QA] Traveler acceptance மற்றும் scope exclusions பதிவு செய்
  - **Acceptance:** Offline maps/cache sync உறுதிப்படுத்தாத feature என்று தெளிவாகப் பதிவாகும்.
  - **Trace:** `M3-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS01-T06** [API] Restricted Maps/Places/Routes keys configuration அமை
  - **Acceptance:** Platform/client restrictions மற்றும் server-secret separation பதிவாகும்.
  - **Trace:** `M3-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.

### M2-MS02 — Create/Edit Trip, ordered stops, draft persistence

**Milestone deliverable:** Trip draft CRUD, stop order and validation pass
**Proposed sprint days:** 03-04 | **Dependencies:** M2-MS01; M1-MS02 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M3-MS02 | **Original target weeks:** 1

- [ ] **M2-MS02-T01** [Data] Trips/TripStops migrations மற்றும் ownership keys அமை
  - **Acceptance:** Stop order மற்றும் trip foreign keys database-ல் உறுதியாக இருக்கும்.
  - **Trace:** `M3-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS02-T02** [API] Create/get/update/cancel trip endpoints உருவாக்கு
  - **Acceptance:** Owner access, required fields மற்றும் dates validate செய்யப்படும்.
  - **Trace:** `M3-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=4h original estimate, accepted=0.
- [ ] **M2-MS02-T03** [Mobile] Trip name, dates, budget, vehicle, headcount form உருவாக்கு
  - **Acceptance:** LKR budget numeric; invalid dates மற்றும் empty title errors காட்டப்படும்.
  - **Trace:** `M3-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS02-T04** [Mobile] Start/stops/end selection மற்றும் reorder draft இணை
  - **Acceptance:** Reorder செய்த stop sequence save/reload பின் அதேபடி இருக்கும்.
  - **Trace:** `M3-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS02-T05** [Mobile] My Plans tabs மற்றும் edit flow உருவாக்கு
  - **Acceptance:** My/Shared/Completed categories authoritative states பயன்படுத்தும்.
  - **Trace:** `M3-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS02-T06** [API] Draft persistence மற்றும் optimistic concurrency இணை
  - **Acceptance:** Stale edit conflict தெளிவாகத் தெரியும்; மற்றவர் trip overwrite ஆகாது.
  - **Trace:** `M3-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS02-T07** [QA] Save/reopen/edit/cancel மற்றும் no-completion tests செய்
  - **Acceptance:** Trip submit rank/count மாற்றாது; rejected form draft அழியாது.
  - **Trace:** `M3-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.

### M2-MS03 — Google Maps, place search and place picker

**Milestone deliverable:** Approved places searchable; denied GPS fallback works
**Proposed sprint days:** 05-06 | **Dependencies:** M2-MS02; M4-MS08 | **Task count:** 4 (4 legacy / 0 new).
**Original milestone references:** M3-MS03 | **Original target weeks:** 2

- [ ] **M2-MS03-T01** [Mobile] Traveler map மற்றும் approved place markers இணை
  - **Acceptance:** Pending/rejected Hunter place public map-ல் வராது.
  - **Trace:** `M3-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS03-T02** [Mobile] Search/current-location reusable picker உருவாக்கு
  - **Acceptance:** Start/add/end மூன்றும் ஒரே picker பயன்படுத்தும்.
  - **Trace:** `M3-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS03-T03** [Mobile] Location denied/manual search மற்றும் provider retry செய்
  - **Acceptance:** GPS permission deny ஆனாலும் manual place search இயங்கும்.
  - **Trace:** `M3-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS03-T04** [QA] Route unavailable மற்றும் wrong-place response சோதனை
  - **Acceptance:** Fabricated route fallback இல்லை; draft valid values பாதுகாக்கப்படும்.
  - **Trace:** `M3-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.

### M2-MS04 — Route geometry, stop reorder, trip constraints

**Milestone deliverable:** Route stop geometry, reorder and constraints consistent
**Proposed sprint days:** 07-08 | **Dependencies:** M2-MS03 | **Task count:** 4 (2 legacy / 2 new).
**Original milestone references:** M3-MS03 | **Original target weeks:** 2

- [ ] **M2-MS04-T01** [API] Place details மற்றும் route provider adapter உருவாக்கு
  - **Acceptance:** Provider ID, name, coordinates மற்றும் route result contract validate ஆகும்.
  - **Trace:** `M3-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS04-T02** [Mobile] Ordered stops route/polyline மற்றும் loading states இணை
  - **Acceptance:** Trip order-க்கு ஏற்ற route காட்டப்படும்; invalid stop message இருக்கும்.
  - **Trace:** `M3-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS04-T03** [QA] Document empty-route / provider-unavailable fallback without inventing travel time
  - **Acceptance:** No fabricated ETA; user can retry or edit stops
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M2-MS04-T04** [API] Persist ordered route geometry and planned-stop order under one shared version
  - **Acceptance:** M3 can consume persisted planned geometry for route safety checks
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M2-MS05 — Suggested plans and editable plan copies

**Milestone deliverable:** Source plans never mutated by copying
**Proposed sprint days:** 09-10 | **Dependencies:** M2-MS02; M2-MS03 | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M3-MS04 | **Original target weeks:** 2

- [ ] **M2-MS05-T01** [API] Eligible suggested plans query உருவாக்கு
  - **Acceptance:** Public/authorized shared completed plans மட்டும் query-ல் வரும்.
  - **Trace:** `M3-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS05-T02** [Mobile] Suggested plan filters மற்றும் cards உருவாக்கு
  - **Acceptance:** Budget/place/vehicle filters மற்றும் no-result state இருக்கும்.
  - **Trace:** `M3-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS05-T03** [API] Copy-plan command மற்றும் source attribution அமை
  - **Acceptance:** New owner/draft ID உருவாகும்; original creator reference காக்கப்படும்.
  - **Trace:** `M3-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS05-T04** [Mobile] Plan preview route, memories மற்றும் daywise display செய்
  - **Acceptance:** Private memories unauthorized preview-ல் தெரியாது.
  - **Trace:** `M3-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS05-T05** [Mobile] Use/Customize draft handoff இணை
  - **Acceptance:** Copied stops/dates/budget பயனரால் மாற்றப்படலாம்.
  - **Trace:** `M3-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS05-T06** [QA] Reuse privacy மற்றும் original immutability tests செய்
  - **Acceptance:** Copy edit பின் source plan unchanged; private plan access மறுக்கப்படும்.
  - **Trace:** `M3-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M2-MS06 — Completed historical segments and reuse policy

**Milestone deliverable:** Consecutive completed segments reused with privacy rules
**Proposed sprint days:** 11-12 | **Dependencies:** M2-MS05; M3-MS09 | **Task count:** 4 (3 legacy / 1 new).
**Original milestone references:** M3-MS04, M3-MS06 | **Original target weeks:** 2

- [ ] **M2-MS06-T01** [API] Historical consecutive segment validation இணை
  - **Acceptance:** வேறு trips-ன் unrelated stop pairs valid route என்று சேர்க்கப்படாது.
  - **Trace:** `M3-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS06-T02** [Data] Visited stops மற்றும் valid history segments சேமி
  - **Acceptance:** Same-trip ordered consecutive evidence மட்டும் history-ல் எழுதப்படும்.
  - **Trace:** `M3-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS06-T03** [Mobile] History View மற்றும் Reuse Plan shortcuts இணை
  - **Acceptance:** Reuse புதிய draft; completed trip original data மாறாது.
  - **Trace:** `M3-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS06-T04** [API] Record complete consecutive completed segments before suggesting historical reuse
  - **Acceptance:** Partial, paused, or unverified segments cannot be presented as completed
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M2-MS07 — AI Trip Plan (external API) and safe draft handoff

**Milestone deliverable:** AI creates reviewable draft, never auto-starts live trip
**Proposed sprint days:** 13-14 | **Dependencies:** M2-MS02; M2-MS03 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M3-MS08 | **Original target weeks:** 3

- [ ] **M2-MS07-T01** [Mobile] AI trip input form உருவாக்கு
  - **Acceptance:** Date, places, LKR budget, vehicle, group, preferences சேகரிக்கப்படும்.
  - **Trace:** `M3-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS07-T02** [API] Server-mediated AI adapter மற்றும் secret handling அமை
  - **Acceptance:** Client-ல் provider secret இல்லை; timeout மற்றும் quota limits இருக்கும்.
  - **Trace:** `M3-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS07-T03** [API] Structured itinerary request/response schema செய்
  - **Acceptance:** Daywise stops/time/cost fields parse செய்து validate செய்யப்படும்.
  - **Trace:** `M3-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS07-T04** [API] Generated place மற்றும் numeric/date validation செய்
  - **Acceptance:** Invalid/unknown places user review தேவை எனக் காட்டப்படும்.
  - **Trace:** `M3-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M2-MS07-T05** [Mobile] AI proposal review மற்றும் editable plan conversion உருவாக்கு
  - **Acceptance:** Estimate labels இருக்கும்; user accept செய்யாமல் trip start ஆகாது.
  - **Trace:** `M3-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS07-T06** [Mobile] Failure, partial result மற்றும் retry states இணை
  - **Acceptance:** Provider failure user inputs-ஐ reset செய்யாது.
  - **Trace:** `M3-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS07-T07** [QA] Malformed AI output மற்றும் budget edit flow சோதனை
  - **Acceptance:** Invalid schema safely rejected; accepted draft normal trip flow-க்கு செல்லும்.
  - **Trace:** `M3-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M2-MS08 — Nearby Find action, weather and sponsored map integration

**Milestone deliverable:** Find occurs only on action; weather stale/failure indicated
**Proposed sprint days:** 15-16 | **Dependencies:** M2-MS03; M7-MS06 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M3-MS07 | **Original target weeks:** 2

- [ ] **M2-MS08-T01** [API] Nearby provider query மற்றும் category mapping உருவாக்கு
  - **Acceptance:** Food/hospital/fuel/police/ATM/attraction categories support ஆகும்.
  - **Trace:** `M3-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS08-T02** [Mobile] Find button மற்றும் nearby result list/map உருவாக்கு
  - **Acceptance:** Click செய்யும் நேரத்தில் மட்டும் 1 km search அனுப்பப்படும்.
  - **Trace:** `M3-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS08-T03** [Mobile] Nearby detail மற்றும் directions action இணை
  - **Acceptance:** Provider coordinates/name சரியாக navigation-க்கு அனுப்பப்படும்.
  - **Trace:** `M3-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS08-T04** [API] Weather provider adapter மற்றும் cache timestamps அமை
  - **Acceptance:** Forecast response source/time/location fields உடன் வரும்.
  - **Trace:** `M3-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS08-T05** [Mobile] Weather/overlay மற்றும் freshness labels உருவாக்கு
  - **Acceptance:** Forecast மற்றும் community hazard labels வேறுபடும்.
  - **Trace:** `M3-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS08-T06** [API] Quota, timeout மற்றும் retry behavior இணை
  - **Acceptance:** Provider outage repetitive continuous search உருவாக்காது.
  - **Trace:** `M3-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS08-T07** [QA] 1 km boundary, denied GPS மற்றும் stale weather cases சோதனை
  - **Acceptance:** No-location explanation மற்றும் real-data-unavailable state evidence இருக்கும்.
  - **Trace:** `M3-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS08-T08** [Mobile] Show weather observation/forecast freshness and error fallback on Traveler map
  - **Acceptance:** Weather timestamp shown; stale data clearly labeled
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M2-MS09 — Traveler rankings and Admin Trips/Historical Routes

**Milestone deliverable:** Admin route data and ranking source use actual records
**Proposed sprint days:** 17-18 | **Dependencies:** M2-MS06; M3-MS09; M5-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M3-MS09 | **Original target weeks:** 3

- [ ] **M2-MS09-T01** [API] Completed-trip eligibility aggregation உருவாக்கு
  - **Acceptance:** Planned/saved/cancelled/invalid trips ranking-ல் சேராது.
  - **Trace:** `M3-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS09-T02** [API] Own rank மற்றும் tie/period policy query இணை
  - **Acceptance:** D11 policy கொண்டு stable ordering மற்றும் public fields மட்டும் வரும்.
  - **Trace:** `M3-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS09-T03** [Mobile] Traveler leaderboard screen மற்றும் module entry உருவாக்கு
  - **Acceptance:** Traveler module-க்குள் accessible; empty/own rank states இருக்கும்.
  - **Trace:** `M3-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS09-T04** [Admin] Trips list, actual timestamps மற்றும் ordered route detail உருவாக்கு
  - **Acceptance:** Planned dates மற்றும் actual start/end தெளிவாக வேறுபடும்.
  - **Trace:** `M3-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS09-T05** [API] Invalid historical segment flag action உருவாக்கு
  - **Acceptance:** Authorized reason/audit பின் ineligible segment reuse query-ல் வராது.
  - **Trace:** `M3-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS09-T06** [Admin] Trip/history filters மற்றும் flagged state controls இணை
  - **Acceptance:** Completed/active/flagged filter மற்றும் review result refresh வேலை செய்யும்.
  - **Trace:** `M3-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS09-T07** [QA] Fake completion, tie மற்றும் flagged route tests செய்
  - **Acceptance:** Save-only rank உயராது; invalid route suggested source-ல் இல்லாது போகும்.
  - **Trace:** `M3-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.

### M2-MS10 — M2 planning integration and provider failure acceptance

**Milestone deliverable:** Maps/AI provider failures, device tests and PR evidence
**Proposed sprint days:** 19-20 | **Dependencies:** M2-MS07; M2-MS08; M2-MS09 | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M3-MS10 | **Original target weeks:** 3

- [ ] **M2-MS10-T01** [QA] Full traveler journey உண்மையான சாதனத்தில் demo செய்
  - **Acceptance:** Start/finish timestamps, route, friends மற்றும் history evidence பதிவு செய்யப்படும்.
  - **Trace:** `M3-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M2-MS10-T02** [QA] Maps/AI/weather provider failure matrix சோதனை
  - **Acceptance:** Failure draft/session-ஐ அழிக்காது; fake output இல்லை.
  - **Trace:** `M3-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS10-T03** [QA] Suggested plan மற்றும் leaderboard cross-check செய்
  - **Acceptance:** Source plan unchanged; eligible completion count database-க்கு பொருந்தும்.
  - **Trace:** `M3-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M2-MS10-T04** [API] Traveler integration blockers சரிசெய்
  - **Acceptance:** Critical state/privacy/provider defects retest செய்யப்பட்டிருக்கும்.
  - **Trace:** `M3-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M2-MS10-T05** [Ops] Provider config, seed routes மற்றும் run guide புதுப்பி
  - **Acceptance:** Secrets இன்றி API env names, limits, demo route steps இருக்கும்.
  - **Trace:** `M3-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M2-MS10-T06** [QA] Peer review மற்றும் module evidence handover செய்
  - **Acceptance:** Reviewed PR, acceptance result மற்றும் known limitations tracker-ல் இணைக்கப்படும்.
  - **Trace:** `M3-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
