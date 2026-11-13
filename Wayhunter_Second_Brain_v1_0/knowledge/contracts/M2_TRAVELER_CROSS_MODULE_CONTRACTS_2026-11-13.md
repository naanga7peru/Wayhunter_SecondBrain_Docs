# WAYHUNTER — M2 Traveler Cross-Module Conflict Prevention Contracts

**Date:** 2026-11-13  
**Doc ID:** WH-CONTRACT-M2-001  
**Status:** `PROPOSED — PENDING TEAM-LEADER + AFFECTED OWNER REVIEW`  
**Current assigned M2 owner:** Thadsha  
**Scope:** Flutter + ASP.NET Core Backend, mock-first development; Angular Admin later  
**Does not mean:** running endpoints, connected APIs, approved ownership migration, working mobile/DB features, or completed project tasks.

## 0. Source-of-truth and legacy tracker mismatch (ACTION REQUIRED)

**Current proposed 523-task allocation:** M1 Shayanthan = Identity/Profile/Friends; M2 Thadsha = Traveler Planning/Maps/AI; M3 Mathi = Active Trip/Safety; M4 Neela = Hunter/Places; M5 Thuvarathan = Games; M6 Kaviyan = Coins/Wallet; M7 Thashvini = Home/Ads/Navigation.  
**Original 490-task screenshot instead lists:** M2 Thadsha = Friends/Safety/Social; M3 Mathi = Traveler/Maps/AI; M7 Thashvini = Admin Platform/Release; M1 Shayanthan includes Home. **Do not silently overwrite historical evidence.**

**Resolution proposed:** Develop with 523-task ownership; team leader approves this specific allocation, then updates the active tracker Overview/member sheets, GitHub `docs/OWNERSHIP_MAP.md`, affected module briefs, and labels the historical workbook *LEGACY* rather than changing original task history. If approval is withheld, stop and explicitly reconcile responsibilities before cross-module implementation.

**Required sign-off:** Team leader (M1/M2/M3/M7 affected); record reviewer, date, PR/meeting reference. Until then the allocation decision is **PENDING APPROVAL**.

## 1. Ownership matrix — exactly one authoritative owner

| Boundary | M2 Thadsha owns | Other owner owns | Must NOT do |
|---|---|---|---|
| Login and user | Trip's `ownerUserId` reference and Traveler UI using M1's authenticated user context | **M1 Shayanthan:** stable UserId, roles, token/auth/session, profile, friends | Do not build a second login/token scheme or trust arbitrary client userId as authorization |
| Planned vs live trip | Trip drafts, saved/edited itineraries, ordered stops, places picker, planned route geometry, suggested/AI drafts | **M3 Mathi:** Start/Pause/Stop/Finish session, trip live GPS, group location sharing consent, hazards, notification delivery | M2 must not own active-trip sessions, persistent live GPS or hazard notification rules |
| Hunter-approved places | Traveler search/selection, show approved Hunter places and third-party provider locations with distinct source/status | **M4 Neela:** Hunter evidence/approval state, trusted Hunter place content, duplicate/restricted checks | Do not mark pending/rejected Hunter submissions as verified or implement Hunter Admin approval |
| Home/navigation | Traveler feature route entry points, screen widget API | **M7 Thashvini:** Home shell, dynamic selected-module tab, global router/theme, ad presentation | Don't edit `lib/app/wayhunter_app.dart`, global router/theme without M7-approved PR |
| Games/leaderboard | Only future Traveler-specific ranking *data source*, if explicitly defined | **M5 Thuvarathan:** common leaderboard UI + Games | Don't create Game ranking UI/logic inside Traveler screens |
| Coins/wallet | No Coin balance mutation from creating/saving a plan | **M6 Kaviyan:** authoritative ledger and all reward events | Do not award coins on trip draft submit or call ledger updates from M2 |

## 2. Draft contract M2 → M3: Planned trip handoff

**Contract ID:** `M2-M3-TRIPPLAN-v0.1-DRAFT` (not a live API).  
**Producer:** M2 Trip Planning. **Consumer:** M3 Active Trip & Safety.  
**Handoff event:** User selects **Start Trip** for an existing, authorized Trip Plan. M2 supplies persisted plan snapshot. M3 determines if/when a *live* session can start.

**Proposed fields for review (types/validation to be confirmed jointly):**

```text
TripPlanHandoff {
  tripPlanId: opaque stable ID,
  ownerUserId: trusted identity reference (server validated),
  planVersion: integer / concurrency token,
  title: string,
  plannedStartDate: ISO local date,
  plannedEndDate: ISO local date,
  orderedStops: [
    { stopId, orderIndex, placeId?, label, latitude?, longitude?, source }
  ],
  plannedRouteGeometry: normalized geometry or explicit unavailable state,
  routeVersion: version/ETag tied to ordered stops,
  draftStatus: Draft | ReadyToStart | Cancelled (names are PROPOSED)
}
```

**Boundary rules:**
- M2 owns plan create/edit/reorder; M3 owns `LiveTripSessionId`, actual start/pause/finish, consent, location updates and active-trip hazards.
- M3 must receive **ordered stops + route geometry version together**; do not allow mismatched/stale geometry after reorder. If planned route is unavailable, mark it explicitly, never fabricate a polyline, ETA, or distance.
- Authorization checks belong on the server; client-supplied `ownerUserId` is not sufficient proof.
- M3 hazard eligibility uses planned route intersection within **1 km** and server report expiry **24 hours**; show original hazard photo capture timestamp according to latest approved rules. M2 provides route, **does not** own alert delivery.
- If M2 re-edits a plan while an M3 session exists, exact allowed behavior is `DECISION_REQUIRED`; neither member invents a sync rule.

**Joint acceptance examples:** saved plan retains order; modifying stop invalidates/recalculates route version; M3 cannot start other user's trip; fake route-unavailable state handled; pause/stop actions never implemented in M2.

## 3. Draft contract M4 → M2: Place Picker

**Contract ID:** `M4-M2-PLACE-v0.1-DRAFT` (not a live API).  
**Producer:** M4 Hunter Places. **Consumer:** M2 Place Picker/Traveler Map.

**Proposed DTO:**

```text
TravelerPlace {
  placeId: opaque stable ID,
  displayName: string,
  latitude: valid -90..90,
  longitude: valid -180..180,
  source: HunterApproved | ExternalProvider | UserDraft (PROPOSED),
  verificationState: Approved | Unverified | Pending | Rejected (PROPOSED),
  district?: string,
  lastVerifiedAtUtc?: ISO-8601 timestamp
}
```

**Rules:**
- Hunter-origin places may appear as **verified Hunter POIs only when M4 says Approved**. Pending/Rejected must not be displayed as verified/public Hunter places.
- External Maps/Places provider candidates are **not** automatically Hunter-approved. Source/verification labels must not be mixed.
- M2 controls selection/search UI and trip-stop references; M4 controls Hunter approval state and place authority.
- Place deletion/rejection after it is referenced by an existing saved plan is `DECISION_REQUIRED`; define snapshot/fallback explicitly before persistent integration.
- Denied GPS permission → manual search entry; don't treat missing GPS as consent. Restricted areas must not be presented as eligible Hunter submission targets.

**Joint acceptance examples:** approved Hunter place visible; pending/rejected hidden from verified list; provider place labelled correctly; manual location search works with GPS denied; duplicate PlaceIds not appended as duplicate stops without review.

## 4. Draft contract M1 → M2: Identity

**Contract ID:** `M1-M2-IDENTITY-v0.1-DRAFT`.
- M1 provides current verified UserId/auth state via centralized identity context.
- M2 only stores a trusted owner ID reference on TripPlan and checks access server-side. M2 must not own OTP, registration, session token issuance or role checks.
- Anonymous/expired session must lead to clear sign-in/error flow (UI design in coordination with M1/M7); never silently save a trip under placeholder production identity.
- Account deletion, shared-trip privacy and edit permission details require M1+M2 review, not assumptions.

## 5. Draft contract M7 ↔ M2: UI/navigation

**Contract ID:** `M7-M2-NAV-v0.1-DRAFT`.
- M2 adds Traveler entry/widgets inside `lib/features/traveller/planning/` and `lib/features/traveller/maps/`.
- M7 owns common app shell, global router, Home → Traveler entry, navigation theme and selected-module bottom tab.
- Agreed entry screen candidates: Traveler Home / Create Trip / My Plans; final route names/navigation parameters require M7+M2 sign-off.
- Bottom nav remains **Home / Selected Module / Contextual Leaderboard / Profile**. M2 must not fork global app shell or modify `main.dart` / `lib/app/wayhunter_app.dart` independently.

## 6. Paths and mock-first workflow (agreed design direction, not an implemented API)

**Flutter ownership paths:**

```text
lib/features/traveller/planning/
  domain/entities/                 # TripPlan, TripStop; M2
  domain/repositories/             # ITripPlanRepository contract; M2
  data/datasources/               # FakeTripPlanDataSource NOW; HTTP adapter LAST
  data/repositories/              # Repository implementation, fake injected now
  presentation/views/             # Create Trip, My Plans, Edit Trip
  presentation/viewmodels/        # State, validation, loading/error handling
lib/features/traveller/maps/      # Place picker, planned route UI, provider adapter interface
```

**Backend ownership paths:**

```text
src/Wayhunter.Domain/Modules/TravelPlanning/
src/Wayhunter.Application/Modules/TravelPlanning/
src/Wayhunter.Api/Controllers/Mobile/TravelPlanning/      # approved route design; live calls later
src/Wayhunter.Infrastructure/Persistence/Repositories/TravelPlanning/
tests/Wayhunter.UnitTests/Modules/TravelPlanning/
tests/Wayhunter.IntegrationTests/Modules/TravelPlanning/
```

- **NOW:** business models, request/response drafts, interfaces, mock in-memory repositories, Flutter views/ViewModels and independent tests.
- **LATER:** shared ApiClient, real ASP.NET HTTP endpoints, EF Core/SQL backing, external Maps/AI, production secrets and device integration tests.
- Do not invent endpoint URLs as existing. All actual API routes must be verified against compiled backend + OpenAPI at integration time.
- M2 changes **only owned paths**; shared project files (`lib/app`, `lib/core/auth`, `lib/core/network`, solution/global EF migrations) require impacted-owner review.

## 7. Conflict-prevention checklist (review before first feature PR)

- [ ] Team leader explicitly approves updated **M2 Traveler / M3 Live Trip / M7 Shell** allocations and marks historical workbook as *legacy* without rewriting its task history.
- [ ] Mathi (M3) agrees TripPlanHandoff fields, route version, status ownership, authorized Start Trip boundary.
- [ ] Neela (M4) agrees PlaceId/location/source/approval states and verified-marker policy.
- [ ] Shayanthan (M1) agrees trusted UserId, auth/session ownership and private fields.
- [ ] Thashvini (M7) agrees Traveler entry routing and protected shared UI ownership.
- [ ] M2 drafts contract examples using **mock data** and unit/widget tests for the above cases.
- [ ] Cross-owner reviews are linked in GitHub PRs; no manual edit of other owners' modules without review.
- [ ] The seven-member tracker reflects correct names, owners and tasks. Do **not** mark any task `Done` until tests, reviewer approval and evidence are present.

## 8. Approval record — fill in; do not pre-approve

| Contract | Required approval | Current state | Evidence/Date |
|---|---|---|---|
| 523-task allocation vs legacy screenshot | Team leader + impacted M1/M2/M3/M7 | **Pending** | — |
| M2-M3 Trip handoff | Thadsha + Mathi | **Pending** | — |
| M4-M2 Approved Place | Neela + Thadsha | **Pending** | — |
| M1-M2 User identity | Shayanthan + Thadsha | **Pending** | — |
| M7-M2 Navigation | Thashvini + Thadsha | **Pending** | — |

**Decisions required:** in-flight plan edit policy; saved-plan behavior after Hunter place becomes rejected/deleted; final enum/ID/route coordinate formats; payload authorization and pagination/error version. These are intentionally **not assumed**.

## 9. Related Second Brain documents

- `knowledge/LATEST_APPROVED_2026-11-11.md` — approved product rules; takes precedence for explicitly documented conflicts.
- `knowledge/TEAM_MILESTONE_TASK_MASTER_2026-11-11.md` — proposed 523 task owner allocation.
- `knowledge/TEAM_GIT_WORKFLOW.md` — cross-owner boundaries and reviewed PR discipline.
- `planning/member_briefs/M2_FULLSTACK_MILESTONES_TASKS.md` — M2 10 milestones / 59 tasks.
- `planning/WAYHUNTER_523_TASKS.md` — actionable task traceability.

**Implementation status:** This file documents a proposed conflict-avoidance contract. It has not changed code, the older tracker, GitHub PRs or any approved business requirement.
