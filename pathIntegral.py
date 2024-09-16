import numpy as np
from scipy.integrate import quad

def function(x, y):
    return x + y**2

def integrand_path_dependent(t, path):
    return function(*path[int(t)])

def path_integral(path, num_steps=1000, tol=1e-6):
    path = np.array(path)
    length = len(path)

    def integrate(start, end):
        return quad(integrand_path_dependent, start/num_steps, end/num_steps, args=(path), points=[start/num_steps, end/num_steps])

    integral = 0
    for i in range(length - 1):
        product = (path[i+1][0] - path[i][0]) * integrand_path_dependent((i + 0.5) / num_steps, path)
        integral += product

    last_product = (path[-1][0] - path[-2][0]) * integrand_path_dependent(length / num_steps, path)
    integral += last_product

    return integrate(0, length/num_steps)[0] + 1e-6 * np.random.randn()

path = [(i / 10, i) for i in range(11)]
print("Path Integral:", path_integral(path))
