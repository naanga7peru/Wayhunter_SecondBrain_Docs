# Critical end-to-end workflows — documentary requirements, not implemented-code claims

## Hunter place request
`Flutter live evidence + GPS → Backend submission PendingAdmin → Angular Admin proof review → Approve/Reject → Publish if approved → unique +200 Coin ledger event → notification and My Hunts status`

### Admin review data
`UserId, DisplayName snapshot, SubmissionId, District, Coordinates, Accuracy, 360/video, photo, duplicate flags, restricted-area flags, submitted time, admin actor, decision reason/timestamp`.

## Game creation
`Flutter create + stages/hints → Backend PendingAdmin → Angular Game Review → Approve/Reject → approved public game +100 Coins to creator once → 30-day countdown from Admin approval → public/active UI removal + Expired/Archived record retained for creator My Games at expiry`.

## Game player result
`Active game → live camera proof per stage → verified eligible final session → separate Admin completion review → +100 Coins once on approval; rejection no credit`.

## Voucher request
`User request → backend verifies available Coins/eligibility → idempotent Coins hold/reservation → Admin reviews user/offer/stock → Approve or Reject → unique stock allocate → actual issue/fulfill → user My Vouchers + notification`.

**APPROVED 2026-11-11:** Require >=10,100 spendable Coins to redeem 10,000; pending request reserves 10,000. On Admin Approve, final debit 10,000 exactly once; on reject release hold. Admin then issues sample voucher image + unique code + QR. No real purchase or bank cash-out.

## Voucher intake
`Approved Supplier/Offer → Admin image/PDF upload OR manual entry → protected source preview → uniqueness/expiry/amount checks → reviewer confirms → available inventory`.

**OPTIONAL:** OCR / QR / barcode scans can suggest fields; not authenticating or issuing vouchers automatically.

## Traveler and friends
`Create/Edit trip draft → Add Friends unified page → follow/social and optional trip invite → accept trip membership → separate live GPS consent → user explicitly Start Trip → near-route hazards/memories/find → user Finish Trip → stop live sharing + completed-trip leaderboard`.

## Audit/notifications
Admin action and Coins mutation require backend persisted event + actor/reason + idempotency key. Notify after commit, and keep in-app status even if push fails.
