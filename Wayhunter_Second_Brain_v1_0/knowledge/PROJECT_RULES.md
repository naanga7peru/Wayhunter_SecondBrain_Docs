# Product rules from current Wayhunter documentation

## Account / Social
- One identity across Traveler, Hunter and Game, with immutable backend-generated `UserId` and display name shown to Admin for review requests.
- Welcome +100 Coins at first eligible verified account activation, **not every reinstall**.
- One unified Followers/Following Friends page from Profile and Create Trip > Add Friends; share install link using OS share sheet; contact discovery only after opt-in and matching privacy policies.
- A follow is not a trip invite. Accepted trip invitation alone does not grant GPS consent.

## Traveler
- Plan trip: name, dates, start, ordered stops, end, budget, vehicle, group size; AI suggested plan is editable, and source plans never overwritten by reuse.
- A trip is ranked as completed **only** with actual Start and Finish events; saving a draft or submitting a plan is not completion.
- Nearby places search on user action (1 km); location sharing explicitly opted in per member; stop sharing at finish.
- Hazards: community report initially unverified; show alerts only to users whose planned trip routes pass within 1 km of reported hazard. Show photo capture time. Active alert automatically disappears after 24 hours; retain existing verification/anti-spam safeguards.

## Hunter
- Current GPS district; live guided 360 video and live normal photo; **gallery proof forbidden**.
- 200m duplicate check yields candidates, not automatic rejection based on distance alone.
- All new submissions go to Admin Pending; each review shows UserId, Name, SubmissionId, evidence and flags; Approved & Published yields **+200 Coins exactly once**; rejection yields zero + reason. My Hunts shows Pending/Approved/Rejected.

## Game
- Creator can upload photo/text hints (creator gallery may be allowed); player proof uses **live camera only**; no compulsory map/kilometer hint.
- Game creation: Admin Approve then public publish and **+100 Coins once** to creator; reject yields zero. Separate review for eligible completed player result: Admin Approve then **+100 Coins once**.
- Game expires exactly 30 days after Admin approval; Flutter shows remaining time. At expiry remove from public/active/playable lists, mark Expired/Archived, retain Game record and creator My Games history. No new/resumed/completed plays after expiry; preserve Coins/audit records. Physical Game DB deletion is NOT the current owner rule.
- Exactly one verified winner per Game. Winner reward (+100 Coins) issued once after Admin approval.

## Coins / Wallet / Redemption
- Single currency **Coins only**; retire HP/RC/XP. Track available/spendable, reserved, lifetime earned. 2,000 lifetime Coins per proposed star-level progress bar; spending must not lower lifetime level.
- Academic demo voucher: 10,000 Coins = LKR 100 sample value only, not a real bank payout. Require at least 10,100 spendable Coins before redeeming 10,000, with at least 100 Coins remaining.
- Pending redemption: Backend reserves/holds 10,000 Coins; prevent double spend; rejection/cancel releases hold once; **Admin Approval permanently deducts 10,000 Coins exactly once**. Voucher issue happens later; never debit again.
- Academic demo voucher: Admin assigns sample voucher image + unique demo code + QR after approval; no real purchase or merchant settlement. Unique code assigned once; only issued demo voucher exposes code/QR and expiry.

## Navigation/Ranking/Notifications
- Global bottom navigation: 1 Home, 2 currently selected module (Traveler/Hunter/Game), 3 Leaderboard, 4 Profile. Leaderboard tab shows the relevant module leaderboard; Game/Hunter/Traveler ranking rules remain separate.
- Game ranks from eligible approved Game-earned Coins; Hunter ranks from approved Hunter-earned Coins; Traveler ranks from actual finished trips.
- Friend requests/accepts, Hunter/Game approval outcomes, voucher results, trip reminder before start, verified/unverified hazard contextual warnings. Reminder never auto-starts a trip.

## Cross-cutting
- Explicit role-based Admin approval. Backend is authority for user identity, permissions, approvals, Coins ledger, redemption, voucher status, and audit.
- No secrets/passwords/voucher codes in frontend localStorage in production. Notify after committed state changes; never confuse UI success with backend acceptance.
