import math
import matplotlib.pyplot as plt
import numpy as np
def poissonDistribution(r, k):
    return math.exp(-r) * math.pow(r, k) / math.factorial(k)
def main():
    x = np.arange(0, 10, 0.01)
    y = []
    for i in x:
        y.append(poissonDistribution(i, 5))
    plt.plot(x, y)
    plt.show()
if __name__ == '__main__':
    main()
