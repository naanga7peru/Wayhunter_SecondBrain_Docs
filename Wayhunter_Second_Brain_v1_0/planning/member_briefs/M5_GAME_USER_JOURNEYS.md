# WAYHUNTER — M5 Game User Journeys

**Task ID:** M5-MS01-T01  
**Owner:** M5 — Thuvarathan  
**Milestone:** M5-MS01 — Game Policies, States and Audit Schema  
**Status:** Draft — Pending Peer Review  
**Source:** Master BRD v2.1, Section 06, Pages 9–10; `LATEST_APPROVED_2026-11-11.md`

## 1. Purpose

Document all 16 Game screens and the two separate approval journeys: Game creation approval and Player completion approval.

This is a requirements document, not evidence of implemented or tested code.

## 2. Game Screen Inventory

| Screen ID | Screen | Main Function |
|---|---|---|
| G-01 | Game Home | Create Game, Play Game, My Games, Rules, Leaderboard, Rewards |
| G-02 | How to Play | Hints, timer, live proof, safety and reward rules |
| G-03 | Play Game List | Show approved, active, unexpired games |
| G-04 | Game Details | Creator, stages, duration, reward and eligibility |
| G-05 | Hint Stage | Photo/text clues, stage progress and server-based timer |
| G-06 | Player Live Camera | In-app camera proof; gallery prohibited |
| G-07 | Proof Review | Retake, submit, Pending/Approved/Rejected status |
| G-08 | Victory | Pending result or confirmed verified victory |
| G-09 | Game Over | Timeout, failure and permitted retry feedback |
| G-10 | Create Game | Title, description, cover, duration and stages |
| G-11 | Photos & Hints | Creator clue images, text and stage ordering |
| G-12 | Preview & Submit | Review draft and submit for Admin approval |
| G-13 | My Games | Created, Played, Pending, Rejected, Active and Archived games |
| G-14 | Game Leaderboard | Ranking from eligible approved Game-earned Coins |
| G-15 | Rewards Store | Open shared Wallet offers and redemption |
| G-16 | Game History | Attempts, stages, results, proofs and Coins history |

## 3. G-UJ-01 — Creator Journey

1. G-01: Select **Create Game**.
2. G-10: Enter game title, description, duration and stages.
3. G-11: Add ordered photo/text clues.
4. G-12: Preview and submit.
5. Backend records GameId, CreatorUserId, creator name snapshot and submission timestamp.
6. Game enters **Pending Admin Review**. It is not public.
7. Admin reviews clues, safety and anti-cheat rules.
8. **If rejected:** Save rejection reason, notify creator, award no Coins.
9. **If approved:** Publish game, record ApprovedAtUtc and ExpiresAtUtc, and send one eligible +100 Creator Coins event to M6.
10. Game is playable only while approved, active and unexpired.
11. At exactly 720 hours after Admin approval, remove the game from public discovery and play.
12. Retain the game as **Expired/Archived** in the creator's My Games and preserve records and audit history.

## 4. G-UJ-02 — Player Journey

1. G-03: Browse approved active games.
2. G-04: Open details and check eligibility. Creator cannot play their own game.
3. Select Start. Backend validates game state and expiry.
4. G-05: View the current stage's photo/text hints and timer.
5. G-06: Capture live camera evidence.
6. G-07: Review and submit proof linked to UserId, GameId, AttemptId, stage and server time.
7. Advance only when the required verification has accepted the stage evidence.
8. Repeat the stage flow until the final eligible completion.
9. Final completion enters **Pending Admin Verification**.
10. Admin reviews the result and anti-cheat evidence.
11. Only one eligible verified winner is allowed per game.
12. On approval, send one eligible +100 Winner Coins event to M6. No credit for pending, rejected, failed or expired results.
13. G-08, G-13 and G-16 display the accurate confirmed or pending result and history.

## 5. Current Approved Game Rules

- Exactly one Admin-verified winner per game.
- Creator cannot win their own game.
- Game creation approval and player winning approval are separate decisions.
- `ExpiresAtUtc = ApprovedAtUtc + 720 hours`.
- Expired games cannot accept new starts, resumed play, completion or winner approval.
- Expired games must be archived, not physically deleted.
- Creator approval = +100 Coins once.
- Verified winner approval = +100 Coins once.
- M6 owns the authoritative Coins ledger and balance changes.
- Player evidence is live-camera-only.
- No mandatory game map or distance meter.
- Rewards, approval decisions and expiry gates must be enforced by the backend.

## 6. Source Conflicts Requiring Attention

**Already resolved by latest approved rules:**

- GA-004: Exactly one verified winner, not multiple.
- GA-007: Exactly 720 hours from Admin approval, not an ambiguous calendar month.
- GA-009: No valid gameplay completion or winner approval after expiry.
- Navigation: Global bottom navigation uses Home / Selected Module / Contextual Leaderboard / Profile.

**DECISION_REQUIRED — Creator clue image source:**

Master BRD GA-005 allows creator clue photos from the gallery. Earlier demo instructions requested direct camera capture. Confirm the intended creator image source before implementing upload behavior. Player proof remains live-camera-only.

## 7. M5-MS01-T01 Acceptance Checklist

- [x] G-01 to G-16 screen inventory documented.
- [x] Game creation journey documented.
- [x] Player completion journey documented.
- [x] Separate Admin approval flows documented.
- [x] Latest explicitly approved game rules referenced.
- [ ] Creator clue media-source conflict reviewed.
- [ ] Peer review and GitHub PR evidence attached.

**Task status:** Draft / In Review — Not Accepted.

**Next milestone task:** M5-MS01-T02 — Winner Count and Expiry Decision Trace.