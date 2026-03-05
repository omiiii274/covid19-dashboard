
---

### PROJECT 5: `covid19-dashboard`

**File: `main.py`**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os, warnings
warnings.filterwarnings('ignore')
os.makedirs('images', exist_ok=True)

print("🦠 Loading COVID-19 data...")
url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv"
df = pd.read_csv(url, parse_dates=['Date'])
print(f"✅ Loaded {len(df)} records | Countries: {df['Country'].nunique()}")

countries = ['United Kingdom', 'United States', 'India', 'Germany', 'Brazil']
df_top = df[df['Country'].isin(countries)].copy()

# ── Plot 1: Confirmed Cases Over Time ──
fig, ax = plt.subplots(figsize=(12, 6))
for country in countries:
    subset = df_top[df_top['Country'] == country]
    ax.plot(subset['Date'], subset['Confirmed'], label=country, lw=2)
ax.set_title('COVID-19 Confirmed Cases Over Time', fontsize=14)
ax.set_ylabel('Confirmed Cases'); ax.legend()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig('images/confirmed_cases.png', dpi=150)
print("✅ Saved: images/confirmed_cases.png")

# ── Plot 2: Deaths Over Time ──
fig, ax = plt.subplots(figsize=(12, 6))
for country in countries:
    subset = df_top[df_top['Country'] == country]
    ax.plot(subset['Date'], subset['Deaths'], label=country, lw=2)
ax.set_title('COVID-19 Deaths Over Time', fontsize=14)
ax.set_ylabel('Deaths'); ax.legend()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig('images/deaths_over_time.png', dpi=150)
print("✅ Saved: images/deaths_over_time.png")

# ── Plot 3: Case Fatality Rate ──
latest = df.groupby('Country').last().reset_index()
latest['CFR'] = (latest['Deaths'] / latest['Confirmed'] * 100).round(2)
top_cfr = latest.nlargest(15, 'Confirmed').sort_values('CFR')

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_cfr['Country'], top_cfr['CFR'], color='#E74C3C')
ax.set_xlabel('Case Fatality Rate (%)'); ax.set_title('CFR — Top 15 Countries by Cases')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout(); plt.savefig('images/case_fatality_rate.png', dpi=150)
print("✅ Saved: images/case_fatality_rate.png")

# ── Plot 4: Daily New Cases (UK) ──
uk = df[df['Country'] == 'United Kingdom'].copy()
uk['Daily_New'] = uk['Confirmed'].diff().clip(lower=0)
uk['Rolling_7'] = uk['Daily_New'].rolling(7).mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(uk['Date'], uk['Daily_New'], alpha=0.3, color='#3498DB', label='Daily Cases')
ax.plot(uk['Date'], uk['Rolling_7'], color='#E74C3C', lw=2, label='7-Day Rolling Average')
ax.set_title('UK Daily New COVID-19 Cases', fontsize=14)
ax.set_ylabel('New Cases'); ax.legend()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45); ax.grid(alpha=0.3)
plt.tight_layout(); plt.savefig('images/uk_daily_cases.png', dpi=150)
print("✅ Saved: images/uk_daily_cases.png")

print("\n🏁 Done! All plots in /images/")
