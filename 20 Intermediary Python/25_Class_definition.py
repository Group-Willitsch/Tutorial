###########################################################
#                                                         #
#              Python       Class definition              #
#                        Tutorial                         #
#                                                         #
###########################################################
# By Adrien Poindron, 2025/11/10
#
# This is covers the steps to define a class in Python.
#
# In this tutorial, we will simulate the molecular dynamics
# of two charged particles in a harmonic potential.
# We will define a class to encapsulate the properties
# and methods related to the simulation.
# The class will include methods to initialize the simulation,
# update positions and velocities using the velocity-Verlet algorithm,
# run the simulation, and save the results to files.
# We will also plot the trajectories of the particles.

# Imports

import numpy as np
import math

import matplotlib.pyplot as plt

import time

# Physical variables defined in calcium_constants.py
# sys.path.append("")
from calcium_constants import *

# Definition of the class
#
# A class is a structure, it does not do anything by itself.
# It is a way to group variables and functions together.
# You can then create instances of the class
# that will have their own variables and can use the functions
# defined in the class.


# This is a class to simulate the dynamics of two charged particles in a harmonic potential
# 1-dimensional problem along z axis
# Initial value problem solver with velocity-Verlet algorithm

class HO:

    def __init__(self,
                mass=m_Ca,
                omega_z=2*np.pi*1e6,
                i_simu=100,
                n_dt=100):
        
        """ Initialize the class with physical and numerical parameters """

        print('Initializing the HO class with parameters:')
        print(f'mass: {mass}, omega_z: {omega_z}, i_simu: {i_simu}, n_dt: {n_dt}.\n')

        self.mass = mass  # mass of one ion
        self.omega_z = omega_z  # axial trapping frequency
        self.i_simu = i_simu  # number of periods to simulate
        
        self.n_dt = n_dt  # number of time steps in one period
        self.dt = 2*np.pi/(omega_z*self.n_dt)  # time step

        # variables for the dynamics
        # initial definition to 0
        self.a = np.zeros((2,i_simu*n_dt))
        self.v = np.zeros((2,i_simu*n_dt))
        self.r = np.zeros((2,i_simu*n_dt))

        print(i_simu*n_dt)

        # initial conditions for positions
        self.r[0,0] = 1e-5  # initial position ion 1
        self.r[1,0] = -1e-5*0 # -1e-5  # initial position ion 2
        # initial conditions for accelerations
        self.a[0,0] = self.a_potential(self.r[0,0]) + self.a_Coulomb(self.r[0,0],self.r[1,0])
        self.a[1,0] = self.a_potential(self.r[1,0]) + self.a_Coulomb(self.r[1,0],self.r[0,0])

        # actual time of the simulation
        # will be updated at each time step
        self.t_act = 0

    def a_potential(self, r):
        """ Harmonic potential acceleration """
        return - self.omega_z**2 * r
    
    def a_Coulomb(self, r0, r1):
        """ Coulomb interaction acceleration """
        r01 = r0 - r1
        return Coul_factor*C_e**2/self.mass * np.sign(r01) / np.abs(r01)**2

    def update_positions(self):
        """ Update positions with velocity-Verlet algorithm """
        self.r[0,self.i_act + 1] = self.r[0,self.i_act] + self.v[0,self.i_act]*self.dt + 0.5*self.a[0,self.i_act]*self.dt**2
        self.r[1,self.i_act + 1] = self.r[1,self.i_act] + self.v[1,self.i_act]*self.dt + 0.5*self.a[1,self.i_act]*self.dt**2
    
    def update_accelerations(self):
        """ Update accelerations with velocity-Verlet algorithm """
        self.a[0,self.i_act + 1] = self.a_potential(self.r[0,self.i_act + 1]) + self.a_Coulomb(self.r[0,self.i_act + 1],self.r[1,self.i_act + 1])
        self.a[1,self.i_act + 1] = self.a_potential(self.r[1,self.i_act + 1]) + self.a_Coulomb(self.r[1,self.i_act + 1],self.r[0,self.i_act + 1])
        print(self.a_potential(self.r[0,self.i_act + 1]))
        print(self.a_Coulomb(self.r[0,self.i_act + 1],self.r[1,self.i_act + 1]))

    def update_velocities(self):
        """ Update velocities with velocity-Verlet algorithm """
        self.v[0,self.i_act + 1] = self.v[0,self.i_act] + 0.5*(self.a[0,self.i_act] + self.a[0,self.i_act + 1])*self.dt
        self.v[1,self.i_act + 1] = self.v[1,self.i_act] + 0.5*(self.a[1,self.i_act] + self.a[1,self.i_act + 1])*self.dt
        
    def run_molecular_dynamics(self, i_simu):
        """ Run the molecular dynamics simulation
        This is the actual function you call outside of the class to run the simulation.
        """

        print('Running molecular dynamics simulation...\n')

        start_time = time.time()

        for i, j in enumerate(range(0, i_simu*self.n_dt-1)):
            self.i_act = i # current time step
            self.update_positions()
            self.update_accelerations()
            self.update_velocities()
            self.t_act += self.dt

        print('Molecular dynamics simulation completed.')
        print('Total number of time steps:', i_simu*self.n_dt, i, j)
        print('Final time:', self.t_act*1e6, 'µs.')

        end_time = time.time()
        print(f'Simulation completed in {end_time - start_time:.5f} seconds.\n')
        
        filename = f'HO_dynamics_ions_mass_{self.mass}_omega_z_{self.omega_z}_i_simu_{self.i_simu}_n_dt_{self.n_dt}' # _{datetime.now().strftime("%Y%m%d_%H%M%S")}

        self.save_dynamics(filename)
        self.save_metadata(filename)
        self.plot_trajectories(filename)
        self.plot_energies(filename)
        self.plot_forces(filename)

        plt.show()


    def plot_trajectories(self,filename):
        """ Plot the trajectories of the ions """

        print('Plotting the trajectories of the ions...\n')

        time_array = np.linspace(0, self.i_simu*2*np.pi/self.omega_z-self.dt, i_simu*n_dt)*1e6

        fig, ax = plt.subplots(3,1, figsize=(10,8), sharex=True)

        ax[0].plot(time_array, self.r[0,:]*1e6, ls='', marker='.', label='Ion 1')
        ax[0].plot(time_array, self.r[1,:]*1e6, ls='', marker='.', label='Ion 2')
        # ax[0].set_xlabel('time (µs)')
        ax[0].set_ylabel('position (µm)')

        ax[1].plot(time_array, self.v[0,:], ls='', marker='.', label='Ion 1')
        ax[1].plot(time_array, self.v[1,:], ls='', marker='.', label='Ion 2')
        # ax[1].set_xlabel('time (µs)')
        ax[1].set_ylabel('velocity (m/s)')

        ax[2].plot(time_array, self.a[0,:], ls='', marker='.', label='Ion 1')
        ax[2].plot(time_array, self.a[1,:], ls='', marker='.', label='Ion 2')
        # ax[2].plot(time_array, self.a[0,:] + self.a[1,:], ls='', marker='.', label='Ion 1+2')
        ax[2].set_xlabel('time (µs)')
        ax[2].set_ylabel('acceleration (m/s$^2$)')

        # plt.title('Trajectories of two ions in a harmonic potential')
        ax[0].legend()
        ax[0].grid()
        ax[1].grid()
        ax[2].grid()

        plt.tight_layout()

        plt.savefig(filename+'_HO_energies.png', dpi=300)

    def plot_energies(self,filename):
        """ Plot the energies of the ions """

        print('Plotting the energies of the ions...\n')

        time_array = np.linspace(0, self.i_simu*2*np.pi/self.omega_z-self.dt, i_simu*n_dt)*1e6

        fig, ax = plt.subplots(4,1, figsize=(10,8), sharex=True)

        ax[0].plot(time_array, 0.5*self.mass*self.omega_z**2*self.r[0,:]**2, ls='', marker='.', label='Ion 1')
        ax[0].plot(time_array, 0.5*self.mass*self.omega_z**2*self.r[1,:]**2, ls='', marker='.', label='Ion 2')
        # ax[0].set_xlabel('time (µs)')
        ax[0].set_ylabel('potential energy (J)')

        ax[1].plot(time_array, 0.5*Coul_factor*C_e**2/np.abs(self.r[0,:]-self.r[1,:]), ls='', marker='.', label='Ion 1')
        ax[1].plot(time_array, 0.5*Coul_factor*C_e**2/np.abs(self.r[1,:]-self.r[0,:]), ls='', marker='.', label='Ion 2')
        # ax[1].set_xlabel('time (µs)')
        ax[1].set_ylabel('coulomb energy (J)')

        ax[2].plot(time_array, 0.5*self.mass*self.v[0,:]**2, ls='', marker='.', label='Ion 1')
        ax[2].plot(time_array, 0.5*self.mass*self.v[1,:]**2, ls='', marker='.', label='Ion 2')
        # ax[0].set_xlabel('time (µs)')
        ax[2].set_ylabel('kinetic energy (J)')

        ax[3].plot(time_array, 0.5*self.mass*self.omega_z**2*(self.r[0,:]**2 + self.r[1,:]**2),
                    ls='', marker='.',
                    color='C3', label='Potential energy')
        ax[3].plot(time_array, 0.5*Coul_factor*C_e**2*(1/np.abs(self.r[0,:]-self.r[1,:])+1/np.abs(self.r[1,:]-self.r[0,:])),
                    ls='', marker='.',
                    color='C4', label='Coulomb energy')
        ax[3].plot(time_array, 0.5*self.mass*(self.v[0,:]**2 + self.v[1,:]**2),
                    ls='', marker='.',
                    color='C5', label='Kinetic energy')
        ax[3].plot(time_array, 0.5*self.mass*self.omega_z**2*(self.r[0,:]**2 + self.r[1,:]**2)\
                                + 0.5*Coul_factor*C_e**2*(1/np.abs(self.r[0,:]-self.r[1,:])+1/np.abs(self.r[1,:]-self.r[0,:]))\
                                + 0.5*self.mass*(self.v[0,:]**2 + self.v[1,:]**2),
                    ls='', marker='.',
                    color='C6', label='Mechanical energy')
        ax[3].set_xlabel('time (µs)')
        ax[3].set_ylabel('acceleration (m/s$^2$)')

        # plt.title('Trajectories of two ions in a harmonic potential')
        ax[0].legend()
        ax[3].legend(title='Total energies')
        ax[0].grid()
        ax[1].grid()
        ax[2].grid()
        ax[3].grid()

        plt.tight_layout()

        plt.savefig(filename+'_HO_energies.png', dpi=300)

    def plot_forces(self,filename):
        """ Plot the forces of the ions """

        print('Plotting the accelerations of the ions...\n')

        time_array = np.linspace(0, self.i_simu*2*np.pi/self.omega_z-self.dt, i_simu*n_dt)*1e6

        fig, ax = plt.subplots(2,1, figsize=(10,8), sharex=True)

        ax[0].plot(time_array, self.a_potential(self.r[0,:]), ls='', marker='.', label='Ion 1')
        ax[0].plot(time_array, self.a_potential(self.r[1,:]), ls='', marker='.', label='Ion 2')
        # ax[0].set_xlabel('time (µs)')
        ax[0].set_ylabel('potential acceleration (m/s$^2$)')

        ax[1].plot(time_array, self.a_Coulomb(self.r[0,:],self.r[1,:]), ls='', marker='.', label='Ion 1')
        ax[1].plot(time_array, self.a_Coulomb(self.r[1,:],self.r[0,:]), ls='', marker='.', label='Ion 2')
        # ax[1].set_xlabel('time (µs)')
        ax[1].set_ylabel('Coulomb acceleration (m/s$^2$)')

        # plt.title('Trajectories of two ions in a harmonic potential')
        ax[0].legend()
        ax[1].legend()
        ax[0].grid()
        ax[1].grid()

        plt.tight_layout()

        plt.savefig(filename+'_HO_accelerations.png', dpi=300)

    def save_dynamics(self, filename):
        """ Save the dynamics to a file """
        print(f'Saving dynamics to file {filename}_dynamics.npz\n')
        np.savez(filename+'_dynamics.npz',
                r=self.r,
                v=self.v,
                a=self.a)
        
    def save_metadata(self, filename):
        """ Save the metadata to a file """
        print(f'Saving metadata to file {filename}_metadata.txt\n')
        with open(filename+'_metadata.txt', 'w') as f:
            f.write(f'mass: {self.mass}\n')
            f.write(f'omega_z: {self.omega_z}\n')
            f.write(f'i_simu: {self.i_simu}\n')
            f.write(f'n_dt: {self.n_dt}\n')
            f.write(f'dt: {self.dt}\n')


# M A I N  P R O G R A M #

# Definition of the main parameters (physical and numerical)

mass = m_Ca  # mass of one ion
omega_z = 2*np.pi*1e6  # axial trapping frequency
i_simu = 20  # number of periods to simulate
n_dt = 500  # number of time steps in one period


# Create an instance of the HO class
simulation = HO(mass, omega_z, i_simu, n_dt)

# Run the molecular dynamics simulation
simulation.run_molecular_dynamics(i_simu)

# simulation is an instance of the class, we can then access its variables and methods.
# We want to call the run_molecular_dynamics method to run the simulation.
# And we can call any other method of the class. For example, we can access the positions of the ions
# positions_ion1 = simulation.r[0,:]
# positions_ion2 = simulation.r[1,:]
#
# Classes are convenient to group variables and functions together.
# They are particularly useful when the number of variables and functions is large.
# They also allow to create multiple instances of the same structure with different parameters.
# For example, we could create another instance of the HO class with different parameters
# simulation2 = HO(mass2, omega_z2, i_simu2, n_dt2)
# and run another simulation with different parameters, with minimal changes to the code.
# Complex molecular dynamics programs can be hundreds of lines long, classes help keeping the code organized.

# End of the program