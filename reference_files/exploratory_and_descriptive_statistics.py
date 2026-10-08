#=======================================
#DataFrame Inspection and Profiling
#=======================================

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

#Returns 5 random rows
df.sample()

#=======================================
#Dimension Info
#=======================================
#Returns (# rows, # columns)
df.shape

#Returns number of rows
df.shape[0]
#Returns number of columns 
df.shape[1]

df.size

#=======================================
#Column Info
#=======================================

#Returns an index of the columns
df.columns
#Returns a list of the columns 
list(df.columns)

#Returns the column names and their data types
df.dtypes  

#=======================================
#Structural Info
#=======================================

#Returns number of rows, columns, missing values, data types, 
# and memory usage
df.info()

df.info(
    verbose=True,
    show_counts=True,
    memory_usage=True #can also do =deep, gives more thorough estimate 
)
#========================================
#Data Quality and Profiling
#========================================

#Returns the count of each distinct values in a Series/column 
#excludes nulls by default
#value_counts(dropna=False) would include nulls

df.value_counts()

#IE
df['common_name'].value_counts()

#Returns the number of unique values for each column 
df.nunique()
#Can select just one column 
df["common_name"].nunique()

#Missing Values
#Returns sum of nulls in each column with headers
df.isna().sum()



#=======================================
#Descriptive Statistics (Numeric)
#=======================================

#Returns descriptive statistics, will only return numeric columns
#count, mean, std, min and max
df.describe()

#include all columns 
df.describe(include="all")
#Can also specify the data type to include 
df.describe(include=["number"])
df.describe(include=["object"])
df.describe(include=["datetime"])

#Can exclude types
df.describe(exclude=["object"])

#Can set the percentiles 
df.describe(percentiles=[0.10, 0.25, 0.50, 0.75, 0.90, 0.99])

#Select a particular column 
df["height_inches"].describe()

#Individual descriptive statistics 
df.mean()
df.median()
df.mode()
df.std() 
df.var()
df.min()
df.max()
df.sum()
df.count()

#IE
df["height_inches"].median()
df.mean(numeric_only=True)

#=======================================
#Quantiles
#=======================================

# returns a specified quantile or list of quantiles
df.quantile()

#IE
df["height_inches"].quantile(0.50)
df["height_inches"].quantile([0.25, 0.50, 0.75])

#======================================
#Correlation 
#======================================
df.corr(numeric_only=True)
#Can specify the method 
df.corr(method="pearson", numeric_only=True)
df.corr(method="spearman", numeric_only=True)
df.corr(method="kendall", numeric_only=True)
