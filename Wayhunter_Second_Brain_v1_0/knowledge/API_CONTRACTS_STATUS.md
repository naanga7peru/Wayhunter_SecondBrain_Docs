# API Contracts — planning interface, NOT verified endpoints

Three target GitHub repositories are **not accessible** via the current connector; therefore no controller routes or Swagger schema have been verified. The following are *capability groups*, not URL or HTTP method contracts:

- Identity: registration, OTP, login/logout, user profile, device safety, permissions.
- Social: followers, follow requests, contacts discoverability, trip invites, accepted members.
- Trips: drafts/plans, stops, active sessions, explicit start/finish, maps/search, group consent, hazards, memories.
- Hunter: submission live proof, duplicate screening, Admin review queue, owner statuses, verified public places.
- Games: creation submission, stages/hints, attempts/proof, two Admin review queues, public expiry.
- Coins: balances (posted/reserved/spendable/lifetime), reward sources, ledger, redemption reservation/release.
- Voucher/Partners: offers, secure source upload, manual review, inventory, unique assignment, issuance, use/expiry.
- Admin: Roles, Permissions, User actions, Audit Logs, Ads/Campaigns, Analytics, Notifications, Settings.

**No new-project controllers/routes are verified; development has not started per owner.** Proposed `/api/mobile/v1` is a suggested naming direction, not an existing endpoint. **Do not copy suggested controller naming into code as though already existing.** When access is restored, create `verified/API_ENDPOINT_INVENTORY.md` from actual controller attributes or OpenAPI and record endpoints with branch/SHA and source paths.
