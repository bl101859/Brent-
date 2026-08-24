# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repo is

The active project is **Caffevolve** — a mobile-app UX prototype for a
caffeine-management app. It lives entirely in a single self-contained HTML file:

- **`Caffevolve/Caffevolve_UX_Prototype.web.50.html`** — the prototype (~17.9k lines, ~875 KB).

The repository also still contains legacy, unrelated content from its origin as a
Microsoft Power BI course repo (`Lab1`–`Lab8/`, `TShirt/`, `MIT License.txt`,
`README.md`). Ignore those unless explicitly asked — all Caffevolve work happens
in `Caffevolve/`.

## Working branch

Develop on **`claude/portal-index-investor-deck-kgbmbu`**. Commit and push there;
do not push to `master` without explicit permission.

## The prototype: architecture

It is **one standalone HTML document** — HTML, CSS, and JS all inline. There is no
build step, package manager, framework, or server. Open it directly in a browser,
or in a Claude Code session use `SendUserFile` with `display: "render"` to view it.

- **No external resources** except Google Fonts (Cormorant Garamond + DM Sans).
  No images, no `fetch`/XHR, no CDN scripts. Keep it that way — it must stay
  openable offline as a single file.
- **Design tokens** live in the `:root` CSS block near the top (colors like
  `--gold`, `--amber`, `--screen-bg`; fonts `--font-display` / `--font-ui`; the
  device frame is `--screen-w: 390px` × `--screen-h: 780px`). Prefer these tokens
  over hard-coded values when styling.
- **JavaScript** is split across several `<script>` blocks near the end of the
  file. It is vanilla JS — plain functions and global state, no modules.

## Navigation model

- Screens are `div`s identified by a screen ID (e.g. `SU0`, `PS1a`, `BN-Decaf`).
- Move between screens with **`goto('SCREEN-ID')`**. Current/previous screen are
  tracked in the globals `currentScreenId` / `previousScreenId`, and the active
  flow in `currentPath` (e.g. `'A'`, `'C2'`).
- `goto()` contains a **bedtime gate**: navigating into a brew-calculation screen
  (`OAS0`, `PS2a`, `PS2rg`) when `sessionBedtime.hasExpired()` redirects to `PS1a`
  first (path `C2` "Just Brew" is exempt). Keep this in mind when adding screens
  to those flows.

### Screen-ID prefixes (flows)

- `SU-*` — setup / onboarding (bean & grind selection, profile creation)
- `SU-ADMIN` — device/admin settings, **PIN-gated** (default PIN `1234`)
- `PS-*` — planning / brew-session screens (the largest group)
- `OAS-*` — brew calculation / offering screens
- `BN-Decaf`, `BN-HTB` — bedtime "how the brew hits" views (animated rings)
- `ECE` — External Caffeine Entry (logging caffeine consumed off-app)
- `CGO` — CaffevolveGo hub
- `P2-*`, `FR-*`, `GLOSSARY` — supporting screens

## Key global state

- **`userProfile`** — a `Proxy` over `profiles[currentProfileIdx]`. Reading/writing
  `userProfile.x` reads/writes the *currently selected* profile. Add profiles via
  `pushNewProfile(obj)`; multiple profiles + sub-profiles are supported.
- **`hopperConfig`** — `{ A: {...}, B: {...} }`, hopper A = caffeinated,
  hopper B = decaffeinated (bean family + roast).
- **`brewSession`**, **`sessionBedtime`** — per-session brew and bedtime state
  (`sessionBedtime.hasExpired()` drives the bedtime gate above).

## The caffeine model (important — get the math right)

Caffeine projections are pharmacokinetic, driven by tier:

- **`CAFFEVOLVE_CEILINGS`** — per-tier limits `{ tpc, bed, peakFloor }` for tiers
  `Lower` / `Moderate` / `Higher` (default `Moderate`).
- **`getCeilings()`** — resolves the active ceilings, honoring per-profile overrides
  (`_customTPC`, `_customBC`, `_instrWHC`, `_instrBed`, `_instrFloor`).
- **`getHalfLifeMins()`** — caffeine half-life in minutes; default hours are
  Lower 7.0 / Moderate 6.0 / Higher 5.0, overridable via `_instrT12`.

When changing anything that affects projections, verify against these helpers
rather than introducing new constants.

## Conventions for changes

- **Preserve the single-file, dependency-free nature.** No new external requests.
- **Reuse design tokens** and existing helper functions (`goto`, `getCeilings`,
  `getHalfLifeMins`, `pushNewProfile`, etc.) instead of duplicating logic.
- Match the surrounding vanilla-JS style (global functions, `document.getElementById`,
  inline styles built as strings). Don't introduce a framework or bundler.
- After edits, re-render the file to confirm it still loads and the affected flow
  works before committing.

## Verifying / viewing

There are no automated tests. To check work, open `Caffevolve/Caffevolve_UX_Prototype.web.50.html` in a
browser (or render it) and click through the affected screens using the screen
selector at the top of the page.
