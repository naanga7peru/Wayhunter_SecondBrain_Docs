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


## 13. Proposed Technical Clarifications — M6 Review v0.2

**Review Reference:** GitHub PR #7

**Reviewer:** Kaviyan — M6 Coins & Wallet

**Review Outcome:** Changes Requested

**Contract Status:** Proposed — Awaiting M6 Agreement

This section responds to the five technical clarifications requested by M6.

These are proposed technical decisions, not approved or implemented interfaces.

### 13.1 RewardType Identifiers

Proposed stable identifiers:

| RewardType | Recipient | Coins | Eligibility |
|---|---|---|---|
| GAME_CREATOR_APPROVED | CreatorUserId | +100 | Admin approves and publishes the Game |
| GAME_WINNER_APPROVED | PlayerUserId | +100 | Admin verifies the single eligible winner |

Rules:

- Both reward types must be distinguishable.
- Pending or rejected results must not generate reward credits.
- M5 identifies reward eligibility.
- M6 owns the authoritative wallet and ledger.
- Final identifier names require M6 owner confirmation.

### 13.2 SourceRecordId Mapping

Proposed mapping:

| RewardType | SourceRecordId | Additional Reference |
|---|---|---|
| GAME_CREATOR_APPROVED | GameId | GamePublicationReviewId |
| GAME_WINNER_APPROVED | GameId | GameAttemptId and GameCompletionReviewId |

Rationale:

- One creator reward is allowed per GameId.
- One winner reward is allowed per GameId.
- Different RewardType values distinguish the two reward categories.
- The winner event must identify the winning GameAttemptId.
- Admin review record references provide approval traceability.

The final SourceRecordId type and mapping must be validated against M6 CoinRewardSources.

### 13.3 Database Uniqueness and Idempotency

Proposed logical source keys:

Creator reward:

`game-creator:{GameId}`

Winner reward:

`game-winner:{GameId}`

Proposed M6 database uniqueness:

`UNIQUE (RewardType, SourceRecordId)`

Required guarantees:

1. One eligible creator reward source per Game.
2. One eligible winner reward source per Game.
3. Duplicate event delivery must not create duplicate reward sources.
4. CoinLedgerEntries must enforce one credit per approved reward source.
5. Repeated processing must return the existing authoritative result.
6. Concurrent processing must not credit the same reward twice.

M5 must enforce the single verified winner independently of the Coins reward uniqueness mechanism.

The final database indexes, constraints and ledger relationship require M6 and Backend architecture agreement.

### 13.4 Reward Processing States and Retries

Proposed processing states:

| State | Meaning | Allowed Action |
|---|---|---|
| Pending | Eligible reward recorded but not yet credited | Process or retry |
| Granted | M6 successfully committed the Coins credit | No additional credit |
| Failed | Processing failed without confirmed credit | Investigate and retry safely |

Proposed flow:

`Pending → Granted`

On processing failure:

`Pending → Failed → Retry → Granted`

Rules:

- Retry must use the same logical reward source key.
- Retry must not create a new eligible reward.
- A previously Granted source must not be credited again.
- M6 must check authoritative ledger records before applying any retry.
- Reward-source status and ledger credit must be committed consistently.
- Failure after a partial operation must be recoverable without duplicate credits.
- Pending and Failed records must remain traceable for reconciliation.

Retry limits, error codes and transport mechanism remain subject to M6 agreement.

### 13.5 Approval Timestamps and Event DTO

Proposed reward event fields:

| Field | Type | Purpose |
|---|---|---|
| EventId | UUID | Stable event identifier |
| EventType | String | Creator or winner approval event |
| RewardType | String | Proposed M6 reward category |
| GameId | UUID | Source Game |
| SourceRecordId | UUID | Proposed mapping to GameId |
| RecipientUserId | UUID | User receiving Coins |
| CoinsAmount | Integer | 100 |
| ApprovedAtUtc | UTC timestamp | Authoritative Admin approval time |
| ApprovalRecordId | UUID | Related Admin approval record |
| GameAttemptId | UUID, nullable | Required for winner reward |
| CorrelationId | UUID | End-to-end traceability |
| RuleVersion | String | Applied reward policy version |

DTO requirements:

- EventId must remain stable across delivery retries.
- RecipientUserId must come from trusted Game records.
- CoinsAmount must be validated server-side.
- ApprovedAtUtc must come from the authoritative backend.
- Client-submitted values must not determine reward eligibility.
- Final DTO structure and serialization require M6 review.

### 13.6 Previously Approved Rewards After Game Expiry

Approved Game expiry rule:

`ExpiresAtUtc = GameApprovedAtUtc + 720 hours`

Rules:

1. New winner approvals at or after ExpiresAtUtc are prohibited.
2. Creator rewards from valid publication approvals remain eligible.
3. Winner rewards approved before expiry remain eligible.
4. A valid previously approved reward may be processed after the Game expires.
5. Processing delay does not invalidate an already eligible reward.
6. Expiry must not produce a second reward or a new winner.
7. Archived Games and their reward audit records must remain traceable.

For example:

- Game published on Day 1.
- Valid winning attempt approved on Day 20.
- Game expires after exactly 720 hours.
- M6 processes the already approved winner reward after expiry.

Expected result:

The existing eligible +100 Coins reward may be granted exactly once.

This does not permit any new winner approval after expiry.

### 13.7 Transaction and Reliability Requirements

Proposed implementation requirements:

- Admin approval must be persisted before reward eligibility is established.
- Winner selection must be atomic and concurrency-safe.
- M5 should persist its reward event transactionally with the authoritative approval, using an outbox or equivalent reliable mechanism.
- M6 should use idempotent ledger processing.
- Failed deliveries must be retryable.
- All reward transitions must be auditable.
- Flutter clients must never directly modify CoinWallets.
- Final API routes and transport adapters will be connected during the agreed integration phase.

### 13.8 M6 Review Acceptance Checklist

- [x] RewardType identifier proposal documented.
- [x] SourceRecordId mapping proposal documented.
- [x] Uniqueness and idempotency approach documented.
- [x] Pending, Granted, Failed and retry behavior documented.
- [x] Approval timestamp and DTO proposal documented.
- [x] Post-expiry processing of previously approved rewards documented.
- [ ] M6 owner confirms final RewardType names.
- [ ] M6 owner confirms SourceRecordId mapping.
- [ ] M6 owner approves database constraints.
- [ ] M6 owner approves processing states and retry contract.
- [ ] M6 owner approves final DTO and expiry behavior.
- [ ] Team architecture review completed.

**Final Status:** Draft — M6 Re-review Required.

No APIs, database constraints or integration tests are claimed as implemented.
