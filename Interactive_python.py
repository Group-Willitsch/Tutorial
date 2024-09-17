###########################################################
#                                                         #
#                   Interactive python                    #
#                        Tutorial                         #
#                                                         #
###########################################################
# By Adrien Poindron, 2024/09/17
#
# This is a tutorial on how to use interactive python
# in your programming environment. (Visual Studio,
# VScodium, Spyder ...)
#
# Open your new file, tuto.py. Note this is the extension
# for python and note the extension for interactive
# notebook (.ipynb) such as for jupyter notebook.
#
# Write your program (See below). Execute the whole
# program or each of its cell. A cell is delimited
# by a set of #%% on top and to the bottom of it.
#
# When executing the cell its outcome shows up in the
# right part of the programming environment (Spyder style).
#
# Start by running the cell below and carry on by reading the comments.
# To run the cell, place ce caret in the cell you want to execute
# by clinking anywhere in the cell.
#
# Then press ctrl+enter to only run the cell
# or press shift+enter to run the cell and move to the next

# %%
# Some imports here

import numpy as np
import matplotlib.pyplot as plt

#%% [markdown]

# An example of markdown cell
# That is used to explain the code with plain text, equations, links ...
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
# %%

