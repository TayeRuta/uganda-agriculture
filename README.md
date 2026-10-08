# Uganda Agriculture: What Five Analyses Show

A synthesis of five public-data analyses of Uganda's agriculture: rainfall, food prices, coffee, irrigation and regional food trade. Together they trace one chain, from rain to harvest to price to trade, and show where the country's agricultural data falls short.

**Read the synthesis: [Uganda's farming runs on rain](https://tayeruta.github.io/uganda-agriculture/)**

## What holds across all five

- **The second rains are the swing season, and the forecastable one.** October–December rainfall varies more than March–May, follows the Indian Ocean Dipole, and can be anticipated from July–August. The second harvest also feeds the December–February maize export peak.
- **Rain reaches prices through the harvest.** A dry first season raises maize prices about 9–11% in September–December.
- **The seasonal price cycle dwarfs weather shocks.** Maize swings about 30% a year between harvest and lean season; storing grain earns about 25–30% in real terms on average.
- **Uganda's maize market is regional.** Prices move almost in step with Kenya's and Rwanda's, and gaps halve within two months; border shocks disrupted flows but did not depress Ugandan prices.
- **Karamoja is the outlier on every measure:** the driest and most volatile rainfall, the highest dry-spell risk, the biggest seasonal price swings, and water that is hardest to reach.
- **Coffee farmers are tied to the world market:** two-thirds of a world price change reaches robusta farmers within the month, and they now get 70–80% of the world robusta price.
- **The weakest link is the data:** official crop statistics cannot detect droughts, trade records disagree by orders of magnitude, and coffee export figures differ by 22–25% between sources.

## The projects

| Project | Report | Code and data |
|---|---|---|
| Rainfall: national, regional and Indian Ocean Dipole analysis, 1990–2025 | [Synthesis report](https://tayeruta.github.io/uganda-rainfall-analysis/reports/synthesis_report.html) | [uganda-rainfall-analysis](https://github.com/TayeRuta/uganda-rainfall-analysis) |
| Food prices: rainfall shocks, the Indian Ocean and crop greenness against market prices | [Report](https://tayeruta.github.io/uganda-food-prices/reports/food_prices_report.html) | [uganda-food-prices](https://github.com/TayeRuta/uganda-food-prices) |
| Coffee: exports, pass-through to farmers, climate exposure and a global benchmark | [Report](https://tayeruta.github.io/uganda-coffee/reports/coffee_report.html) · [Benchmark](https://tayeruta.github.io/uganda-coffee/reports/benchmark_report.html) | [uganda-coffee](https://github.com/TayeRuta/uganda-coffee) |
| Irrigation: need and water access across 135 districts | [Report](https://tayeruta.github.io/uganda-irrigation/reports/irrigation_report.html) | [uganda-irrigation](https://github.com/TayeRuta/uganda-irrigation) |
| Food trade: staple trade with six neighbours, source gaps and price links | [Report](https://tayeruta.github.io/uganda-food-trade/reports/trade_report.html) | [uganda-food-trade](https://github.com/TayeRuta/uganda-food-trade) |

## Other sectors

- [Uganda tourism](https://github.com/TayeRuta/uganda-tourism): who comes, when, and what goes unsold ([report](https://tayeruta.github.io/uganda-tourism/reports/tourism_report.html))
- [Uganda hospitality](https://github.com/TayeRuta/uganda-hospitality): how full hotels are, how big the sector is, where the graded hotels are, and how reliable the statistics are ([report](https://tayeruta.github.io/uganda-hospitality/reports/hospitality_report.html))

## Rebuilding the page

The "farm year" calendar on the page is built from small tables published in the five project repositories:

```bash
pip install pandas numpy
python scripts/build_synthesis_data.py
```

## License

Code is released under the MIT License. Data remain under the terms of their original providers.
