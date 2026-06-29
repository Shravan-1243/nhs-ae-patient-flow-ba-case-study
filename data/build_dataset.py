"""
Builds a 12-month A&E performance dataset for a single representative
NHS acute trust ("Thameswood NHS Foundation Trust" - illustrative, not real).

Method: national-level monthly 4-hour breach rates and attendance volumes
are anchored to NHS England's own published statistics (see data_dictionary.md
for sources). Trust-level figures are modelled around the national average
with realistic seasonal variation (winter pressure, etc.), scaled to a
mid-sized Type 1 A&E department (~ 220 attendances/day average).

This mirrors how a contract BA would receive trust-level extracts in a real
engagement - the analytical approach and BA documentation are the deliverable,
not a claim that this exact file is an official NHS publication.
"""
import pandas as pd
import numpy as np

np.random.seed(42)

months = pd.date_range("2025-04-01", "2026-03-01", freq="MS")
month_labels = [m.strftime("%b-%Y") for m in months]

# National 4-hr breach rate trend (% over 4 hrs), anchored to published figures:
# Apr25 ~28%, gradually worsening through winter, Mar26 = 36.2% (official, cited)
national_breach_pct = [28.1, 29.4, 27.8, 26.9, 28.3, 31.2, 35.8, 38.4, 37.1, 34.6, 33.9, 36.2]

# Trust runs ~3-4pp worse than national average in winter months (typical for
# mid-sized Type 1 acute trusts per Nuffield Trust / NHS Confed commentary)
trust_adjustment = [3.5, 3.1, 2.8, 2.4, 2.9, 3.8, 5.1, 5.9, 5.2, 4.4, 4.0, 4.6]
trust_breach_pct = [round(n + a, 1) for n, a in zip(national_breach_pct, trust_adjustment)]

# Attendance volumes - seasonal, winter peak, mild upward YoY trend (record
# national attendances reported May 2026)
base_daily_attendances = 215
seasonal_factor = [1.00, 0.97, 0.95, 0.93, 0.96, 1.04, 1.12, 1.18, 1.10, 1.05, 1.02, 1.09]
days_in_month = [30, 31, 30, 31, 31, 30, 31, 31, 28, 31, 30, 31]

rows = []
for i, m in enumerate(months):
    daily_avg = base_daily_attendances * seasonal_factor[i]
    total_attendances = round(daily_avg * days_in_month[i])
    breach_pct = trust_breach_pct[i]
    seen_within_4h = round(total_attendances * (1 - breach_pct / 100))
    breached_4h = total_attendances - seen_within_4h

    # 12-hour trolley waits (post decision-to-admit) - small % of breaches,
    # rising trend consistent with national reporting
    twelve_hr_pct_of_breaches = [0.04, 0.04, 0.035, 0.03, 0.035, 0.045, 0.06, 0.07,
                                   0.065, 0.05, 0.045, 0.055][i]
    twelve_hr_waits = round(breached_4h * twelve_hr_pct_of_breaches)

    # Emergency admissions - roughly 22-26% of attendances, higher in winter
    admission_rate = [0.222, 0.218, 0.215, 0.21, 0.217, 0.231, 0.248, 0.256,
                       0.245, 0.234, 0.228, 0.241][i]
    emergency_admissions = round(total_attendances * admission_rate)

    # Staffing - nursing vacancy rate (%), modelled around published 6.7% NHS
    # average (Dec 2025) with mild winter dip due to sickness/agency reliance
    nursing_vacancy_pct = [6.9, 6.8, 6.6, 6.5, 6.7, 7.1, 7.8, 8.2, 7.9, 7.4, 7.0, 7.3][i]

    rows.append({
        "month": month_labels[i],
        "month_start": m.strftime("%Y-%m-%d"),
        "total_attendances": total_attendances,
        "seen_within_4hrs": seen_within_4h,
        "breached_4hr_target": breached_4h,
        "four_hr_breach_pct": breach_pct,
        "twelve_hr_trolley_waits": twelve_hr_waits,
        "emergency_admissions": emergency_admissions,
        "admission_rate_pct": round(admission_rate * 100, 1),
        "nursing_vacancy_pct": nursing_vacancy_pct,
    })

df = pd.DataFrame(rows)
df.to_csv("trust_ae_performance_apr25_mar26.csv", index=False)
print(df.to_string(index=False))
print("\nSaved trust_ae_performance_apr25_mar26.csv")
