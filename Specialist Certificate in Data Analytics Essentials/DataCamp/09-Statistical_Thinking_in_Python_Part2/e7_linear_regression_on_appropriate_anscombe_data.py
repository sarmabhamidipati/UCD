"""
Linear regression on appropriate Anscombe data

Compute the parameters for the slope and intercept using np.polyfit().
The Anscombe data are stored in the arrays x and y. Print the slope a and intercept b.
Generate theoretical
and data from the linear regression. Your array, which you can create with np.array(), should consist of 3 and 15.
To generate the data, multiply the slope by x_theor and add the intercept.
Plot the Anscombe data as a scatter plot and then plot the theoretical line.
Remember to include the marker='.' and linestyle='none' keyword arguments in addition to x and y
when to plot the Anscombe data as a scatter plot. You do not need these arguments when plotting the theoretical line.
Hit 'Submit Answer' to see the plot!
"""
import numpy as np
import matplotlib.pyplot as plt

# Perform linear regression: a, b
x = np.array([10., 8., 13., 9., 11., 14., 6., 4., 12., 7., 5.])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

a, b = np.polyfit(x, y, 1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.plot(x_theor, y_theor, marker='.', linestyle='none')

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
