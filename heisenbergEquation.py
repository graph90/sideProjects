import numpy as np
import matplotlib.pyplot as plt
import math
def heisenbergEquation():
    A = float(input('Enter the operator: '))
    H = float(input('Enter the Hamiltonian: '))
    t = float(input('Enter the time: '))
    i = float(input('Enter the imaginary unit: '))
    hbar = float(input('Enter the Planck constant: '))
    heisenbergEquation = np.gradient(A) + (1/hbar)*np.cross(H, A)
    print('Heisenberg equation: ', heisenbergEquation)
heisenbergEquation()
