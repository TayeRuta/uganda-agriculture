"""
Build the "farm year" calendar for index.html from the five projects' published tables, and inject it.

Every input is a small table already committed to one of the project repositories, fetched from GitHub,
so the page can be rebuilt without re-running any of the analyses.

Usage (from anywhere):
    python scripts/build_synthesis_data.py
"""
import io
import json
import re
import urllib.request
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / 'index.html'
RAW = 'https://raw.githubusercontent.com/TayeRuta/{repo}/main/{path}'
MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def csv(repo, path, **kw):
    req = urllib.request.Request(RAW.format(repo=repo, path=path), headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return pd.read_csv(io.BytesIO(r.read()), **kw)


def region(clim, name):
    """Climatology row for a region; the published file labels them e.g. 'Central Region region'."""
    match = [r for r in clim.index if r.startswith(name)]
    if len(match) != 1:
        raise SystemExit(f'expected one region starting {name!r}, found {match}')
    return clim.loc[match[0]]


def main():
    rain = csv('uganda-rainfall-analysis', 'data/raw/uganda_rainfall_by_region_1990_2025.csv')
    rain = rain[rain['year'].between(1991, 2020)]
    clim = rain.groupby(['region', 'month'])['rainfall_mm'].mean().unstack()

    prices = csv('uganda-food-prices', 'data/processed/seasonal_price_profiles.csv')
    prices.columns = ['commodity', 'market'] + list(prices.columns[2:])
    maize = prices[prices['commodity'] == 'Maize (white)'][MON].median()

    trade = csv('uganda-food-trade', 'data/processed/export_seasonality.csv', index_col=0)
    coffee = csv('uganda-coffee', 'data/processed/export_calendar.csv', index_col=0)

    rows = [
        {'key': 'rain_c', 'label': 'Rain, Central (two seasons)', 'unit': 'mm', 'kind': 'rain', 'v': region(clim, 'Central').tolist(),
         'src': 'Rainfall analysis', 'url': 'https://tayeruta.github.io/uganda-rainfall-analysis/reports/regional_report.html'},
        {'key': 'rain_n', 'label': 'Rain, Northern (one long season)', 'unit': 'mm', 'kind': 'rain', 'v': region(clim, 'Northern').tolist(),
         'src': 'Rainfall analysis', 'url': 'https://tayeruta.github.io/uganda-rainfall-analysis/reports/regional_report.html'},
        {'key': 'maize_price', 'label': 'Maize price vs yearly average', 'unit': '%', 'kind': 'price', 'v': maize.tolist(),
         'src': 'Food prices', 'url': 'https://tayeruta.github.io/uganda-food-prices/reports/food_prices_report.html'},
        {'key': 'maize_kenya', 'label': 'Maize to Kenya, share of year', 'unit': '%', 'kind': 'flow', 'v': trade['Kenya (maize)'].tolist(),
         'src': 'Food trade', 'url': 'https://tayeruta.github.io/uganda-food-trade/reports/trade_report.html'},
        {'key': 'robusta', 'label': 'Robusta coffee exports, share of year', 'unit': '%', 'kind': 'flow', 'v': coffee['robusta'].tolist(),
         'src': 'Coffee', 'url': 'https://tayeruta.github.io/uganda-coffee/reports/coffee_report.html'},
        {'key': 'arabica', 'label': 'Arabica coffee exports, share of year', 'unit': '%', 'kind': 'flow', 'v': coffee['arabica'].tolist(),
         'src': 'Coffee', 'url': 'https://tayeruta.github.io/uganda-coffee/reports/coffee_report.html'},
    ]
    for r in rows:
        r['v'] = [round(float(x), 2) for x in r['v']]
    data = {'months': MON, 'rows': rows}
    payload = json.dumps(data, separators=(',', ':'), allow_nan=False).replace('</', '<\\/')
    s = PAGE.read_text()
    s, n = re.subn(r'(<script id="report-data" type="application/json">)(.*?)(</script>)',
                   lambda m: m.group(1) + payload + m.group(3), s, flags=re.S)
    if n != 1:
        raise SystemExit(f'expected one report-data block, found {n}')
    PAGE.write_text(s)
    print('updated index.html')
    for r in rows:
        print(f"{r['label']:40s}", ' '.join(f'{x:6.1f}' for x in r['v']))


if __name__ == '__main__':
    main()
