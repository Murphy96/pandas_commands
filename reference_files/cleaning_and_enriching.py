#Cleaning and Enriching Data


import pandas as pd

data = {
    "common_name": ['goldenrod', 'lupine','foxglove', 'yarrow'], 
    "height_inches": [48, 18, 48, 30 ],
    "sowing_season": ['fall', 'fall', 'fall', 'fall' ], 
    "light": ['full sun', 'full sun, partial shade', 'full sun, partial shade', 'full sun' ]
}

df=pd.DataFrame(data)

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
df = df.dropna(axis=1) #