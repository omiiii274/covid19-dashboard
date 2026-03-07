
# 🦠 COVID-19 Data Analysis & Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

## 📋 About This Project

This project analyses real-world COVID-19 data from the Johns Hopkins University COVID-19 Data Repository — the most widely cited source of pandemic data globally. The analysis tracks cumulative cases, deaths, case fatality rates (CFR), and daily infection trends across 5 major countries, with detailed analysis of UK daily case patterns.

Working with real-world public health data requires handling messy data, computing epidemiological metrics, and creating visualisations that make complex trends accessible to non-technical audiences. These are core skills for any data scientist working in healthcare.

## ❓ What Questions Does This Answer

1. **How did the pandemic progress differently across countries?** — Cumulative case and death curves show timing and scale differences
2. **Which countries had the highest fatality rates?** — CFR comparison reveals differences in testing, healthcare capacity, and demographics
3. **What did the UK's infection waves look like?** — Daily case analysis with rolling averages reveals wave patterns tied to variant emergence
4. **How can raw case data be misleading?** — Weekend reporting dips create artificial patterns that rolling averages smooth out

## 🔬 How It Works

**Data Source**: Johns Hopkins University CSSE COVID-19 Dataset — contains daily cumulative confirmed cases, deaths, and recoveries for 190+ countries from January 2020 onwards.

**Analysis Steps**:
1. Loaded and cleaned the dataset (handling missing values, date parsing)
2. Filtered data for 5 countries: UK, US, India, Germany, Brazil
3. Plotted cumulative confirmed cases and deaths over time
4. Computed Case Fatality Rate (CFR = Deaths / Confirmed Cases × 100) for the top 15 countries by total cases
5. Calculated daily new cases for the UK by differencing cumulative totals
6. Applied 7-day rolling average to smooth weekend reporting artefacts

## 📊 Key Findings

| Country | Total Cases | Total Deaths | CFR |
|---------|-------------|-------------|-----|
| United States | Highest absolute count | Highest absolute count | ~1.1% |
| India | Second highest | — | ~1.2% |
| Brazil | — | — | ~1.9% |
| United Kingdom | — | — | ~1.4% |
| Germany | — | — | ~1.2% |

Key observations:
- **US** accumulated the highest absolute case count due to population size and testing capacity
- **CFR varies significantly** (0.5% to 3.5%) between countries, reflecting testing rates, healthcare quality, and age demographics
- **UK daily cases** show clear wave structure corresponding to Alpha (early 2021), Delta (mid 2021), and Omicron (late 2021/early 2022) variants
- **7-day rolling average** eliminates weekend reporting dips that create misleading spikes and troughs

## 🛠️ Tools Used

| What | Tool |
|------|------|
| Data source | Johns Hopkins University CSSE COVID-19 Data |
| Programming | Python 3.9 |
| Data handling | Pandas, NumPy |
| Plotting | Matplotlib |
| Date handling | matplotlib.dates |

## 📁 Files In This Project
