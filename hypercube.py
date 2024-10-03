import numpy as np
import itertools
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_hypercube_vertices(n):
    return list(itertools.product([0, 1], repeat=n))

def project_to_3d(vertices, n):
    if n > 3:
        projected_vertices = [vertex[:3] for vertex in vertices]
    else:
        projected_vertices = vertices
    return projected_vertices

def plot_hypercube_3d(vertices, filename="hypercube.png"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs, ys, zs = zip(*vertices)
    ax.scatter(xs, ys, zs)

    for i, v1 in enumerate(vertices):
        for v2 in vertices[i+1:]:
            if np.sum(np.abs(np.array(v1) - np.array(v2))) == 1:
                ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], 'b')

    plt.savefig(filename)
    print(f"Plot saved as {filename}")

n = 4
vertices = generate_hypercube_vertices(n)

projected_vertices = project_to_3d(vertices, n)

plot_hypercube_3d(projected_vertices)
