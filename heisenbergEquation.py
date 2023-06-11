import numpy as np
import matplotlib.pyplot as plt
import math
def heisenbergEquation():

    A = float(raw_input('Enter the operator: '))
    # Define the Hamiltonian
    H = float(raw_input('Enter the Hamiltonian: '))
    # Define the time
    t = float(raw_input('Enter the time: '))
    # Define the imaginary unit
    i = float(raw_input('Enter the imaginary unit: '))
    # Define the Planck constant
    hbar = float(raw_input('Enter the Planck constant: '))
    # Calculate the Heisenberg equation
    heisenbergEquation = np.gradient(A) + (1/hbar)*np.cross(H, A)
    # Print the Heisenberg equation
    print ('Heisenberg equation: ', heisenbergEquation)
heisenbergEquation()