# Python control flow examples
###################################################
# Python control flow examples
##################################################

###################################################
# If statements
# An if statement is a conditional statement that runs or skips code based on whether a condition is true or false.
##################################################

# Here's a simple example.
phone_balance = 50
bank_balance = 1000
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
    
    
###################################################
# loops
# Python has two kinds of loops - for loops and while loops. A for loop is used to "iterate", or do something repeatedly, over an iterable.
##################################################

###################################################
# for loops
##################################################
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)
    
    
###################################################
# for loops with range
# Notes on using range():

# If you specify one integer inside the parentheses withrange(), it's used as the value for 'stop,' and the defaults are used for the other two.
# e.g. - range(4) returns 0, 1, 2, 3
# If you specify two integers inside the parentheses withrange(), they're used for 'start' and 'stop,' and the default is used for 'step.'
# e.g. - range(2, 6) returns 2, 3, 4, 5
# Or you can specify all three integers for 'start', 'stop', and 'step.'
# e.g. - range(1, 10, 2) returns 1, 3, 5, 7, 9
##################################################

for i in range(3):
    print("Hello!")
    

###################################################
# while loops, 
# aka indefinite iteration which is when a loop repeats an unknown number of times and ends when some condition is met
##################################################    

## adds the last element of the card_deck list to the hand list
## until the values in hand add up to 17 or more
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <= 17:
    hand.append(card_deck.pop())


###################################################
# break
# use break to exit loop
##################################################    

## search for factors, iterating through numbers ranging from 2 to the number itself
num =22
for i in range(2, num):

## number is not prime if modulo is 0

    if (num % i) == 0:
        print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
        break


###################################################
# continue
# use continue keyword to skip 1 iteration of loop
##################################################    

## iterate through the check_prime list
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
## check if the number is 2
    if num == 2:
        print("{} IS a prime number".format(num))
        continue
    


###################################################
# Zip and Enumerate
# use zip to  returns an iterator that combines multiple iterables into one sequence of tuples.
##################################################

# Each tuple contains the elements in that position from all the iterables. For example, printing

# combine letters and numbers
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))
    
    
# use enumerate to return an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

# print a letter and it's index
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
    
    
# use zip and enumerate to combine multiple iterables into one 

# combine all coordinates into one interable that contains a label mapped to a coordinate set
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point)) # <- unpacked the tuple using * operator

for point in points:
    print(point)
    

# zip two different lists into a dictionary
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)


# unzip a set of tuples
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast) # <- unpacked the tuple using * operator
print(names)
print(heights)


# transpose a matrix stored as tuples using zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data)) # <- unpacked the tuple using * operator
print(data_transpose)


# use list comprehension to quickly. List comprehensions allow us to create a list using a for loop in one step.

# extract first names from the list
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)


# filter names
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
