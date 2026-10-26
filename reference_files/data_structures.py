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

#-------Set
# unique elements, unordred collection 

#-------Dictionary
# key-value pairs, mutalbe, insertion-ordered

