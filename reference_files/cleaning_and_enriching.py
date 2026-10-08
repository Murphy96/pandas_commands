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
