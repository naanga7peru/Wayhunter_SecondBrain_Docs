# WAYHUNTER — SECOND BRAIN v1.0

**இது Academic Final Project Second Brain. Folder Structure/Development இன்னும் தொடங்கவில்லை; GitHub-ல் Push செய்யப்படவில்லை. Current Rules: `knowledge/LATEST_APPROVED_2026-11-11.md` (முதலில் இதைப் படிக்கவும்). Source PDFs reference/historical versions.**

## 1. இதில் என்ன உள்ளது?
- `sources/` — ஐந்து தற்போதைய PDF references (Master BRD v2.1; Admin Flow v1.1; Flutter v2.1; Angular Admin v3.1; ERD v1.1).
- `knowledge/` — Codex/Team பயன்படுத்த படிக்கக்கூடிய Project Context, User Journeys, Business Rules, Decisions, Security, API boundaries, Development Status.
- `repo_overlays/` — ஒவ்வொரு GitHub Repo-க்கும் தனி `AGENTS.md` + `docs/second-brain/CONTEXT.md`.
- `tools/` — பாதுகாப்பான Repo file inventory tool; ஒவ்வொரு clone-ன் உண்மையான path-ஐ உன்னிடமிருந்து பெற வேண்டும்.

## 2. உன் 3 புதிய GitHub Repositories
1. Angular Admin — https://github.com/naanga7peru/Wayhunter_mobile_application_admindashboard_angular
2. Flutter — https://github.com/naanga7peru/Wayhunter_mobile_application_frontend_flutter
3. Backend — https://github.com/naanga7peru/Wayhunter_mobile_application_Backend

**2026-11-11 access result:** தற்போதைய GitHub Plugin connection மூலம் 3 repos-க்கும் 404 வருகிறது. இது private/permission பிரச்சினையாக இருக்கலாம்; *repo இல்லை / காலியாக உள்ளது* என்பது verified fact அல்ல. இந்த Package-ல் actual repo code audit செய்யப்படவில்லை.

## 3. GitHub connection சரிசெய்ய
GitHub App-க்கு `naanga7peru` organization-ன் இந்த மூன்று repos-க்கும் access கொடு (GitHub organization Settings > GitHub Apps / Installed GitHub Apps; organization owner approval தேவைப்படலாம்). பிறகு ChatGPT-ல் மீண்டும் code audit செய்யலாம். Public ஆக்கத் தேவையில்லை.

## 4. Windows-ல் பயன்படுத்துவது
ZIP-ஐ extract பண்ணு. 3 GitHub repos-ஐ local-ல் clone பண்ணியிருந்தால் இந்த ZIP-ல் உள்ள `repo_overlays/<repo>/AGENTS.md`-ஐ அந்த repo root-க்கு copy செய்; கூடவே அதன் `docs/second-brain/CONTEXT.md` மற்றும் `docs/second-brain/ACTIVE_RULES.md`-ஐ copy செய். **ஏற்கெனவே `AGENTS.md` இருந்தால் overwrite செய்யாதே.** Existing instructions-ஐ merge செய்து commit review செய்.

Codex-க்கு example prompt:
> `Read AGENTS.md, docs/second-brain/ACTIVE_RULES.md and CONTEXT.md first. Admin approval debits 10,000 Coins once (10,100 spendable minimum); Game archives after 30 days; treat repos as not-yet-scaffolded until verified. Propose folder/API plans before edits.`

## 5. Source priority
1. **User-approved newest business decisions** (unapproved suggestions are not rules).
2. **Master BRD v2.1** for functional baseline and conflicts; still draft, not final signoff.
3. **Admin Working Process v1.1** for functional Admin steps; proposed scanning not approved.
4. **Flutter Architecture v2.1 / Angular Architecture v3.1** for *proposed* design boundaries.
5. **ERD v1.1** for *proposed* schema, not migrated DB.
6. **GitHub actual code** when accessible is authoritative for *implemented state*, not product intent.

## 6. Current resolved rules & genuinely pending items — do not silently decide
- **Resolved (2026-11-11):** Admin Approval-ல் 10,000 Coins deduct; minimum 10,100 spendable; 100 மீதி; sample voucher image + unique code + QR.
- **Resolved (2026-11-11, owner clarification):** ஒரு Game-க்கு ஒரே verified winner; Admin approval-லிருந்து 30 நாட்களில் Public/Playable UI-ல் இருந்து hide செய்து, Database மற்றும் Creator My Games-ல் Expired/Archived-ஆக வைத்திரு; countdown காட்ட வேண்டும்.
- **Resolved (2026-11-11):** Hazard route-க்கு 1 km-க்குள் இருப்பவர்களுக்கு மட்டும்; photo capture time காட்டி 24 மணி நேரத்தில் active alert நீக்க வேண்டும்.
- **Resolved (2026-11-11):** Bottom nav: Home / selected module / Leaderboard / Profile.
- **Still pending:** Exact Admin RBAC roles; optional voucher OCR/barcode intake not mandatory; technical API code verification requires repository access.

## 7. Security
Never commit API keys, OTPs, private voucher codes, .env secrets, database passwords, personal GPS trails, or raw contacts. No real admin balance changes from the browser; backend is authority.

**Package assembled 2026-11-11. No GitHub commits, branches, SQL migrations, or production deployments were executed.**
