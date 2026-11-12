# M6 — Coins, Wallet & Vouchers: 10 milestones & 75 tasks

**Purpose:** One member completes Flutter + Backend + SQL/EF + Angular Admin + tests for their module in the same 3 repositories. Project plan: team approval pending; no implemented code is asserted.

**Angular scope:** ADM-11, ADM-12, ADM-13. **Full team contracts** are in `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md`.

## Milestones and tasks

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
