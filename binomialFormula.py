import math
import matplotlib.pyplot as plt
import numpy as np
def binomialFormula(n, p, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x)) * math.pow(p, x) * math.pow(1 - p, n - x)
def main():
    x = np.arange(0, 10, 0.01)
    y = []
    for i in x:
        y.append(binomialFormula(10, 0.5, i))
    plt.plot(x, y)
    plt.show()
main()