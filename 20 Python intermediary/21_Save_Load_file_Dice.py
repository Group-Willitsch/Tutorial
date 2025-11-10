import numpy as np
import random
import time

### Define problem

# define size of the dice
dice = 20

# Number of consecutive throws
# Repeating
throw = 10
# all throw results will be stored in result
result = []

### Numerical experiment

# many throws
# This loop is executed a number of time
# equal to throw
for i in range(throw):
    # this loop select a random number between 1 and dice
    # and append it to result
    result_tmp = random.randrange(dice) + 1
    result.append( result_tmp )

# Print the result
print(result)
# its mean and standard deviation
print(np.mean(result),np.std(result))

### Save throws in a separate file
# two strategies :
# native python outout
# numpy save

## We will now create a file and write the result

# Retrive the date under format YYYYMMDD-hhmmss
timestr = time.strftime("%Y%m%d-%H%M%S")
# set a name for a file using timestr
filename = f'dice_{timestr}'

# Native python file open and save
# write in a file that is named filename
with open(filename+'.dat', 'w') as outfile:
    for i,j in enumerate(result):
        outfile.write(f'{i};{j}\n')

# using numpy savez
# nice because variables are stored in independent arrays
# and they are compressed in an archive

np.savez(filename,
                result = result,
                result_mean = np.mean(result),
                result_std = np.std(result))

# If you later want to open this file in another program

# open any text file
# using numpy loadtxt function
i,a = np.loadtxt(filename+'.dat',
                skiprows = 0, usecols=(0,1),
                delimiter = ';',
                unpack=True)
print(a)

# or numpy load function
# if you saved using numpy savez function
with np.load(filename+'.npz') as data:
    a = data['result']
    b = data['result_mean']
    c = data['result_std']

print(a)
print(b,c)