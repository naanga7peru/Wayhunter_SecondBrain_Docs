# M3 — Active Trip, Safety & Notifications: 10 milestones & 69 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-08, ADM-09, ADM-16. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

### M3-MS01 — Live-trip/safety event contracts, privacy and schema

**Milestone deliverable:** Only approved session/consent events enter safety stream
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 5 (5 legacy / 0 new).
**Original milestone references:** M2-MS01, M3-MS01 | **Original target weeks:** 1

- [ ] **M3-MS01-T01** [Design] GPS sharing consent மற்றும் retention rules பதிவு செய்
  - **Acceptance:** Accept invite மட்டும் live location-ஐ enable செய்யாது.
  - **Trace:** `M2-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS01-T02** [Design] Hazard report lifecycle மற்றும் threshold decisions பதிவு செய்
  - **Acceptance:** Reported/Verified/Resolved/Expired transitions மற்றும் D08 requirements இருக்கும்.
  - **Trace:** `M2-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS01-T03** [QA] Social/safety acceptance checklist தயாரி
  - **Acceptance:** Consent revoke, duplicate requests, blocked viewer மற்றும் stale GPS cases இருக்கும்.
  - **Trace:** `M2-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS01-T04** [Data] Trips, ordered stops, sessions மற்றும் history schema வரைவு செய்
  - **Acceptance:** Planned மற்றும் actual timestamps தனியாக இருக்கும்.
  - **Trace:** `M3-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS01-T05** [API] Trip DTO மற்றும் Friends/GPS contract ஒப்பந்தம் எழுது
  - **Acceptance:** Draft ID, accepted members, session ID மற்றும் consent reference வரையறுக்கப்படும்.
  - **Trace:** `M3-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.

### M3-MS02 — Start/Pause/Resume/Stop trip session and live map

**Milestone deliverable:** Session state change idempotent; pause/recover/stop tested
**Proposed sprint days:** 03-04 | **Dependencies:** M3-MS01; M2-MS02; M1-MS04 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M3-MS05 | **Original target weeks:** 2

- [ ] **M3-MS02-T01** [Data] TripSessions மற்றும் actual StartedAt storage அமை
  - **Acceptance:** ஒரே trip-க்கு duplicate active session constraint இருக்கும்.
  - **Trace:** `M3-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS02-T02** [API] Start Trip command மற்றும் state validation உருவாக்கு
  - **Acceptance:** Authorized planned trip மட்டுமே Active ஆகும்; timestamp server-generated.
  - **Trace:** `M3-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS02-T03** [Mobile] Start confirmation மற்றும் live map controls உருவாக்கு
  - **Acceptance:** Start, Find, Hazard, Memories, Friends, Pause, Finish entries இருக்கும்.
  - **Trace:** `M3-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS02-T04** [API] Session recovery/reconnect endpoint உருவாக்கு
  - **Acceptance:** App restart existing active session-ஐ மீட்டெடுக்கும்.
  - **Trace:** `M3-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS02-T05** [Mobile] Route sampling consent மற்றும் stale GPS display இணை
  - **Acceptance:** GPS unavailable என்றால் route unavailable/stale எனக் காட்டப்படும்.
  - **Trace:** `M3-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS02-T06** [API] Group and hazard modules-க்கு active-session contract இணை
  - **Acceptance:** Inactive trip location events அனுமதிக்கப்படாது.
  - **Trace:** `M3-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS02-T07** [QA] Double-start, reminder மற்றும் reconnect tests செய்
  - **Acceptance:** Reminder trip தொடங்காது; repeated Start ஒரே session தரும்.
  - **Trace:** `M3-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M3-MS03 — Trip invitations, membership and authorization

**Milestone deliverable:** Trip invitation acceptance never implies GPS consent
**Proposed sprint days:** 05-06 | **Dependencies:** M3-MS01; M1-MS07; M2-MS02 | **Task count:** 5 (5 legacy / 0 new).
**Original milestone references:** M2-MS05 | **Original target weeks:** 2

- [ ] **M3-MS03-T01** [Data] TripInvitations மற்றும் TripMembers relations அமை
  - **Acceptance:** Invitation reference, state, sender/recipient மற்றும் uniqueness constraint இருக்கும்.
  - **Trace:** `M2-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS03-T02** [API] Trip invite endpoint மற்றும் eligibility checks எழுது
  - **Acceptance:** Owner permission, blocked user மற்றும் duplicate invitation checks pass ஆகும்.
  - **Trace:** `M2-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS03-T03** [API] Invitation state changes மற்றும் idempotency செய்
  - **Acceptance:** Repeated accept ஒரே member relation மட்டும் உருவாக்கும்.
  - **Trace:** `M2-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS03-T04** [API] Membership notifications மற்றும் revoked access இணை
  - **Acceptance:** Cancelled/removed membership private trip access-ஐ நிறுத்தும்.
  - **Trace:** `M2-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS03-T05** [QA] Invite authorization மற்றும் no-auto-GPS சோதனை
  - **Acceptance:** Accepted invite GPS sharing-ஐ தானாகத் தொடங்காது.
  - **Trace:** `M2-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.

### M3-MS04 — Consent-based group GPS, Friends Nearby and I'm Safe

**Milestone deliverable:** Opt-in sharing, distance checks, revoke and reconnect pass
**Proposed sprint days:** 07-08 | **Dependencies:** M3-MS02; M3-MS03 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M2-MS06 | **Original target weeks:** 2

- [ ] **M3-MS04-T01** [API] Trip share consent மற்றும் revocation endpoint உருவாக்கு
  - **Acceptance:** Authenticated accepted member மட்டுமே தன் consent-ஐ மாற்றலாம்.
  - **Trace:** `M2-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS04-T02** [API] SignalR group authorization மற்றும் location events செய்
  - **Acceptance:** Trip membership/consent இல்லாத subscriber precise GPS பெற முடியாது.
  - **Trace:** `M2-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS04-T03** [Mobile] GPS publish lifecycle மற்றும் pause controls இணை
  - **Acceptance:** Active session + consent இருந்தால் மட்டும் updates அனுப்பப்படும்.
  - **Trace:** `M2-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS04-T04** [Mobile] Friends Nearby distance மற்றும் status list உருவாக்கு
  - **Acceptance:** Live/paused/offline/stale labels மற்றும் update time காட்டப்படும்.
  - **Trace:** `M2-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS04-T05** [API] I am Safe event மற்றும் separation alert rules இணை
  - **Acceptance:** Configured threshold மட்டும் alert உருவாக்கும்; stale data live என காட்டப்படாது.
  - **Trace:** `M2-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS04-T06** [API] Finish, leave, revoke cleanup இணை
  - **Acceptance:** Trip finish பின் subscriptions/location publication நிற்கும்.
  - **Trace:** `M2-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS04-T07** [QA] Two-device reconnect மற்றும் unauthorized listener சோதனை
  - **Acceptance:** Reconnect fresh state பெறும்; revoked member புதிய GPS update பெறாது.
  - **Trace:** `M2-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS04-T08** [API] Separate invitation acceptance from per-person live-location-sharing consent
  - **Acceptance:** Invite does not grant GPS visibility; consent can be revoked immediately
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M3-MS05 — Report Hazard live proof, upload and review

**Milestone deliverable:** Photo timestamp captured, safety review and upload tested
**Proposed sprint days:** 09-10 | **Dependencies:** M3-MS02 | **Task count:** 4 (4 legacy / 0 new).
**Original milestone references:** M2-MS09 | **Original target weeks:** 3

- [ ] **M3-MS05-T01** [Data] Hazard states, GPS/time மற்றும் expiry fields உருவாக்கு
  - **Acceptance:** Reported/Verified/Resolved/Expired states மற்றும் evidence references இருக்கும்.
  - **Trace:** `M2-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS05-T02** [Mobile] Live camera hazard report form உருவாக்கு
  - **Acceptance:** Active trip, category, description, GPS/time மற்றும் proof submit ஆகும்.
  - **Trace:** `M2-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS05-T03** [API] Hazard create மற்றும் allowed transition endpoints உருவாக்கு
  - **Acceptance:** Initial report unverified; reporter தன்னைத் தானே verify செய்ய முடியாது.
  - **Trace:** `M2-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS05-T04** [Admin] Hazard review/verify/resolve/expire screen உருவாக்கு
  - **Acceptance:** Authorized action reason/audit உடன் alerts-ன் active state-ஐ மாற்றும்.
  - **Trace:** `M2-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.

### M3-MS06 — Route-based 1-km hazard alerts, capture time and 24h expiry

**Milestone deliverable:** Route within 1 km only; warnings expire 24h from server report
**Proposed sprint days:** 11-12 | **Dependencies:** M3-MS05; M2-MS04 | **Task count:** 6 (3 legacy / 3 new).
**Original milestone references:** M2-MS09 | **Original target weeks:** 3

- [ ] **M3-MS06-T01** [API] Route proximity, age, direction மற்றும் cooldown match செய்
  - **Acceptance:** D08 values பயன்படுத்தி unrelated/expired hazard alerts தவிர்க்கப்படும்.
  - **Trace:** `M2-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS06-T02** [Mobile] Hazard pop-up, dismiss மற்றும் detail view இணை
  - **Acceptance:** Freshness, approximate location, verification label காட்டப்படும்.
  - **Trace:** `M2-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS06-T03** [QA] Two-user hazard, resolved மற்றும் repeated-GPS cases சோதனை
  - **Acceptance:** Relevant active trip alerts ஒருமுறை; expired/resolved மீண்டும் alert தராது.
  - **Trace:** `M2-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS06-T04** [QA] Reject stale/invalid photo time metadata and handle segment-route change rematching
  - **Acceptance:** Time spoof and route update cannot trigger unsupported hazard warnings
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M3-MS06-T05** [API] Store ReportedAtUtc server-side, expire warning at +24h and show validated photo capture time
  - **Acceptance:** Warning disappears at 24h; historic records and photo timestamp remain
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M3-MS06-T06** [API] Use 1-km distance from planned route polyline, not distance from current user position
  - **Acceptance:** Only eligible intersecting planned routes get hazard warnings
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M3-MS07 — Trip Memories and private media

**Milestone deliverable:** Trip memories private as configured; retry handles duplicates
**Proposed sprint days:** 13-14 | **Dependencies:** M3-MS02; M1-MS05 | **Task count:** 6 (6 legacy / 0 new).
**Original milestone references:** M2-MS07 | **Original target weeks:** 2

- [ ] **M3-MS07-T01** [Data] Memories மற்றும் media permissions schema உருவாக்கு
  - **Acceptance:** Trip/place/owner/media links மற்றும் public/private fields சேமிக்கப்படும்.
  - **Trace:** `M2-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS07-T02** [API] Signed upload மற்றும் size/type checks இணை
  - **Acceptance:** Owner-authorized upload; corrupt/disallowed file request மறுக்கப்படும்.
  - **Trace:** `M2-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS07-T03** [Mobile] Add Memory photo/video/caption form உருவாக்கு
  - **Acceptance:** Trip/place context மற்றும் chosen privacy save ஆகும்.
  - **Trace:** `M2-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS07-T04** [API] Post create/read/delete endpoints உருவாக்கு
  - **Acceptance:** Owner delete மட்டும் அனுமதி; private post unauthorized request மறுக்கப்படும்.
  - **Trace:** `M2-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS07-T05** [API] Media orphan cleanup மற்றும் deleted post handling செய்
  - **Acceptance:** Failed upload மற்றும் deleted links பாதுகாப்பாக cleanup செய்யப்படும்.
  - **Trace:** `M2-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS07-T06** [QA] Memory visibility மற்றும் upload retry சோதனை
  - **Acceptance:** Owner/member/public viewer cases மற்றும் duplicate upload failure evidence இருக்கும்.
  - **Trace:** `M2-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.

### M3-MS08 — Notification dispatch, reminders and Admin composer

**Milestone deliverable:** Outbox retries; Admin scheduled sends and deep links tested
**Proposed sprint days:** 15-16 | **Dependencies:** M3-MS01; M1-MS03 | **Task count:** 15 (15 legacy / 0 new).
**Original milestone references:** M2-MS01, M2-MS08, M7-MS06 | **Original target weeks:** 1, 3

- [ ] **M3-MS08-T01** [Design] Notification types மற்றும் user preferences map செய்
  - **Acceptance:** Social, trip, Hunter, Game, Coins, voucher, safety categories இருக்கும்.
  - **Trace:** `M2-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS08-T02** [Data] Notification/outbox/delivery tables உருவாக்கு
  - **Acceptance:** Unique event-recipient key, target reference மற்றும் delivery state இருக்கும்.
  - **Trace:** `M2-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS08-T03** [API] Persisted event dispatcher மற்றும் retry worker உருவாக்கு
  - **Acceptance:** FCM failure business transaction-ஐ rollback செய்யாது; retry duplicate தராது.
  - **Trace:** `M2-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS08-T04** [API] Device token registration மற்றும் FCM adapter இணை
  - **Acceptance:** Token owner சரிபார்க்கப்படும்; invalid token cleanup இருக்கும்.
  - **Trace:** `M2-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T05** [API] Trip reminder scheduling/cancel/reschedule செய்
  - **Acceptance:** Planned time change job-ஐ update செய்யும்; reminder Start event உருவாக்காது.
  - **Trace:** `M2-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T06** [API] Social, approval, Coins, voucher templates இணை
  - **Acceptance:** User preferences மதிக்கப்படும்; lock-screen-ல் private GPS இல்லை.
  - **Trace:** `M2-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T07** [Mobile] Notifications inbox, unread மற்றும் deep links உருவாக்கு
  - **Acceptance:** App reopen பின் persisted history மற்றும் current target status கிடைக்கும்.
  - **Trace:** `M2-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T08** [QA] Duplicate delivery, denied push மற்றும் reminder tests செய்
  - **Acceptance:** Push off இருந்தாலும் in-app status சரி; cancelled trip reminder வராது.
  - **Trace:** `M2-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS08-T09** [API] Composer recipient selection மற்றும் role/district filters உருவாக்கு
  - **Acceptance:** Only authorized scopes; membership/preferences rules மதிக்கப்படும்.
  - **Trace:** `M7-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T10** [Admin] Message composer, template selection மற்றும் preview உருவாக்கு
  - **Acceptance:** Sender, audience, text மற்றும் destination link preview இருக்கும்.
  - **Trace:** `M7-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T11** [API] Send/schedule/cancel commands engine-க்கு இணை
  - **Acceptance:** Unique event ID மற்றும் schedule state persisted ஆகும்.
  - **Trace:** `M7-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T12** [Admin] Bulk-send confirmation மற்றும் recipient count display செய்
  - **Acceptance:** Confirm இன்றி bulk send இல்லை; final audience count தெரியும்.
  - **Trace:** `M7-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS08-T13** [API] Sensitive text/target guard மற்றும் audit செய்
  - **Acceptance:** Private GPS/secret values push-ல் இல்லை; unapproved hotel promo scope இல்லை.
  - **Trace:** `M7-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS08-T14** [Admin] Delivery history, failed attempts மற்றும் read stats உருவாக்கு
  - **Acceptance:** Queued/sent/failed/read states engine records-க்கு பொருந்தும்.
  - **Trace:** `M7-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS08-T15** [QA] Duplicate schedule, cancelled send மற்றும் token failure tests செய்
  - **Acceptance:** Retries duplicate audience notification தராது; failure visible ஆகும்.
  - **Trace:** `M7-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M3-MS09 — Finish Trip, session history and consent cleanup

**Milestone deliverable:** Finish revokes live sharing and records accurate history
**Proposed sprint days:** 17-18 | **Dependencies:** M3-MS02; M3-MS04; M3-MS06 | **Task count:** 6 (5 legacy / 1 new).
**Original milestone references:** M3-MS06 | **Original target weeks:** 2

- [ ] **M3-MS09-T01** [API] Finish command மற்றும் start/end validation உருவாக்கு
  - **Acceptance:** StartedAt இல்லாத trip complete ஆகாது; FinishedAt server time இருக்கும்.
  - **Trace:** `M3-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS09-T02** [API] Idempotent finish மற்றும் completion eligibility செய்
  - **Acceptance:** Retry duplicate completion/count உருவாக்காது.
  - **Trace:** `M3-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS09-T03** [API] Finish event மூலம் group GPS மற்றும் monitoring நிறுத்து
  - **Acceptance:** Active subscribers மற்றும் location publish flow revoke ஆகும்.
  - **Trace:** `M3-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS09-T04** [Mobile] Trip summary மற்றும் completed history views உருவாக்கு
  - **Acceptance:** Actual date, stops, memories, route availability காட்டப்படும்.
  - **Trace:** `M3-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS09-T05** [QA] Finish-before-start, duplicate finish மற்றும் missing GPS சோதனை
  - **Acceptance:** Invalid finish மறுக்கப்படும்; fabricated route உருவாகாது.
  - **Trace:** `M3-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS09-T06** [API] On Finish Trip revoke every active group location stream and cancel pending reminders
  - **Acceptance:** No updates visible to group after trip ends
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M3-MS10 — Admin Hazard/Group safety and end-to-end acceptance

**Milestone deliverable:** Admin hazard and group module permissions and end-to-end safety tests
**Proposed sprint days:** 19-20 | **Dependencies:** M3-MS06; M3-MS08; M3-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M2-MS10, M3-MS10 | **Original target weeks:** 3

- [ ] **M3-MS10-T01** [Admin] Group Trips list மற்றும் consent-safe detail உருவாக்கு
  - **Acceptance:** Invites, member status, safety flags மற்றும் minimum location மட்டும் காட்டப்படும்.
  - **Trace:** `M2-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS10-T02** [API] Group support actions மற்றும் access audit இணை
  - **Acceptance:** Role-authorized intervention reason/actor/time பதிவு செய்யப்படும்.
  - **Trace:** `M2-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS10-T03** [QA] Friends → Invite → Start → sharing → Finish demo செய்
  - **Acceptance:** Consent revocation மற்றும் trip-finish cleanup இரண்டு சாதனங்களில் நிரூபிக்கப்படும்.
  - **Trace:** `M2-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS10-T04** [QA] Approval events மற்றும் failure recovery இணைந்து சோதனை
  - **Acceptance:** Hunter/Game/Coins events inbox-ல் ஒருமுறை வரும்; push failure status அழிக்காது.
  - **Trace:** `M2-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M3-MS10-T05** [API] Social/safety blockers மற்றும் stale-state defects சரிசெய்
  - **Acceptance:** Critical privacy/state defects retest evidence உடன் close ஆகும்.
  - **Trace:** `M2-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M3-MS10-T06** [Ops] Event contracts, run steps மற்றும் peer review இணை
  - **Acceptance:** Notifications/Hazards/Groups API docs, demo evidence மற்றும் reviewed PR இருக்கும்.
  - **Trace:** `M2-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M3-MS10-T07** [QA] Permissions மற்றும் GPS interruption regression செய்
  - **Acceptance:** Deny/pause/reconnect/finish states privacy rules-க்கு ஏற்ப இருக்கும்.
  - **Trace:** `M3-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
