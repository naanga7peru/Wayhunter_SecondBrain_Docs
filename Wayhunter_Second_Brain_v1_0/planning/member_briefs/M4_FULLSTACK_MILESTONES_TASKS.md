# M4 — Hunter & Places: 10 milestones & 73 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-04, ADM-06. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

### M4-MS01 — Hunter requirements, evidence and place-domain schema

**Milestone deliverable:** Hunter evidence DTOs and required source timestamps defined
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS01 | **Original target weeks:** 1

- [ ] **M4-MS01-T01** [Design] H-01 முதல் H-14 flow மற்றும் states பட்டியல் தயாரி
  - **Acceptance:** Capture, preview, submit, My Hunts, reward, leaderboard paths இருக்கும்.
  - **Trace:** `M4-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS01-T02** [Design] Run Guide demo GPS/360 gaps பதிவு செய்
  - **Acceptance:** Simulated checks completed production feature என்று குறிக்கப்படாது.
  - **Trace:** `M4-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS01-T03** [Data] Submission, evidence, decisions மற்றும் place schema வரைவு செய்
  - **Acceptance:** UserId/name snapshot, district, GPS/time, private evidence references இருக்கும்.
  - **Trace:** `M4-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS01-T04** [API] Submit/review/reward event DTO ஒப்பந்தம் எழுது
  - **Acceptance:** Submission ID மற்றும் single reward source reference M6 உடன் ஒப்புக்கொள்ளப்படும்.
  - **Trace:** `M4-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS01-T05** [Design] 200 m candidate screening மற்றும் rejection rules பிரி
  - **Acceptance:** Distance மட்டும் automatic rejection செய்யாது என்று documented rule இருக்கும்.
  - **Trace:** `M4-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS01-T06** [Design] Capture accuracy, size, duration மற்றும் restricted data decisions பதிவு செய்
  - **Acceptance:** D10/D17 policy owners மற்றும் unresolved configuration fields இருக்கும்.
  - **Trace:** `M4-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS01-T07** [QA] Hunter acceptance matrix மற்றும் review evidence தயார் செய்
  - **Acceptance:** Gallery, GPS, duplicate, approve/reject, reward retry cases இருக்கும்.
  - **Trace:** `M4-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.

### M4-MS02 — GPS permission and current-district restriction

**Milestone deliverable:** Only current district eligible; deny/spoof flows fail safely
**Proposed sprint days:** 03-04 | **Dependencies:** M4-MS01; M1-MS04 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS02 | **Original target weeks:** 1

- [ ] **M4-MS02-T01** [Mobile] Hunter Home மற்றும் Add Place form உருவாக்கு
  - **Acceptance:** Search, My Hunts, Add Place, leaderboard entries இருக்கும்.
  - **Trace:** `M4-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS02-T02** [Mobile] GPS permission, freshness மற்றும் accuracy capture செய்
  - **Acceptance:** Latitude/longitude/accuracy/time read-only evidence fields ஆக இருக்கும்.
  - **Trace:** `M4-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS02-T03** [API] District resolution மற்றும் eligibility adapter உருவாக்கு
  - **Acceptance:** Current coordinates-க்கு district result server-side validate செய்யப்படும்.
  - **Trace:** `M4-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS02-T04** [Mobile] Detected district lock மற்றும் denied help states இணை
  - **Acceptance:** Manual coordinate/district override மூலம் submit செய்ய முடியாது.
  - **Trace:** `M4-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS02-T05** [Data] Capture session மற்றும் draft linkage சேமி
  - **Acceptance:** GPS sample மற்றும் upcoming media session same submission-க்கு இணையும்.
  - **Trace:** `M4-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS02-T06** [API] Stale/impossible GPS signals review flags உருவாக்கு
  - **Acceptance:** Suspicious values silent approval பெறாது; flags reviewer-க்கு தெரியும்.
  - **Trace:** `M4-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS02-T07** [QA] District boundary, low accuracy மற்றும் permission-denied tests செய்
  - **Acceptance:** Configured accuracy/freshness gate மற்றும் retry behavior evidence இருக்கும்.
  - **Trace:** `M4-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.

### M4-MS03 — Mandatory live guided 360 capture

**Milestone deliverable:** Mandatory guided 360 real camera capture validated
**Proposed sprint days:** 05-06 | **Dependencies:** M4-MS02 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M4-MS03 | **Original target weeks:** 2

- [ ] **M4-MS03-T01** [Mobile] Live camera preview மற்றும் video capture flow உருவாக்கு
  - **Acceptance:** Camera permission உடன் capture; gallery picker entry இல்லை.
  - **Trace:** `M4-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS03-T02** [Mobile] Guided sweep instructions, timer மற்றும் progress UI செய்
  - **Acceptance:** Guided sweep என்ற label; spherical 360 என தவறாகக் கூறாது.
  - **Trace:** `M4-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS03-T03** [Mobile] Start/cancel/retake மற்றும் interruption recovery செய்
  - **Acceptance:** Interrupted/empty recording valid evidence ஆக ஏற்கப்படாது.
  - **Trace:** `M4-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS03-T04** [Mobile] Video playback preview மற்றும் confirm flow உருவாக்கு
  - **Acceptance:** User preview பார்த்து retake/confirm செய்ய முடியும்.
  - **Trace:** `M4-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS03-T05** [API] Capture-session, media type மற்றும் duration validation செய்
  - **Acceptance:** Configured limits மீறும்/corrupt video reject ஆகும்.
  - **Trace:** `M4-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS03-T06** [API] Private upload authorization மற்றும் metadata linkage செய்
  - **Acceptance:** Submission/session ownerக்கு மட்டும் video attach அனுமதி.
  - **Trace:** `M4-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS03-T07** [QA] Gallery bypass, camera deny மற்றும் corrupt-video tests செய்
  - **Acceptance:** Direct endpoint misuse மற்றும் invalid file cases safely rejected.
  - **Trace:** `M4-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS03-T08** [Mobile] Block place submission if mandatory guided 360 evidence absent
  - **Acceptance:** Submit remains unavailable until live 360 evidence exists
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M4-MS04 — Live normal photo, protected evidence upload

**Milestone deliverable:** Normal photo requires live capture; protected metadata/media
**Proposed sprint days:** 07-08 | **Dependencies:** M4-MS03 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS04 | **Original target weeks:** 2

- [ ] **M4-MS04-T01** [Mobile] Add Normal Photo மற்றும் live camera capture உருவாக்கு
  - **Acceptance:** Video preview பின் photo flow; gallery route இல்லை.
  - **Trace:** `M4-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS04-T02** [Mobile] Photo preview, retake மற்றும் confirm controls செய்
  - **Acceptance:** Rejected photo மீண்டும் capture செய்யலாம்; confirmed thumbnail காட்டப்படும்.
  - **Trace:** `M4-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS04-T03** [API] Photo content/type/size checks செயல் படுத்து
  - **Acceptance:** Zero-byte/corrupt/mismatched content evidence மறுக்கப்படும்.
  - **Trace:** `M4-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS04-T04** [API] Photo/video upload signatures மற்றும் private access அமை
  - **Acceptance:** Public URL மூலம் private proof திறக்க முடியாது.
  - **Trace:** `M4-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS04-T05** [Data] Evidence bundle மற்றும் upload state references சேமி
  - **Acceptance:** Video/photo/GPS/time same submission session-க்கு இணையும்.
  - **Trace:** `M4-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS04-T06** [Mobile] Upload progress, retry மற்றும் draft recovery இணை
  - **Acceptance:** Network retry duplicate evidence/submission உருவாக்காது.
  - **Trace:** `M4-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS04-T07** [QA] Private proof authorization மற்றும் upload-failure tests செய்
  - **Acceptance:** Owner/reviewer மட்டும் proof பார்க்கலாம்; orphan upload path கையாளப்படும்.
  - **Trace:** `M4-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M4-MS05 — Duplicate 200m/restricted-zone/district screening

**Milestone deliverable:** 200m duplicate candidates and restricted areas surfaced
**Proposed sprint days:** 09-10 | **Dependencies:** M4-MS04 | **Task count:** 8 (8 legacy / 0 new).
**Original milestone references:** M4-MS05, M7-MS08 | **Original target weeks:** 2, 3

- [ ] **M4-MS05-T01** [Data] Approved place spatial lookup மற்றும் candidate store அமை
  - **Acceptance:** Candidate distance மற்றும் matched place IDs submission-க்கு இணையும்.
  - **Trace:** `M4-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS05-T02** [API] 200 m nearby duplicate query உருவாக்கு
  - **Acceptance:** Configured radius boundary சோதிக்கப்படும்; zero candidates support ஆகும்.
  - **Trace:** `M4-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS05-T03** [API] Name/category similarity மற்றும் media similarity signals இணை
  - **Acceptance:** Signals விளக்கமாகப் பதிவாகும்; score மட்டும் automatic reject செய்யாது.
  - **Trace:** `M4-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS05-T04** [Mobile] Nearby candidate preview மற்றும் user review screen உருவாக்கு
  - **Acceptance:** Existing candidate விவரம் மற்றும் continue/back actions இருக்கும்.
  - **Trace:** `M4-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS05-T05** [API] Curated restricted-zone geofence checks இணை
  - **Acceptance:** D17 approved zone data/version மற்றும் escalation reason பதிவு செய்யப்படும்.
  - **Trace:** `M4-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS05-T06** [Admin] Duplicate/restricted flags reviewer payload-ல் காட்டி இணை
  - **Acceptance:** Candidate links, distance மற்றும் safety reasons queue detail-ல் தெரியும்.
  - **Trace:** `M4-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS05-T07** [QA] Adjacent distinct places மற்றும் restricted-boundary tests செய்
  - **Acceptance:** 200 m உள்ள distinct location automatic reject ஆகாது; flagged case queue-க்கு வரும்.
  - **Trace:** `M4-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS05-T08** [Admin] Restricted-zone source import மற்றும் map preview உருவாக்கு
  - **Acceptance:** Curated authorized data/source/version; unsupported Google guarantee இல்லை.
  - **Trace:** `M7-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M4-MS06 — Submit place, Pending status and My Hunts

**Milestone deliverable:** Pending state visible with My Hunts status history
**Proposed sprint days:** 11-12 | **Dependencies:** M4-MS05 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS06 | **Original target weeks:** 2

- [ ] **M4-MS06-T01** [API] Idempotent Hunter submit endpoint உருவாக்கு
  - **Acceptance:** Complete live evidence மற்றும் authenticated owner validate ஆகும்.
  - **Trace:** `M4-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS06-T02** [Data] Submission + admin queue atomic write அமை
  - **Acceptance:** Queue write failure silent public place உருவாக்காது.
  - **Trace:** `M4-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS06-T03** [Mobile] Review & Submit summary screen உருவாக்கு
  - **Acceptance:** Place, district, media, flags மற்றும் submission confirmation தெரியும்.
  - **Trace:** `M4-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS06-T04** [Mobile] My Hunts list மற்றும் owner-only detail உருவாக்கு
  - **Acceptance:** Pending/Approved/Rejected மற்றும் rejection reason காட்டப்படும்.
  - **Trace:** `M4-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS06-T05** [API] Status refresh API மற்றும் authorized live update இணை
  - **Acceptance:** Backend status source; client self-approve செய்ய முடியாது.
  - **Trace:** `M4-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS06-T06** [Mobile] Pending/no-reward UI மற்றும் retry guard செய்
  - **Acceptance:** Pending submission reward balance உயர்த்தாது.
  - **Trace:** `M4-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS06-T07** [QA] Duplicate submit, name snapshot மற்றும் visibility tests செய்
  - **Acceptance:** ஒரே retry ஒரே submission; pending place public map-ல் வராது.
  - **Trace:** `M4-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.

### M4-MS07 — Admin verify/approve/reject with one reward event

**Milestone deliverable:** Admin approval publishes once, +200 event once; reject no reward
**Proposed sprint days:** 13-14 | **Dependencies:** M4-MS06; M6-MS02; M1-MS09 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M4-MS07 | **Original target weeks:** 2

- [ ] **M4-MS07-T01** [Admin] Hunter queue filters மற்றும் UserId/name list உருவாக்கு
  - **Acceptance:** District/status/time filters மற்றும் pending count இயங்கும்.
  - **Trace:** `M4-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS07-T02** [Admin] Evidence, GPS, candidates மற்றும் safety detail உருவாக்கு
  - **Acceptance:** Private video/photo authorized reviewer-க்கு மட்டும் கிடைக்கும்.
  - **Trace:** `M4-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS07-T03** [API] Approve command publication மற்றும் reward event இணை
  - **Acceptance:** Eligible approval place publish மற்றும் one reward source உருவாக்கும்.
  - **Trace:** `M4-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS07-T04** [API] Reject/request-evidence/flag transitions அமை
  - **Acceptance:** Rejection reason கட்டாயம்; exception actions audit trail உடன் இருக்கும்.
  - **Trace:** `M4-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS07-T05** [Admin] Decision confirmation மற்றும் stale-review conflict UI செய்
  - **Acceptance:** Already-reviewed submission-ல் misleading second approval success இல்லை.
  - **Trace:** `M4-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS07-T06** [API] Approval notification மற்றும் Coins ledger reconciliation இணை
  - **Acceptance:** +200 once மற்றும் congratulations event; reject event reward தராது.
  - **Trace:** `M4-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS07-T07** [QA] Double approval, reject மற்றும் failed reward recovery tests செய்
  - **Acceptance:** Concurrent reviewer/retry இரண்டாவது reward உருவாக்காது.
  - **Trace:** `M4-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS07-T08** [API] Publish only after authorized Admin approval; emit HunterApprovedEligible once
  - **Acceptance:** No +200 credit for Pending/Rejected; duplicate approvals do not generate new event
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M4-MS08 — Approved place publication, search and Admin Places

**Milestone deliverable:** Places published/searchable and Admin actions audited
**Proposed sprint days:** 15-16 | **Dependencies:** M4-MS07 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS08 | **Original target weeks:** 3

- [ ] **M4-MS08-T01** [API] Published places query மற்றும் district/search filters உருவாக்கு
  - **Acceptance:** Approved+Published records மட்டும் public endpoint-ல் வரும்.
  - **Trace:** `M4-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS08-T02** [Mobile] Existing Discoveries map/list மற்றும் Place Details உருவாக்கு
  - **Acceptance:** Public photos, directions, description மற்றும் accurate badge தெரியும்.
  - **Trace:** `M4-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS08-T03** [Admin] Places list/detail மற்றும் edit/archive UI உருவாக்கு
  - **Acceptance:** Raw pending submission separate Hunter queue-ல் இருக்கும்.
  - **Trace:** `M4-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS08-T04** [API] Place edit/deactivate commands மற்றும் audit செய்
  - **Acceptance:** Privileged role/reason மற்றும் mobile visibility update இருக்கும்.
  - **Trace:** `M4-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS08-T05** [API] Duplicate place merge மற்றும் reference preservation செய்
  - **Acceptance:** Memories/trips/history references முறியாது; original audit தொடரும்.
  - **Trace:** `M4-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS08-T06** [Admin] Official history மற்றும் then/now source fields இணை
  - **Acceptance:** Historical content-க்கு source/attribution பதிவு; private proof public ஆகாது.
  - **Trace:** `M4-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS08-T07** [QA] Publish/archive/merge மற்றும் evidence isolation tests செய்
  - **Acceptance:** Archived place public search-ல் இல்லை; merged references valid.
  - **Trace:** `M4-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M4-MS09 — Hunter ranking, profile links and reward presentation

**Milestone deliverable:** Hunter ranks derive from approved hunts; reward UI reflects ledger
**Proposed sprint days:** 17-18 | **Dependencies:** M4-MS07; M5-MS09; M6-MS03 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS09 | **Original target weeks:** 3

- [ ] **M4-MS09-T01** [API] Hunter reward-source aggregation உருவாக்கு
  - **Acceptance:** Welcome/Game Coins மற்றும் pending credits Hunter rank-ல் சேராது.
  - **Trace:** `M4-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS09-T02** [API] Fraud reversal மற்றும் tie policy rank handling செய்
  - **Acceptance:** Reversed/ineligible credits exclude ஆகும்; D11 stable order இருக்கும்.
  - **Trace:** `M4-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS09-T03** [Mobile] Hunter leaderboard மற்றும் own rank view உருவாக்கு
  - **Acceptance:** Module-only entry, pagination மற்றும் no-data states இருக்கும்.
  - **Trace:** `M4-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS09-T04** [Mobile] Reward summary மற்றும் congratulations UI இணை
  - **Acceptance:** Approvalக்கு பின் 200 Coins; pending/reject-ல் false success இல்லை.
  - **Trace:** `M4-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS09-T05** [Mobile] My Hunts → place/reason/reward detail routes இணை
  - **Acceptance:** Current backend result சரியான destination-க்கு வழி காட்டும்.
  - **Trace:** `M4-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS09-T06** [API] Profile Hunt tab மற்றும் count contracts இணை
  - **Acceptance:** M1 profile owner statuses/public counts சரியான scope பயன்படுத்தும்.
  - **Trace:** `M4-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS09-T07** [QA] Rank source isolation மற்றும் reversal tests செய்
  - **Acceptance:** Approved Hunter event மட்டும் rank மாற்றும்; repeated refresh duplicates இல்லை.
  - **Trace:** `M4-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.

### M4-MS10 — M4 real-device QA, moderation and handover

**Milestone deliverable:** Real-device camera, GPS, moderation, offline errors tested
**Proposed sprint days:** 19-20 | **Dependencies:** M4-MS08; M4-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M4-MS10 | **Original target weeks:** 3

- [ ] **M4-MS10-T01** [QA] Physical-device GPS/video/photo capture demo நடத்து
  - **Acceptance:** Simulation labels இன்றி actual capture metadata/evidence பதிவாகும்.
  - **Trace:** `M4-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS10-T02** [QA] Admin approve/reject மற்றும் My Hunts refresh சோதனை
  - **Acceptance:** அதே submission UserId/name மற்றும் result இரு clients-லும் பொருந்தும்.
  - **Trace:** `M4-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS10-T03** [QA] 200 m duplicates மற்றும் private media regression செய்
  - **Acceptance:** Distinct nearby place, denied proof access மற்றும் published visibility pass ஆகும்.
  - **Trace:** `M4-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS10-T04** [QA] Upload/review network retry மற்றும் concurrency சோதனை
  - **Acceptance:** Repeated requests duplicate places/rewards உருவாக்காது.
  - **Trace:** `M4-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M4-MS10-T05** [API] Hunter blockers மற்றும் capture defects சரிசெய்
  - **Acceptance:** Critical defects retest evidence உடன் முடிக்கப்பட்டிருக்கும்.
  - **Trace:** `M4-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M4-MS10-T06** [Ops] Capture limits, zone setup மற்றும் run guide எழுது
  - **Acceptance:** Required permissions/config, demo steps மற்றும் remaining decisions தெரியும்.
  - **Trace:** `M4-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M4-MS10-T07** [QA] Peer review, PR மற்றும் test evidence இணை
  - **Acceptance:** Reviewer-approved module with acceptance links கிடைக்கும்.
  - **Trace:** `M4-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
