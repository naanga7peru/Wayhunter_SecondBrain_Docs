# Proposed architecture boundary guide

## Flutter Mobile (proposed)
Feature-first + Clean Architecture + MVVM + Riverpod + GoRouter + repository interfaces. Agreed UI designs/flow references should guide new implementation; these new target repositories have no code audit and owner says project folders/development have not started. Feature groups: `auth`, `home`, `traveller`, `friends`, `hunter`, `games`, `leaderboards`, `profile`, `wallet`, `notifications`, `places`, `weather`, `advertisements`. Map-first UI: real Sri Lanka Google Maps and Places search, route preview, live trip map, Hunter current-district verified places; no fabricated map or compulsory game map hints.

## Angular Admin (proposed)
Standalone components + feature folders for all 17 modules + lazy routing; Signals/RxJS for UI state and HTTP; typed DTOs; Admin guards and per-action permission checks (backend mandatory). `core/`, `layout/`, `shared/`, `features/`. Keep current sidebar/cards/screens once actual repo inspected; do not assume previous organization's repo files exist here.

## ASP.NET Core Backend (proposed)
Clean Architecture Modular Monolith, EF Core + SQL Server, protected Cloudinary media, server-side validation, tokens/RBAC/OTP, audit, idempotent Coins ledger and reservations, notifications / optional SignalR and scheduled expiry/reminders. Controllers and exact endpoints are not verified until repo code/Swagger are read.

## SQL (proposed)
ERD v1.1 comprises **118 baseline proposed tables**, approximately 200 FK links, 13 conceptual domains; extra proposed voucher-source and optional scan results model. The quantity is an engineering suggestion, not necessarily the final database table count. **DO NOT run migrations solely from the ERD.** Actual SQL Server schema/EF migrations must be examined.

## Inter-app ownership
`Flutter` = capture/edit/display/send requests; `Angular` = authorized admin review/control UI; `ASP.NET Core` = irreversible decisions, payments/coins status, privacy authorization; `SQL Server` = durable records; `Cloudinary/FCM/Google/etc` = approved external integrations.
