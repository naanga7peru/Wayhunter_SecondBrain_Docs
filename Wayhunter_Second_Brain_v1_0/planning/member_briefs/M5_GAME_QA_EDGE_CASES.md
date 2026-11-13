# WAYHUNTER — M5 Game QA & Edge-Case Test Plan

**Task ID:** M5-MS01-T07

**Owner:** M5 — Games, Anti-Cheat & Leaderboard

**Milestone:** M5-MS01 — Game Policy, States and Architecture

**Status:** Draft — Review Pending

**Test Execution Status:** Not Started

## 1. Purpose

Define planned quality assurance scenarios for the Wayhunter Game module, covering publication, proof validation, Admin decisions, winner eligibility, expiry, anti-cheat, and Coins reward integration.

This document is a QA planning artifact, not evidence of completed testing.

## 2. Scope

The planned QA coverage includes:

- Game creation and Admin publication
- Creator eligibility
- Player participation and stage progression
- Live-camera evidence submission
- Proof rejection and attempt closure
- Game expiry and archival
- Single verified winner enforcement
- Anti-cheat and replay prevention
- M6 Coins reward contracts
- Backend authorization and database integrity
- Network, timeout, and concurrent-request edge cases

## 3. Test Environments

Testing is planned across:

1. Flutter mobile Game module
2. ASP.NET Core Game backend
3. SQL Server persistence
4. Angular Admin Game review module
5. M6 Wallet integration through an agreed adapter

During initial development, mocks and test doubles may be used.

Real API integration and end-to-end testing will happen in the agreed integration phase.

Do not mark a scenario as passed until it has been executed and evidence has been recorded.

## 4. Test Status Definitions

| Status | Meaning |
|---|---|
| Not Run | Test not yet executed |
| Pass | Actual result matches expected result |
| Fail | Actual result differs from expected result |
| Blocked | Dependency or unresolved decision prevents testing |
| Retest | Fix applied; verification still required |

All scenarios below initially have status **Not Run**, unless explicitly marked **Blocked by Decision**.

## 5. Test Data Requirements

Prepare controlled test accounts:

- User A — Game creator
- User B — Eligible player
- User C — Competing player
- User D — Admin reviewer
- User E — Other authorized Admin reviewer

Prepare games with these states:

- Draft
- Pending Admin review
- Rejected
- Published and active
- Near expiry
- Expired
- Archived
- Verified winner already selected

Use test media with known ownership and capture source.

Do not use live personal data for security or anti-cheat testing.

## 6. Game Creation and Publication

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-001 | Creator submits valid game | Game enters Pending Admin review |
| QA-002 | Creator submits incomplete required fields | Backend rejects invalid submission |
| QA-003 | Admin approves eligible game | Game becomes published |
| QA-004 | Admin rejects game | Game remains unavailable for public play |
| QA-005 | Unauthorized user attempts approval | Request rejected |
| QA-006 | Repeated Admin publication approval | No duplicate publication reward |
| QA-007 | Creator checks pending game | Waiting for Admin verification displayed |
| QA-008 | Approved game appears in discovery | Only eligible active games appear |

**Status:** Not Run

## 7. Creator and Player Eligibility

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-009 | Creator attempts to play own game | Blocked |
| QA-010 | Unauthenticated player starts game | Authentication required |
| QA-011 | Player starts unpublished game | Blocked |
| QA-012 | Player starts expired game | Blocked |
| QA-013 | Player starts game with confirmed winner | Blocked |
| QA-014 | Eligible player starts active game | Attempt created |
| QA-015 | Client bypasses Flutter eligibility controls | Backend still enforces restrictions |

**Status:** Not Run

## 8. Camera Proof and Stage Validation

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-016 | Player captures live stage proof | Eligible proof can be submitted |
| QA-017 | Player attempts gallery proof | Gallery selection prohibited |
| QA-018 | Player submits proof for wrong stage | Rejected |
| QA-019 | Player skips required stage | Blocked |
| QA-020 | Player reuses another attempt's proof | Rejected or flagged |
| QA-021 | Player submits duplicate proof request | No duplicate stage completion |
| QA-022 | Proof references another user's media | Rejected |
| QA-023 | Modified client claims live capture without valid evidence | Cannot bypass server validation |

**Status:** Not Run

**Open Decision:** Creator clue-image gallery versus camera-only policy remains unresolved. Its related test must remain blocked until the Product Owner confirms the rule.

## 9. Three-Rejection and Attempt Closure

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-024 | First proof rejection | Rejection recorded |
| QA-025 | Second proof rejection | Rejection recorded |
| QA-026 | Third proof rejection | Current attempt closed |
| QA-027 | Closed attempt submits another proof | Blocked |
| QA-028 | Closed attempt requests winner approval | Blocked |
| QA-029 | Same review rejection delivered twice | Duplicate delivery must not count twice |
| QA-030 | Player requests new attempt after three rejections | Blocked by retry-policy decision |

**Status:** Not Run

The rejected-proof counter must reflect distinct authoritative rejection decisions, not duplicate network deliveries.

## 10. Single-Winner Enforcement

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-031 | First eligible completion approved | One verified winner recorded |
| QA-032 | Second player approved after winner exists | Blocked |
| QA-033 | Two Admins approve different winners simultaneously | At most one winner committed |
| QA-034 | Repeated approval of same winning attempt | No second winner or reward |
| QA-035 | Creator attempts to receive winner status | Blocked |
| QA-036 | Failed completion requests winner verification | Blocked |
| QA-037 | Game expires before a pending winner decision | New winner approval blocked |

**Status:** Not Run

Winner selection must be concurrency-safe. Database constraints and atomic transaction behavior require backend architecture validation.

## 11. Expiry and Archival

Approved expiry formula:

`ExpiresAtUtc = ApprovedAtUtc + 720 hours`

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-038 | Game active immediately before expiry | Eligibility determined by authoritative server time |
| QA-039 | Game reaches expiry boundary | New participation blocked at expiry |
| QA-040 | New attempt after expiry | Blocked |
| QA-041 | Existing attempt resumes after expiry | Blocked |
| QA-042 | Completion approval requested after expiry | New approval blocked |
| QA-043 | Expired game shown in public discovery | Hidden |
| QA-044 | Creator views expired game history | Archived record available |
| QA-045 | Duplicate expiry processing event | No duplicate harmful state transition |
| QA-046 | User changes mobile device clock | Expiry unchanged |

**Status:** Not Run

Expiry must not physically delete historical game or audit records.

## 12. M6 Coins Reward Contract

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-047 | Eligible creator publication approval | Creator receives one +100 Coins reward through M6 |
| QA-048 | Eligible verified single winner | Winner receives one +100 Coins reward through M6 |
| QA-049 | Game pending approval | No creator reward |
| QA-050 | Game rejected | No creator reward |
| QA-051 | Player completion rejected | No winner reward |
| QA-052 | Same creator reward event delivered twice | Credit applied once |
| QA-053 | Same winner reward event delivered twice | Credit applied once |
| QA-054 | M6 temporarily unavailable | Eligible reward remains traceable for retry/reconciliation |
| QA-055 | Retry after successful credit | No duplicate ledger credit |

**Status:** Not Run

M5 must not directly mutate the M6 CoinWallets balance.

M6 contract approval is required before final integration acceptance.

## 13. Safety and Anti-Cheat

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-056 | Game contains unsafe instructions | Admin can reject publication |
| QA-057 | Game directs users into restricted areas | Flagged or rejected through safety review |
| QA-058 | Player reuses proof from another account | Rejected or flagged |
| QA-059 | Impossible stage order detected | Suspicious activity recorded |
| QA-060 | Player rapidly repeats invalid submissions | Appropriate validation or protection applied |
| QA-061 | Player reports an unsafe game | GameReport created |
| QA-062 | Admin investigates anti-cheat flag | Review decision recorded |
| QA-063 | Suspicious flag exists without confirmed misconduct | No automatic unsupported punishment |

**Status:** Not Run

## 14. Network, Timeout and Failure Scenarios

| ID | Test Scenario | Expected Result |
|---|---|---|
| QA-064 | Network disconnects during proof upload | No false successful submission |
| QA-065 | Player resubmits after a network timeout | Duplicate-safe processing |
| QA-066 | Backend restarts during game approval | Persisted state remains consistent |
| QA-067 | Two requests update same attempt concurrently | No invalid state transition |
| QA-068 | Unauthorized API request modifies winner | Rejected |
| QA-069 | Invalid GameId or AttemptId provided | Safe validation failure |
| QA-070 | Duplicate Admin review request | Idempotent handling |
| QA-071 | Stage timer reaches deadline | Behavior follows confirmed timeout policy |

**Status:** Not Run

Stage timeout semantics must be confirmed before QA-071 can be accepted.

## 15. Required Test Evidence

For each executed test, record:

- Test Case ID
- Test Date
- Tester
- Environment
- App / API version or commit
- Input data
- Actual result
- Pass / Fail / Blocked status
- Screenshot or sanitized log reference
- Related bug or GitHub issue
- Retest result when applicable

Avoid storing authentication secrets, personal information, or private media in GitHub issue attachments.

## 16. Unresolved Decisions

The following must remain explicitly open until confirmed:

1. Creator clue-image capture source: gallery or camera-only.
2. Whether a player can create another attempt after three rejected proofs.
3. Exact stage timeout, pause and retry behavior.
4. Concrete database enforcement for one verified winner.
5. Exact M6 event schema, uniqueness constraints and reward-status contract.
6. Final Admin response to confirmed collusion.

Test cases affected by unresolved decisions must be marked Blocked, not Pass.

## 17. M5-MS01 Milestone Review

Required prior documentation:

- T01 — Game User Journeys
- T02 — Winner and Expiry Rules
- T03 — Camera and Proof Rules
- T04 — Game Database Schema
- T05 — M6 Coins Reward Contract
- T06 — Safety, Replay and Eligibility Rules
- T07 — QA and Edge-Case Test Plan

Merging documents is not proof of Product Owner acceptance or completed implementation.

## 18. Acceptance Checklist

- [x] Game publication scenarios documented.
- [x] Creator and player eligibility scenarios documented.
- [x] Live-camera proof scenarios documented.
- [x] Three-rejection closure scenarios documented.
- [x] Single-winner concurrency scenarios documented.
- [x] 720-hour expiry and archival scenarios documented.
- [x] M6 Coins idempotency scenarios documented.
- [x] Safety and anti-cheat scenarios documented.
- [x] Network and failure scenarios documented.
- [ ] Team QA / Backend reviewer approval.
- [ ] M6 owner validates reward integration cases.
- [ ] Product Owner decisions and milestone acceptance recorded.
- [ ] Planned tests executed during development and integration.

**Document Status:** Draft — Not Accepted

**M5-MS01 Status:** Review Pending

**Next Phase:** Proceed with the next approved M5 development milestone after documenting and tracking outstanding dependencies.