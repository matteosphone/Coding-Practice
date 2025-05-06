# ======================================
# 📅 pandas DateTime Drill Set 
# ======================================
#%% 
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

# --------------------------------------
# Problem 9: Break timestamps into time components
# --------------------------------------
log_times = pd.Series(["2024-01-01 08:15:30", "2024-01-01 16:45:05"])
log_times = pd.to_datetime(log_times)

# Task:
# Get the hour, minute, and second for each timestamp
print(log_times.dt.hour)
print(log_times.dt.minute)
print(log_times.dt.second)

# --------------------------------------
# Problem 10: Derive calendar position for each date
# --------------------------------------
# Task:
# Get the day of the year and which quarter the date falls into
print(log_times.dt.dayofyear)
print(log_times.dt.quarter)

# --------------------------------------
# Problem 11: Separate calendar date and clock time
# --------------------------------------
# Task:
# From each datetime, extract the part that represents just the date,
# and the part that represents just the time

print(log_times.dt.date)
print(log_times.dt.time)

# --------------------------------------
# Problem 12: Translate dates into human-friendly names
# --------------------------------------
# Task:
# Return the full name of the month and the full name of the day of the week
print(log_times.dt.month_name())
print(log_times.dt.day_name())

# --------------------------------------
# Problem 13: Generate the current date and current date+time
# --------------------------------------
# Task:
# Print today's date (midnight) and also the full current time
print(pd.Timestamp.today())
print(pd.Timestamp.now())

# --------------------------------------
# Problem 14: Convert duration strings into time offsets
# --------------------------------------
durations = pd.Series(["2 days", "5 hours", "1 day 6 hours"])

# Task:
# Turn each duration string into a format you can add to a datetime
duration_offsets = pd.to_timedelta(durations)
print(duration_offsets)

# --------------------------------------
# Problem 15: Advance a project schedule by two days
# --------------------------------------
project_dates = pd.Series(["2024-06-01", "2024-06-05"])
project_dates = pd.to_datetime(project_dates)

# Task:
# Add 2 full calendar days to each of these dates
print(project_dates + pd.to_timedelta("2 days"))

# --------------------------------------
# Problem 16: Measure durations in total seconds
# --------------------------------------
start = pd.to_datetime(["2024-01-01 08:00:00", "2024-01-02 10:00:00"])
end = pd.to_datetime(["2024-01-01 09:30:00", "2024-01-02 13:15:00"])

# Task:
# Get the full time difference between start and end, measured in seconds
total_seconds = (start - end).total_seconds()
print(total_seconds)

# --------------------------------------
# Problem 17: Find rows from February using the row labels
# --------------------------------------
df = pd.DataFrame({
    "sales": [100, 200, 150, 300],
    "date": pd.to_datetime(["2024-01-01", "2024-02-15", "2024-02-25", "2024-03-05"])
})
df = df.set_index("date")

# Task:
# Return only the rows where the date is in February
df_feb = df[df.index.month == 2]
print(df_feb)
# %%
