###########################################################
#                                                         #
#                  Python        1  0  1                  #
#                        Tutorial                         #
#                                                         #
###########################################################
# By Adrien Poindron, 2025/11/10
#
# This is a tutorial to get started in python.
#
# Outline
# 6. Control structures
# 7. Functions
# 8. Modules and packages
# 9. File handling
# 10. Error handling
# 11. Useful libraries

###########################################################
# Control structures may be interesting to you
# they allow you to make decisions in your code
# For instance, you can use if statements

my_list = [1, 2, 3, 4, 5]

print('Use if statements:')
# You can use if statements to make decisions
if my_list[0] == 1:
    print('The first element of the list is 1')
else:
    print('The first element of the list is not 1')

# You can also use for and while loops

print('Loop over the list and display the index and the value:')
# You can loop over a list and simultaneously get the index and the value
for index, element in enumerate(my_list):
    print(index, element)

print('Find the maximum element of the list:')
# You can loop over a list and get the index and the value of the maximum element
max_value = 0
max_index = 0
for index, element in enumerate(my_list):
    if element > max_value:
        max_value = element
        max_index = index
print(max_index, max_value)

# You can also use while loops
# It is useful when you don't know the number of iterations in advance
print('Find the first element bigger than 3:')
index = 0
while my_list[index] <= 3:
    index += 1
print(my_list[index])

###########################################################
# List comprehension is a powerful feature of python
# It allows you to define a list in a single line

# You can define a list with list comprehension
print('Define a list with list comprehension:')
my_list = [i for i in range(10)]
print(my_list)

# And you can also define a list with list comprehension with a condition
# Here we only keep the even numbers
print('Define a list with list comprehension with a condition:')
my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)

# For instance if you have a list of filenames with different extensions
# You can keep only the .txt files
print('Keep only the .txt files:')
filenames = ['file1.txt', 'file2.csv', 'file3.txt', 'file4.csv']
txt_files = [i for i in filenames if i[:-4] == '.txt']
print(txt_files)

# You can create a new list from an existing list
# For instance multiply the elements by 20
print('Create a new list from an existing list:')
new_list = [i*20 for i in my_list]
print(new_list)

# Note that new_list * 20 does not work as expected
new_list = new_list * 20
print(new_list)
# it repeats the list 20 times

###########################################################
# More fancy useful things

# find all the leap years between 1000 and 100000
print('Find all the leap years between 1000 and 100000:')
leap_years = [i for i in range(1000, 100000) if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)]
print(leap_years)

# Use loops to generate a list of filenames
print('Generate a list of filenames:')
filenames = ['file' + str(i) + '.txt' for i in range(10)]
print(filenames)

# The same using f-strings
print('Generate a list of filenames using f-strings:')
filenames = [f'file{i}.txt' for i in range(10)]
print(filenames)

# You can also use f-strings to display variables
print('Display variables using f-strings:')
print(f'my_integer = {my_integer}')
print(f'my_float = {my_float}')
print(f'my_list = {my_list}')

# Use of f-strings to display variables with a given format (here 2 digits after the comma)
print('Display variables with a given format using f-strings:')
print(f'my_float = {my_float:.2f}')
print(f'my_list[2] = {my_list[2]:08.2f}')
# f-string in scientific notation with 3 leading zeros and 7 digits in total
print(f'my_float = {my_float:.3e}')
