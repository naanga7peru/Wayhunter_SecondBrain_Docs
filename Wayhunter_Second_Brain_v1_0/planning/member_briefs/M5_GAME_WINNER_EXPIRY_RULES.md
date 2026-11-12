# WAYHUNTER — M5 Game Winner & Expiry Rules

**Task ID:** M5-MS01-T02
**Owner:** M5 — Thuvarathan
**Milestone:** M5-MS01 — Game Policies, States and Audit Schema
**Status:** Draft — Pending Peer Review
**Sources:** Master BRD v2.1 Section 06; `knowledge/LATEST_APPROVED_2026-11-11.md`

## 1. Purpose

Record the final approved decisions for game winner eligibility, game expiration and ongoing attempts.

This document resolves the superseded D02, D03 and D04 decision notes in the older BRD.

## 2. D02 — Single Verified Winner

**Decision: APPROVED**

- Each community game allows exactly one eligible, Admin-verified winner.
- The game creator cannot win their own game.
- Player completion must be reviewed by an authorized Admin.
- A submitted completion is PendingAdminVerification, not an automatic win.
- Only the first eligible completion confirmed as the game's winner may receive the winner reward.
- Multiple Admin approvals must not create multiple winners.
- Repeated requests must not produce duplicate winner records or Coin rewards.
- Rejected, failed, pending or ineligible completions receive no winner Coins.

**Reward contract:**

- Approved Game Creator: +100 Coins exactly once.
- Approved Single Game Winner: +100 Coins exactly once.
- M5 produces eligible reward events.
- M6 is responsible for authoritative Coin ledger entries and balances.

## 3. D03 — Game Expiry

**Decision: APPROVED**

Game expiry starts only when Admin approves and publishes the game.

```text
ExpiresAtUtc = ApprovedAtUtc + 720 hours
```

- 720 hours equals 30 consecutive 24-hour periods.
- Calendar-month calculations are not permitted.
- The backend is the authoritative source of approval and expiry timestamps.
- Before publication, Pending and Rejected games are not available to public players.
- At expiry, the game becomes unavailable for public discovery and play.
- Expired games remain in the creator's My Games as Expired/Archived.
- Do not physically delete game history, evidence or audit records.
- Flutter must display the remaining time using the server-provided expiry value.

## 4. D04 — In-progress Game Expiry

**Decision: APPROVED**

When the game expiry timestamp is reached:

- Block new game starts.
- Block resuming existing attempts.
- Block further stage progression or completion.
- Block new winner approval and winner rewards after expiry.
- Retain existing attempts, proofs, decisions and history for audit.
- Display an accurate expired-game status to affected players.

Expiry must be checked by the backend even if an expiry worker has not yet updated the stored game status.

## 5. Game State Overview

```text
Draft
  ↓
Pending Admin Review
  ├── Rejected
  └── Approved / Published / Active
           ↓
       Expired / Archived
```

Flagging or disabling a game is a separate controlled Admin action with an audit trail.

## 6. Required Backend Integrity

- Store GameId and immutable CreatorUserId.
- Store ApprovedAtUtc and ExpiresAtUtc.
- Store winner identity, game attempt reference and Admin decision.
- Enforce a maximum of one approved winner per GameId.
- Validate eligibility and expiry on the server.
- Make Admin decisions and reward events idempotent.
- Record actor, timestamp, reason and source references for audit.

These are design requirements, not confirmation that the database or APIs are implemented.

## 7. Source Conflict Resolution

| Decision | Old BRD Status | Latest Approved Rule |
|---|---|---|
| D02 — Winner count | First vs multiple winners unresolved | Exactly one Admin-verified winner |
| D03 — Game lifetime | Calendar month vs 30 days unresolved | Exactly 720 hours after approval |
| D04 — Ongoing attempt at expiry | Decision required | No resume, completion or win after expiry |

The latest approved rules override only these conflicting older statements.

## 8. Acceptance Checklist

- [x] D02 final winner policy documented.
- [x] D03 exact expiry calculation documented.
- [x] D04 in-progress expiry behavior documented.
- [x] Creator and winner reward ownership identified.
- [x] Older BRD conflicts traced.
- [ ] Peer review completed.
- [ ] GitHub PR reviewed and approved.

**Task status: Draft — Not Accepted**

**Next Task:** M5-MS01-T03 — Creator Gallery vs Player Live-Proof Rules.