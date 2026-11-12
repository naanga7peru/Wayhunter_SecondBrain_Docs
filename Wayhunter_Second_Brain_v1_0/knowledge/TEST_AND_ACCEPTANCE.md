# Acceptance tests to implement later — academic project requirements, not test results

**Status:** Not run. The team has not started project code/folders. This is the verified *rule checklist* and not proof of implementation.

## Identity, friends & access
- User ID is unique/immutable; eligible verified first account gets welcome +100 only once despite retry/reinstall; OTP/auth invalid states do not mint rewards.
- Followers/Following unified page accessible from Profile and Create Trip; follow != trip invite != GPS-sharing consent; contact discovery opt-in; blocked/private users protected.
- Every privileged Admin approval requires backend role checks and audit, not Angular guard alone.

## Hunter
- Gallery is blocked for Hunter live 360 guided evidence and normal photo; current GPS district and 200m **candidate** duplicate screening are enforced; proximity alone must not auto-reject.
- Pending -> Rejected requires reason/no Coins; Pending -> Admin Approved publishes approved place and credits +200 once only. My Hunts shows own Pending/Approved/Rejected and evidence remains private.

## Game
- Creation Pending -> Approved publishes and credits creator +100 once; Rejected gives none. Player proof is live camera; Admin player-completion review is separate.
- **One winner per game**: simultaneous approvals and retries cannot produce two winners or double +100 winning Coins; creator cannot win own game.
- Expiry timestamp = Admin approval UTC + 30 * 24h. Countdown uses backend timestamp. At expiry game disappears from public/playable lists, remains in creator My Games **Expired/Archived** and database; repeated expiry job is safe.
- No new, resumed, or completed attempt can qualify after expiry; previous ledger/audit records persist unchanged.

## Coins, redemption & voucher
- Ledger is authoritative; spendable = posted minus active reservations; no two concurrent requests may reuse held Coins.
- **>=10,100 spendable Coins is required** to reserve 10,000; exactly 10,100 passes and leaves 100; 10,099 fails. Pending hold does not post a debit.
- Admin Approval consumes reservation and debits 10,000 **exactly once**; rejection/cancellation before approval releases the hold once. Voucher issue/fulfill never debits again.
- A failed voucher issuance after approval leaves a visible approved/unissued state; idempotent retry can issue a **single** unique sample code/QR. Do not assume automatic refund or a real supplier settlement.
- Only assigned/issued voucher displays code+QR and expiry; used/expired/demo code cannot be reused; source image/PDF private and manually reviewed. OCR/barcode intake optional and never auto-authenticating.

## Traveler, hazards, notifications & navigation
- Saving or submitting a Trip does not count as completed; valid explicit Start then Finish counts toward Traveler leaderboard and ends group GPS sharing.
- Hazard alert ONLY when planned route is within **1 km** of location, including route planning and active-trip views. Show verified/unverified status and source **photo capture time**; after **24 hours** from trusted report timestamp no active alert. Out-of-route users get none.
- The 4 tabs are Home / dynamic selected-module / context Leaderboard / Profile; module rankings use correct Game/Hunter/Traveler source metrics.
- Friend request, trip start reminder, Admin decisions and Coins/voucher notifications reflect persisted events; notification delivery failure does not undo transactions or duplicate alerts.

## Evidence standard
Record when implemented: repo/branch/SHA, specific files, expected vs actual output, tests run, failed cases, linked rule ID. Proposed architecture and old screenshots are not test evidence.
