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

#df['height'] > 30

#Put inside the DataFrame
df[df['height_inches']> 30]

