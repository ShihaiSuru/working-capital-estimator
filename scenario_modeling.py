#!/usr/bin/env python3
"""Scenario and sensitivity modeling for working capital."""

def scenario_analysis(base_dso, base_dio, base_dpo, daily_sales):
    scenarios = {
        "Optimistic": (base_dso - 10, base_dio - 5, base_dpo + 5),
        "Base": (base_dso, base_dio, base_dpo),
        "Pessimistic": (base_dso + 15, base_dio + 10, base_dpo - 5),
    }
    results = {}
    for name, (dso, dio, dpo) in scenarios.items():
        cycle = dso + dio - dpo
        wc = (cycle / 365) * (daily_sales * 365)
        results[name] = {"cash_cycle_days": cycle, "wc_need": round(wc)}
    return results

if __name__ == "__main__":
    print(scenario_analysis(45, 30, 20, 10000))
