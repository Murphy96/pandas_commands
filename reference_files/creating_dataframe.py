#DataFrame creation examples
#1) DataFrame directly from python data
#2) DataFrame from a CSV
#3) Data from an API into a DataFrame

import pandas as pd


#1) Creating a DataFrame from a dictionary 

data = {
    "common_name": ['goldenrod', 'lupine','foxglove', 'yarrow'], 
    "height_inches": [48, 18, 48, 30 ],
    "sowing_season": ['fall', 'fall', 'fall', 'fall' ], 
    "light": ['full sun', 'full sun, partial shade', 'full sun, partial shade', 'full sun' ]
}

df=pd.DataFrame(data)

print(df)

#2) Creating a DataFrame from a CSV
import pandas as pd

df = pd.read_csv(
    "PATH/TO/FILE.csv",
    header=0, 
    # first row is the header, this is default, 
    # can use 1,2 etc meaning those rows are the header, 
    # zero-based indexing
    
     # or can specify header names in code
     # header=None,
     # names=["column_name_1", "column_name_2", "column_name_3"]


    usecols=["column1", "column2"],
    #can be selected by column name or by position/index
    # if using index, 0 based index, inclusive

    parse_dates=["date_column"],
    #converts dates into a datetime type
    na_values=["N/A", "NULL"]
    #assigns certain values as missing data, 
    # ie N/A in source data would be treated as NaN in DataFrame
)

# Creating a DataFrame from an API

import requests
import pandas as pd

url = "API_URL"

params = {
    "parameter1": "value1",
    "parameter2": "value2"
}

response = requests.get(
    url,
    params=params
)

response.raise_for_status()

#response returns a json object 

data = response.json()

df = pd.DataFrame(data["RECORDS_KEY"])


df["date"] = pd.to_datetime(df["date"])
#This takes an existing column in the df called 'data' and converts it to 
#date/time and replaces it in the dataframe. There will be more transformations later

print(df)





#An example: 
#JSON returned from API that looks something like this: 
data = {
    "location": {
        "latitude": 35.7796,
        "longitude": -78.6382
    },

    "hourly": {
        "time": [
            "2026-10-05T08:00",
            "2026-10-05T09:00",
            "2026-10-05T10:00"
        ],
        "temperature": [
            18.2,
            19.5,
            21.1
        ],
        "precipitation": [
            0.0,
            0.2,
            0.0
        ],
        "humidity": [
            85,
            80,
            72
        ],
        "wind_speed": [
            5.2,
            6.1,
            7.0
        ]
    }
}

#Hourly Key is the interest so: 
df = pd.DataFrame(data["hourly"])

#Let's say this gives more columns, we're only interested in a handful

#This selects the 5 we care about, drops the rest out of the frame
df = df[
    [
        "time",
        "temperature",
        "precipitation",
        "humidity",
        "rain"
    ]
]

# Or, with the steps together: 

df = pd.DataFrame(data["hourly"])[
    [
        "time",
        "temperature",
        "precipitation",
        "humidity",
        "rain"
    ]
]

#Add information from the parameters 
#create DataFrame then: 
df["latitude"] = params["latitude"]
df["longitude"] = params["longitude"]




#Looping through a series of parameters for an API example 

locations = [
    {"zip_code": "27701", "latitude": 35.7796, "longitude": -78.6382},
    {"zip_code": "27601", "latitude": 35.7796, "longitude": -78.6330},
    {"zip_code": "27514", "latitude": 35.9132, "longitude": -79.0558}
]

all_weather = []

for location in locations:

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "hourly": "temperature_2m,precipitation",
        "timezone": "America/New_York"
    }

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params=params
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["hourly"])

    df["zip_code"] = location["zip_code"]
    df["latitude"] = location["latitude"]
    df["longitude"] = location["longitude"]

    all_weather.append(df)

#above returns a list of dataframes for each parameter
weather_df = pd.concat(
    all_weather,
    ignore_index=True
)
#concatinates each DataFrame into a single DataFrame


#Taking it another step farther, if you were generating a fact and dimension table
# with your parameters as a dimension table 
#This is a pseudocode loop: 

for location in locations:

    # 1. Check whether location exists
    location_key = find_location(location)

    # 2. If it doesn't exist, create it
    if location_key is None:
        location_key = create_location(location)

    # 3. Get weather
    weather_data = get_weather(location)

    # 4. Tag weather with location_key
    weather_data["location_key"] = location_key

    # 5. Add weather to collection
    all_weather.append(weather_data)

#this command would replace any existing data in a previous weather_df, 
#the generated DataFrame would be stored in a database where the new frame(s) 
#would be appended to an existing set of tables
weather_df = pd.concat(all_weather, ignore_index=True)