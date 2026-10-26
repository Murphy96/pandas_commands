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



#-------Set
# unique elements, unordred collection 

#-------Dictionary
# key-value pairs, mutalbe, insertion-ordered

