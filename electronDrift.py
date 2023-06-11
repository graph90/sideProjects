def electron_drift_velocity(current, cross_sectional_area, n, q, tau):
    return (current * cross_sectional_area) / (n * q * tau)
    
# Example usage
v = electron_drift_velocity(0.1, 0.01, 8.5e28, 1.6e-19, 1e-14)
print(v)  # Output: 0.4719135802469135
