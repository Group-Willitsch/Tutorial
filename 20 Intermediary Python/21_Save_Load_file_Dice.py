###########################################################
#                                                         #
#             Python       Data save and load             #
#                        Tutorial                         #
#                                                         #
###########################################################
# By Adrien Poindron, 2025/11/10
#
# This is covers the steps to save and load data
#
# In this tutorial, we will simulate the throw of 2 6-sided dices
# multiple times, store the results, and save them to a file.
# We will then demonstrate how to load the data back from the file.
# This tutorial will use both native Python file handling
# and NumPy's save/load functions for demonstration.
#
# The plot of this data will be covered in another tutorial.

# Outline
# 1. Imports
# 2. Definition of the problem
# 3. Numerical experiment
# 4. Save throws in a separate file
# 5. Load data from file


# 1. Imports

# Python can use external code stored in what we call libraries or packages.
# You can install those packages using pip or conda.
# Then you need to tell the code you are using those packages by importing them.

import numpy as np # used to actually save and load data
import random # used to generate sample data
import time



### 2. Definition of the problem
# Now we will simulate multiple throws of dices

# define the number of faces of the dice
faces = 6
# define the number of dice
dices = 2

# Number of consecutive throws
throw = 100

# all throw results will be stored in result
result = []


### 3. Numerical experiment

# loop over the number of throws
for i in range(throw):
    # this loop repeats the throw of dices
    # and appends it to result
    result_tmp = sum(random.randrange(faces) + 1 for _ in range(dices))
    result.append( result_tmp )

# Print the result
print(result)
print()

# its mean and standard deviation
print('average and standard deviation of the result :')
print(f'{np.mean(result):.5f} $\pm$ {np.std(result):.5f}')
print()


### 4. Save throws in a separate file
# two strategies :
# a. native python outout
# b. numpy savez

## We will now create a file

# Retrive the date under format YYYYMMDD-hhmmss
timestr = time.strftime("%Y%m%d-%H%M%S")
# set a name for a file using timestr
filename = f'dices_{timestr}'

print(f'Saving data in file {filename}')
print()

# Now we can save the data in a file called filename

# a. Native python file open and save

# write in a file that is named filename
with open(filename+'.dat', 'w') as outfile:
    for i,j in enumerate(result):
        outfile.write(f'{i};{j}\n')

# b. using numpy savez
# nice because variables are stored in independent arrays
# and they are compressed in an archive
# each archive with an explicit name so you cannot mix them up

np.savez(filename,
                result = result,
                result_mean = np.mean(result),
                result_std = np.std(result),
                dices = dices,
                faces = faces,
                throw = throw)

# You see not only i save the data (result, result_mean and result_std)
# but also some metadata such as the faces size and number of throws

### 5. Load data from file

# If you later want to open this file in another program

# open any text file
# using numpy loadtxt function
i,a = np.loadtxt(filename+'.dat',
                skiprows = 0, usecols=(0,1),
                delimiter = ';',
                unpack=True)
print(a)
print()

# or numpy load function
# if you saved using numpy savez function
with np.load(filename+'.npz') as data:
    a = data['result']
    b = data['result_mean']
    c = data['result_std']

print(a)
print(b,c)
print()

print('Compare loaded data with original data:')
print('Mean difference:', np.abs(np.mean(result)-b))
print('Std difference:', np.abs(np.std(result)-c))
print()

# You should see that the loaded data matches the original data
# with negligible differences due to numerical precision.

# This concludes the tutorial on saving and loading data in Python.