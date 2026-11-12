# M1 — Identity, Profile, Friends & Settings: 10 milestones & 106 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-01, ADM-03, ADM-17. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

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
