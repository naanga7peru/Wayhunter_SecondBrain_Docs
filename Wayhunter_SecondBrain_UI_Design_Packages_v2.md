# WAYHUNTER — SECOND BRAIN UI DESIGN & FLUTTER PACKAGE RULES

**Version:** UI-V2.0 | **Date:** 11 November 2026 | **Status:** User-approved visual direction | **Applies to:** Flutter mobile UI only  
**Purpose:** Single source of truth for the Wayhunter UI appearance, required/optional Flutter packages, integration steps and UI review tests. This file is intended to be placed in the Second Brain alongside, not instead of, the BRD.

> **Priority / visual override:** This document supersedes earlier Wayhunter *visual/background/theme* instructions wherever they conflict. It does NOT supersede approved functional requirements, routes, admin verification, wallet/Coins policy, game rules, APIs, database design or existing user journeys. UI reference mockups are illustrative, not functional specifications.

## 1. FINAL DECISION — WHAT THE USER APPROVED

1. **ONLY Login / Sign In and Home use the existing scenic photo background asset**, `wayhunter_auth_home_bg.png`. Do not use the photo as a full-screen background on Traveller, Hunter, Game, Profile, Wallet, Settings, Create Account, OTP, Forgot Password or other screens.
2. **ALL OTHER Flutter screens use Image 1's soft muted teal/grey background appearance**, implemented as a Flutter gradient, NOT as a pasted screenshot/photo. This is a restrained frosted-glass aesthetic: softened green-grey gradient, very subtle depth, semi-transparent cards, rounded corners and clear text.
3. **Image 2 futuristic 3D/cube/glow look is NOT approved** for the app. Do not add holographic stacked 3D shapes, excessive neon, or unrelated interface objects.
4. Module accents: **Traveller = blue/cyan**, **Location Hunter = green**, **Game = purple**. Profile/Settings/Wallet = neutral teal/cyan with green only for success and red for destructive actions.
5. Keep existing functionality and screen structure. Use the background and visual components without replacing forms, map controls, photo workflows, admin states, navigation or data with the reference image's health-app content.
6. **Home keeps the three original PNG cards** (Traveller, Hunter, Game), with transparent surrounding pixels, not black boxed backgrounds. Do not alter the art/images or change their filenames.

### 1.1 Important asset mapping

| Existing source image | Approved use | Notes |
|---|---|---|
| `wayhunter_auth_home_bg.png` | Full-screen Login and Home ONLY | Keep image aspect, add readable overlay if required. If a logo is baked into the image, do not add a second logo. |
| `traveller.png` | Home Traveller button/banner | Original transparent PNG; `BoxFit.contain`; do not add opaque backing. |
| `hunder.png` | Home Location Hunter button/banner | Filename is intentionally `hunder.png`; do not silently rename it. |
| `game.png` | Home Game button/banner | Original transparent PNG; keep size and proportions. |
| User-provided **Image 1** | Visual reference for all other screen *background and glass style* | NOT an asset to draw as the whole screen. Do not reproduce its health-related text, charts or icons. |
| User-provided **Image 2** | Rejected aesthetic reference | Do NOT use its 3D visuals or heavy glow as the app theme. |

**Design interpretation:** Image 1 contains soft teal-green/grey phone UI with semi-transparent milky cards. Replicate its **color temperature, soft gradient and frosted surfaces**, while retaining Wayhunter's own features.

## 2. THEME TOKENS — CONSISTENT DEFAULTS

These are recommended UI starting values (adjust for contrast and device tests), not BRD business rules.

| Token | Suggested value / rule |
|---|---|
| Soft screen background | Top `#678C88` → middle `#9CB7B2` → bottom `#628783`, vertical gradient, *non-photo* |
| Secondary haze | Low-opacity `#D7E6E1` overlays or radial highlight; no large decorative objects |
| Frosted card | `Colors.white.withOpacity(0.20)` or compatible `.withValues(alpha: 0.20)` |
| Card border | Soft white at 0.35 opacity, 1 logical px |
| Card radius | 20–24 logical px; pill/button corners 16–24 px |
| Glass blur | Start `ImageFilter.blur(sigmaX: 8, sigmaY: 8)`; clip to panel; use selectively |
| Main text on light glass | Deep teal/navy `#153039`; check contrast in emulator |
| Text over dark scenic image | White `#F6FBFC` with shadow/gradient to maintain contrast |
| Subtext | `#33535B` on light glass; slightly softer teal |
| Traveller accent | `#13BDEA` (cyan) / `#1379AE` for high-contrast foreground |
| Hunter accent | `#27C17C` (green) / `#146C4E` for high-contrast foreground |
| Game accent | `#A36AF0` (purple) / `#6636B2` for high-contrast foreground |
| Danger / error | `#C6424C` with text and explicit confirm dialog |
| Layout padding | Horizontal 16–20; gaps 8/12/16; control min height 48 |
| Bottom navigation | Fixed 4-icon floating glass bar with existing routes: Home / Hunter / Leaderboard / Profile |

**Text contrast matters:** Soft transparent cards should not make form labels, text or icons disappear. Use darker text on pale glass; use bright text only on a genuinely dark surface. Text appearance takes priority over exact opacity numbers.

## 3. PACKAGE POLICY — MINIMUM DEPENDENCIES FIRST

### 3.1 Flutter SDK built-ins (REQUIRED WIDGETS; NO ADDITIONAL PACKAGE)

| UI purpose | Use built-in Flutter API | Notes |
|---|---|---|
| Soft gradient backgrounds | `DecoratedBox`, `BoxDecoration`, `LinearGradient` | All screens EXCEPT Login/Home |
| Scenic Login and Home image | `Image.asset`, `Stack`, `Positioned.fill` | Use original uploaded asset |
| Frosted glass | `ClipRRect`, `BackdropFilter`, `ImageFilter.blur` | Limit blur area; costly if full-screen/repeated excessively |
| Transparent cards + borders | `Container`, `BoxDecoration`, `Border`, `BoxShadow` | Keep soft edges and readable contrast |
| Forms | `TextFormField`, `InputDecoration`, `Form`, `DropdownButtonFormField` | Use existing validation logic |
| Navigation / transitions | Existing router + `AnimatedContainer`, `AnimatedSwitcher`, `PageRouteBuilder` | Do not replace app router |
| Responsive layouts | `SafeArea`, `LayoutBuilder`, `MediaQuery`, `Expanded`, `Flexible`, `SingleChildScrollView` | Prevent overflow; respect keyboard, notch, accessibility |
| Icons | `Icons` / `Icon` | No new icon package needed for basic UI |
| Images and badges | `Image.asset`, `ClipRRect`, `CircleAvatar` | Retain exact PNG graphics |
| Snackbars/dialogs | `SnackBar`, `AlertDialog`, `showDialog` | Never claim backend approval from UI alone |

### 3.2 Third-party packages (ADD ONLY WHEN THE CURRENT PROJECT NEEDS THEM)

| Package | Priority | Use case | Install | Notes |
|---|---|---|---|---|
| `flutter_animate` | **Recommended (optional)** | Small entrance fade/slide, transitions | `flutter pub add flutter_animate` | Keep animations 150–300 ms; avoid constant shimmer/loops. |
| `google_fonts` | Optional | Consistent typography if existing fonts are insufficient | `flutter pub add google_fonts` | Let pub resolve a compatible SDK version; don't hard-pin newest. Bundle fonts before offline production if needed. |
| `animated_notch_bottom_bar` | Optional **alternative** | If the team specifically approves moving-notch bottom navigation | `flutter pub add animated_notch_bottom_bar` | Use **one** nav implementation, not this plus a custom floating nav. Preserve exact 4 routes. |
| `cached_network_image` | Optional for remote data | Placeholder/error/cached photos of real places/trips | `flutter pub add cached_network_image` | Not needed for 4 local assets. Web caching may have limitations. |
| `flutter_svg` | Optional only for SVG | If new assets are actually SVG | `flutter pub add flutter_svg` | NOT needed for `traveller.png`, `hunder.png` or `game.png`. |

**Existing app packages: KEEP, NOT RE-INSTALL FOR THIS UI CHANGE.** Reuse the project’s current `go_router` (if present), Riverpod/MVVM, maps, localization, camera and API packages. `flutter_localizations`/`intl` are about translation/formatting, not glass styling. The Hunter 360° camera and Traveller map are existing functional integrations and should not be replaced with new look-alike UI packages.

**Avoid:** piling on several competing navigation libraries (`animated_notch_bottom_bar`, `fancy_bottom_navigation_plus`, `curved_navigation_bar_pro`) simultaneously; adding a glassmorphism plugin for an effect Flutter already provides; installing heavy 3D/shader libraries for Image 2 effects (not approved).

### 3.3 Compatibility / update rule

Run `flutter --version`, inspect existing `pubspec.yaml` and `pubspec.lock`, and resolve package dependencies using `flutter pub add <package>`; use the version compatible with the project's Flutter/Dart SDK. Document changed dependency versions in the pull request. Never replace the whole existing `pubspec.yaml` with a sample file.

## 4. SCREEN-BY-SCREEN UI BACKGROUND AND COMPONENT MAP

| Screen / flow | Background | Glass UI elements | Preserve behavior |
|---|---|---|---|
| **Login / Sign In** | Original scenic photo | Frosted sign-in form, login button, language selector | Password, OTP/device binding, form errors, existing route |
| **Home** | Original scenic photo | Transparent top bar, search, ad banner, 3 original mode PNG buttons, floating 4-icon nav | Ads interval, route callbacks, live home content |
| Register / Create Account | Image-1 soft teal-grey gradient | Rounded text fields, step feedback | Name/email/phone/password/validation |
| OTP / Forgot / Reset Password | Same soft gradient | Small focused authentication panels | OTP expiry, resend cooldown, reset conditions |
| Traveller landing | Same soft gradient + cyan accents | Create Trip/My Plans glass actions; trusted places cards | Existing approved Traveller actions |
| Create Trip / Place Picker | Same soft gradient + cyan | Glass fields, date/place controls; map is genuine map widget | Stops, route, budget, vehicle, friends, dates |
| Suggested Plans / My Plans / AI Plan | Same soft gradient + cyan | Frosted list rows/cards, status chips, concise CTAs | Copy/edit/use plan and API response states |
| Start Trip / Live Map | **Real map content in map area**, glass floating controls; soft gradient only outside map | Find, Hazard, Memory, Friends, I’m Safe, Pause/Stop controls | GPS, 1km Find, consent, trip status, route data |
| Location Hunter landing | Same soft gradient + green accents | District indicator, search and discovery list | Current district and GPS-based restrictions |
| Add Place / 360° Capture | Same soft gradient on forms; **real live camera preview** in capture area | Rounded camera controls, step progress | Live camera only, required 360°, duplicate check, admin pending/approval |
| Hunter My Discoveries | Same soft gradient + green | List cards, waiting/approved/rejected labels | Show real admin approval state |
| Game landing / My Games | Same soft gradient + purple | Game cards, create/play actions, expiry chips | Winner/expiry/admin rules |
| Create / Play Game | Same soft gradient + purple | Photo/text hint cards and step buttons | No map/distance meter on clue screen; do not invent answers |
| Profile | Same soft gradient, neutral teal | Avatar, tabs, Coins total, rounded actions | Profile & social data; no RC/HP/XP top chips |
| My Wallet / Redeem / Vouchers | Same soft gradient, neutral teal | Coins balance, star-level bar, voucher/request cards | 10,100 minimum spendable to request 10,000; retain 100; admin reservation/approval |
| Settings / Security / Language / Privacy | Same soft gradient | Light frosted settings rows, switches, dropdowns and dialogs | Tamil/Sinhala/English, account/privacy/logout logic |

**Exception for functional surfaces:** A working map, live camera, 360° preview, user photo/video, or image-based place card naturally displays its real content *inside its allocated widget*. “No photo background” means do not wallpaper the **screen backdrop** with the scenic asset. It does NOT ban functional photos, media, or maps.

## 5. NAVIGATION AND UI STATE RULES

- Show **Home / Hunter / Leaderboard / Profile** in the main fixed bottom bar; use the current route definitions and current selected state. The Game module is reached through the Home Game card and existing Game routes; do not invent a fifth bottom-nav tab.
- Prefer a custom Flutter-only rounded glass navigation bar if it already exists. Use `animated_notch_bottom_bar` only after an explicit choice to replace it; never stack both.
- Transitions must be subtle, quick and optionally reduced for accessibility. No background animations that interfere with input or GPS/map performance.
- Buttons must have active, disabled, loading, success and error states as appropriate. Real admin verification status MUST come from the current source of truth, never hardcoded “Approved”.
- The bottom bar stays visible on main pages; keyboard screens must let users reach submit/buttons. Keep fixed header/footer where the original journey requires, and allow only the **content** to scroll on short devices when needed.
- Keep permissions, auth guards, GPS evidence, camera origin, API calls, Coins holds/debits, one-winner Game policy, 30-day expiry after admin publication and hazards notifications unchanged. These are not theme decisions.

## 6. FILES / COMPONENT ARCHITECTURE — DO NOT OVERWRITE WORK

```text
wayhunter_mobile/
  assets/images/
    wayhunter_auth_home_bg.png        # Login & Home ONLY
    traveller.png                     # Home banner
    hunder.png                        # Home banner, original spelling
    game.png                          # Home banner
  lib/
    core/theme/
      wayhunter_colors.dart           # UI theme constants
      wayhunter_theme.dart            # ThemeData / typography
    core/widgets/
      wayhunter_screen_background.dart # choose scenic vs soft gradient
      wayhunter_glass_card.dart        # reusable frosted card
      wayhunter_glass_button.dart
      wayhunter_glass_bottom_nav.dart  # adapt existing nav, don't duplicate
    features/...                      # EXISTING feature-first MVVM + Riverpod
  pubspec.yaml                        # MERGE changes; never replace
```

**These are suggested locations, NOT a demand to restructure existing code.** If equivalent shared widgets/themes already exist, edit those instead of creating duplicates. In particular, do not overwrite `main.dart`, `app_router.dart`, the existing Riverpod providers or any backend/service files.

## 7. IMPLEMENTABLE FLUTTER EXAMPLE — BACKGROUND + GLASS

This sample uses only the Flutter SDK and can be adapted into the existing UI component library.

```dart
import 'dart:ui';
import 'package:flutter/material.dart';

class WayhunterScreenBackground extends StatelessWidget {
  const WayhunterScreenBackground({
    super.key,
    required this.isLoginOrHome,
    required this.child,
  });

  final bool isLoginOrHome;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return Stack(
      fit: StackFit.expand,
      children: [
        if (isLoginOrHome)
          Image.asset(
            'assets/images/wayhunter_auth_home_bg.png',
            fit: BoxFit.cover,
          )
        else
          const DecoratedBox(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Color(0xFF678C88),
                  Color(0xFF9CB7B2),
                  Color(0xFF628783),
                ],
              ),
            ),
          ),
        child,
      ],
    );
  }
}

class WayhunterGlassCard extends StatelessWidget {
  const WayhunterGlassCard({super.key, required this.child});
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(22),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
        child: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.20),
            borderRadius: BorderRadius.circular(22),
            border: Border.all(color: Colors.white.withOpacity(0.35)),
          ),
          child: child,
        ),
      ),
    );
  }
}
```

**Usage (example):** `WayhunterScreenBackground(isLoginOrHome: false, child: SafeArea(child: ExistingTravellerScreenContent()))`. Login and Home use `true`. Keep the real app's screen widgets and apply this as a wrapper; do NOT replace the screen with a screenshot.

### 7.1 `pubspec.yaml` — merge under the existing `flutter:` block

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/images/wayhunter_auth_home_bg.png
    - assets/images/traveller.png
    - assets/images/hunder.png
    - assets/images/game.png
```

**Note:** The snippet is an illustration of one `flutter:` section, not an instruction to create a duplicate key. Preserve pre-existing assets and dependencies. For older/newer Flutter APIs, use whichever supported color-opacity API your project already uses.

## 8. DEVELOPMENT COMMANDS (WINDOWS / VS CODE / EMULATOR)

```powershell
# From the current Flutter project root
flutter --version
flutter pub get
flutter pub add flutter_animate      # only if animations are required
flutter pub add google_fonts        # OPTIONAL, only if approved
# flutter pub add animated_notch_bottom_bar  # OPTIONAL alternative nav ONLY
flutter analyze
flutter test
flutter devices
flutter run -d <device-id-from-flutter-devices>
```

If dependencies are changed, restart the app fully. Do not assume the emulator ID is always `emulator-5554`. Test on an Android emulator for the final mobile UI; Chrome preview alone is insufficient.

## 9. APPROVAL AND TEST CHECKLIST

- [ ] Login and Home use the original scenic background; no other screen accidentally uses it.
- [ ] All other screen backdrops look like Image 1: soft teal-grey gradient, not a copied screenshot, not Image 2's 3D art.
- [ ] Original `traveller.png`, `hunder.png` and `game.png` remain untouched, with no black rectangle behind them.
- [ ] Traveller blue/cyan, Hunter green, Game purple accents are consistent and readable.
- [ ] All existing screen functions/buttons, text fields, route names and exact bottom-nav 4 destinations remain intact.
- [ ] Real map, camera, 360° evidence, app/user media render in their functional content areas.
- [ ] Screen sizes 320×568, 320×640, 360×800, 390×844 and text scaling/keyboard open have no overflows or clipped submit buttons.
- [ ] `flutter analyze`, relevant widget tests and emulator smoke tests pass.
- [ ] No business logic, coins math, game expiry, admin approval states, auth or API changes were made in this UI-only update.
- [ ] Feature PR provides before/after screenshots + list of changed files + package versions changed.

## 10. SECOND BRAIN / CODEX IMPLEMENTATION INSTRUCTION

> **Implement Wayhunter UI styling only. Read this document and the authoritative BRD first. Preserve all existing feature-first Clean Architecture/MVVM with Riverpod, app routes, screens and backend behavior. Use `wayhunter_auth_home_bg.png` as the full-screen background ONLY for Login and Home, plus original transparent mode-card PNGs on Home. All other screens get the Image-1-inspired soft teal/grey Flutter gradient with subtle frosted glass cards, rounded buttons and high-contrast text. Use blue/cyan Traveller, green Hunter, purple Game accents. Do not adopt Image 2's futuristic 3D effects or its mock content. Prefer built-in Flutter glass primitives; install optional packages only when genuinely needed and compatible. Do not overwrite `main.dart`, `app_router.dart` or `pubspec.yaml`; make small incremental changes. Do not change business logic. Verify responsive screens and report tests and changed files.**

## 11. PACKAGE DOCUMENTATION (CHECK BEFORE INSTALLING)

- Official Flutter blur widget: https://api.flutter.dev/flutter/widgets/BackdropFilter-class.html
- Animation: https://pub.dev/packages/flutter_animate
- Fonts: https://pub.dev/packages/google_fonts
- Optional bottom nav: https://pub.dev/packages/animated_notch_bottom_bar
- Optional remote image cache: https://pub.dev/packages/cached_network_image
- Optional SVG: https://pub.dev/packages/flutter_svg

**Delivery note:** This file is a **UI specification**, not proof that every screen is implemented or that all listed optional packages have been installed.
