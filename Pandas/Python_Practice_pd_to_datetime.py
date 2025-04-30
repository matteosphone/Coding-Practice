# ======================================
# 📅 pandas DateTime Drill Set 
# ======================================

import pandas as pd

# --------------------------------------
# Problem 1: Convert raw strings to datetime
# --------------------------------------
timestamps = pd.Series(["2023-07-01", "2023-07-15", "2023-08-03"])

# Convert them into proper datetime objects
dt_timestamps = pd.to_datetime(timestamps)

# --------------------------------------
# Problem 2: Extract month number (1–12)
# --------------------------------------
months = dt_timestamps.dt.month
print("Months:", months)

# --------------------------------------
# Problem 3: Get weekday name for each date
# --------------------------------------
day_names = dt_timestamps.dt.day_name()
print("Weekday Names:", day_names)

# --------------------------------------
# Problem 4: Filter dates that occur in July
# --------------------------------------
july_dates = dt_timestamps[dt_timestamps.dt.month == 7]
print("Dates in July:", july_dates)

# --------------------------------------
# Problem 5: Days between signup and last active
# --------------------------------------
signup = pd.Series(["2024-01-01", "2024-02-15", "2024-03-01"])
last_active = pd.Series(["2024-01-10", "2024-02-25", "2024-03-20"])

signup_dt = pd.to_datetime(signup)
last_active_dt = pd.to_datetime(last_active)

days_passed = last_active_dt - signup_dt
print("Days Passed:", days_passed)

# --------------------------------------
# Problem 6: Total seconds between signup and last active
# --------------------------------------
seconds_passed = days_passed.dt.total_seconds()
print("Seconds Passed:", seconds_passed)

# --------------------------------------
# Problem 7: Identify start and end of month
# --------------------------------------
events = pd.Series(["2024-01-01", "2024-01-15", "2024-01-31"])
events = pd.to_datetime(events)

first_of_month = events.dt.is_month_start
last_of_month = events.dt.is_month_end

print("Is First of Month:", first_of_month)
print("Is Last of Month:", last_of_month)

# --------------------------------------
# Problem 8: Shift each transaction forward by 2 weeks
# --------------------------------------
tx_dates = pd.Series(["2024-05-01", "2024-05-03", "2024-05-05"])
tx_dates = pd.to_datetime(tx_dates)

tx_dates_2wks = tx_dates + pd.Timedelta(weeks=2)
print("Shifted Transactions:", tx_dates_2wks)
