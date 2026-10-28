#------------------------------------------------------------------------------------
# Data Structures in Python
#------------------------------------------------------------------------------------

#Main Data Structures 
#-----4 primary built-in collection types--------

#-------List 
# ordered, mutable, allows duplicates

# General purpose for a series of items 

sensor_readings = [21.5, 22.1, 21.8]

sensor_readings.append(23.0)
sensor_readings[0] = 20.9


# .pop()
fruits = ['apple', 'banana', 'cherry', 'date']

# 1. Pop without arguments (removes the last item)
last_fruit = fruits.pop()
print(last_fruit)  # Output: 'date'
print(fruits)      # Output: ['apple', 'banana', 'cherry']

# 2. Pop with a specific index
second_fruit = fruits.pop(1)
print(second_fruit) # Output: 'banana'
print(fruits)       # Output: ['apple', 'cherry']



# .extend(), 
# Adds items to a list, must be interable, use whenever you're adding each item from another iterable 

morning_readings = [21.5, 22.0, 22.3]
afternoon_readings = [24.1, 24.5, 23.9]

morning_readings.extend(afternoon_readings)

print(morning_readings)
# [21.5, 22.0, 22.3, 24.1, 24.5, 23.9]



#-------Tuple   
# ordered, immutable, allows duplicates
# used when a group of values belongs together
# (ummutable) it's elements cannot be reassigned, added, or removed from the tuple after creation

sensor_location = (35.99, -78.90)

latitude = sensor_location[0]
longitude = sensor_location[1]

#Can be used within a list to keep data together
#Helpful for: 
    #fixed groups of related values
    #returning multiple results from a funciton 
    # representing coordinates or RGB color values 
    # using an immutable squence as a dictonary key  

location_history = [
    (35.99, -78.90),
    (36.01, -78.92),
    (36.03, -78.95)
]

#Tuples are shallowly immutable, if the tuple contains a list, the list inside can be changed
record = ("sensor_A", [21.5, 22.1])
record[1].append(23.0)  # Valid

#-------Named Tuples
# A dictionary like tuple, where the fields have names instead of using the index   

from collections import namedtuple

SensorReading = namedtuple(
    "SensorReading",
    ["sensor_id", "temperature", "humidity"]
)

reading = SensorReading("S101", 22.5, 61.0)

print(reading.sensor_id)   # S101
print(reading.temperature) # 22.5
print(reading[1])          # 22.5

#Applied example: 
from collections import namedtuple

SensorStats = namedtuple(
    "SensorStats",
    ["minimum", "maximum", "average"]
)

def calculate_stats(values):
    return SensorStats(
        min(values),
        max(values),
        sum(values) / len(values)
    )

stats = calculate_stats([20.0, 22.0, 24.0])

print(stats.average)  # 22.0

# Could do the same thing with a dictonary 

def calculate_stats(values):
    return {
        "minimum": min(values),
        "maximum": max(values),
        "average": sum(values) / len(values)
    }

stats = calculate_stats([20.0, 22.0, 24.0])

print(stats["average"])  # 22.0

#Both work, 
# named tumple is a good fit when the output has a fixed schema and you need an immutable record
# dictonary is a good fit when you want to change, add, or remove fields 

#-------Dictionary
# key-value pairs, mutalbe, insertion-ordered, each key identifies a value 

sensor = {
    "sensor_id": "S101",
    "temperature": 22.5,
    "humidity": 61.0
}

# retrieve values 
print(sensor["temperature"])  # 22.5

# modify the dictionary 

sensor["temperature"] = 23.0
sensor["battery"] = 87
del sensor["humidity"] 


# Safe lookup with a default
battery = sensor.get("battery", 100) # useful for processing inconsisent input, like JSON returned from an API. 
#It returns a default value if a key is absent instead of raising a KeyError, this doesn't edit the orignal dictonary 

# Check whether a key exists
if "temperature" in sensor:
    print(sensor["temperature"])

# Get keys, values, or key-value pairs
print(sensor.keys())
print(sensor.values())
print(sensor.items())


#-------Set
# unique elements, unordred collection, if a duplicate is added, one copy is kept
sensor_ids = {"S101", "S102", "S103"}

sensor_ids.add("S104")
sensor_ids.add("S101")

print(sensor_ids)
# Contains S101, S102, S103, S104 (order not guaranteed)


#Set  operations
# Sets are not indexed, used for testing membership and comparing groups

today = {"S101", "S102", "S103"}
yesterday = {"S102", "S103", "S104"}

print(today & yesterday)  # Intersection
# {"S102", "S103"}

print(today - yesterday)  # Difference
# {"S101"}

print(today | yesterday)  # Union
# All four unique IDs




