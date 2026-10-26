#------------------------------------------------------------------------------------------------------
# Working with Dates
#------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------
#Date and time types in Pandas
#------------------------------------------------------------------------------------------------------

#str / object | Text that may contain a date | "2026-10-15"

#datetime64[ns] | Date and time, typically with nanosecond precision | 2026-10-15 14:30:00

#datetime64[ns, UTC] | Date and time with a UTC timezone | 2026-10-15 18:30:00+00:00

#date | Python date without a time | date(2026, 10, 15)

#timedelta64[ns] | A duration or difference between dates | 5 days

#Period | A time interval, such as a month or quarter | 2026-10


#create example DataFrame
import pandas as pd

df = pd.DataFrame({
    "employee_id": [101, 102, 103],
    "hire_date": [
        "2022-03-15",
        "2024-07-01",
        "2026-01-20"
    ],
    "last_review": [
        "2025-03-15",
        "2025-07-01",
        None
    ]
})

print(df.dtypes)

#------------------------------------------------------------------------------------------------------
#Convert strings into dates
#------------------------------------------------------------------------------------------------------

df["hire_date"] = pd.to_datetime(df["hire_date"])
df["last_review"] = pd.to_datetime(df["last_review"])

print(df.dtypes)

#With format argument 

df["hire_date"] = pd.to_datetime(
    df["hire_date"],
    format="%Y-%m-%d"
)

# %Y	Four-digit year	2026
# %y	Two-digit year	26
# %m	Month, zero-padded	10
# %d	Day, zero-padded	15
# %H	Hour, 24-hour clock	14
# %I	Hour, 12-hour clock	02
# %M	Minute	30
# %S	Second	45
# %f	Fractional seconds	123456
# %p	AM or PM	PM
# %b	Abbreviated month name	Oct
# %B	Full month name	October


#Examples of format conversions 

# 10/15/2026
pd.to_datetime("10/15/2026", format="%m/%d/%Y")

# 15-10-2026
pd.to_datetime("15-10-2026", format="%d-%m-%Y")

# October 15, 2026
pd.to_datetime("October 15, 2026", format="%B %d, %Y")

# 2026-10-15 14:30:00
pd.to_datetime(
    "2026-10-15 14:30:00",
    format="%Y-%m-%d %H:%M:%S"
)

#------------------------------------------------------------------------------------------------------
#Handling Invalid Dates
#------------------------------------------------------------------------------------------------------

#Handling invalid dates

df = pd.DataFrame({
    "event_date": [
        "2026-10-01",
        "2026-10-15",
        "not available",
        "2026-02-30",
        None
    ]
})

df["event_date"] = pd.to_datetime(
    df["event_date"],
    format="%Y-%m-%d",
    errors="coerce" #conversts to NaT instead of stopping execution 
)




#------------------------------------------------------------------------------------------------------
#Example: Creating Invalid Date Log
#------------------------------------------------------------------------------------------------------

import logging
import pandas as pd

# Configure logging to append to the file
logging.basicConfig(
    filename="etl_errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Preserve original values
raw_dates = df["event_date"].copy()

# Parse dates
df["event_date"] = pd.to_datetime(
    raw_dates,
    format="%Y-%m-%d",
    errors="coerce"
)

# Identify invalid dates (excluding originally missing values)
invalid_dates = raw_dates.notna() & df["event_date"].isna()

# Log errors
if invalid_dates.any():
    logging.error(
        "Invalid date count: %s",
        invalid_dates.sum()
    )

    logging.error(
        "Invalid date records:\n%s",
        df.loc[invalid_dates].to_string()
    )
