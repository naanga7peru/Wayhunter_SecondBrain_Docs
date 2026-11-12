# WAYHUNTER — Detailed Task Register (490 legacy + 33 policy-aligned = 523)

**Source:** original `Wayhunter_7_Member_Work_Tracker_Dec01_2026.xlsx` 490 tasks; existing 70 old milestone IDs preserved in legacy reference. `NEW` tasks are derived implementation checkpoints, not additional BRD business decisions.

**Fields for every task:** New ID, source original ID, exact action, layer, status, acceptance definition, original estimate/target/evidence, proposed owner. `Demo - Verify` is not Accepted.

## M1 — Identity, Profile, Friends & Settings

### M1-MS01 — Identity architecture, privacy & shared UserId contract

**Milestone deliverable:** UserId, RBAC interface, profile/privacy contract approved in a PR
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 8 (8 legacy / 0 new).
**Original milestone references:** M1-MS01, M7-MS01 | **Original target weeks:** 1

- [ ] **M1-MS01-T01** [Design] Auth மற்றும் Home flow பட்டியல் தயாரி
  - **Acceptance:** Register, OTP, login, recovery, logout, Home routes பட்டியலில் இருக்கும்.
  - **Trace:** `M1-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T02** [Design] Demo login மற்றும் உண்மையான login வேறுபாடு பதிவு செய்
  - **Acceptance:** Run Guide கூறும் prototype behavior தனியாகக் குறிக்கப்பட்டிருக்கும்.
  - **Trace:** `M1-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T03** [API] UserId மற்றும் approval identity DTO ஒப்பந்தம் எழுது
  - **Acceptance:** UserId, name snapshot, item ID, server timestamp fields வரையறுக்கப்பட்டிருக்கும்.
  - **Trace:** `M1-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T04** [Design] Account status transition வரைவு அமை
  - **Acceptance:** PendingVerification, Active, Suspended, deletion நிலைகளுக்கு allowed actions இருக்கும்.
  - **Trace:** `M1-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T05** [Design] பொது profile மற்றும் private fields பிரி
  - **Acceptance:** Email, phone, private GPS public response-ல் சேராத schema இருக்கும்.
  - **Trace:** `M1-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T06** [Design] Navigation மற்றும் மொழி keys பட்டியல் தயாரி
  - **Acceptance:** Home, Profile, Friends, Wallet-ல் global leaderboard இல்லை; D01 பதிவு இருக்கும்.
  - **Trace:** `M1-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T07** [QA] Identity acceptance cases மற்றும் handoff உறுதி செய்
  - **Acceptance:** M2–M7 owners பயன்படுத்தும் user contract மற்றும் AT-REG cases review செய்யப்படும்.
  - **Trace:** `M1-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS01-T08** [API] ASP.NET shared auth hooks, errors மற்றும் API contracts அமை
  - **Acceptance:** Standard error, correlation ID, auth requirements மற்றும் route conventions இருக்கும்.
  - **Trace:** `M7-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.

### M1-MS02 — User schema, roles and database migration

**Milestone deliverable:** Identity migrations enforce uniqueness and stable UserId; QA
**Proposed sprint days:** 03-04 | **Dependencies:** M1-MS01; M7-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M1-MS02 | **Original target weeks:** 1

- [ ] **M1-MS02-T01** [Data] Users மற்றும் UserProfiles tables உருவாக்கு
  - **Acceptance:** UserId primary key, timestamps, status மற்றும் profile relation migration இயங்கும்.
  - **Trace:** `M1-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS02-T02** [Data] Email மற்றும் username uniqueness அமை
  - **Acceptance:** Case-normalized duplicate values database அளவில் மறுக்கப்படும்.
  - **Trace:** `M1-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS02-T03** [Data] Sessions, OTP மற்றும் consent storage அமை
  - **Acceptance:** Expiry, revocation, attempts மற்றும் consent timestamps சேமிக்கப்படும்.
  - **Trace:** `M1-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS02-T04** [API] Server-generated UserId வழங்கு
  - **Acceptance:** Display name edit செய்தாலும் அதே UserId தொடரும்.
  - **Trace:** `M1-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS02-T05** [API] Profile read DTO மற்றும் ownership checks எழுது
  - **Acceptance:** Owner/private/public response fields வேறுபட்டு unauthorized request மறுக்கப்படும்.
  - **Trace:** `M1-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS02-T06** [Data] Development seed users உருவாக்கு
  - **Acceptance:** Active, unverified, suspended sample accounts production secrets இன்றி கிடைக்கும்.
  - **Trace:** `M1-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS02-T07** [QA] Migration மற்றும் duplicate identity சோதனை செய்
  - **Acceptance:** Empty database setup, duplicate email, renamed profile cases evidence உடன் pass ஆகும்.
  - **Trace:** `M1-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.

### M1-MS03 — Registration, OTP and welcome eligibility event

**Milestone deliverable:** OTP expires/cooldown; verified activation event unique
**Proposed sprint days:** 05-06 | **Dependencies:** M1-MS02; M6-MS02 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M1-MS03 | **Original target weeks:** 1

- [ ] **M1-MS03-T01** [Mobile] Registration form மற்றும் field validation உருவாக்கு
  - **Acceptance:** Name, email, password, confirm errors தெளிவாகக் காட்டப்படும்.
  - **Trace:** `M1-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T02** [API] Registration endpoint மற்றும் password hashing அமை
  - **Acceptance:** Password plaintext storage/logging இல்லை; provisional user உருவாகும்.
  - **Trace:** `M1-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=4h original estimate, accepted=0.
- [ ] **M1-MS03-T03** [API] OTP provider adapter மற்றும் email template இணை
  - **Acceptance:** Provider success/failure தனித்தனியாகக் காட்டப்படும்; secret backend-ல் இருக்கும்.
  - **Trace:** `M1-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T04** [API] OTP expiry, attempts, resend cooldown செயல் படுத்து
  - **Acceptance:** Expired/reused code மற்றும் அதிக attempts மறுக்கப்படும்.
  - **Trace:** `M1-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T05** [Mobile] OTP input, resend countdown மற்றும் retry UI இணை
  - **Acceptance:** Wrong code, resend wait, network failure states இயங்கும்.
  - **Trace:** `M1-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T06** [API] Verified activation event-ஐ Coins service-க்கு அனுப்பு
  - **Acceptance:** ஒரே user activation மீண்டும் அழைத்தாலும் ஒரே welcome reward source இருக்கும்.
  - **Trace:** `M1-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T07** [QA] Registration-to-Home மற்றும் duplicate bonus சோதனை
  - **Acceptance:** Valid OTP activates account; reinstall/retry இரண்டாவது bonus தராது.
  - **Trace:** `M1-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS03-T08** [API] Verify account activation emits one welcome-eligibility event only, never posts Coins directly
  - **Acceptance:** M6 must handle +100 Coins idempotently; retries produce one ledger credit
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M1-MS04 — Login, password recovery, Admin authorization

**Milestone deliverable:** Access, reset, role checks and audit cannot be bypassed
**Proposed sprint days:** 07-08 | **Dependencies:** M1-MS02; M1-MS03 | **Task count:** 10 (9 legacy / 1 new).
**Original milestone references:** M1-MS04, M7-MS02 | **Original target weeks:** 1, 2

- [ ] **M1-MS04-T01** [API] Sign-in endpoint மற்றும் account-state gate உருவாக்கு
  - **Acceptance:** Unverified/suspended users-க்கு அனுமதிக்கப்பட்ட response மட்டும் வழங்கப்படும்.
  - **Trace:** `M1-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T02** [Mobile] Login form மற்றும் secure token storage இணை
  - **Acceptance:** Credentials persist ஆகாது; token storage மற்றும் auth redirects சோதிக்கப்படும்.
  - **Trace:** `M1-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T03** [API] Session expiry மற்றும் refresh/revocation policy செயல் படுத்து
  - **Acceptance:** Expired/revoked session protected endpoint-ஐ அணுக முடியாது.
  - **Trace:** `M1-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T04** [API] Password reset token flow உருவாக்கு
  - **Acceptance:** Single-use expiring token மட்டுமே password மாற்ற அனுமதிக்கும்.
  - **Trace:** `M1-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T05** [Mobile] Forgot/reset password screens உருவாக்கு
  - **Acceptance:** Confirm mismatch, expiry, success மற்றும் return-to-login paths இருக்கும்.
  - **Trace:** `M1-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS04-T06** [API] Logout மற்றும் password-change session invalidation செய்
  - **Acceptance:** Logout பின் பழைய session protected API call தோல்வியடையும்.
  - **Trace:** `M1-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS04-T07** [QA] Login abuse மற்றும் recovery negative cases சோதனை
  - **Acceptance:** Rate limit, invalid password, reused reset token மற்றும் logout checks evidence இருக்கும்.
  - **Trace:** `M1-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T08** [API] Admin account/role/permission model மற்றும் login gate அமை
  - **Acceptance:** Public admin signup இல்லை; non-admin token access மறுக்கப்படும்.
  - **Trace:** `M7-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS04-T09** [API] Role policies மற்றும் API authorization matrix செய்
  - **Acceptance:** Screen hidden மட்டும் அல்ல; backend permission checks அமலும் இருக்கும்.
  - **Trace:** `M7-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
  - **Existing evidence/blocker (unchanged):** evidence=—; blocker=Ads Guide p.5: Ads demo endpoints production
authorization இல்லாமல் உள்ளன. RBAC matrix-ல் admin
Ads list/create/edit/status/upload மற்றும் public
active/event routes-ஐ தனியாகச் சேர்த்து சோதிக்கவும்.
- [ ] **M1-MS04-T10** [QA] Document API authorization matrix for 17 admin modules with server-side enforcement
  - **Acceptance:** Unauthorized requests are rejected by backend, not merely hidden in Angular
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M1-MS05 — Profile editor, privacy and visibility

**Milestone deliverable:** Profile privacy access checks and edit/visibility UI pass
**Proposed sprint days:** 09-10 | **Dependencies:** M1-MS04 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M1-MS06 | **Original target weeks:** 2

- [ ] **M1-MS05-T01** [Mobile] My Profile header மற்றும் editable fields உருவாக்கு
  - **Acceptance:** Name, username, avatar, bio, public location values load ஆகும்.
  - **Trace:** `M1-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS05-T02** [API] Profile update endpoint மற்றும் validation இணை
  - **Acceptance:** Owner மட்டுமே update செய்யலாம்; duplicate username மறுக்கப்படும்.
  - **Trace:** `M1-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS05-T03** [API] Avatar media ownership மற்றும் upload authorization இணை
  - **Acceptance:** மற்ற user media ID-ஐ avatar ஆக unauthorized attach செய்ய முடியாது.
  - **Trace:** `M1-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS05-T04** [Mobile] Other User Profile view உருவாக்கு
  - **Acceptance:** Private contact/wallet/GPS தகவல் இல்லாத public DTO காட்டப்படும்.
  - **Trace:** `M1-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS05-T05** [API] Public/private privacy rules மற்றும் blocked viewer gate செய்
  - **Acceptance:** Unauthorized follower/private-trip content request server-ல் மறுக்கப்படும்.
  - **Trace:** `M1-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS05-T06** [Mobile] Edit success, cancel மற்றும் stale data refresh இணை
  - **Acceptance:** Cancel பழைய profile-ஐ காப்பாற்றும்; save பின் புதிய name காட்டப்படும்.
  - **Trace:** `M1-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS05-T07** [QA] Profile authorization மற்றும் privacy matrix சோதனை
  - **Acceptance:** Owner, follower, non-follower, blocked user cases evidence உடன் pass ஆகும்.
  - **Trace:** `M1-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.

### M1-MS06 — Followers, follow requests, blocking

**Milestone deliverable:** Follow requests, block, privacy races pass tests
**Proposed sprint days:** 11-12 | **Dependencies:** M1-MS04 | **Task count:** 10 (10 legacy / 0 new).
**Original milestone references:** M2-MS01, M2-MS02 | **Original target weeks:** 1

- [ ] **M1-MS06-T01** [Design] Social மற்றும் group user journeys வரைவு செய்
  - **Acceptance:** Profile Friends மற்றும் Trip Add Friends ஒரே screen context என்பதைக் காட்டும்.
  - **Trace:** `M2-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS06-T02** [Data] Follows, requests, blocks மற்றும் trip invite schema உருவாக்கு
  - **Acceptance:** Directed follow, accepted membership, GPS consent தனி relations ஆக இருக்கும்.
  - **Trace:** `M2-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS06-T03** [API] Follow/invite event payload ஒப்பந்தம் எழுது
  - **Acceptance:** Actor, recipient, entity ID, state version மற்றும் event ID இருக்கும்.
  - **Trace:** `M2-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS06-T04** [Data] Follow மற்றும் request uniqueness constraints அமை
  - **Acceptance:** Self-follow மற்றும் duplicate active relation சேமிக்க முடியாது.
  - **Trace:** `M2-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS06-T05** [API] Public follow/unfollow endpoints எழுது
  - **Acceptance:** Authenticated user மட்டும் தன் directed relation-ஐ மாற்றலாம்.
  - **Trace:** `M2-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS06-T06** [API] Private follow approve/decline/cancel commands எழுது
  - **Acceptance:** Target owner மட்டுமே pending request-ஐ முடிக்க முடியும்.
  - **Trace:** `M2-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS06-T07** [API] Block/unblock மற்றும் protected content rules இணை
  - **Acceptance:** Blocked profile/private trip access மற்றும் invitations மறுக்கப்படும்.
  - **Trace:** `M2-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS06-T08** [API] Followers/following counts மற்றும் search endpoint உருவாக்கு
  - **Acceptance:** Counts persisted relation states-க்கு பொருந்தும்; pagination இருக்கும்.
  - **Trace:** `M2-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS06-T09** [API] Follow transition notification events வெளியிடு
  - **Acceptance:** ஒரே accepted transition மீண்டும் duplicate notification தராது.
  - **Trace:** `M2-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS06-T10** [QA] Follow race, duplicate மற்றும் privacy cases சோதனை
  - **Acceptance:** Simultaneous requests unique relation-ஐ காப்பாற்றும்; blocked user tests pass.
  - **Trace:** `M2-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.

### M1-MS07 — Friends screen, native invites and opt-in contact discovery

**Milestone deliverable:** Invitations/contacts require permission and support revoke
**Proposed sprint days:** 13-14 | **Dependencies:** M1-MS06; M2-MS02 | **Task count:** 17 (16 legacy / 1 new).
**Original milestone references:** M2-MS03, M2-MS04, M2-MS05 | **Original target weeks:** 2

- [ ] **M1-MS07-T01** [Mobile] Followers/Following tabs மற்றும் user cards உருவாக்கு
  - **Acceptance:** Search, count, follow/follow-back/unfollow states சரியாகக் காட்டப்படும்.
  - **Trace:** `M2-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T02** [Mobile] Private follow requests inbox உருவாக்கு
  - **Acceptance:** Accept/Decline action பின் authoritative state refresh ஆகும்.
  - **Trace:** `M2-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T03** [Mobile] Profile entry context மற்றும் return navigation இணை
  - **Acceptance:** Profile-ல் follower count tap அதே Friends view-ஐ திறக்கும்.
  - **Trace:** `M2-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T04** [Mobile] Trip context selection மற்றும் draft return இணை
  - **Acceptance:** Friends page-ல் இருந்து திரும்பும்போது trip draft values அழியாது.
  - **Trace:** `M2-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T05** [Mobile] Native OS share chooser மற்றும் app link இணை
  - **Acceptance:** Installed sharing apps மட்டும் chooser-ல் வரும்; Gmail API தேவையில்லை.
  - **Trace:** `M2-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T06** [Mobile] Empty/error/permission explanation states சேர்க்க
  - **Acceptance:** No matches மற்றும் network failure நிலைகளுக்கு actionable retry இருக்கும்.
  - **Trace:** `M2-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T07** [QA] இரண்டு entry routes மற்றும் native invite சோதனை
  - **Acceptance:** Profile/Trip இரண்டிலும் ஒரே behavior; app link open flow evidence இருக்கும்.
  - **Trace:** `M2-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T08** [Mobile] Contacts purpose மற்றும் permission prompt உருவாக்கு
  - **Acceptance:** Permission deny செய்தாலும் normal app usage தொடரும்.
  - **Trace:** `M2-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T09** [API] Discoverability consent update endpoint உருவாக்கு
  - **Acceptance:** Opt-in/opt-out timestamp மற்றும் preference சேமிக்கப்படும்.
  - **Trace:** `M2-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T10** [API] Minimized contact match endpoint உருவாக்கு
  - **Acceptance:** Approved D07 method மூலம் eligible registered matches மட்டும் திரும்பும்.
  - **Trace:** `M2-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=4h original estimate, accepted=0.
- [ ] **M1-MS07-T11** [Mobile] My Contacts matched account list மற்றும் Follow இணை
  - **Acceptance:** Raw address book/non-user contacts public results-ல் காட்டப்படாது.
  - **Trace:** `M2-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T12** [API] Contact match rate limit மற்றும் retention control செய்
  - **Acceptance:** Bulk enumeration requests கட்டுப்படும்; தேவையற்ற raw contacts persist ஆகாது.
  - **Trace:** `M2-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T13** [Mobile] Consent revoke மற்றும் denied retry behavior இணை
  - **Acceptance:** Revoke பின் புதிய matching நிற்கும்; cached matches refresh/clear ஆகும்.
  - **Trace:** `M2-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T14** [QA] Contacts privacy மற்றும் no-match cases சோதனை
  - **Acceptance:** Non-discoverable account மறைக்கப்படும்; deny/revoke/no-match evidence இருக்கும்.
  - **Trace:** `M2-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T15** [Mobile] Trip invitation list மற்றும் accept/decline UI உருவாக்கு
  - **Acceptance:** Recipient-ன் pending invite action பின் membership refresh ஆகும்.
  - **Trace:** `M2-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS07-T16** [Mobile] Create Trip draft-ல் selected/accepted friends காட்டி இணை
  - **Acceptance:** Pending மற்றும் accepted invitees தனித்தனியாகத் தெரியும்.
  - **Trace:** `M2-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS07-T17** [QA] Require explicit contacts consent and reversible discoverability without exposing address book
  - **Acceptance:** Denied/revoked consent leaves no contact-upload capability or stale match results
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M1-MS08 — Profile tabs, languages, settings and cross-module links

**Milestone deliverable:** Profile tabs route safely; language & shared rewards are read-only
**Proposed sprint days:** 15-16 | **Dependencies:** M1-MS05; M1-MS06; M7-MS01 | **Task count:** 17 (17 legacy / 0 new).
**Original milestone references:** M1-MS05, M1-MS07, M1-MS08, M2-MS07 | **Original target weeks:** 2, 3

- [ ] **M1-MS08-T01** [Mobile] Profile மூலம் Wallet மற்றும் Friends routes இணை
  - **Acceptance:** Wallet தனி bottom-nav ஆக வராது; safe back navigation இருக்கும்.
  - **Trace:** `M1-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T02** [Mobile] Tamil, Sinhala, English localization keys சேர்க்க
  - **Acceptance:** Language choice save ஆகும்; குறைந்த திரையில் text overflow இல்லை.
  - **Trace:** `M1-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=4h original estimate, accepted=0.
- [ ] **M1-MS08-T03** [API] Profile summary aggregate endpoint உருவாக்கு
  - **Acceptance:** Games, posts, trips, hunts counts authenticated domain data-லிருந்து வரும்.
  - **Trace:** `M1-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS08-T04** [Mobile] Games tab-ஐ My Games மற்றும் history-க்கு இணை
  - **Acceptance:** Pending result verified win ஆக காட்டப்படாது.
  - **Trace:** `M1-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T05** [Mobile] Posts tab மற்றும் Post Details entry இணை
  - **Acceptance:** Visibility/ownership விதிகள் list மற்றும் detail-ல் ஒன்றாக இருக்கும்.
  - **Trace:** `M1-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T06** [Mobile] Trips tab upcoming/completed grouping இணை
  - **Acceptance:** Actual completion இல்லாத trip completed group-ல் வராது.
  - **Trace:** `M1-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T07** [Mobile] Hunt Places tab-ஐ My Hunts-க்கு இணை
  - **Acceptance:** Owner Pending/Approved/Rejected நிலைகள் பார்க்க முடியும்.
  - **Trace:** `M1-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T08** [Mobile] Level star, badge மற்றும் Wallet shortcut இணை
  - **Acceptance:** Coins service lifetime-earned progress காட்டும்; redeem செய்ததால் level குறையாது.
  - **Trace:** `M1-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T09** [QA] Cross-module profile counts மற்றும் routes சோதனை
  - **Acceptance:** புதிய approval/finish பின் counts refresh ஆகும்; private values leak இல்லை.
  - **Trace:** `M1-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS08-T10** [Mobile] Settings home மற்றும் category routes உருவாக்கு
  - **Acceptance:** Security, language, privacy, notifications, help, about, delete, logout entries இருக்கும்.
  - **Trace:** `M1-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T11** [API] Password change endpoint மற்றும் confirmation இணை
  - **Acceptance:** Current password verified; mismatch மற்றும் unauthorized changes மறுக்கப்படும்.
  - **Trace:** `M1-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS08-T12** [API] Language/privacy/notification preferences சேமி
  - **Acceptance:** Reopen பின் backend-saved preferences திரும்ப வரும்.
  - **Trace:** `M1-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T13** [Mobile] Help, FAQ மற்றும் issue submission form இணை
  - **Acceptance:** Required fields மற்றும் support request reference காட்டப்படும்.
  - **Trace:** `M1-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T14** [Mobile] About, version, terms மற்றும் policy links சேர்க்க
  - **Acceptance:** Release build-ன் உண்மையான version மற்றும் approved links காட்டப்படும்.
  - **Trace:** `M1-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS08-T15** [API] Deletion request மற்றும் identity confirmation flow உருவாக்கு
  - **Acceptance:** D12 retention/Coins policy பதிவு இல்லாமல் destructive production delete செயல்படாது.
  - **Trace:** `M1-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M1-MS08-T16** [QA] Settings persistence மற்றும் cancel/re-auth paths சோதனை
  - **Acceptance:** Delete cancel, wrong identity, changed language மற்றும் logout cases pass ஆகும்.
  - **Trace:** `M1-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS08-T17** [Mobile] Post Details மற்றும் trip memory list இணை
  - **Acceptance:** Public/private data source-க்கு ஏற்ப media மற்றும் caption காட்டப்படும்.
  - **Trace:** `M2-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.

### M1-MS09 — Admin authentication, Users, Security & Audit Logs

**Milestone deliverable:** Admin settings/users audit, role restrictions and route guards pass
**Proposed sprint days:** 17-18 | **Dependencies:** M1-MS04; M7-MS08 | **Task count:** 14 (14 legacy / 0 new).
**Original milestone references:** M1-MS09, M7-MS02, M7-MS08 | **Original target weeks:** 1, 3

- [ ] **M1-MS09-T01** [API] Admin user search/filter endpoint உருவாக்கு
  - **Acceptance:** UserId/name/status/district filters மற்றும் pagination வேலை செய்யும்.
  - **Trace:** `M1-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T02** [Admin] Users list மற்றும் user detail views உருவாக்கு
  - **Acceptance:** Immutable ID, name, account status மற்றும் allowed summaries காட்டப்படும்.
  - **Trace:** `M1-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T03** [API] Warn/Suspend/Reactivate commands உருவாக்கு
  - **Acceptance:** Permitted role, reason, actor/time மற்றும் prior/new state பதிவு செய்யப்படும்.
  - **Trace:** `M1-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T04** [Admin] Sensitive action confirmation மற்றும் reason form இணை
  - **Acceptance:** Empty reason submit ஆகாது; latest state refresh ஆகும்.
  - **Trace:** `M1-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS09-T05** [API] User detail-ல் domain summaries இணை
  - **Acceptance:** Trip/hunt/game/Coins data read-only; casual balance edit இல்லை.
  - **Trace:** `M1-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS09-T06** [QA] Suspension தாக்கத்தை domain owners உடன் சோதனை
  - **Acceptance:** New submissions/redeems session policy-க்கு ஏற்ப மறுக்கப்படும்.
  - **Trace:** `M1-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T07** [QA] Private data மற்றும் non-admin endpoint access சோதனை
  - **Acceptance:** Unauthorized user 403 பெறும்; private GPS/export fields வெளியே வராது.
  - **Trace:** `M1-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T08** [Admin] Admin login, forgot/reset மற்றும் session UI இணை
  - **Acceptance:** Generic login errors, timeout மற்றும் logout behavior இருக்கும்.
  - **Trace:** `M7-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T09** [API] Admin action audit context மற்றும் sensitive-log redaction செய்
  - **Acceptance:** Actor/time/target/before-after recorded; secrets/OTP log ஆகாது.
  - **Trace:** `M7-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS09-T10** [QA] Admin role, session timeout மற்றும் route-bypass tests செய்
  - **Acceptance:** Ordinary user direct URL/API மூலமும் forbidden action செய்ய முடியாது.
  - **Trace:** `M7-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T11** [API] Config versions மற்றும் sensitive-setting role checks உருவாக்கு
  - **Acceptance:** Economic/safety changes reason/actor/version உடன் save ஆகும்.
  - **Trace:** `M7-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T12** [Admin] Media/GPS/expiry/threshold settings UI உருவாக்கு
  - **Acceptance:** D03/D05/D08/D10 values validated; effective rules domain owners-க்கு கிடைக்கும்.
  - **Trace:** `M7-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T13** [Admin] Admin roles, permissions மற்றும் audit search உருவாக்கு
  - **Acceptance:** Only permitted role admin management செய்யலாம்; actions audited.
  - **Trace:** `M7-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS09-T14** [QA] Invalid configuration மற்றும் unauthorized config change tests செய்
  - **Acceptance:** Past transactions retain historic rules; invalid thresholds reject ஆகும்.
  - **Trace:** `M7-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M1-MS10 — M1 API/Flutter/Admin full-stack acceptance

**Milestone deliverable:** M1 integration run with test logs and review evidence
**Proposed sprint days:** 19-20 | **Dependencies:** M1-MS08; M1-MS09 | **Task count:** 8 (8 legacy / 0 new).
**Original milestone references:** M1-MS10, M2-MS10 | **Original target weeks:** 3

- [ ] **M1-MS10-T01** [QA] Registration முதல் profile வரை end-to-end flow நடத்தி பதிவு செய்
  - **Acceptance:** OTP, login, profile edit, settings மற்றும் logout evidence ஒரே test run-ல் இருக்கும்.
  - **Trace:** `M1-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS10-T02** [QA] Account ownership மற்றும் ID stability regression செய்
  - **Acceptance:** Name change அனைத்து approval queues-லும் stable UserId-ஐ மாற்றாது.
  - **Trace:** `M1-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS10-T03** [QA] Offline மற்றும் expired session handling சோதனை
  - **Acceptance:** Sensitive data stale state-ல் unauthorized காட்டப்படாது; retry path இருக்கும்.
  - **Trace:** `M1-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS10-T04** [QA] மூன்று மொழி மற்றும் accessibility review முடி
  - **Acceptance:** Labels, contrast, touch targets மற்றும் text scale defects பதிவு/சரி செய்யப்படும்.
  - **Trace:** `M1-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS10-T05** [API] Identity integration defects சரிசெய்
  - **Acceptance:** Module blocker defects close ஆகி reviewer மீண்டும் சோதித்திருப்பார்.
  - **Trace:** `M1-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M1-MS10-T06** [Ops] Auth configuration மற்றும் local run guide புதுப்பி
  - **Acceptance:** Secrets இன்றி env key names, migrations, seed/run steps இருக்கும்.
  - **Trace:** `M1-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS10-T07** [QA] Peer review, PR மற்றும் demo evidence இணை
  - **Acceptance:** Accepted tasks-க்கு approved review மற்றும் evidence link tracker-ல் இருக்கும்.
  - **Trace:** `M1-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M1-MS10-T08** [QA] Contacts, blocks மற்றும் private posts regression செய்
  - **Acceptance:** Revoked/blocked viewers protected content பெறமாட்டார்கள்.
  - **Trace:** `M2-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.

## M2 — Traveler Planning, Maps & AI

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

## M3 — Active Trip, Safety & Notifications

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

## M4 — Hunter & Places

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

## M5 — Games, Anti-Cheat & Leaderboard

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

## M6 — Coins, Wallet & Vouchers

### M6-MS01 — Coins-only rules, levels and transactions contract

**Milestone deliverable:** Only Coins, one source of truth, 2000 level-bar semantics
**Proposed sprint days:** 01-02 | **Dependencies:** None | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS01 | **Original target weeks:** 1

- [ ] **M6-MS01-T01** [Design] Coins reward மற்றும் accounting rule table தயாரி
  - **Acceptance:** Welcome 100, Hunter 200, creator 100, eligible player 100 என்ற source rules இருக்கும்.
  - **Trace:** `M6-MS01-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T02** [Design] Available, Reserved, Total மற்றும் Lifetime Earned விளக்கம் எழுது
  - **Acceptance:** ஒரே currency-ன் distinct fields; balance versus earned distinction தெளிவாக இருக்கும்.
  - **Trace:** `M6-MS01-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T03** [API] Reward grant/reverse DTO மற்றும் unique source key ஒப்பந்தம் செய்
  - **Acceptance:** RewardType+SourceId+RecipientUserId contract அனைத்து owners-க்கும் கிடைக்கும்.
  - **Trace:** `M6-MS01-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T04** [Design] Level increment மற்றும் redemption threshold decisions பதிவு செய்
  - **Acceptance:** 2,000 earned threshold; D05 > அல்லது >= 10,000 open என்று இருக்கும்.
  - **Trace:** `M6-MS01-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T05** [Design] Cash reference மற்றும் actual fulfillment boundary பதிவு செய்
  - **Acceptance:** 10,000 Coins=LKR100 reference; D06 live cash/partner readiness உறுதி தேவை.
  - **Trace:** `M6-MS01-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T06** [Design] Old HP/RC/XP removal மற்றும் migration decision எழுது
  - **Acceptance:** Invented conversion இல்லை; old balances இருந்தால் D13 approved migration தேவை.
  - **Trace:** `M6-MS01-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS01-T07** [QA] Ledger/redeem concurrency மற்றும் rollback test cases தயாரி
  - **Acceptance:** Double credit, double hold, approve/reject race, voucher stock cases இருக்கும்.
  - **Trace:** `M6-MS01-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-11, estimate=2h original estimate, accepted=0.

### M6-MS02 — Authoritative append-only ledger and spendable balance

**Milestone deliverable:** Concurrent wallet writes cannot overspend or duplicate ledger
**Proposed sprint days:** 03-04 | **Dependencies:** M6-MS01; M1-MS02 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS02 | **Original target weeks:** 1

- [ ] **M6-MS02-T01** [Data] Wallets, transactions, reservations மற்றும் rule versions schema செய்
  - **Acceptance:** Integer Coins, decimal LKR reference, immutable transaction/source IDs இருக்கும்.
  - **Trace:** `M6-MS02-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS02-T02** [Data] Unique reward/idempotency மற்றும் version constraints அமை
  - **Acceptance:** Duplicate source-recipient credit database constraint-ல் மறுக்கப்படும்.
  - **Trace:** `M6-MS02-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS02-T03** [API] Transactional ledger write மற்றும் wallet projection செய்
  - **Acceptance:** Ledger sum மற்றும் available/reserved totals reconcile ஆகும்.
  - **Trace:** `M6-MS02-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS02-T04** [API] Wallet read API மற்றும் owner/role authorization உருவாக்கு
  - **Acceptance:** Private wallet unauthorized profile response-ல் கிடைக்காது.
  - **Trace:** `M6-MS02-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS02-T05** [API] Compensating correction entry model உருவாக்கு
  - **Acceptance:** Existing ledger row overwrite/delete இல்லாமல் reversal reference இருக்கும்.
  - **Trace:** `M6-MS02-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS02-T06** [API] Money/Coins arithmetic மற்றும் bounds validation செய்
  - **Acceptance:** Negative/overflow/unapproved amount மற்றும் floating rounding mismatch மறுக்கப்படும்.
  - **Trace:** `M6-MS02-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS02-T07** [QA] Ledger balance, rollback மற்றும் concurrent credit tests செய்
  - **Acceptance:** Failure partial balance உருவாக்காது; duplicate key ஒரு credit மட்டும் தரும்.
  - **Trace:** `M6-MS02-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=1, due=2026-11-14, estimate=4h original estimate, accepted=0.

### M6-MS03 — Idempotent welcome, Hunter and Game coin events

**Milestone deliverable:** Reward events +100/+200/+100/+100 idempotent
**Proposed sprint days:** 05-06 | **Dependencies:** M6-MS02; M1-MS03; M4-MS07; M5-MS07 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS03 | **Original target weeks:** 2

- [ ] **M6-MS03-T01** [API] Verified first-account welcome handler உருவாக்கு
  - **Acceptance:** ஒரே eligible activated user-க்கு 100 Coins மட்டும் வழங்கப்படும்.
  - **Trace:** `M6-MS03-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS03-T02** [API] Approved Hunter reward handler இணை
  - **Acceptance:** Admin-approved eligible submission-க்கு 200 Coins ஒரு source reference உடன் வரும்.
  - **Trace:** `M6-MS03-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS03-T03** [API] Approved created-game reward handler இணை
  - **Acceptance:** Published approved game creator-க்கு 100 Coins once கிடைக்கும்.
  - **Trace:** `M6-MS03-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS03-T04** [API] Admin-approved player result handler இணை
  - **Acceptance:** D02 eligible result மட்டும் 100 Coins பெறும்; pending/reject 0.
  - **Trace:** `M6-MS03-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS03-T05** [API] Outbox/retry மற்றும் reward reconciliation job செய்
  - **Acceptance:** Approval committed ஆனால் notification/reward processing retry safely recover ஆகும்.
  - **Trace:** `M6-MS03-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS03-T06** [API] Reward events-ஐ notification மற்றும் ranking consumers-க்கு இணை
  - **Acceptance:** Source module/category மற்றும் confirmed state payload-ல் இருக்கும்.
  - **Trace:** `M6-MS03-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS03-T07** [QA] Repeated events மற்றும் partial failure matrix சோதனை
  - **Acceptance:** All four sources retry பின் balance/ledger count சரியாக இருக்கும்.
  - **Trace:** `M6-MS03-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-17, estimate=4h original estimate, accepted=0.

### M6-MS04 — Wallet dashboard, 2000-coin progress and history

**Milestone deliverable:** Wallet & history stay consistent across app/admin
**Proposed sprint days:** 07-08 | **Dependencies:** M6-MS02; M6-MS03 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M6-MS04 | **Original target weeks:** 2

- [ ] **M6-MS04-T01** [API] Wallet summary மற்றும் lifetime-earned level calculation செய்
  - **Acceptance:** D11-approved initial-level formula மற்றும் 2,000 earned boundary சரியாக இருக்கும்.
  - **Trace:** `M6-MS04-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS04-T02** [Mobile] Wallet balances மற்றும் star/progress bar உருவாக்கு
  - **Acceptance:** Available/Reserved/Total Earned labels குழப்பமின்றி தெரியும்.
  - **Trace:** `M6-MS04-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS04-T03** [API] Transaction history filters மற்றும் pagination உருவாக்கு
  - **Acceptance:** Reward/hold/debit/release/correction source IDs மற்றும் timestamps வரும்.
  - **Trace:** `M6-MS04-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS04-T04** [Mobile] Transaction history மற்றும் detail view உருவாக்கு
  - **Acceptance:** Pending/final status மற்றும் Coins direction தெளிவாகக் காட்டப்படும்.
  - **Trace:** `M6-MS04-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS04-T05** [Mobile] Wallet Rules மற்றும் conversion reference panel உருவாக்கு
  - **Acceptance:** Actual cash-out enabled என்று தவறாகக் காட்டாது; applicable rule version தெரியும்.
  - **Trace:** `M6-MS04-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS04-T06** [API] Profile level மற்றும் module ranking read contracts இணை
  - **Acceptance:** Spendable amount மற்றும் lifetime earned source mix ஆகாது.
  - **Trace:** `M6-MS04-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS04-T07** [QA] 1,999/2,000/2,001 level மற்றும் spend tests செய்
  - **Acceptance:** Agreed level formula boundary சரி; redeem மட்டும் level குறைக்காது.
  - **Trace:** `M6-MS04-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS04-T08** [API] Calculate level progress on lifetime earned Coins with a 2000-Coin level-bar baseline
  - **Acceptance:** Profile/wallet UI reads one server source; legacy currencies hidden
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M6-MS05 — Voucher offers, catalog and 10100-coin eligibility

**Milestone deliverable:** At least 10100 spendable for a 10000 redemption request
**Proposed sprint days:** 09-10 | **Dependencies:** M6-MS02; M6-MS04 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M6-MS05 | **Original target weeks:** 2

- [ ] **M6-MS05-T01** [Data] Partners, offers, stock மற்றும் redemption requests schema செய்
  - **Acceptance:** Offer validity, Coins price, supplier reference மற்றும் owner fields இருக்கும்.
  - **Trace:** `M6-MS05-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T02** [API] Available offers query மற்றும் eligibility checks செய்
  - **Acceptance:** Expired/inactive/no-stock offers eligible redeem என்று வராது.
  - **Trace:** `M6-MS05-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T03** [Mobile] Redeem Rewards catalogue மற்றும் request form உருவாக்கு
  - **Acceptance:** Coins requirement, reference LKR, merchant terms மற்றும் validity தெரியும்.
  - **Trace:** `M6-MS05-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T04** [API] Approved threshold மற்றும் amount validation செய்
  - **Acceptance:** D05 selected > அல்லது >= policy boundary test pass ஆகும்.
  - **Trace:** `M6-MS05-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T05** [Mobile] Confirm Request preview மற்றும் cancellation UI செய்
  - **Acceptance:** Requested Coins, expected available amount மற்றும் confirmation காட்டப்படும்.
  - **Trace:** `M6-MS05-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS05-T06** [API] Redemption idempotency மற்றும் request identity அமை
  - **Acceptance:** UserId/name/request ID/server timestamp; duplicate click same request தரும்.
  - **Trace:** `M6-MS05-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T07** [QA] Threshold, expired offer மற்றும் insufficient balance tests செய்
  - **Acceptance:** Invalid request reservation/debit உருவாக்காது.
  - **Trace:** `M6-MS05-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-20, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS05-T08** [API] Enforce spendable balance >=10100 before requesting the 10000 Coins sample voucher
  - **Acceptance:** User with 10000 is rejected; with 10100 can request and retains >=100 afterward
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M6-MS06 — Reserve 10000 pending, Admin Approve debit once, reject release

**Milestone deliverable:** Pending reserves 10000; approve final debit once; reject releases
**Proposed sprint days:** 11-12 | **Dependencies:** M6-MS05; M1-MS04 | **Task count:** 8 (7 legacy / 1 new).
**Original milestone references:** M6-MS06 | **Original target weeks:** 2

- [ ] **M6-MS06-T01** [API] Transactional hold மற்றும் spendable balance validation செய்
  - **Acceptance:** Pending request reserved amount மட்டும் உயர்த்தும்; double spend தடுக்கப்படும்.
  - **Trace:** `M6-MS06-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS06-T02** [Mobile] Request Status மற்றும் pending balance labels உருவாக்கு
  - **Acceptance:** Total/current/available/reserved வேறுபாடு தெளிவாக காட்டப்படும்.
  - **Trace:** `M6-MS06-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS06-T03** [Admin] Redemption queue மற்றும் held Coins/stock review உருவாக்கு
  - **Acceptance:** Requester UserId/name, amount, terms, hold மற்றும் supplier stock தெரியும்.
  - **Trace:** `M6-MS06-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS06-T04** [API] Approve command மற்றும் final debit transaction உருவாக்கு
  - **Acceptance:** Sufficient valid hold மற்றும் stock/capacity இருந்தால் once debit finalize ஆகும்.
  - **Trace:** `M6-MS06-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS06-T05** [API] Reject/cancel command மற்றும் release transaction செய்
  - **Acceptance:** Reason/audit உடன் hold release; duplicate credit இல்லை.
  - **Trace:** `M6-MS06-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS06-T06** [Admin] Approve/reject confirmation மற்றும் stale request handling செய்
  - **Acceptance:** Conflicting second decision success எனக் காட்டப்படாது.
  - **Trace:** `M6-MS06-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS06-T07** [QA] Concurrent requests மற்றும் approve/reject race சோதனை
  - **Acceptance:** Overspend/negative available/duplicate debit/release எதுவும் நிகழாது.
  - **Trace:** `M6-MS06-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=2, due=2026-11-22, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS06-T08** [QA] Separate Pending 10000-Coin reservation from final debit; approve consumes hold once
  - **Acceptance:** Duplicate approve/reject and concurrent requests cannot double debit/release
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M6-MS07 — Sample voucher unique code/QR issuance and retry

**Milestone deliverable:** QR and unique code displayed only after successful issuance; retries safe
**Proposed sprint days:** 13-14 | **Dependencies:** M6-MS06 | **Task count:** 9 (7 legacy / 2 new).
**Original milestone references:** M6-MS07 | **Original target weeks:** 3

- [ ] **M6-MS07-T01** [API] Unique voucher allocation மற்றும் stock reservation செய்
  - **Acceptance:** ஒரே code இரண்டு users-க்கு issue ஆகாது; failed allocation safe recovery இருக்கும்.
  - **Trace:** `M6-MS07-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS07-T02** [API] Fulfillment state மற்றும் supplier settlement reference செய்
  - **Acceptance:** Approved மற்றும் Issued/Fulfilled தனித்தனி states; actual proof reference இருக்கும்.
  - **Trace:** `M6-MS07-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS07-T03** [Mobile] My Vouchers Pending/Issued/Used/Expired list உருவாக்கு
  - **Acceptance:** Unissued item usable code/QR போலக் காட்டப்படாது.
  - **Trace:** `M6-MS07-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS07-T04** [Mobile] Voucher Details மற்றும் secure owner access உருவாக்கு
  - **Acceptance:** Genuine code/QR, amount, expiry மற்றும் merchant terms தெரியும்.
  - **Trace:** `M6-MS07-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS07-T05** [API] One-use validation மற்றும் usage audit endpoint உருவாக்கு
  - **Acceptance:** Repeated redeem/consume already-used voucher-ஐ மறுக்கும்.
  - **Trace:** `M6-MS07-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS07-T06** [API] Expiry/revocation மற்றும் failed fulfillment reconciliation செய்
  - **Acceptance:** No fake cash-success; policy-defined correction/release references பதிவு செய்யப்படும்.
  - **Trace:** `M6-MS07-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS07-T07** [QA] Concurrent code issue, wrong owner மற்றும் used/expired tests செய்
  - **Acceptance:** Stock/ledger/assignment reconcile; unauthorized voucher code access இல்லை.
  - **Trace:** `M6-MS07-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS07-T08** [Mobile] Display demo voucher QR, sample image, unique code only to eligible owner
  - **Acceptance:** No voucher appears as issued before successful issuance
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.
- [ ] **M6-MS07-T09** [API] Issue unique sample voucher image/code/QR after approved debit with resumable issuance
  - **Acceptance:** Issue failure retains approved-unissued state and retry never debits again
  - **Trace:** `NEW from approved-rule/architecture` | Original status: `Not Started` | Review: `Not reviewed` | Source: Derived from latest approved rules / architecture; new planning task
  - **Original reference fields:** week=—, due=—, estimate=—, accepted=0.

### M6-MS08 — Admin Coins, offers, voucher inventory and redemption

**Milestone deliverable:** Admin role-gated review, inventory and audit pass
**Proposed sprint days:** 15-16 | **Dependencies:** M6-MS07; M1-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS08 | **Original target weeks:** 3

- [ ] **M6-MS08-T01** [Admin] Wallet search, ledger மற்றும் level read views உருவாக்கு
  - **Acceptance:** UserId/name search; available/reserved/earned மற்றும் source references இருக்கும்.
  - **Trace:** `M6-MS08-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS08-T02** [API] Privileged correction/reversal command உருவாக்கு
  - **Acceptance:** Reason, approval policy, compensating entry மற்றும் actor audit கட்டாயம்.
  - **Trace:** `M6-MS08-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS08-T03** [Admin] Partner directory மற்றும் agreement metadata form உருவாக்கு
  - **Acceptance:** Approved contract/reference இல்லாத offer live eligibility பெறாது.
  - **Trace:** `M6-MS08-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS08-T04** [Admin] Offer stock/code import மற்றும் validation உருவாக்கு
  - **Acceptance:** Duplicate/invalid/expired voucher inventory import மறுக்கப்படும்.
  - **Trace:** `M6-MS08-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS08-T05** [Admin] Settlement status மற்றும் fulfillment exception view உருவாக்கு
  - **Acceptance:** Pending issue, stock shortage, failed delivery மற்றும் proof reference தெரியும்.
  - **Trace:** `M6-MS08-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS08-T06** [API] Coins rules versioning மற்றும் historic terms preservation செய்
  - **Acceptance:** New reward values past transactions-ஐ மறுகணக்கிடாது.
  - **Trace:** `M6-MS08-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS08-T07** [QA] Admin role isolation மற்றும் unauthorized correction tests செய்
  - **Acceptance:** User Management-ல் casual balance edit இல்லை; forbidden role write reject ஆகும்.
  - **Trace:** `M6-MS08-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-24, estimate=3h original estimate, accepted=0.

### M6-MS09 — Audit, ledger reconciliation and data migration controls

**Milestone deliverable:** Existing ledger reconciliation and immutable audit preserved
**Proposed sprint days:** 17-18 | **Dependencies:** M6-MS08 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS09 | **Original target weeks:** 3

- [ ] **M6-MS09-T01** [Ops] Existing HP/RC/XP data inventory ஆய்வு செய்
  - **Acceptance:** Old data இருக்கிறதா என்ற evidence மற்றும் D13 migration decision பதிவு இருக்கும்.
  - **Trace:** `M6-MS09-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS09-T02** [Data] Approved migration அல்லது clean-seed pathway செயல் படுத்து
  - **Acceptance:** Invented exchange இல்லை; backup/dry-run/reconciliation report இருக்கும்.
  - **Trace:** `M6-MS09-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS09-T03** [QA] Mobile/Admin obsolete currency labels scan செய்
  - **Acceptance:** HP/RC/XP active labels/business formulas இல்லாததை evidence உறுதிசெய்யும்.
  - **Trace:** `M6-MS09-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS09-T04** [API] Minted/reserved/debited/released aggregate endpoints உருவாக்கு
  - **Acceptance:** M7 dashboard/report totals authoritative ledger-க்கு பொருந்தும்.
  - **Trace:** `M6-MS09-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS09-T05** [API] Wallet/ledger/stock exception reconciliation query உருவாக்கு
  - **Acceptance:** Unbalanced hold, orphan code மற்றும் duplicate source diagnostics கிடைக்கும்.
  - **Trace:** `M6-MS09-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS09-T06** [QA] Fraud correction மற்றும் leaderboard/lifetime update சோதனை
  - **Acceptance:** Valid earned totals மற்றும் module ranks agreed reversal policy-க்கு ஏற்ப புதுப்படும்.
  - **Trace:** `M6-MS09-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS09-T07** [Ops] Partner/cash release readiness மற்றும் terms பதிவு செய்
  - **Acceptance:** D06 unresolved என்றால் real cash payout disabled; demo clearly labelled.
  - **Trace:** `M6-MS09-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-26, estimate=2h original estimate, accepted=0.

### M6-MS10 — Wallet redemption concurrency and demo acceptance

**Milestone deliverable:** Double approve/race/issue failure scenarios accepted
**Proposed sprint days:** 19-20 | **Dependencies:** M6-MS09 | **Task count:** 7 (7 legacy / 0 new).
**Original milestone references:** M6-MS10 | **Original target weeks:** 3

- [ ] **M6-MS10-T01** [QA] Reward sources முதல் wallet வரை full demo செய்
  - **Acceptance:** Welcome/Hunter/Game balances மற்றும் ledger source counts reconcile ஆகும்.
  - **Trace:** `M6-MS10-T01` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS10-T02** [QA] Redeem approve/reject/fulfill end-to-end சோதனை
  - **Acceptance:** Pending hold, final debit, release மற்றும் issued voucher correct ஆகும்.
  - **Trace:** `M6-MS10-T02` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS10-T03** [QA] Concurrent overspend/reward/voucher retry suite நடத்து
  - **Acceptance:** Double-spend, duplicate credit/debit மற்றும் duplicate code assignment இல்லை.
  - **Trace:** `M6-MS10-T03` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS10-T04** [QA] Threshold, level மற்றும் expired-stock boundary tests செய்
  - **Acceptance:** Owner-approved D05/level/expiry values-க்கு evidence இருக்கும்.
  - **Trace:** `M6-MS10-T04` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=3h original estimate, accepted=0.
- [ ] **M6-MS10-T05** [API] Ledger மற்றும் wallet integration blockers சரிசெய்
  - **Acceptance:** Critical accounting defects retest/reconciliation பின் close ஆகும்.
  - **Trace:** `M6-MS10-T05` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=4h original estimate, accepted=0.
- [ ] **M6-MS10-T06** [Ops] Wallet operations, corrections மற்றும் recovery guide எழுது
  - **Acceptance:** Approvals, inventory, reconciliation, failure recovery steps documented.
  - **Trace:** `M6-MS10-T06` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.
- [ ] **M6-MS10-T07** [QA] Peer review மற்றும் acceptance evidence handover செய்
  - **Acceptance:** Reviewed PR, ledger extracts மற்றும் demo results tracker-ல் இணையும்.
  - **Trace:** `M6-MS10-T07` | Original status: `Not Started` | Review: `Not reviewed` | Source: Original 2026-12-01 tracker
  - **Original reference fields:** week=3, due=2026-11-29, estimate=2h original estimate, accepted=0.

## M7 — Home, Ads, Campaigns & Analytics

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

