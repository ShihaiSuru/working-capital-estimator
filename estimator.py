#!/usr/bin/env python3
"""Working capital requirement estimator."""

def estimate_wc(receivables_days, inventory_days, payables_days, daily_sales):
    operating_cycle = receivables_days + inventory_days
    cash_cycle = operating_cycle - payables_days
    wc_need = (cash_cycle / 365) * (daily_sales * 365)
    return round(wc_need)

if __name__ == "__main__":
    need = estimate_wc(45, 30, 20, 10000)
    print(f"Estimated working capital need: ₹{need:,}")
