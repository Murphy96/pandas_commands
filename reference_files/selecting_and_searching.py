#Selecting and Searching DataFrames

import pandas as pd

data = {
    "common_name": ['goldenrod', 'lupine','foxglove', 'yarrow'], 
    "height_inches": [48, 18, 48, 30 ],
    "sowing_season": ['fall', 'fall', 'fall', 'fall' ], 
    "light": ['full sun', 'full sun, partial shade', 'full sun, partial shade', 'full sun' ]
}

df=pd.DataFrame(data)

#============================================
#Selecting columns
#============================================ 

#returns a Series
df["light"]
#returns a DataFrame, can select mutliple columns
df[['light']]
df[['common_name', 'light','sowing_season']]

#============================================
#Selecting rows 
#============================================ 

#Create a condition, returns a Boolean Series

df['height'] > 30

#Put inside the DataFrame
df[df['height_inches']> 30]

#Multiple conditions, & is AND, | is OR
df[
   (df['sowing_season']=='fall') &
   (df['height_inches']>30)
]


#=========================================
# Working with loc
#=========================================

#loc is a selection based on labels/conidtions, inclusive of the ending label 
#df.loc[row_selection, column_selection]



df.loc[[0,2]] #returns row 0 and row 2
df.loc[0, "common_name"] #selects first row, value from common_name column
df.loc[[0,2],['common_name','height_inches']] #selects first three rows, values from common_name and height_inches


df.loc[0:2] #returns row 0 through row 2 (3 rows total)
df.loc[0:2, ['common_name','height_inches']] #returns row 0 through 2 and values from common_name and height_inches

#=========================================
# Working with iloc
#=========================================

#iloc is a slection based on integer-position, exclusive of ending label 