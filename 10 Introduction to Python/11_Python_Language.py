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
# 7. List comprehension
# 8. f-strings


# 6. Control structures

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

print()

# You can also use for and while loops

print('Loop over the list and display the index and the value:')
# You can loop over a list and simultaneously get the index and the value
for index, element in enumerate(my_list):
    print(index, element)
print()

print('Find the maximum element of the list:')
# You can loop over a list and get the index and the value of the maximum element
max_value = 0
max_index = 0
for index, element in enumerate(my_list):
    if element > max_value:
        max_value = element
        max_index = index
print(max_index, max_value)
print()

# Here you want to go through all the elements of the list
# and find the maximum one
# so you use a for loop

# You can also use while loops
# It is useful when you don't know the number of iterations in advance
print('Find the first element bigger than 3:')
index = 0
while my_list[index] <= 3:
    index += 1
print(my_list[index])
print()

# In that case you do not know in advance how many iterations you will need
# so you use the while loop


# 7. List comprehension

# List comprehension is a powerful feature of python
# It allows you to define a list in a single line

# You can define a list with list comprehension
print('Define a list with list comprehension:')
my_list = [i for i in range(10)]
print(my_list)
print()

# And you can also define a list with list comprehension with a condition
# Here we only keep the even numbers
print('A list of even natural integers smaller or equal to 10:')
my_list = [i for i in range(10) if i % 2 == 0]
print(my_list)
print()

# For instance if you have a list of filenames with different extensions
# You can keep only the .txt files
print('Keep only the .txt files:')
filenames = ['file1.txt', 'file2.csv', 'file3.txt', 'file4.csv']
txt_files = [i for i in filenames if i[:-4] == '.txt']
print(txt_files)
print()

# You can create a new list from an existing list
# For instance multiply the elements by 20
print('Create a new list from an existing list:')
new_list = [i*20 for i in my_list]
print(new_list)
print()

# Note that new_list * 20 does not work as expected
new_list = new_list * 20
print(new_list)
print()
# it repeats the list 20 times

# Notice how concise this next code is compared to other programming languages!
# Find all the leap years between 2000 and 2400
print('Find all the leap years between 2000 and 2400:')
leap_years = [i for i in range(2000, 2400) if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)]
# That is a nice one liner !
print(leap_years)
print('Number of leap years found:', len(leap_years))
print('Notice how 2000 and 2400 are leap years but 2100, 2200 and 2300 are not!')
print()

# Use loops to generate a list of filenames
print('Generate a list of filenames:')
filenames = ['file' + str(i) + '.txt' for i in range(10)]
print(filenames)
print()


# 8. f-strings
# f-strings are a powerful feature of python
# They allow you to format strings in a concise way
# You can print text and variables togetgher easily

# The same list of filenames using f-strings
print('Generate a list of filenames using f-strings:')
filenames = [f'file{i}.txt' for i in range(10)]
print(filenames)
print()

my_integer = 42
my_float = 3.14159

# You can also use f-strings to display variables
print('Display variables using f-strings:')
print(f'my_integer = {my_integer}')
print(f'my_float = {my_float}')
print(f'my_list = {my_list}')
print()

# Use of f-strings to display variables with a given format (here 2 digits after the comma)
print('Display variables with a given format using f-strings:')
print(f'my_integer = {my_integer:05d}')
print(f'my_float = {my_float:.2f}')
print(f'my_list[2] = {my_list[2]:08.2f}')
# f-string in scientific notation with 3 leading zeros and 7 digits in total
print(f'my_float = {my_float:.3e}')
print()

# You can also use f-strings to create strings
print('Create strings using f-strings:')
filename = f'result_{my_integer}_{my_float:.2f}.txt'
print(f'Generated filename: {filename}')
print()
# That is very useful to create filenames with variable values in them
# You can also use f-strings to do calculations inside the string
print('Do calculations inside f-strings:')
print(f'The sum of {my_integer} and {my_float:.2f} is {my_integer + my_float:.2f}')
print()
# That is very useful to display results of calculations directly
# without having to create intermediate variables

###########################################################

# End of the tutorial

# Keep in mind that this is just a brief introduction to Python.
# Python is a very rich language with many libraries and features.
# You can explore more advanced topics such as:
# - Object-oriented programming
# - Functional programming
# - Data analysis with pandas
# - Scientific computing with NumPy and SciPy
# - Machine learning with scikit-learn and TensorFlow
# - Web development with Django and Flask
# - And much more!

# Feel free to explore Python further on your own.
# Resources on the web, books, and online courses can help you deepen your knowledge.
# They will help you learn far better than using AI tools.

# If you are more interested in scientific programming,
# you can explore two other tutorials that are available:
# - "Interactive Python" that shows you how to use interactive python in your programming environment.
# - "Jupyter Notebooks" that shows you how to use Jupyter notebooks for your scientific programming.
# That is very convenient to mix code, text, equations and plots in a single document.
#
# Then for applications to scientific needs you can go to the "Intermediary Python" tutorial.
#
# Thank you for reading this tutorial !