"""
The first principal component
The first principal component of the data is the direction in which the data varies the most. In this exercise,
your job is to use PCA to find the first principal component of the length and width measurements of the grain samples,
and represent it as an arrow on the scatter plot.

The array grains gives the length and width of the grain samples. PyPlot (plt)
and PCA have already been imported for you.
Instructions
100 XP

    Make a scatter plot of the grain measurements. This has been done for you.
    Create a PCA instance called model.
    Fit the model to the grains data.
    Extract the coordinates of the mean of the data using the .mean_ attribute of model.
    Get the first principal component of model using the .components_[0,:] attribute.
    Plot the first principal component as an arrow on the scatter plot, using the plt.arrow() function.
    You have to specify the first two arguments - mean[0] and mean[1].

"""
import numpy as np
# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.decomposition import PCA

grains = np.array([[3.312, 5.763],
                   [3.333, 5.554],
                   [3.337, 5.291],
                   [3.379, 5.324],
                   [3.562, 5.658],
                   [3.312, 5.386],
                   [3.259, 5.563],
                   [3.302, 5.42],
                   [3.465, 6.053],
                   [3.505, 5.884],
                   [3.242, 5.714],
                   [3.201, 5.438],
                   [3.199, 5.439],
                   [3.156, 5.479],
                   [3.114, 5.482],
                   [3.333, 5.351],
                   [3.383, 5.119],
                   [3.514, 5.527],
                   [3.466, 5.205],
                   [3.049, 5.226],
                   [3.129, 5.658],
                   [3.168, 5.52],
                   [3.507, 5.618],
                   [2.936, 5.099],
                   [3.245, 5.789],
                   [3.421, 5.833],
                   [3.026, 5.395],
                   [2.956, 5.395],
                   [3.221, 5.541],
                   [3.065, 5.516],
                   [2.975, 5.454],
                   [3.371, 5.757],
                   [3.186, 5.717],
                   [3.15, 5.585],
                   [3.328, 5.712],
                   [3.485, 5.709],
                   [3.464, 5.826],
                   [3.683, 5.832],
                   [3.288, 5.656],
                   [3.298, 5.397],
                   [3.156, 5.348],
                   [3.158, 5.351],
                   [3.201, 5.138],
                   [3.396, 5.877],
                   [3.462, 5.579],
                   [3.155, 5.376],
                   [3.393, 5.701],
                   [3.377, 5.57],
                   [3.291, 5.545],
                   [3.258, 5.678],
                   [3.272, 5.585],
                   [3.434, 5.674],
                   [3.113, 5.715],
                   [3.199, 5.504],
                   [3.113, 5.741],
                   [3.212, 5.702],
                   [3.377, 5.388],
                   [3.412, 5.384],
                   [3.419, 5.662],
                   [3.032, 5.159],
                   [2.85, 5.008],
                   [2.879, 4.902],
                   [3.042, 5.076],
                   [3.07, 5.395],
                   [3.026, 5.262],
                   [3.119, 5.139],
                   [3.19, 5.63],
                   [3.158, 5.609],
                   [3.153, 5.569],
                   [2.882, 5.412],
                   [3.561, 6.191],
                   [3.484, 5.998],
                   [3.594, 5.978],
                   [3.93, 6.154],
                   [3.486, 6.017],
                   [3.438, 5.927],
                   [3.403, 6.064],
                   [3.814, 6.579],
                   [3.639, 6.445],
                   [3.566, 5.85],
                   [3.467, 5.875],
                   [3.857, 6.006],
                   [3.864, 6.285],
                   [3.772, 6.384],
                   [3.801, 6.366],
                   [3.651, 6.173],
                   [3.764, 6.084],
                   [3.67, 6.549],
                   [4.033, 6.573],
                   [4.032, 6.45],
                   [3.785, 6.581],
                   [3.796, 6.172],
                   [3.693, 6.272],
                   [3.86, 6.037],
                   [3.485, 6.666],
                   [3.463, 6.139],
                   [3.81, 6.341],
                   [3.552, 6.449],
                   [3.512, 6.271],
                   [3.684, 6.219],
                   [3.525, 5.718],
                   [3.694, 5.89],
                   [3.892, 6.113],
                   [3.681, 6.369],
                   [3.755, 6.248],
                   [3.786, 6.037],
                   [3.806, 6.152],
                   [3.573, 6.033],
                   [3.763, 6.675],
                   [3.674, 6.153],
                   [3.769, 6.107],
                   [3.791, 6.303],
                   [3.902, 6.183],
                   [3.737, 6.259],
                   [3.991, 6.563],
                   [3.719, 6.416],
                   [3.897, 6.051],
                   [3.815, 6.245],
                   [3.769, 6.227],
                   [3.857, 6.493],
                   [3.962, 6.315],
                   [3.563, 6.059],
                   [3.387, 5.762],
                   [3.771, 5.98],
                   [3.582, 5.363],
                   [3.869, 6.111],
                   [3.594, 6.285],
                   [3.687, 5.979],
                   [3.773, 6.513],
                   [3.69, 5.791],
                   [3.755, 5.979],
                   [3.825, 6.144],
                   [3.268, 5.884],
                   [3.395, 5.845],
                   [3.408, 5.776],
                   [3.465, 5.477],
                   [3.574, 6.145],
                   [3.231, 5.92],
                   [3.286, 5.832],
                   [3.472, 5.872],
                   [2.994, 5.472],
                   [3.073, 5.541],
                   [3.074, 5.389],
                   [2.967, 5.224],
                   [2.777, 5.314],
                   [2.687, 5.279],
                   [2.719, 5.176],
                   [2.967, 5.267],
                   [2.911, 5.386],
                   [2.648, 5.317],
                   [2.84, 5.263],
                   [2.776, 5.405],
                   [2.833, 5.408],
                   [2.693, 5.22],
                   [2.755, 5.175],
                   [2.675, 5.25],
                   [2.849, 5.053],
                   [2.745, 5.394],
                   [2.678, 5.444],
                   [2.695, 5.304],
                   [2.879, 5.451],
                   [2.81, 5.35],
                   [2.847, 5.267],
                   [2.968, 5.333],
                   [2.794, 5.011],
                   [2.941, 5.105],
                   [2.897, 5.319],
                   [2.837, 5.417],
                   [2.668, 5.176],
                   [2.715, 5.09],
                   [2.701, 5.325],
                   [2.845, 5.167],
                   [2.763, 5.088],
                   [2.763, 5.136],
                   [2.641, 5.278],
                   [2.821, 4.981],
                   [2.71, 5.186],
                   [2.642, 5.145],
                   [2.758, 5.18],
                   [2.893, 5.357],
                   [2.775, 5.09],
                   [3.017, 5.236],
                   [2.909, 5.24],
                   [2.85, 5.108],
                   [3.026, 5.495],
                   [2.683, 5.363],
                   [2.716, 5.413],
                   [2.675, 5.088],
                   [2.821, 5.089],
                   [2.787, 4.899],
                   [2.717, 5.046],
                   [2.804, 5.091],
                   [2.953, 5.132],
                   [2.63, 5.18],
                   [2.975, 5.236],
                   [3.126, 5.16],
                   [3.054, 5.224],
                   [3.128, 5.32],
                   [2.911, 5.41],
                   [3.155, 5.073],
                   [2.989, 5.219],
                   [3.135, 4.984],
                   [2.81, 5.009],
                   [3.091, 5.183],
                   [2.96, 5.204],
                   [2.981, 5.137],
                   [2.795, 5.14],
                   [3.232, 5.236],
                   [2.836, 5.175],
                   [2.974, 5.243]])
# Make a scatter plot of the untransformed points
plt.scatter(grains[:,0], grains[:,1])

# Create a PCA instance: model
model = PCA()

# Fit model to points
model.fit(grains)

# Get the mean of the grain samples: mean
mean = model.mean_

# Get the first principal component: first_pc
first_pc = model.components_[0,:]

# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)

# Keep axes on same scale
plt.axis('equal')
plt.show()