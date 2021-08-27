"""
Comparing percentiles to ECDF
The percentile variables from the previous exercise are available in the workspace as ptiles_vers and percentiles.

Note that to ensure the Y-axis of the ECDF plot remains between 0 and 1, you will need to rescale
the percentiles array accordingly - in this case, dividing it by 100.

    Plot the percentiles as red diamonds on the ECDF.
    Pass the x and y co-ordinates - ptiles_vers and percentiles/100 - as positional arguments
    and specify the marker='D', color='red' and linestyle='none' keyword arguments.
    The argument for the y-axis - percentiles/100 has been specified for you.
    Display the plot.

"""
import numpy as np
import matplotlib.pyplot as plt


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y


versicolor_petal_length = np.array([4.7, 4.5, 4.9, 4., 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4.,
                                    4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4., 4.9, 4.7, 4.3, 4.4,
                                    4.8, 5., 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
                                    4., 4.4, 4.6, 4., 3.3, 4.2, 4.2, 4.2, 4.3, 3., 4.1])

# Specify array of percentiles: percentiles
percentiles = [2.5, 25, 50, 75, 97.5]
# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length, percentiles)
#print(ptiles_vers)

x_vers, y_vers = ecdf(versicolor_petal_length)

# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles / 100, marker='D', color='red', linestyle='none')

# Show the plot
plt.show()
