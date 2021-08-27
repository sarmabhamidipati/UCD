"""
Plotting the Binomial PMF

    Using np.arange(), compute the bin edges such that the bins are centered on the integers.
    Store the resulting array in the variable bins.
    Use plt.hist() to plot the histogram of n_defaults with the normed=True and bins=bins keyword arguments.
    Show the plot.

"""
import e20_how_many_defaults_might_we_expect
import matplotlib.pyplot as plt
import numpy as np

# Compute bin edges: bins
bins = np.arange(0, max(e20_how_many_defaults_might_we_expect.n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(e20_how_many_defaults_might_we_expect.n_defaults, bins=bins)

# Label axes

_ = plt.xlabel('number of defaults')
_ = plt.ylabel('CDF')

# Show the plot
plt.show()
