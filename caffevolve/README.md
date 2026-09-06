# Caffevolve — Royalty Model & Brand Assets

Confidential / internal planning. Directional model, **not** a forecast.

## Files

- **`royalty-model-calculator.html`** — interactive royalty-model calculator (v4). Combines the v2 office
  stock-and-flow seeding engine (five levers) and the v3 café seeding engine (`N · c_cafe · r1`). The
  base case is the **seeded-only floor** (café + office seeding + commercial units); an optional,
  independent Direct / home-tier stream (units/yr + growth, net of an overlap haircut) is **off by
  default** and gated to start no earlier than the first licensee ship. Includes an OEM-anchored
  Low/Base/High ramp selector, N sensitivity, and the top-down ceiling check. Self-contained — open in
  any browser (fonts load from Google Fonts).
- **`royalty-model-onepager.html`** — Base-case investor one-pager (source). Built for print
  (`@page` US Letter); use the browser Print dialog to produce the PDF.
- **`royalty-model-onepager.pdf`** / **`.docx`** — rendered one-pager (US Letter). Figures are generated
  from the same model, so all four artifacts agree.
- **`logo-lockup.html`** — Caffevolve logo lockup (bean offset 30px right of center).

## Base case (v4) — headline figures

Direct off, mix 60 / 40, Base ramp (2 OEMs by Yr 5): **~$1.74M** cumulative 5-yr royalty, **~$1.1M**
Year-5 run-rate, commercial carrying **~79%** of royalty.

## Model inputs — status

- **Anchored:** the commercial units-placed ramp, OEM-signed — Low/Base/High = 1 / 2 / 4 OEMs by Year 5
  (totals `[6, 250, 1500, 4500, 9500]` at Base), split office/café by the office-share ramp
  `OFRAC = [0.5, 0.72, 0.667, 0.622, 0.579]`. Editable — replace with your live signings.
- **Assumed (pilot-measured):** the five office levers, the three café levers, and the Intro/Premier
  consumer mix (60 / 40).
- **Optional / off by default:** the Direct channel (`d₀, g, h`, start year) — least-anchored, not in
  the base case; upside only, gated on a DTC test and on first licensee ship.
- **Derived & cited:** the ceiling denominator is **~1.3M premium machines/yr (global)** = $1.12B
  super-automatic bean-to-cup (DataHorizzon, 2024) ÷ ~$850 blended consumer ASP. Order-of-magnitude
  guardrail; see the Sources & citations section in the calculator / one-pager.

## Market anchors (verified Sep 2026)

| Segment | Figure | Firm |
|---|---|---|
| Premium espresso + capsule (global) | $7.40B (2025), 5.08% CAGR | Fortune Business Insights |
| Super-automatic bean-to-cup (global) | $1.12B (2024), 7.2% CAGR | DataHorizzon Research |
| Connected / "smart" (global) | ~$0.4–6.8B range (not cleanly tracked) | Market.us / Fact.MR / Market Glass |

## Locked economics

Net wholesale ≈ 50% of MSRP ($1,250 / $300 / $100) · 5 / 7 / 8 royalty band at base 7% · attach folded
into placements (≈100% within the licensed lane).
