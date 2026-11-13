# WAYHUNTER — M5 Game & M6 Coins Reward Contracts

**Task ID:** M5-MS01-T05

**Owner:** M5 — Thuvarathan

**Milestone:** M5-MS01 — Game Policies, States and Audit Schema

**Status:** Draft — Pending M6 Review

## 1. Purpose

Define how approved Game creation and verified Game winning produce eligible Coins reward events for the M6 Wallet module.

This document describes a proposed interface contract. It does not claim implemented APIs, event processing or tested integrations.

## 2. Module Responsibilities

### M5 — Games Module

- Manage game creation, publication and Admin review.
- Manage player attempts, evidence and completion reviews.
- Enforce exactly one verified winner per game.
- Block creator from winning their own game.
- Validate expiry before accepting winner approval.
- Produce eligible reward events after authoritative approval.
- Prevent duplicate reward-source generation.

### M6 — Coins Module

- Own CoinWallets, CoinRewardSources and CoinLedgerEntries.
- Validate reward eligibility and deduplication contract.
- Award approved Coins exactly once.
- Maintain authoritative balances and lifetime earnings.
- Handle duplicate delivery and safe retries.
- Return or expose the authoritative reward status.

M5 must never modify CoinWallets directly.

## 3. Reward Eligibility Rules

| Event | Recipient | Coins | Trigger |
|---|---|---:|---|
| Game Creator Approved | CreatorUserId | +100 | Admin approves and publishes an eligible game |
| Game Winner Approved | PlayerUserId | +100 | Admin verifies the game's single eligible winner |
| Game Draft | None | 0 | No approval |
| Game Pending | None | 0 | Waiting for Admin |
| Game Rejected | None | 0 | Creation rejected |
| Player Pending | None | 0 | Waiting for final review |
| Player Rejected / Failed | None | 0 | Completion not accepted |
| Game Expired | None | 0 | New winner approval after expiry prohibited |

## 4. Proposed Reward Event Contract

Required fields:

| Field | Purpose |
|---|---|
| EventId | Unique event identifier |
| EventType | Creator approval or winner approval |
| GameId | Source game |
| RecipientUserId | User receiving Coins |
| SourceRecordId | Approved source record for deduplication |
| RewardType | Creator or Winner reward category |
| CoinsAmount | 100 |
| ApprovedAtUtc | Authoritative approval timestamp |
| CorrelationId | Trace Admin decision to reward processing |
| RuleVersion | Applicable approved Coins policy |

For winner rewards, the event must also reference the verified GameAttemptId.

Final DTO names, serialization, error codes and API routes require M6 agreement.

## 5. Proposed Idempotency Keys

Creator reward:

`game-creator:{GameId}`

Winner reward:

`game-winner:{GameId}`

These are proposed stable logical keys, not already implemented database columns.

M6 must enforce uniqueness for an approved reward source. Retries must reuse the same logical key.

A second winner for the same GameId must not produce another eligible reward.

## 6. Game Creation Approval Flow

1. Creator submits a game.
2. Game enters PendingAdmin status.
3. Admin reviews the game's clues, safety and rules.
4. Admin rejects or approves.
5. On approval, backend records the authoritative publication decision.
6. M5 records one eligible Creator reward source event.
7. M6 processes that reward source and credits +100 Coins once.
8. Repeated approval or event delivery must not credit again.

Game publication must remain valid independently of notification delivery.

## 7. Game Winner Approval Flow

1. Player completes all required stages.
2. Completion enters PendingAdminVerification.
3. Admin reviews proofs and anti-cheat evidence.
4. Backend checks creator exclusion, game expiry and winner eligibility.
5. Exactly one eligible winner is atomically confirmed.
6. M5 records one eligible Winner reward source event.
7. M6 credits the verified winner +100 Coins once.
8. Other submissions cannot create additional winners or winning credits.

A pending completion is not a confirmed win.

## 8. Integration with ERD v1.1

M5 references these existing proposed entities:

- Games
- GameAttempts
- GamePublicationReviews
- GameCompletionReviews

M6 owns:

- CoinWallets
- CoinRewardSources
- CoinLedgerEntries

Shared integration support may use:

- OutboxMessages
- AdminReviewCases
- AdminAuditEvents

The proposed ERD defines CoinRewardSources fields including RewardType, SourceRecordId, RecipientUserId, CoinsAmount and RewardStatus.

M1 owns the shared Users.UserId identity.

No duplicate Coins or User tables should be created in M5.

## 9. Reliability and Security

- Only authorized Admin decisions can establish reward eligibility.
- Server timestamps are authoritative.
- Do not award Coins based on Flutter button presses.
- The approval decision and reward event should be persisted transactionally, for example through an outbox pattern.
- Event processing must tolerate delivery retries.
- A failed or delayed M6 credit must remain traceable for reconciliation.
- Notifications must not be treated as proof of successful credit.
- Keep source IDs, reviewer references and audit history.
- Never expose wallet mutation permissions through a public Game client.

## 10. Integration Deferral

During initial module development:

- Use contracts and test doubles or mocks.
- Keep Game business logic and M6 ledger logic separated.
- Do not invent a working API route.
- Do not modify another member's Coins implementation.
- Connect the real M5-to-M6 API/event adapter during the agreed integration phase.

## 11. Questions for M6 Owner Review

1. Confirm creator and winner RewardType identifiers.
2. Confirm SourceRecordId mapping and uniqueness constraints.
3. Confirm event/DTO field names and agreed transport mechanism.
4. Confirm how M5 observes Pending, Granted or Failed reward status.
5. Confirm exactly-once ledger handling and recovery after processing failure.

## 12. Acceptance Checklist

- [x] Creator +100 approved reward contract documented.
- [x] Single eligible winner +100 contract documented.
- [x] Proposed unique reward keys documented.
- [x] M5 and M6 ownership boundaries documented.
- [x] Pending, rejection and duplicate handling documented.
- [ ] M6 owner approves the interface.
- [ ] Team peer review and PR approval completed.

**Task status:** Draft — Not Accepted

**Next Task:** M5-MS01-T06 — Game Safety, Replay and Eligibility Policies.