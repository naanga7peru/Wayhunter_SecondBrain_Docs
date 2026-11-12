# M5 — Games, Anti-Cheat & Leaderboard: 10 milestones & 74 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-10. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

### M5-MS01 — Game policies, states and audit schema

**Milestone deliverable:** Game flows, policies and review state machine documented
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS01 | **Original target weeks:** 1

- [ ] **M5-MS01-T01** [Design] G-01 முதல் G-16 game journeys பட்டியல் உருவாக்கு
  - **Acceptance:** Creator submit/publish மற்றும் player final approval தனித்தனி flows இருக்கும்.
  - **Trace:** `M5-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS01-T02** [Design] Winner count மற்றும் expiry decisions பதிவு செய்
  - **Acceptance:** D02 first-vs-multi, D03 month semantics, D04 in-progress expiry open என்று இருக்கும்.
  - **Trace:** `M5-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS01-T03** [Design] Creator gallery versus player live-proof rules பதிவு செய்
  - **Acceptance:** BRD creator clues gallery அனுமதி; Run Guide camera-only demo வேறுபாடு flag ஆகும்.
  - **Trace:** `M5-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS01-T04** [Data] Games, stages, attempts, proofs மற்றும் decisions schema வரைவு செய்
  - **Acceptance:** Creator/player IDs, server timestamps மற்றும் source references இருக்கும்.
  - **Trace:** `M5-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS01-T05** [API] Game approval/reward contracts M6 உடன் ஒப்பந்தம் செய்
  - **Acceptance:** Creator +100 மற்றும் eligible player +100 unique reward keys இருக்கும்.
  - **Trace:** `M5-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS01-T06** [Design] Safety, replay மற்றும் own-game eligibility விதிகள் எழுது
  - **Acceptance:** Dangerous tasks, answer leakage, collusion review cases குறிப்பிடப்படும்.
  - **Trace:** `M5-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS01-T07** [QA] Game acceptance மற்றும் edge-case checklist உருவாக்கு
  - **Acceptance:** Pending, reject, timeout, expiry, duplicate approval tests இருக்கும்.
  - **Trace:** `M5-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.

### M5-MS02 — Create Game clues, steps and draft

**Milestone deliverable:** Photo+text clue steps persist and validate
**Proposed sprint days:** 03-04 | **Dependencies:** M5-MS01; M1-MS04 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS02 | **Original target weeks:** 1

- [ ] **M5-MS02-T01** [Data] Games/stages/clues migrations உருவாக்கு
  - **Acceptance:** Ordered stage keys, creator ownership, draft state மற்றும் media refs இருக்கும்.
  - **Trace:** `M5-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS02-T02** [API] Game draft CRUD மற்றும் validation உருவாக்கு
  - **Acceptance:** Owner மட்டுமே edit செய்யலாம்; missing title/stage/duration reject ஆகும்.
  - **Trace:** `M5-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS02-T03** [Mobile] Create Game form மற்றும் stage editor உருவாக்கு
  - **Acceptance:** Title, description, cover, duration மற்றும் reorder controls இருக்கும்.
  - **Trace:** `M5-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS02-T04** [Mobile] Creator clue image upload மற்றும் text entry இணை
  - **Acceptance:** BRD-க்கு ஏற்ப creator gallery clues அனுமதி; player proof route தனி.
  - **Trace:** `M5-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS02-T05** [API] Clue media ownership மற்றும் safe public/private fields பிரி
  - **Acceptance:** Hidden proof/answers public play payload-ல் leak ஆகாது.
  - **Trace:** `M5-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS02-T06** [Mobile] Draft preview மற்றும் resume behavior இணை
  - **Acceptance:** Reopen draft ordered stages/captions-ஐ காப்பாற்றும்.
  - **Trace:** `M5-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS02-T07** [QA] Draft validation, stage reorder மற்றும் creator upload tests செய்
  - **Acceptance:** Invalid stage reject; normal creator gallery clue accepted.
  - **Trace:** `M5-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.

### M5-MS03 — Admin create approval, publication and creator eligibility

**Milestone deliverable:** Public only after Admin approve; +100 creator event once
**Proposed sprint days:** 05-06 | **Dependencies:** M5-MS02; M6-MS02 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS03 | **Original target weeks:** 2

- [ ] **M5-MS03-T01** [API] Submit Game command மற்றும் PendingAdmin queue செய்
  - **Acceptance:** GameId/UserId/name snapshot மற்றும் timestamp queue-ல் இருக்கும்.
  - **Trace:** `M5-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS03-T02** [Mobile] Submission confirmation மற்றும் Pending/Rejected UI இணை
  - **Acceptance:** Approvalக்கு முன் game public available list-ல் இல்லை.
  - **Trace:** `M5-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS03-T03** [Admin] Game creation queue மற்றும் clue/safety review screen உருவாக்கு
  - **Acceptance:** Reviewer stages/media/time மற்றும் creator identity பார்க்க முடியும்.
  - **Trace:** `M5-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS03-T04** [API] Approve/publish command மற்றும் creator reward event இணை
  - **Acceptance:** PublishedAt மற்றும் configured ExpiresAt save; +100 once source உருவாகும்.
  - **Trace:** `M5-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS03-T05** [API] Reject/flag/disable commands மற்றும் audit செய்
  - **Acceptance:** Reject reason கட்டாயம்; no reward; disabled game play blocked.
  - **Trace:** `M5-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS03-T06** [Admin] Decision reason, confirmation மற்றும் conflict refresh செய்
  - **Acceptance:** Double reviewer stale state தெளிவாகக் காட்டப்படும்.
  - **Trace:** `M5-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS03-T07** [QA] Publish/reject/retry மற்றும் creator credit சோதனை
  - **Acceptance:** Pending/rejected 0; approved creator 100; retries duplicate இல்லை.
  - **Trace:** `M5-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=4h original estimate, accepted=0.

### M5-MS04 — Discover games, eligible start and permissions

**Milestone deliverable:** Only valid/approved games playable by authorized users
**Proposed sprint days:** 07-08 | **Dependencies:** M5-MS03 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS04 | **Original target weeks:** 2

- [ ] **M5-MS04-T01** [API] Available games query மற்றும் active filters உருவாக்கு
  - **Acceptance:** Pending/rejected/expired/disabled games exclude ஆகும்.
  - **Trace:** `M5-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS04-T02** [Mobile] Game Home, How to Play மற்றும் game cards உருவாக்கு
  - **Acceptance:** Review/reward policy, safety instructions மற்றும் timer terms தெரியும்.
  - **Trace:** `M5-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS04-T03** [Mobile] Game Details மற்றும் Start confirmation உருவாக்கு
  - **Acceptance:** Creator, stage count, duration மற்றும் current eligibility காட்டப்படும்.
  - **Trace:** `M5-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS04-T04** [Data] Attempt schema மற்றும் active-attempt uniqueness அமை
  - **Acceptance:** User/game/session association மற்றும் StartedAt இருக்கும்.
  - **Trace:** `M5-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS04-T05** [API] Start attempt command மற்றும் server deadline உருவாக்கு
  - **Acceptance:** Creator own-game play reject; expired game new attempt reject.
  - **Trace:** `M5-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS04-T06** [Mobile] Resume attempt மற்றும் already-started feedback இணை
  - **Acceptance:** Repeated Start புதிய reward eligibility உருவாக்காது.
  - **Trace:** `M5-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS04-T07** [QA] Own game, expired game மற்றும் concurrent start tests செய்
  - **Acceptance:** Unauthorized start மறுக்கப்படும்; one active attempt rule pass ஆகும்.
  - **Trace:** `M5-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M5-MS05 — Hint-stage validation and server time

**Milestone deliverable:** Hints are validated server-side; no invented distance meter
**Proposed sprint days:** 09-10 | **Dependencies:** M5-MS04 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS05 | **Original target weeks:** 2

- [ ] **M5-MS05-T01** [API] Current stage query மற்றும் allowed progression உருவாக்கு
  - **Acceptance:** Future answer/proof data unauthorized response-ல் வராது.
  - **Trace:** `M5-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS05-T02** [Mobile] Photo/text clue stage screen உருவாக்கு
  - **Acceptance:** Stage number, clue மற்றும் timer தெளிவாக இருக்கும்; map/km mandatory இல்லை.
  - **Trace:** `M5-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS05-T03** [API] Server deadline மற்றும் stage timeout validation செய்
  - **Acceptance:** Device clock மாற்றி expired attempt-ஐ தொடர முடியாது.
  - **Trace:** `M5-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS05-T04** [Mobile] Timer background/resume synchronization இணை
  - **Acceptance:** App reopen server remaining time-ஐ பயன்படுத்தும்.
  - **Trace:** `M5-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS05-T05** [API] Fail/cancel/retry eligibility policy செய்
  - **Acceptance:** Failed attempt reward இல்லை; new retry rules D02/D04-க்கு பொருந்தும்.
  - **Trace:** `M5-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS05-T06** [Mobile] Game Over மற்றும் progress indicators உருவாக்கு
  - **Acceptance:** Timeout/failure reason மற்றும் eligible retry action காட்டப்படும்.
  - **Trace:** `M5-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS05-T07** [QA] Clock-change, reconnect மற்றும் stage-skip tests செய்
  - **Acceptance:** Client stage index மாற்றினாலும் locked progression bypass ஆகாது.
  - **Trace:** `M5-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M5-MS06 — Player live evidence and stage moderation

**Milestone deliverable:** Camera proof and reviewer audit with rejection tested
**Proposed sprint days:** 11-12 | **Dependencies:** M5-MS05 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS06 | **Original target weeks:** 2

- [ ] **M5-MS06-T01** [Mobile] Player live camera capture/retake flow உருவாக்கு
  - **Acceptance:** Gallery proof entry இல்லை; permission-denied path இருக்கும்.
  - **Trace:** `M5-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS06-T02** [API] Proof session binding மற்றும் content validation செய்
  - **Acceptance:** Game/attempt/stage/user/time mismatch reject ஆகும்.
  - **Trace:** `M5-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS06-T03** [Data] Private proof asset மற்றும் decision references சேமி
  - **Acceptance:** Proof state மற்றும் reviewer/server checks audit செய்யக்கூடியதாக இருக்கும்.
  - **Trace:** `M5-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS06-T04** [API] Proof submit/replay protection மற்றும் dedup செய்
  - **Acceptance:** Same proof retry duplicate stage advancement தராது.
  - **Trace:** `M5-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS06-T05** [API] Stage acceptance policy மற்றும் advance command உருவாக்கு
  - **Acceptance:** Configured authorized check ஏற்ற பின் மட்டும் அடுத்த stage unlock ஆகும்.
  - **Trace:** `M5-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS06-T06** [Mobile] Pending/Approved/Rejected proof feedback இணை
  - **Acceptance:** Server state வரை client victory/reward காட்டாது.
  - **Trace:** `M5-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS06-T07** [QA] Gallery injection, stale proof மற்றும் stage race tests செய்
  - **Acceptance:** Invalid proof மறுக்கப்படும்; concurrent retries ஒரே progression தரும்.
  - **Trace:** `M5-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.

### M5-MS07 — Exactly one Admin-verified winner and reward eligibility

**Milestone deliverable:** One verified winner only, creator ineligible; +100 once
**Proposed sprint days:** 13-14 | **Dependencies:** M5-MS06; M6-MS02 | **Task count:** 9 (7 legacy / 2 new).
**Original milestone references:** M5-MS07 | **Original target weeks:** 2

- [ ] **M5-MS07-T01** [API] Final completion PendingAdmin result உருவாக்கு
  - **Acceptance:** Player UserId/name, attempt, stage proofs மற்றும் deadline evidence இருக்கும்.
  - **Trace:** `M5-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS07-T02** [Admin] Player completion approval queue மற்றும் evidence detail உருவாக்கு
  - **Acceptance:** Creator review queue-இலிருந்து தனி result queue தெரியும்.
  - **Trace:** `M5-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS07-T03** [API] Winner eligibility மற்றும் atomic result decision செய்
  - **Acceptance:** Approved D02 winner policy concurrent result review-லும் பாதுகாக்கப்படும்.
  - **Trace:** `M5-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS07-T04** [API] Approved player reward source மற்றும் audit இணை
  - **Acceptance:** +100 once; pending/reject/timeout எந்த credit-மும் தராது.
  - **Trace:** `M5-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS07-T05** [API] Suspicious proof reject மற்றும் reason notification செய்
  - **Acceptance:** Reason My Games-ல் திரும்பும்; reward bypass இல்லை.
  - **Trace:** `M5-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS07-T06** [Mobile] Victory Pending/Approved மற்றும் rejection result UI செய்
  - **Acceptance:** Coins confirmed ஆகும் வரை pending result label இருக்கும்.
  - **Trace:** `M5-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS07-T07** [QA] Concurrent winners, repeated approval மற்றும் failed reward tests செய்
  - **Acceptance:** Winner rule மற்றும் exactly-once credit evidence பதிவு செய்யப்படும்.
  - **Trace:** `M5-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS07-T08** [QA] Atomically reject a second winner even under simultaneous Admin approvals
  - **Acceptance:** Exactly one winner record and one eligible winner-credit source per game
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M5-MS07-T09** [API] Block creator from receiving player-winner approval
  - **Acceptance:** Creator cannot win own community game
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M5-MS08 — 30-day approval-anchored expiry; archive, not delete

**Milestone deliverable:** At ApprovedAt+720h game unplayable, still in My Games
**Proposed sprint days:** 15-16 | **Dependencies:** M5-MS03; M5-MS07 | **Task count:** 9 (7 legacy / 2 new).
**Original milestone references:** M5-MS08 | **Original target weeks:** 3

- [ ] **M5-MS08-T01** [API] Approved one-month calculation மற்றும் expiry worker செய்
  - **Acceptance:** D03 calendar/30-day policy மற்றும் timezone boundary tests இருக்கும்.
  - **Trace:** `M5-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T02** [API] Public query/start command expiry gates இணை
  - **Acceptance:** Worker தாமதமானாலும் expired game new start அனுமதிக்காது.
  - **Trace:** `M5-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T03** [API] In-progress expiry decision handling செய்
  - **Acceptance:** D04 selected rule-க்கு ஏற்ப attempt continue/fail; unverified late reward இல்லை.
  - **Trace:** `M5-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T04** [Mobile] My Games Created tab மற்றும் status filters உருவாக்கு
  - **Acceptance:** Draft/Pending/Approved/Rejected/Active/Expired history தெரியும்.
  - **Trace:** `M5-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T05** [Mobile] Played/Pending Result/Completed history உருவாக்கு
  - **Acceptance:** Played date, stages, final status மற்றும் confirmed Coins காட்டப்படும்.
  - **Trace:** `M5-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T06** [Data] Soft archive மற்றும் retention references காப்பாற்று
  - **Acceptance:** Expiry record/evidence/audit-ஐ physical delete செய்யாது.
  - **Trace:** `M5-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS08-T07** [QA] Month end, expired reopen மற்றும் archived history சோதனை
  - **Acceptance:** Boundary expiry சரி; creator மற்றும் player records தொடர்ந்து தெரியும்.
  - **Trace:** `M5-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS08-T08** [API] Anchor game expiration to Admin-approved UTC publication time + exactly 720 hours
  - **Acceptance:** No calendar-month ambiguity; Flutter uses backend expiry
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M5-MS08-T09** [QA] Soft archive expired game and block new/resumed play and completion post-expiry
  - **Acceptance:** Expired game absent from public discovery, present in creator My Games
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M5-MS09 — Game leaderboard, anti-cheat and wallet entry

**Milestone deliverable:** Leaderboard rankings and abuse controls use trusted states
**Proposed sprint days:** 17-18 | **Dependencies:** M5-MS08; M6-MS03 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS09 | **Original target weeks:** 3

- [ ] **M5-MS09-T01** [API] Game creation/play Coins aggregation உருவாக்கு
  - **Acceptance:** Hunter/welcome/pending/reversed credits Game leaderboard-ல் இல்லை.
  - **Trace:** `M5-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS09-T02** [Mobile] Game leaderboard, own rank மற்றும் tie display உருவாக்கு
  - **Acceptance:** Module-specific entry மற்றும் D11 tie/period rules இருக்கும்.
  - **Trace:** `M5-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS09-T03** [Mobile] Rewards Store entry-ஐ shared Wallet offers-க்கு இணை
  - **Acceptance:** Live stock/terms மற்றும் correct Coins requirement காட்டப்படும்.
  - **Trace:** `M5-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS09-T04** [API] Repeated creator-player patterns மற்றும் suspicious signals பதிவு செய்
  - **Acceptance:** Flags reviewer-க்கு ஆதாரமாக வரும்; automatic blind ban இல்லை.
  - **Trace:** `M5-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS09-T05** [Admin] Flagged game/attempt drilldown மற்றும் controlled disable செய்
  - **Acceptance:** Actor/reason/audit மற்றும் current availability update இருக்கும்.
  - **Trace:** `M5-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS09-T06** [API] Fraud reversal நிகழ்வின் ranking update இணை
  - **Acceptance:** M6 compensating ledger correction பின் ineligible credits rank-ல் நீங்கும்.
  - **Trace:** `M5-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS09-T07** [QA] Rank source isolation மற்றும் abuse review tests செய்
  - **Acceptance:** Pending result rank உயராது; non-admin disable/reverse மறுக்கப்படும்.
  - **Trace:** `M5-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.

### M5-MS10 — Game end-to-end race-condition and regression tests

**Milestone deliverable:** Concurrent winner/expiry/reward integration tests pass
**Proposed sprint days:** 19-20 | **Dependencies:** M5-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M5-MS10 | **Original target weeks:** 3

- [ ] **M5-MS10-T01** [QA] Two-user creator/player full journey பதிவு செய்
  - **Acceptance:** Separate creation/result admin approvals மற்றும் இரு 100-Coin source refs இருக்கும்.
  - **Trace:** `M5-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS10-T02** [QA] Live proof, timer மற்றும் own-game regressions சோதனை
  - **Acceptance:** Gallery bypass, clock change, stage skip, creator self-play மறுக்கப்படும்.
  - **Trace:** `M5-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS10-T03** [QA] Expiry, archive மற்றும் winner policy cases சோதனை
  - **Acceptance:** D02/D03/D04 selected behavior evidence உடன் இருக்கும்.
  - **Trace:** `M5-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS10-T04** [QA] Review/reward retry மற்றும் concurrent decision tests செய்
  - **Acceptance:** No duplicate payout அல்லது unauthorized winner state.
  - **Trace:** `M5-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M5-MS10-T05** [API] Game integration blockers சரிசெய்
  - **Acceptance:** Critical gameplay/state/reward defects reviewer retest செய்யப்பட்டிருக்கும்.
  - **Trace:** `M5-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M5-MS10-T06** [Ops] Game setup, policy values மற்றும் demo guide எழுது
  - **Acceptance:** Clue media rules, timers, expiry settings மற்றும் test users documented.
  - **Trace:** `M5-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M5-MS10-T07** [QA] Peer-reviewed PR மற்றும் acceptance evidence இணை
  - **Acceptance:** Game module review மற்றும் known limitations supervisor demo-க்கு கிடைக்கும்.
  - **Trace:** `M5-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
