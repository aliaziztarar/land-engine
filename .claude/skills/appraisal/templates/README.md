# Appraisal templates

## BuildUp's Master Basic Appraisal workbook
Each BuildUp member has their own copy; the setup skill records where it is (`profile/profile.json`, `buildup_workbook`). For a new site: copy it to the site's folder as `<TITLE> - appraisal.xlsx`, clear the previous site's inputs, keep every formula.

Tabs: Base Financial Appraisal (the appraisal), GDV Variance (a sales price stress, costs linked to Base), Comparables (house types, sizes, values; feeds Base), Cashflow, Drawdown Calculations, S Curve, Fact Find (site facts and the stamp duty rate), and two back end tabs.

Typed cells on the Base tab (everything else is a formula):
- C3 site address; C4 planning link.
- On the Comparables tab: house types, floor areas (square feet), unit values and counts; these flow into Base rows 8 and 9 (affordable) and 13 to 16 (open market). Affordable values are the registered provider's price.
- G22 planning cost provisional percentage of GDV (or itemised planning costs in the rows below); J23 application fee.
- J38 S106 per home (put the evidence in the note column Q); rows 39 to 49 further contributions (CIL, nutrient credits, education, Building Safety Levy), each with its note.
- J51 utilities per home; J54 and J55 (affordable) and J58 to J61 (open market) build rate per square foot from the costing calculator.
- J63 contingency percentage; G65 to G68 fee percentages; G69 to G73 fixed fees; J76 estate agency percentage; G80 legal fee per home.
- C82 Site Value: the landowner's price only, never the residual. E83 introduction fee percentage; E85 legal percentage; stamp duty from Fact Find.
- C93 Target Profit on Sale: the programme's target (26 percent for BuildUp from 17 November 2026). C94 then shows the residual land value with planning: GDV times one minus the target, less all costs except land and planning.
Add these rows below the sheet so the user's own margin shows without manual sums: sale price to a housebuilder (C94); less price to the landowner (C82); less planning costs (O21); less buying costs (L83 to L85); less overage to a third party (typed); joint margin; margin as a percentage; and a check of the housebuilder's profit if it pays that sale price (should equal the target). Planning costs come out before any joint venture split; confirm the order with the programme each time.

## BuildUp's costing calculator
Each member has their own copy (`profile/profile.json`, `buildup_calculator`). Calculator tab, dropdowns only:
1. Area: Broad Area, County, Location (the district as the cost data names it). A warning appears if the three do not match or there is no data for the location.
2. Build type: New build; Estate housing (or flats); 2-storey for ordinary houses.
3. General: Specification Medium; Date start, the quarter building would begin.
4. Results: Result A per square metre, Result B per square foot. Type Result B into the build rate cells.
How the figure is built: the Prices Data tab holds cost data by location with lower quartile, mean and upper quartile at a base quarter; Medium takes the mean; the start quarter multiplies it by the cost index movement from the base quarter (the factor); Result B is Result A divided by 10.7639. When the programme issues a newer calculator, replace the file and update the profile.

## appraisal-template.md
A plain layout for a first desk run, or for a user without a programme workbook.
