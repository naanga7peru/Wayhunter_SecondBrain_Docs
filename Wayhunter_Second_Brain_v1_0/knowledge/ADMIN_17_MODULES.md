# Angular Admin: 17 module inventory — functional reference v1.1

| ID | Module | Primary responsibilities |
|---|---|---|
| ADM-01 | Admin Authentication | Login, OTP, password recovery, RBAC, session, login audit |
| ADM-02 | Dashboard | Verified summary cards, pending counts, quick actions, financial/ads activity |
| ADM-03 | User Management | Search UserId, profile/activity/wallet, warn/suspend/reactivate with audit |
| ADM-04 | Hunter Verification | Pending proof, GPS/current district, guided 360/photo, duplicate/restricted checks, approve/reject/hold |
| ADM-05 | Advertisement Management | Sponsor content, creative, district targeting, schedule, home banner rotation, impressions/clicks |
| ADM-06 | Places Management | Approved published places, edit/category, merge, hide, history |
| ADM-07 | Trips & Historical Routes | Trip sessions, start/end truth, consecutive completed route reuse, flagged trip reports |
| ADM-08 | Hazard Management | Reports, review, verify/resolve/expire/flag; contextual traveler alerts |
| ADM-09 | Group Trip Management | Invites, membership, opt-in GPS sharing, I'm Safe, safety audit |
| ADM-10 | Game Management & Anti-Cheat | Separate game creation/player completion approval queues, proof, winner, expiry |
| ADM-11 | Coins & Rewards Management | Coins ledger, holds, lifetime earned, reward source idempotency, correction audit |
| ADM-12 | Merchant & Voucher Inventory | Partner offers, image/PDF or manual source, admin verification, inventory, proposed scanner |
| ADM-13 | Redemption & Settlements | User requests, Coins hold, Admin Approve debits 10,000 once (>=10,100 spendable), issue unique demo voucher afterward; commercial settlement not required in academic demo |
| ADM-14 | Campaign Management | Sponsor campaign, district, budget, eligibility, schedule, analytics |
| ADM-15 | Reports & Analytics | Date/district filtered KPIs and export; no invented metrics |
| ADM-16 | Notifications Management | Compose/schedule, FCM delivery state, state-driven event notifications |
| ADM-17 | Settings, Security & Audit Logs | Versioned rules, Admin roles, restricted zones, integration status, immutable audit |

**v1.1 working-process nuance + current owner rules:** Voucher photo/PDF upload + manual verification are documented. Voucher **QR generation/display** is needed for demo; supplier OCR/barcode/QR **scanner intake** remains optional. Debit timing is resolved on Admin Approval (not on issue). The actual implementation in the new `naanga7peru` repo is not verified.
