# Status mapping — clarification only, not an approved new database enum

Use these conceptual states consistently across Flutter, Backend and Angular. Concrete DTO/SQL enum names are **proposed** until API contracts are implemented; do not assume they already exist.

| Flow | Backend conceptual state | Mobile/user display | Admin action | Rule |
|---|---|---|---|---|
| Hunter | Submitted/PendingAdmin/UnderReview | Pending / Waiting for Admin verification | Review | No Coins |
| Hunter | Approved/Published | Approved; Congratulations +200 Coins | Approve exactly once | Public only after approval |
| Hunter | Rejected | Rejected + reason | Reject with reason | No Coins |
| Game creation | Draft/PendingAdmin | Draft/Pending | Review | No creator +100 until Approve |
| Game creation | Approved/Published/Active | Available | Approve exactly once | Creator +100 once, 30-day clock begins |
| Game creation | Rejected | Rejected + reason | Reject | No creator +100 |
| Game expiry | Expired/Archived | Creator My Games: Expired; public list: hidden | Automatic expiry | Retain DB/creator history |
| Game play | InProgress / PendingCompletionReview | In Progress / Result Pending | Review completion | No player +100 yet |
| Game verified win | WinnerApproved | Victory +100 Coins | Approve exactly one winner | Do not approve a second winner |
| Redemption | Pending/Reserved | Pending; posted Coins unchanged, spendable held | Review | 10,100 eligibility |
| Redemption | Approved/Unissued | Approved; sample voucher not usable yet | Approve; final debit once | Do not double debit on issuance |
| Redemption | Rejected/Cancelled | Rejected/Cancelled; hold released | Reject/Cancel | No permanent debit |
| Voucher | Issued / Used / Expired | My Vouchers accordingly | Allocate/Issue/Mark use | Unique code/QR issued once |
| Hazard | Reported(Unverified) / Verified | Label truthfully | Verify if supported | Relevant route only, 24h active |
| Hazard | Resolved / Expired / Invalid | No active alert | Resolve/Expire/Flag | Keep audit |
| Trip | Draft/Planned / Active / Completed | My Plans / Live Trip / History | User Start then Finish | Save != Finish |

The mapping does not add new user-facing screens, money flows, or approval requirements. If a screen shows fewer statuses than backend, that is a display grouping—not permission to hide a rejection reason or misstate an approval.
