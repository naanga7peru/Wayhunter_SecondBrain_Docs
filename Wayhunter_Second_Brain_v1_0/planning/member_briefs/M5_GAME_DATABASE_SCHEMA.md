# WAYHUNTER — M5 Game Database Schema Design

**Task ID:** M5-MS01-T04

**Owner:** M5 — Thuvarathan

**Milestone:** M5-MS01 — Game Policies, States and Audit Schema

**Status:** Draft — Pending Architecture Review

**Sources:**
- `05_Full_ERD_v1.1.pdf`, Page 12 — Games Domain
- Master BRD v2.1, Section 06
- `knowledge/LATEST_APPROVED_2026-11-11.md`

## 1. Purpose

Document the proposed database structure for the Wayhunter Game module without conflicting with shared Identity, Admin, Media and Coins domains.

No database migration or implemented SQL tables are claimed by this document.

## 2. Game Domain — 11 Proposed Tables

| Table | Primary Key | Main Foreign Keys | Purpose |
|---|---|---|---|
| Games | GameId | CreatorUserId, CoverMediaId?, CampaignId? | Game identity and publication |
| GameStages | GameStageId | GameId | Ordered stages |
| GameClues | GameClueId | GameStageId, MediaAssetId? | Photo/text clues |
| GamePublicationReviews | GamePublicationReviewId | GameId, ReviewerUserId, AdminReviewCaseId? | Creation review |
| GameAttempts | GameAttemptId | GameId, PlayerUserId | Player sessions |
| GameStageProofs | GameStageProofId | GameAttemptId, GameStageId, MediaAssetId | Live evidence |
| GameStageProofReviews | GameStageProofReviewId | GameStageProofId, ReviewerUserId | Stage verification |
| GameCompletionReviews | GameCompletionReviewId | GameAttemptId, ReviewerUserId, AdminReviewCaseId? | Final approval |
| GameAntiCheatFlags | GameAntiCheatFlagId | GameId, GameAttemptId?, ActorUserId? | Anti-cheat audit |
| GameExpiryEvents | GameExpiryEventId | GameId | Expiry audit |
| GameReports | GameReportId | GameId, ReporterUserId | Reports |

The names above follow the proposed ERD v1.1.

## 3. Important Existing ERD Columns

### Games

- `GameId` — uniqueidentifier, PK
- `CreatorUserId` — uniqueidentifier, FK
- `CampaignId` — uniqueidentifier, nullable FK
- `CoverMediaId` — uniqueidentifier, nullable FK
- `Title` — nvarchar(150)
- `Description` — nvarchar(2000), nullable
- `CreationStatus` — nvarchar(24)
- `PublishedAtUtc` — datetime2(3), nullable
- `ExpiresAtUtc` — datetime2(3), nullable
- `ArchivedAtUtc` — datetime2(3), nullable
- `DurationSeconds` — int, nullable
- `UserNameSnapshot` — nvarchar(150)

### GameStages and GameClues

`GameStages` stores `GameId`, `StageOrder`, optional title and optional stage time limit.

`GameClues` stores `GameStageId`, optional `MediaAssetId`, `ClueType`, optional `ClueText` and `SortOrder`.

Stage order must be validated, and future-stage answers or private proof details must not be exposed to players.

### GameAttempts and GameStageProofs

`GameAttempts` records `GameId`, `PlayerUserId`, `AttemptStatus`, `StartedAtUtc`, optional `FinishedAtUtc` and optional `ElapsedSeconds`.

`GameStageProofs` records `GameAttemptId`, `GameStageId`, `MediaAssetId`, `ProofStatus`, `CapturedAtUtc` and `IsLiveCapture`.

The backend must verify that the submitted stage belongs to the attempt's game.

### Admin Review and Audit

`GamePublicationReviews` records the Admin creation decision.

`GameStageProofReviews` records stage evidence decisions.

`GameCompletionReviews` records final completion decisions.

All must preserve reviewer identity, decision, reason where applicable and server review time.

### Game Expiry and Anti-Cheat

`GameExpiryEvents` preserves expiry events and rule version.

`GameAntiCheatFlags` stores suspicious activity flags, reasons and dispositions.

`GameReports` stores user reports and their current status.

## 4. Shared Module Relationships

**M1 — Identity**

- `Games.CreatorUserId` references `Users.UserId`.
- `GameAttempts.PlayerUserId` references `Users.UserId`.
- Reviewer identities reference the shared Users system.
- Game module must not create a duplicate Users table.

**Shared Media**

- Cover images, clue images and camera proofs use `MediaAssets.MediaAssetId`.
- Sensitive player proof media must remain private.
- Creator clue gallery/camera source remains subject to the recorded decision conflict.

**Admin Operations**

- Approval records may reference `AdminReviewCases`.
- Only authorized reviewers may approve publication or final results.
- Decisions must be auditable.

**M6 — Coins**

- M5 provides approved creator and winner reward source events.
- M6 owns `CoinRewardSources`, `CoinLedgerEntries` and `CoinWallets`.
- M5 must not directly edit users' wallet balances.
- Creator reward: +100 Coins once per eligible published game.
- Winner reward: +100 Coins once per eligible verified winner.

**M7 — Campaigns**

- Optional `Games.CampaignId` references a campaign owned by the relevant shared module.

## 5. Approved Game Rules for the Database

- One verified winner per game.
- Creator cannot win their own game.
- Creation and completion require separate Admin decisions.
- `ExpiresAtUtc = ApprovedAtUtc + 720 hours`.
- Expired games block new starts, resume, completion and winner approval.
- Game history and audit records remain after expiry.
- Expiry is a soft archive, not physical deletion.
- Server-side eligibility, timestamps and validation are mandatory.

## 6. Architecture Review Findings

### REVIEW-01 — Approval Time Anchor

The proposed `Games` table contains `PublishedAtUtc`, but not a separate `ApprovedAtUtc` column.

Confirm whether publication and approval occur in the same authoritative transaction, or whether an immutable approval timestamp must be added.

Do not silently change the ERD.

### REVIEW-02 — Single-Winner Database Enforcement

`GameCompletionReviews` references `GameAttemptId` but does not directly store a unique winner allocation per GameId.

The implementation design must enforce one winner atomically, even when two Admins approve competing attempts simultaneously.

A transaction and a database uniqueness mechanism are required. The exact schema solution needs review.

### REVIEW-03 — Attempt Deadline

`GameAttempts` stores `StartedAtUtc` and `ElapsedSeconds`, but no explicit `DeadlineAtUtc` in the proposed diagram.

Confirm how the backend will enforce timer expiry independently of the player's device clock.

### REVIEW-04 — Stage and Proof Integrity

Ensure that:

- Stage order cannot be duplicated improperly.
- Game proof belongs to the correct attempt and game.
- Repeated proof submission does not cause repeated progression.
- Rejected or pending evidence never creates winner eligibility.
- Private media ownership is checked.

### REVIEW-05 — Creator Clue Source

Master BRD GA-005 allows creator gallery images, while the earlier camera-only demo rule differs.

Do not finalize the creator upload restriction until the authorized source conflict is resolved.

Player live camera proof remains mandatory.

## 7. Proposed Database Integrity Checks

For later technical design review:

- Foreign keys for game, user, stage, attempt and media relationships.
- Unique ordered-stage keys within each game.
- Atomic single-winner allocation.
- Idempotent publication, completion and reward events.
- Server UTC timestamps.
- Expiry checks on every relevant gameplay operation.
- Controlled Admin decision state transitions.
- Secure access to private proof media.
- Audit retention after soft archive.

These are proposed implementation checks, not existing verified SQL constraints.

## 8. Acceptance Checklist

- [x] All 11 proposed Games tables documented.
- [x] Primary keys and important foreign keys identified.
- [x] Creator and player UserId relationships identified.
- [x] Relevant server timestamps identified.
- [x] M1, M6, Admin and Media dependencies documented.
- [x] Schema gaps recorded for architecture review.
- [ ] Exact schema enforcement reviewed with team.
- [ ] Peer-reviewed PR approved.

**Task status:** Draft — Not Accepted

**Next task:** M5-MS01-T05 — Game Approval and M6 Reward Contracts.