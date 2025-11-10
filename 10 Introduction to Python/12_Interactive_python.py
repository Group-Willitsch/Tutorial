###########################################################
#                                                         #
#                   Interactive python                    #
#                        Tutorial                         #
#                                                         #
###########################################################
# By Adrien Poindron, 2024/09/17
#
# This is a tutorial on how to use interactive python
# in your programming environment. (Visual Studio Code,
# VScodium, Spyder ...)

# Open this file in your editor.
#
# In interactive python, you can write code in cells.
# Cells are blocks of code that can be executed independently.
# They are identified by special markers (#%%).
#
# Cells are useful to organize your code and
# to test small parts of your code without running
# the whole program.
# But this is still a python program (.py) so you can
# run it as a whole if you want.


# Start by running the cell below and carry on by reading the comments.
# To run the cell, place the caret in the cell you want to execute.
#
# Then press ctrl+enter to only run the cell
# or press shift+enter to run the cell and move to the next

# %%
# Some imports here

import numpy as np
import matplotlib.pyplot as plt

#%%

my_interesting_variable = 42
print('The answer to the ultimate question of life, the universe and everything is', my_interesting_variable)
print()

#%% [markdown]

# An example of markdown cell that is used to explain
# a program with plain text, equations, links ...
#
# Let us consider a 1D harmonic oscillator
#
# \begin{equation}
# \hat{H} = \frac{1}{2}(\hat{p}^2+\omega^2\hat{q}^2) = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right) \approx \frac{1}{2}(\hat{a}\hat{a}^\dagger)
# \end{equation}
# The last approximation is used in https://qutip.org/docs/latest/guide/guide-steady.html#example-harmonic-oscillator-in-thermal-bath
#
# Then we solve
#
# \begin{equation}
# \frac{\mathrm{d}\hat{\rho}}{\mathrm{d}t} = -\frac{i}{\hbar}[\hat{\mathcal{H}}_{tot},\hat{\rho}] + \hat{\mathcal{L}}\hat{\rho}
# \end{equation}
#
# using `mesolve` (see https://qutip.org/docs/latest/guide/dynamics/dynamics-master.html and https://qutip.org/docs/latest/guide/dynamics/dynamics-time.html#function-based-time-dependence).

# %%
# A plot

x = np.linspace(0,1000)
y = np.linspace(0,1000)

plt.plot(x,y)
plt.grid()
plt.title('A simple plot')
plt.xlabel('x axis')
plt.ylabel('y axis')

# %%

