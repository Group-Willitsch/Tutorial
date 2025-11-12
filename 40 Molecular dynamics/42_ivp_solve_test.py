# %% Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def state_plotter(times, states, fig_num):
    num_states = np.shape(states)[0]
    num_cols = int(np.ceil(np.sqrt(num_states)))
    num_rows = int(np.ceil(num_states / num_cols))
    plt.figure(fig_num)
    plt.clf()
    fig, ax = plt.subplots(num_rows, num_cols, num=fig_num, clear=True,
                         squeeze=False)
    for n in range(num_states):
        row = n // num_cols
        col = n % num_cols
        ax[row][col].plot(times, states[n], 'k.:')
        ax[row][col].set(xlabel='Time',
                         ylabel='$y_{:0.0f}(t)$'.format(n),
                         title='$y_{:0.0f}(t)$ vs. Time'.format(n))
        
    for n in range(num_states, num_rows * num_cols):
        fig.delaxes(ax[n // num_cols][n % num_cols])

    fig.tight_layout()

    return fig, ax


# %% Define derivative function
def f(t, y):
    # print(t)
    dydt = [y[1], y[2], 0]
    return dydt

# %% Define time spans, initial values, and constants
tspan = np.linspace(0, 10, 100)
yinit = [0, 1, -9.8066]

# %% Solve differential equation
sol = solve_ivp(lambda t, y: f(t, y), 
                [tspan[0], tspan[-1]],
                yinit,
                method = 'RK23',
                t_eval=tspan,
                rtol = 1e-5)

print(sol)
print(sol.y)
print(sol.y[0])
print(np.shape(sol.y))

# %% Plot states
state_plotter(sol.t, sol.y, 1)

# %%

# %% Define derivative function
def f(t, y, potato):
    # print(t)
    dydt = [y[1], -y[0] * (2*np.pi)**2]
    return dydt

# %% Define time spans, initial values, and constants
tspan = np.linspace(0, 5, 200)
yinit = [5,0]

# %% Solve differential equation
sol = solve_ivp(lambda t, y: f(t,y,tspan), 
                [tspan[0], tspan[-1]],
                yinit,
                method = 'RK45',
                t_eval=tspan,
                rtol = 1e-5)

print(sol)
print(sol.y)
print(sol.y[0])
print(np.shape(sol.y))

# %% Plot states
state_plotter(sol.t, sol.y, 1)
# %%

print(np.shape(sol.y))
print(sol)

# %%
