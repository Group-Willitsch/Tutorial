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
# 1. What is Python
# 2. Install and use python
# 3. Basic syntax
# 4. Variables and types
# 5. Lists and tuples



# 1. What is Python

# Python is a free and open-source programming language widely used in a very broad range of fields
# such as web development, data science, artificial intelligence, scientific computing,
# graphical interface, command control, and much more ! Anything is possible with Python !

# Python is known for its simplicity and readability, making it a great choice for beginners. Python
# has a large and active community, which means there are plenty of resources and libraries available.
# If you do not know, ask Google, StackOverflow, or other forums ! You will always find help.

# Now it is time to explain how Python is working and how you can install it and use it.
# First, you install a specific version of Python on your computer.
# Then, you write your code in text files with the extension .py.
# Finally, you can run your code using the Python interpreter.
# As simple as that. Because it is an interpreted language, you can run your code directly
# without the need for compilation. This is different from other languages like C, C++, or ForTran.


# 2. Install and use python

# I advice you to install Python using an environment manager like Anaconda or Miniconda.
# It will allow you to easily manage different versions of Python and different packages.
# You can download Miniconda here: https://docs.conda.io/en/latest/miniconda.html
# Follow the instructions to install it on your computer.

# Once installed, you can create a new environment with a specific version of Python.
# For instance, to create an environment with Python 3.10, you can use the following command:
# conda create -n myenv python=3.10

# Then you can open a terminal, activate the environment, and run python commands.
# To activate the environment, you can use the following command:
# conda activate myenv
# On the terminal you should see (myenv) at the beginning of the line.
# To deactivate the environment, you can use the following command:
# conda deactivate

# Now everything is ready to use Python. You need a sample code to start with.
# You can use this very program as a starting point.
# Try to run this program with your python environment.


# 3. Basic syntax


# You should see some text in the terminal when you execute this program:
print('Hello World! This is my first python program.')
print('Let us learn python together!')
print()

# Here we go with the basics of python.
# It is orientated to beginners that come from a scientific background.

###########################################################
# Defining variables can be done anywhere in the code
# No need to declare the type (int, float, str, list, ...)

# You can create integer variables
my_integer = 50
# Or float variables
my_float = 3.1415926

# Now you can print these variables
print('Initial values of variables:')
print(my_integer)
print(my_float)
print()

# You can change those variables anytime, even change their type without any declaration
my_integer = my_integer + 10
my_float = 'coucou !'

print('Modified values of variables:')
print(my_integer)
print(my_float)
print()

print('Now my_float is a string and not a float anymore !')

# 4. Variables and types

# Some more display options
# You can display the type of the variables
print('Display type of variables:')
print(type(my_integer))
print(type(my_float))
print()


# 5. Lists and tuples
# Lists are very useful data structures in Python. They can hold multiple values in a single variable.
# Lists are ordered, changeable, and allow duplicate values.

# Tuples are similar to lists, but they are immutable, meaning they cannot be changed after creation.

my_list = [1, 5, 2, 3, 4]
my_tuple = (10, 20, 30)

# you can print a list or a tuple
print('Display a list:')
print(my_list)
print('Display a tuple:')
print(my_tuple)
print()

# You can display the length of a list or tuple
print('Display length of a list:')
print(len(my_list))
print('Display length of a tuple:')
print(len(my_tuple))
print()

print('Different displays of a list:')
# You can also display the value of a list at a specific index
print(my_list[0])
# You can also look at a slice of a list
print(my_list[1:3])
print()
# Or loop over all the elements, one by one
for element in my_list:
    print(element)
print()

print('Display the last element of the list:')
print(my_list[-1])
print()

# You can also find the index of an element in a list
print(my_list.index(5))
print()

print('Different displays of a tuple:')
# You can also display the value of a tuple at a specific index
print(my_tuple[0])
# You can also look at a slice of a tuple
print(my_tuple[1:3])
# It is like lists, except you cannot modify them

###########################################################
# You are interested in modifying a list

print('Append 6 to the list:')
# You can also add an element to a list
my_list.append(6)
print(my_list)
print()

print('Remove 6 from the list:')
# You can also remove an element from a list
my_list.remove(6)
print(my_list)
print()

# There are many other things you can do with lists
# You can find all the methods available for a list by typing
# help(list)

# This is it for this introduction to Python.
# You can now explore more advanced topics like control structures, functions, modules, file handling,
# error handling, and useful libraries.
# All of this is pure python. Scientific related libraries will be covered in other tutorials.
# Happy coding !