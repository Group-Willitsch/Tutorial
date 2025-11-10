import numpy as np
import math

from scipy.integrate import solve_ivp
from scipy.interpolate import approximate_taylor_polynomial

import os
import sys
sys.path.append("../../Functions")
from calcium_constants import *

import time
from datetime import datetime

class DDDAO_3:
    '''
        Class to represent a 1D Doubly-Driven and Damped Anharmonic Oscillator (DDDAO).
        Uses solve_ivp from scipy module to solve the ODE. RK45 method is well suited.
        The drives are electric tickle and NW.
        This class is used for experiments where the drive frequency or phase is sweeped.
        It requires a lot of data to dissipate the transients.
        The idea is to save only a small part of the variables to limit the memory usage.

        Based on
        N. Akerman, S. Kotler, Y. Glickman, Y. Dallal, A. Keselman, and R. Ozeri.
        Single-ion nonlinear mechanical oscillator, PRA 82 (2010).
        https://journals.aps.org/pra/abstract/10.1103/PhysRevA.82.061402.
    '''

    def __init__(self,
                V_tkl = 0.025, V_nw = 1, V_piezo = 1,
                omega_z = 422500*2*np.pi, omega_drive = 422500*2*np.pi,
                phi_tkl = 0, phi_nw = 0,                
                B = -4e19,
                cooling_rate = 0, nl_damping_rate = 0,
                n_dt = 2000,
                i_init = 2500,i_drive = 5000, i_freq_sweep = 5000, i_smooth_sweep = 10,
                solve_ivp_method = 'RK45',
                sweep_length = 21,
                add_string = '100'):

    # def __init__(self,*args,**kwargs):
    #     for arg in args:
    #         print(arg)
    #         print("-" * 40)
    #     for kw in kwargs:
    #         print(kw, ":", kwargs[kw])

        self.arguments = locals()
        print(self.arguments)
        for i,keys in enumerate(self.arguments):
            # arguments[keys] = str(arguments[keys]).lower()
            print(f'{i:02d}  {keys:17s} {self.arguments[keys]}')

    def update_parameters(self):
        self.sweep_length = self.arguments['sweep_length']
        print(self.sweep_length)

        for i,j in enumerate(self.arguments):
            print(f'Eval. {self.arguments[j]} now')
            if isinstance(self.arguments[j],(list,tuple,np.ndarray)) == True:
                print('list')
                print(len(self.arguments[j]))
                if len(self.arguments[j]) != int(self.sweep_length):
                    print(f'{i:02d}th arg. = {j} = has wrong length {len(self.arguments[j])} rather than {self.sweep_length} !')
            elif isinstance(self.arguments[j],(str)) == True:
                print('string')
            elif isinstance(self.arguments[j],(int,float,complex)) == True:
                print('scalar')
                self.arguments[j] = [self.arguments[j]]*self.sweep_length


        for i,keys in enumerate(self.arguments):
            # arguments[keys] = str(arguments[keys]).lower()
            print(f'{i:02d}  {keys:17s} {self.arguments[keys]}')

        print(self.arguments['V_tkl'][0])

omega_z = np.linspace(400,500,23)*2*np.pi

simulation = DDDAO_3(omega_z=omega_z)
simulation.update_parameters()