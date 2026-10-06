# Inspecting data within a DataFrame

import pandas as pd

data = {
    "common_name": ['goldenrod', 'lupine','foxglove', 'yarrow'], 
    "height_inches": [48, 18, 48, 30 ],
    "sowing_season": ['fall', 'fall', 'fall', 'fall' ], 
    "light": ['full sun', 'full sun, partial shade', 'full sun, partial shade', 'full sun' ]
}

df=pd.DataFrame(data)


#Returns first 5 rows by default, can specify number of rows
df.head()

#Prints just the first row
print(df.head(1))

#Prints the last row(s)
df.tail()

#Returns (# rows, # columns)
df.shape

#Returns number of rows
df.shape[0]
#Returns number of columns 
df.shape[1]

#Returns an index of the columns
df.columns
#Returns a list of the columns 
list(df.columns)

#Returns the column names and their data types
df.dtypes  


#Returns number of rows, columns, missing values, data types, 
# and memory usage
df.info()

#Returns descriptive statistics, will only return numeric columns
#count, mean, std, min and max
df.describe()
#Select a particular column 
df["height_inches"].describe()


