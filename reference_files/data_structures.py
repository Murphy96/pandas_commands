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


#Example ingestion pipeline 
incoming_ids = {"S101", "S102", "S105"}
registered_ids = {"S101", "S102", "S103", "S104"}

new_ids = incoming_ids - registered_ids

print(new_ids)
# {"S105"}

#Best for removing duplicates, finding new or missing IDs, checking if something esists, comparing categories or groups

#---------------------------------------------------------------------------
# Specialized Collection Types 
#---------------------------------------------------------------------------

# deque: double-ended queue --------------------------------------------------------------
    #designed for adding or removing items at either end efficeiently 
    #Lists best for random acceess by index or append at the end 
    # This is best for when an algorithm repeatedly adds or removes items from front and back 
from collections import deque

tasks = deque(["file_001.csv", "file_002.csv"])

tasks.append("file_003.csv")
tasks.appendleft("urgent_file.csv")

next_task = tasks.popleft()

print(next_task)  # urgent_file.csv

# Counter: count repeated values ----------------------------------------------------------
    # can build with a dictionary and loop
    # best for data-quality summaries, frquency analysis, event counts, and tracking categories errors in ETL jobs

from collections import Counter

statuses = [
    "success", "failure", "success",
    "success", "failure"
]

counts = Counter(statuses)

print(counts["success"])  # 3
print(counts.most_common(1))  # [('success', 3)]

#defaultdict: group values without checking every key-------------------------------------
    #use for grouping records by category, sensor, region, or date 
    #accessing a missing key in defaultdict can create that key, so this can mutate data
    #Do not use for large batches, groupby or other approaches will be less memory intensive

from collections import defaultdict

readings_by_sensor = defaultdict(list) #list tells the object to create when a new key is accessed, will create an empty list as the value for a new key

readings_by_sensor["S101"].append(22.5)
readings_by_sensor["S101"].append(23.0)
readings_by_sensor["S102"].append(21.8)

print(readings_by_sensor["S101"])
# [22.5, 23.0]

#example for an ETL workload (SMALL BATCH ONLY)

from collections import defaultdict
import pandas as pd

# Simulated raw data extracted from a source
raw_data = [
    {"sensor_id": "S101", "timestamp": "10:00", "temperature": 22.5},
    {"sensor_id": "S102", "timestamp": "10:00", "temperature": 21.8},
    {"sensor_id": "S101", "timestamp": "10:05", "temperature": 23.0},
    {"sensor_id": "S103", "timestamp": "10:05", "temperature": 24.1},
    {"sensor_id": "S102", "timestamp": "10:05", "temperature": 22.0},
    {"sensor_id": "S101", "timestamp": "10:10", "temperature": 22.7},
]

# Transformation: group readings by sensor
readings_by_sensor = defaultdict(list)

for record in raw_data:
    sensor_id = record["sensor_id"]
    temperature = record["temperature"]

# heapq: a priority queue----------------------------------------
#heap lets you efficiently retrieve the smallest item 
#use for selecting the next lowest- priority number, scheduling tasks by piorirty, 
# mainatining the smallest or largest few values without sorting an entire collection every time \

import heapq

priorities = [5, 1, 8, 2]

heapq.heapify(priorities)

next_priority = heapq.heappop(priorities)

print(next_priority)  # 1

# queue.Queue: a thread safe queue---------------------------------
# designed to coordinate work between threads safely, supports blocking and coordination features
#use for multithreaded producer-consumer systems where one part of the program produces work 
#and the other processes it
#for asynchronous code using asyncio, there are corresponding asynchronous queue types

from queue import Queue

work_queue = Queue()

work_queue.put("file_001.csv")
work_queue.put("file_002.csv")

next_file = work_queue.get()
print(next_file)  # file_001.csv

work_queue.task_done()

# dataclass: a richer version of named tuples ---------------------
#allows for the defintion of a record with named fields, but unlike a 
#named tumple, mutable by default, can be made immutable  
from dataclasses import dataclass

@dataclass
class SensorReading:
    sensor_id: str
    temperature: float
    humidity: float

reading = SensorReading("S101", 22.5, 61.0)

print(reading.temperature)  # 22.5

reading.temperature = 23.0  # Valid

#immutable 
@dataclass(frozen=True)
class SensorReading:
    sensor_id: str
    temperature: float

#-------------------------------------------------------------
# Putting it all together example: 
#-------------------------------------------------------------
from collections import Counter, defaultdict
from dataclasses import dataclass

@dataclass
class SensorReading:
    sensor_id: str
    temperature: float
    timestamp: str


raw_records = [
    {"sensor_id": "S101", "temperature": 22.5,
     "timestamp": "2026-10-26T09:00:00"},
    {"sensor_id": "S102", "temperature": 24.0,
     "timestamp": "2026-10-26T09:01:00"},
    {"sensor_id": "S101", "temperature": 23.0,
     "timestamp": "2026-10-26T09:02:00"}
]

# Convert incoming dictionaries to structured records.
readings = [
    SensorReading(**record)
    for record in raw_records
]

# Find the unique sensors.
sensor_ids = {reading.sensor_id for reading in readings}

# Group temperatures by sensor.
temperatures_by_sensor = defaultdict(list)

for reading in readings:
    temperatures_by_sensor[reading.sensor_id].append(
        reading.temperature
    )

# Count how many records belong to each sensor.
records_by_sensor = Counter(
    reading.sensor_id for reading in readings
)

print(sensor_ids)
print(temperatures_by_sensor["S101"])
print(records_by_sensor)