# WAYHUNTER — M5 Camera & Gallery Rules

**Task ID:** M5-MS01-T03

**Owner:** M5 — Thuvarathan

**Milestone:** M5-MS01

**Status:** Draft — Pending Review

## 1. Purpose

Document the difference between Game Creator clue images and Game Player live camera proof.

## 2. Game Creator — G-10 / G-11

**Master BRD v2.1, GA-005:**
- Creator can select clue images from the gallery.
- Creator can add text hints.
- Creator can reorder game stages.

**Earlier Demo Guide:**
- Camera-only behavior was requested for the Game module.

**Conflict status: DECISION_REQUIRED**

The final creator image-source policy requires confirmation against the latest approved Game requirements.

Do not implement gallery or camera-only enforcement for creator uploads until this conflict is resolved.

## 3. Game Player — G-06 / G-07

**Confirmed requirements:**
- Player must capture proof using the in-app live camera.
- Gallery selection is prohibited.
- Proof must be associated with UserId, GameId, AttemptId, StageId and server timestamp.
- Proof must be validated by the backend.
- Rejected proof must not advance the stage.
- Pending proof must not award Coins.
- Three rejected proofs close the attempt under the previously established gameplay rule.

## 4. Security & Anti-Cheat

- Validate proof ownership and the active game attempt.
- Reject mismatched or replayed submissions.
- Prevent duplicate stage advancement.
- Never expose private proof files publicly.
- Preserve verification and rejection audit records.
- Do not grant winner rewards before authorized final approval.

## 5. Acceptance Checklist

- [x] Master BRD creator gallery rule documented.
- [x] Earlier camera-only demo behavior documented.
- [x] Player live-camera-only rule documented.
- [x] Proof security requirements documented.
- [ ] Creator image-source conflict resolved by authorized review.
- [ ] Peer review and GitHub PR approval obtained.

**Task status: Draft — Not Accepted.**

**Next Task:** M5-MS01-T04 — Game Database Schema Design.