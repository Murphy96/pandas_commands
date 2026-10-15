#Cleaning and Enriching Data


import pandas as pd

data = {
    "common_name": ['goldenrod', 'lupine','foxglove', 'yarrow'], 
    "height_inches": [48, 18, 48, 30 ],
    "sowing_season": ['fall', 'fall', 'fall', 'fall' ], 
    "light": ['full sun', 'full sun, partial shade', 'full sun, partial shade', 'full sun' ]
}

df=pd.DataFrame(data)

#============================================================================================
#Replacing Missing Values
#============================================================================================

#Basic syntax fillna()

df['common_name'] = df['common_name'].fillna('Unknown')

#Can use strings, numerica values etc


#Replace Nulls with Mean of column 

df['height_inches'] = df['height_inches'].fillna(df['height_inches'].mean()) #mean ignores missing values by default

#Replace Nulls with the Median 

df['height_inches'] = df['height_inches'].fillna(df['height_inches'].median())


#=============================================================================================
#Finding Missing Values
#=============================================================================================

#Finds missing values, returns a Boolean DataFrame where True means a missing value
df.isna()
df.isnull() #effectively interchangeable

#Count missing values by column 
df.isna().sum()

#Find rows containing missing values 
df[df.isna().any(axis=1)]

#Find rows where a particular column is missing 
df[df["common_name"].isna()]

#Find row where a value is not missing 
df[df['common_name'].notna()]

#============================================================================================
#Removing Missing Values
#============================================================================================

#Remove rows containing missing values 
df = df.dropna()

#Only remove rows where a particular column is null 
df = df.dropna(subset=['common_name']) #Remove row if common_name is null

#Remove columns containing nulls 
df = df.dropna(axis=1) #axis=0 is rows, axis=1 is columns 



#============================================================================================
#Replacing Specific Values
#============================================================================================

#Replace a specific value 

df['common_name'] = df['common_name'].replace(
    'yarrow', 
    'sneezewort'
)

#Replace multiple values 

df['common_name'] = df['common_name'].replace({
    'yarrow':'sneezewort', 
    'goldenrod': 'zig-zag goldenrod', 
    'lupine': 'wild lupine'
})

#Replace empty strings 
df['common_name'] = df['common_name'].replace('', pd.NA)

#Replace common nulls 

df = df.replace({
    'unknown': pd.NA,
    'Unknown': pd.NA,
    'N/A': pd.NA,
    'n/a': pd.NA,
    'NULL': pd.NA,
    'null': pd.NA,
    '': pd.NA
})

#Can do this directly during ingestion 
df = pd.read_csv(
    "data.csv",
    na_values = ["", "NULL", "N/A", "NA", "null"]
)

#============================================================================================
#Handling Duplicates 
#============================================================================================

#Returns a Boolean Series where True means row is a duplicate of an earlier row
df.duplicated()

#Count duplicates
df.duplicated().sum()

#Return duplicate rows
df[df.duplicated()]

#Find duplicates in a specific column 
df[df.duplicated(subset = ['common_name'])]

#Find duplicates in multiple columns, will look at the combination for duplicate combos 
df[df.duplicated(
    subset = ['common_name', 'sowing_season']
)]

#See all duplicates, both copies(by default, duplicated() keeps the first occurrence)
df[df.duplicated(
   subset = ['common_name'], 
   keep = False
    )]

#Remove duplicates 
df = df.dropduplicates()

#Remove duplicates based on a column 
df = df.drop_duplicates(
    subset=['common_name']
)

#Keep the first record 
df = df.drop_duplicates(
    subset = ['common_name'],
    keep = 'first'
)

#Keep the last record 
df = df.drop_duplicates(
    subset = ['common_name'], 
    keep = 'last'
)

#Remove every record involved in a duplicate 
df = df.drop_duplicates(
    subset = ['common_name'], 
    keep = False
)

#============================================================================================
#Working with Strings
#============================================================================================

#Strip whitespace
df['common_name'] = df['common_name'].str.strip()

#Change case 
df['common_name'] = df['common_name'].str.lower() #all lowercase
df['common_name'] = df['common_name'].str.upper() #all uppercase
df['common_name'] = df['common_name'].str.title() #Title case, PROPER in SQL

#============================================================================================
#Converting Data Types
#============================================================================================

df['height_inches'] = df['height_inches'].astype(int) #casts column as integer 
df['common_name'] = df['common_name'].astype(str) #casts column as string
df['height_inches'] = df['height_inches'].astype(float) #casts column as float

# pd.to_numeric() converts columns to numeric 

df['height_inches'] = pd.to_numeric(
    df['height_inches'], 
    errors = 'coerce' #values that cannot be converted become NaN
)

#Convert dates
df['plant_date'] = pd.to_datetime(
    df['plant_date']
)

#Convert dats & specify the source format
df["plant_date"] = pd.to_datetime(
    df["plant_date"],
    format = "%m/%d/%Y"
)

# with invalid values
df['plant_date'] = pd.to_datetime(
    df['plant_date'], 
    errors = 'coerce' #invalid dates become NaT
)

#============================================================================================
#Working with Dates
#============================================================================================
#Specify date format 
#.strftime() converts datetime into a string 
df["plant_date"] = df["plant_date"].dt.strftime("%m/%d/%Y")

#Extracting date components
df['plant_date'] = df['plant_date'].dt.year 
df['plant_date'] = df['plant_date'].dt.month
df['plant_date'] = df['plant_date'].dt.day
df['plant_date'] = df['plant_date'].dt.day_name()


#============================================================================================
#Working with Columns 
#============================================================================================

#Renaming columns 
df = df.rename(columns = {
    'common_name': 'CommonName', 
    'sowing_season': 'SowingSeason'
})

#============================================================================================
#Creating Calculated Columns 
#============================================================================================

#Let's say we need to add 10% to height due to a new fertilizer

df['height_inches']
df['fertilizer_boost'] = df['height_inches'] * 0.10

df['fertilized_height'] = (
    df['height_inches'] + df['fertilizer_boost']
)

#Conditional caluclated Columns 

df['plant_stature'] = df['height_inches'].apply(
    lambda x: 'Tall' if x > 35
    else 'Medium' if x > 20
    else 'Ground Cover'
)

#============================================================================================
#Using NumPy to Create Calculated Columns 
#============================================================================================
#Can also use numpy, np.where()
#np.where(condition, value_if_true, value_if_false)

import numpy as np

df['plant_stature'] = np.where(
    df['height_inches'] > 35, 
    'Tall', 
    'Standard'
)

#Can combine Boolean conditions 
df["classification"] = np.where(
    (df["height_inches"] > 20) &
    (df["sowing_season"] == "fall"),
    "Fall Tall",
    "Other"
)

#Multiple conditions with np.select()
#np.select(
#   conditions,
#    choices,
#    default=value
#)
conditions = [
    df["height_inches"] >= 35, #Checked first
    df["height_inches"] >= 20, #Checked second
]

choices = [
    "Tall",
    "Medium",
]

df["plant_stature"] = np.select(
    conditions,
    choices,
    default="Ground Cover"
)

#Multiple compound conditions with np.select()

conditions = [
    (df["height_inches"] > 35) &
    (df["sowing_season"] == "fall"),

    (df["height_inches"] > 35) &
    (df["sowing_season"] == "spring"),

    df["height_inches"] > 20
]

choices = [
    "Fall Tall",
    "Spring Tall",
    "Medium"
]

df["plant_category"] = np.select(
    conditions,
    choices,
    default="Ground Cover"
)

#============================================================================================
#Using Assign to Create Multiple Calculated Columns 
#============================================================================================
#Assign returns a DataFrame, doesn't modify the existing DataFrame
df = df.assign(
    fertilizer_boost=df["height_inches"] * 0.10,
    fertilized_height=df["height_inches"] * 1.10
)


#============================================================================================
#Applied Example: Creating Surrogate Keys
#============================================================================================

#Creating a simple key based on index, will not check if information is added 
df["employee_key"] = df.index + 1

#Possible to generate this on the warehouse side using SQL

CREATE TABLE dim_employee
(
    employee_key INT IDENTITY(1,1) PRIMARY KEY,
    employee_id INT,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);


#ETL creating a temp row identifier  using range()
#range(start, stop, step ) default start = 0, default step = 1, stop is exclusive
#Output is a range object 

df["etl_row_id"] = range(
    1,
    len(df) + 1
)

#============================================================================================
#Applied Example: Generating a Globally Unique ID using UUIDs
#============================================================================================

#using UUID, outputs are: 550e8400-e29b-41d4-a716-446655440000
#very low collision probability 
#Not for use as a traditional integer surrogate key, best for use as ETL/batch tracking 

import uuid

df["etl_row_id"] = [
    uuid.uuid4()
    for _ in range(len(df))
]

#Example using uuid for a batch identifier 
import pandas as pd
import uuid

# Example source data
df = pd.DataFrame({
    "image_name": [
        "image_001.jpg",
        "image_002.jpg",
        "image_003.jpg"
    ],
    "nitrogen_reading": [12.4, 10.8, 14.1]
})

# Generate ONE UUID for this ingestion batch
batch_id = str(uuid.uuid4())

# Generate a separate UUID for each row
df["etl_row_id"] = [
    str(uuid.uuid4())
    for _ in range(len(df))
]

# Assign the SAME batch ID to every row in this load
df["batch_id"] = batch_id

print(df)

#============================================================================================
#Applied Example: Pandas Cleaning Pipeline 
#============================================================================================

import pandas as pd
import numpy as np

df = pd.read_csv(
    "employees.csv",
    na_values=["", "NULL", "N/A"]
)

# Inspect
df.info()

# Standardize column names
df = df.rename(columns={
    "Employee ID": "employee_id",
    "Hire Date": "hire_date"
})

# Clean strings
df["name"] = df["name"].str.strip().str.title()
df["department"] = df["department"].str.strip()

# Convert data types
df["employee_id"] = pd.to_numeric(
    df["employee_id"],
    errors="coerce"
)

df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)

df["hire_date"] = pd.to_datetime(
    df["hire_date"],
    errors="coerce"
)

# Remove duplicate employees
df = df.drop_duplicates(
    subset=["employee_id"]
)

# Fill missing salary with median
df["salary"] = df["salary"].fillna(
    df["salary"].median()
)

# Fill missing department
df["department"] = df["department"].fillna(
    "Unknown"
)

# Create calculated column
df["bonus"] = df["salary"] * 0.10

# Create another calculated column
df["total_compensation"] = (
    df["salary"] + df["bonus"]
)

# Create date-derived column
df["hire_year"] = df["hire_date"].dt.year

# Batch-level ETL identifier
df["etl_row_id"] = [
    str(uuid.uuid4())
    for _ in range(len(df))
]