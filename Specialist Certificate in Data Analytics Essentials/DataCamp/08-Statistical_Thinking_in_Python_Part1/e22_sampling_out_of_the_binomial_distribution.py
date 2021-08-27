"""
Sampling out of the Binomial distribution

    Draw samples out of the Binomial distribution using np.random.binomial().
    You should use parameters n = 100 and p = 0.05, and set the size keyword argument to 10000.
    Compute the CDF using your previously-written ecdf() function.
    Plot the CDF with axis labels. T
    he x-axis here is the number of defaults out of 100 loans, while the y-axis is the CDF.
    Show the plot.

"""
import e6_computing_the_ecdf
import e20_how_many_defaults_might_we_expect
import matplotlib.pyplot as plt
import numpy as np

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n=100, p=0.05, size=10000)

# Compute CDF: x, y
x, y = e6_computing_the_ecdf.ecdf(e20_how_many_defaults_might_we_expect.n_defaults)

# Plot the CDF with axis labels
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('number of defaults')
_ = plt.ylabel('CDF')

# Show the plot
plt.show()
