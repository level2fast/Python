###################################################
# Tuples
# Tuples are ordered, immutable types in Python
##################################################
# Cool things we can do with tuples in Python

print("Tuples")
print("#####################################")
# store location as tuple: "()" indicates that this is a tuple
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

# store dimensions as a tuple
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# store dimensions directly
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
print("#####################################")
print("\n")

###################################################
# Lists
# Lists are ordered mutable types in Python
#################################################
# Some cool things we can do with lists in Python
print("Lists")
print("#####################################")

# Some cool things we can do with lists in Python

# use the "join" method to take a list of strings and return a string consisting of the list elements
# joined by a separator string
list1 = ["fore", "aft", "starboard", "port"]
print(list1)
new_str = "\n".join(list1)
print(new_str)

list2 = ["García", "O'Kelly", "Davis"]
name = "-".join(list2)
print(name)

# add an element to the end of a list using the "append" method
letters = ['a', 'b', 'c', 'd']
print(letters)
letters.append('z')
print(letters)


print("#####################################")
print("\n")

###################################################
# Sets
# Sets are unordered mutable types in Python
#################################################
# Some cool things we can do with sets in Python
print("Sets")
print("#####################################")

# remove duplicates 
print("remove duplicates")
numbers = [99, 100, 1, 3, 4, 99, 100]
print(numbers)
unique_nums = set(numbers)
print(unique_nums)
# One of the key properties of a set is that it only contains unique elements. 
# So even if you create a new set with a list of elements that contains duplicates, 
# Python will remove the duplicates when creating the set automatically.
print("\n")

# add elements to sets
# remove elements using the pop method
print("add element, remove element")
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("set: " , fruit)

print("Is watermelon in set? ","watermelon" in fruit)  # check for element

print("Add watermelon")
fruit.add("watermelon")  # add an element
print(fruit)

print("pop value from set: ",fruit.pop())  # remove a random element
# Although, when you pop an element from a set, a random element is removed. 
# Remember that sets, unlike lists, are unordered so there is no "last element".
print(fruit)
print("\n")

# perform mathemeatical set operations like union, intersection, and difference 

import time

# Sample data
set1 = set(range(1000))
set2 = set(range(500, 1500))
list1 = list(set1)
list2 = list(set2)

# Union
start_time = time.time()
union_set = set1.union(set2)
print("Set Union Time:", time.time() - start_time)

start_time = time.time()
union_list = list(set(list1 + list2))
print("List Union Time:", time.time() - start_time)

# Intersection
start_time = time.time()
intersection_set = set1.intersection(set2)
print("Set Intersection Time:", time.time() - start_time)

start_time = time.time()
intersection_list = [x for x in list1 if x in set2]
print("List Intersection Time:", time.time() - start_time)

# Difference
start_time = time.time()
difference_set = set1.difference(set2)
print("Set Difference Time:", time.time() - start_time)

start_time = time.time()
difference_list = [x for x in list1 if x not in set2]
print("List Difference Time:", time.time() - start_time)
print("#####################################")
print("\n")


###################################################
# Dictionary
# Dictionaries are mutable types that store key->value pairs in Python
#################################################
# Some cool things we can do with sets in Python
print("Dictionaries")
print("#####################################")

# store keys with different types
print("keys with different types")
random_dict = {"abc": 1, 5: "hello"}
print(random_dict)
print("\n")

# check if key is in the Dictionary
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print("Dictionary: ", elements)
print("Is carbon in elements:","carbon" in elements)
print("Is dilithium in elements:", elements.get("dilithium"))

# check if key is returned
n = elements.get("dilithium")
print("Is dilithium not in elements: ", n is None)
print("Is dilithium in elements: ", n is not None)


print("#####################################")
print("\n")


###################################################
# Compound Data Structures
# Compuond Data Structures are containers in other containers
#################################################
# Some cool things we can do with Compound Data Structures in Python

# create a dictionary of dictionaries
print("dictionary of dictionaries")
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
print("elements dict: ", elements)

print("get hydrogens weight")
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print("Hydrogens weight:",hydrogen_weight)
print("\n")

print("elements dict: ", elements)
print("add new key")
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
print("added oxygen", oxygen)
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements: ', elements)
print("\n")

print("add new element")
student_records = {
    'John': {
        'age': 20,
        'major': 'Computer Science',
        'grades': [85, 90, 92]
    },
    'Emma': {
        'age': 19,
        'major': 'Mathematics',
        'grades': [95, 88, 91]
    }
}
print("student records dict", student_records)
print("add a new student")
student_records['Alex'] = {
    'age': 21,
    'major': 'Physics',
    'grades': [80, 85, 88]
}
print("student records dict", student_records)
print("\n")

print("add a new grade to student record")
student_records['Alex']['grades'].append(88)
print("student records dict", student_records)


print("#####################################")
print("\n")
