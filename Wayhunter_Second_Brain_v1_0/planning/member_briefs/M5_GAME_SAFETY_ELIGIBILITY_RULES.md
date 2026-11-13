# WAYHUNTER — M5 Game Safety, Replay & Eligibility Rules

- **Task ID:** M5-MS01-T06
- **Owner:** M5 — Thuvarathan
- **Module:** Games, Anti-Cheat & Leaderboard
- **Status:** Draft — Peer Review Pending
## 1. Purpose
Define safety, replay prevention, participant eligibility and anti-cheat policies for the Wayhunter real-world Game module.
This document describes business rules and proposed enforcement. It does not claim implemented backend code or completed tests.
## 2. Approved Game Rules
1. One game can have only one verified winner.
2. The game creator cannot play their own game.
3. All games require Admin approval before becoming public.
4. Game expiry is exactly 720 hours after authoritative Admin approval/publication.
5. Expired games become unavailable for public play but remain archived in the database.
6. Players must capture proof using the in-app live camera.
7. Gallery uploads cannot be used for player proof.
8. Three rejected proofs close the current attempt.
9. A verified winner reward is +100 Coins, administered through M6.
10. Pending, rejected and failed attempts do not qualify for a winner reward.
## 3. Player Eligibility
A player is eligible to begin a game only when:

- The player is authenticated.
- The game is published and active.
- The game has not expired.
- The player is not the game creator.
- No verified winner already exists.
- The player is not otherwise blocked by an applicable safety or security decision.

Eligibility must be validated by the backend.

Flutter UI restrictions alone are insufficient.

## 4. Game Creator Restrictions

- The creator can submit and manage their own game.
- The creator can view publication status and review feedback.
- The creator must not create a playable attempt on their own game.
- The creator must not submit winner proofs for their own game.
- The creator must never receive the winner reward for their own game.

Creator publication rewards and winner rewards are separate.

## 5. Live Camera Proof Policy

Players must capture stage evidence using the in-app camera.

Required validation:

- Proof belongs to the authenticated player.
- Proof belongs to an eligible active attempt.
- Proof belongs to the expected game stage.
- Media metadata is linked to its source attempt.
- Proof is submitted while the game and attempt are eligible.
- Evidence must not be substituted with another player's uploaded file.

The GameStageProofs data model should support the IsLiveCapture field.

The backend should not rely on a client-provided IsLiveCapture flag alone as proof of authenticity.

Server-side checks and media ownership verification are required.

**Open decision:** The approved live-camera restriction applies to player proof. Conflicting source guidance on whether game creators may select clue images from the gallery remains unresolved and requires Product Owner confirmation.

## 6. Replay and Duplicate Prevention

The system should detect or reject:

- Repeated submission of the same proof as a new stage completion.
- Attempts to reuse evidence belonging to another GameAttemptId.
- Attempts to use a proof for the wrong GameStageId.
- Duplicate review requests that could trigger repeated state changes.
- Repeated completion events intended to claim more rewards.
- Requests from an already closed attempt.

Every proof must have a unique GameStageProofId.

Review decisions must be traceable and repeat-safe.

A duplicate request must never generate an additional verified winner.

## 7. Three-Rejection Rule

The attempt-level rejection counter starts at zero.

When an Admin or authorized verification process rejects submitted evidence, the attempt rejection count is updated.

| Rejections | Result |
|---|---|
| 0 | Attempt remains eligible |
| 1 | First rejection recorded |
| 2 | Second rejection recorded |
| 3 | Attempt closed — no further proof submissions |

After the third rejection:

- AttemptStatus becomes Closed/Failed according to the final agreed state model.
- The player cannot continue that attempt.
- The closed attempt cannot be approved as a winner.
- A GameAudit or equivalent record should capture the closure reason.

**Decision required:** Whether the same player may begin a completely new attempt after failing remains subject to an explicit retry policy. Do not silently allow unlimited new attempts.

## 8. Game Expiry Rules

The approved expiry duration is:

`ExpiresAtUtc = ApprovedAtUtc + 720 hours`

At expiry:

- Game disappears from public discovery and available-game lists.
- New attempts are blocked.
- Existing attempts cannot resume or complete.
- New final winner approvals are blocked.
- Expired game records remain available for historical and creator views.
- Reward processing for an already valid, previously approved result must remain idempotent and auditable.

Expiry must be checked using the authoritative backend clock.

Client-device time must not determine expiry eligibility.

## 9. Single Verified Winner Enforcement

A game can have only one confirmed winner.

The winner approval process must:

1. Verify Admin authorization.
2. Check game publication status.
3. Confirm the game has not expired.
4. Verify that the player is not the creator.
5. Validate completion and evidence reviews.
6. Check that no confirmed winner exists.
7. Atomically commit the winner decision.
8. Generate the eligible winner reward source exactly once.

Two simultaneous Admin approvals must not produce two winners.

Database-level uniqueness and concurrency-safe approval logic require architecture review.

## 10. Unsafe Game Content

Game creators must not encourage participants to:

- Trespass onto private or restricted property.
- Enter dangerous or prohibited locations.
- Perform hazardous driving or traffic violations.
- Enter unsafe structures or physically risky environments.
- Threaten, harass or expose another person's private information.
- Perform illegal acts to complete a stage.

Admin review must be able to reject unsafe game instructions.

Approved games that are subsequently reported as dangerous must be eligible for Admin investigation and an appropriate safety restriction.

## 11. Anti-Cheat Checks

Examples of suspicious behavior:

- Player attempts their own game.
- Reused images or repeated proof identifiers.
- Invalid stage order.
- Impossible or manipulated completion timestamps.
- Repeated automated submissions.
- Contradictory media ownership information.
- Multiple attempts to claim the same winning result.
- Collusion between creator and player.

Suspicious events should be recorded in GameAntiCheatFlags.

A flag is evidence for review, not automatically proof of cheating.

Any penalty or rejection must follow the agreed review policy.

## 12. Reporting and Admin Review

The GameReports model should support player reports of:

- Unsafe game instructions.
- Suspected cheating.
- Inappropriate clues.
- Restricted-location activities.
- Other policy violations.

Admin reviewers must be able to inspect relevant proof, attempts and audit records.

Review decisions should include:

- ReviewerUserId
- Decision
- Reason
- ReviewedAtUtc

Final field naming must align with the shared ERD and Admin architecture.

## 13. Timer and Attempt Integrity

- Server timestamps must be authoritative.
- Flutter timers are presentation aids, not security controls.
- Stages must be completed in the required order.
- Expired or closed attempts must reject further completion.
- Attempt deadline representation requires schema review.
- A player must not be able to reset an active timer by editing client-side values.

The exact pause, retry and stage-timeout behavior must follow separately approved game rules.

## 14. Module Dependencies

### M1 — Authentication

- Authenticated UserId
- Account and authorization validation
- Creator and player identity checks

### M5 — Game Backend

- Game eligibility
- Proof validation
- Winner enforcement
- Attempt closure
- Anti-cheat flags

### M6 — Wallet

- +100 Coins for an approved eligible winner
- Unique reward source handling
- No direct wallet balance updates by M5

### Angular Admin

- Publication review
- Proof review
- Completion verification
- Suspicious activity review
- Audit history

These integrations will be connected during the agreed implementation/integration phases.

## 15. Proposed QA Checklist

- [ ] Creator cannot start their own game.
- [ ] Unapproved game cannot be played.
- [ ] Expired game cannot be started.
- [ ] Expired game cannot approve a new winner.
- [ ] Player cannot upload gallery proof.
- [ ] Duplicate proof submission is safely rejected.
- [ ] Wrong-stage proof is rejected.
- [ ] Third rejected proof closes the attempt.
- [ ] Closed attempt cannot submit further proof.
- [ ] Two concurrent winner approvals produce at most one winner.
- [ ] Repeated winner event does not duplicate Coins.
- [ ] Suspicious activity creates a reviewable flag.
- [ ] Unsafe game reports can be investigated.
- [ ] Expired game remains archived.
- [ ] Reviewer actions are auditable.

These are planned tests, not completed test results.

## 16. Decisions Requiring Confirmation

- Creator clue image: gallery selection versus camera-only.
- Whether a player can start a new attempt after three proof rejections.
- Final retry limits and timeout behavior.
- Exact enforcement mechanism for the single-winner database constraint.
- Administrative consequences for confirmed collusion.

Do not mark these as approved until the Product Owner or responsible architecture reviewer confirms them.

## 17. Acceptance Checklist

- [x] Creator eligibility restrictions documented.
- [x] Single-winner policy documented.
- [x] Player live-camera proof policy documented.
- [x] Replay and duplicate prevention rules documented.
- [x] Three-rejection attempt closure documented.
- [x] Safety and anti-cheat policies documented.
- [x] QA scenarios identified.
- [ ] Open policy decisions resolved or explicitly tracked.
- [ ] Team peer review completed.
- [ ] Product Owner acceptance recorded.

**Task status:** Draft — Not Accepted

**Next Task:** M5-MS01-T07 — Game QA and Edge-Case Checklist.