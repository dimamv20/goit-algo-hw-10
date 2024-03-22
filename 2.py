import numpy as np

def f(x):
    return x ** 2

a = 0
b = 2

num_points = 100000

x_values = np.random.uniform(a, b, num_points)
y_values = np.random.uniform(0, f(b), num_points)  

points_under_curve = sum(1 for x, y in zip(x_values, y_values) if y <= f(x))

rectangle_area = (b - a) * f(b) 
integral_approximation = rectangle_area * (points_under_curve / num_points)

print("Monte Carlo method:", integral_approximation)
