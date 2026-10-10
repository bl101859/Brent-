# Caffevolve Investor Brief: sources and verification

The two-page brief (`Caffevolve_Investor_Brief.pdf` / `.html`) merges:

- **Investor deck**: `Caffevolve_Investor_Deck_web.html` (project files)
- **Investor portal**: `index.html` (project files), chapters 4 (The Leap), 6 (Plan my Day), 8 (The Market), 9 (The Business), 10 (The Opportunity) and 11 (Version II)
- **Think · Act · Plan one-pagers**: `Think_Act_Plan_web.pdf`, `Think_Act_Plan_NDA_web.pdf` (branch `claude/funny-newton-ypkbci`)
- **Version II vision one-pager**: `Version-II/Caffevolve_Version_II_Vision_web.html` (branch `claude/gifted-goldberg-i5962c`)
- **Royalty model base case**: `caffevolve/royalty-model-onepager.html` (branch `claude/coffee-appliance-market-sizing-0oxdal`)

## Platform claims checked against the prototype

All line numbers refer to `caffevolve_prototype_web_current.html` on branch
`claude/gifted-goldberg-i5962c` (commit `e97830d`), the newest prototype in the repo.

| Claim in the brief | Where it is implemented |
|---|---|
| Caffeine Behavior Instrument turns everyday questions into personal ceilings and decay rate | `su8Compute()` L16454; questions e.g. L16283, L16310; results stored as `_instrWHC`, `_instrBed`, `_instrT12` L16602–16604 |
| Ceilings and decay rate are personal, tiered defaults otherwise | `CAFFEVOLVE_CEILINGS` L7620, `getCeilings()` L7625, `getHalfLifeMins()` L7636 |
| Dual-ceiling engine: strongest blend that clears both ceilings | `computeRecommendedBlend()` L10458; binding ceiling `Math.min(maxCafMgByTPC, maxCafMgByBed)` L10492 |
| Live 24-hour standing, personal decay, carry past midnight | `eceDecayedMg()` L12006; midnight carry-forward L11373; `halfLifeMinsForProfile()` L7650 |
| Bedtime is required before a brew calculation | bedtime gate in `goto()` L8947 |
| Two hoppers: caffeinated (A) and decaf (B) | `hopperConfig` L7678 |
| Beans blended, then ground; additives dispensed in-stream | device-flow comment L5213 (the hardware itself is covered by the provisional apparatus claims, not the prototype) |
| OAS: venue picker (worksite / coffee shop / convenience store), fitting drinks ranked first | `oasCompute()` L13117; venue tabs L7143; fit-first sort L14022–14023 |
| ECE logs drinks had away from the device | ECE screens around L6549; daily log `dailyLogAdd()` L11429 |
| Plan my Day projects the whole day against both ceilings | `pmdProject()` L20428 |
| Protect one drink; one tap suggests the smallest changes | `pmdToggleProtect()` L20801, `pmdComputeFix()` L21015, "Fix it for me" button L5496 |
| Saved plan resurfaces at brew time | `pmdReminderMatch()` L21209 (±90 min window) |
| Sub-Profiles: up to 6 on Advancara, 3 on other tiers, by day and time window | `MAX_SUB_PROFILES` L19193; `getActiveSubProfile()` L15911 |
| Manual override always honored | `brewSession.isManual` used in `computeRecommendedBlend()` L10504 |
| Office device brews against the same profile and logs to the same day | `officeBrew()` L13234; `setOfficeCaffevolve()` L13729 |
| Four device tiers | `DEVICE_TIER` / `CULMINARA_TIERS` L19190–19191 |

## Differences found between the materials and the prototype

- **Plan my Day rebalance.** The deck and portal describe "Star up to two drinks" and "Rebalance for me … no drink is removed." The prototype protects **one** drink (`pmdToggleProtect`, L20801), labels the button **"Fix it for me"**, and as a last resort can remove unprotected drinks (`pmdComputeFix` phase 2, L21041). The brief uses the prototype's behavior ("protect the one drink you won't give up … smallest changes").
- **Grind compensation.** The deck says the device adjusts grind automatically as the blend ratio shifts. Nothing in the prototype does this, so the brief leaves it out.
- **"64% of coffee drinkers give up their afternoon coffee"** (portal, Chapter 4) has no source in the materials, so the brief leaves it out.

## Business figures

- Market: Fortune Business Insights ($7.4B, 2025, ~5.1%/yr) and DataHorizzon Research ($1.1B, 2024, ~7.2%/yr), as cited in the portal and royalty one-pager.
- Royalty: Low / Base / High = $735K / $1.74M / $4.16M five-year total, seeded-only; commercial share 79% (royalty model v4 base case).
- Round: $250K as five $50K post-money SAFEs, $6M cap, MFN + pro rata; use of proceeds per portal Round Structure (deck's $15K engineering + $95K prototype = the portal's $110K hardware line).
