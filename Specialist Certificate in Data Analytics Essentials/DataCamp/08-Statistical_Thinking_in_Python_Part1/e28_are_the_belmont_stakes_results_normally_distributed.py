"""
Are the Belmont Stakes results Normally distributed?

    Compute mean and standard deviation of Belmont winners' times with the two outliers removed.
    The NumPy array belmont_no_outliers has these data.
    Take 10,000 samples out of a normal distribution with this mean and standard deviation using np.random.normal().
    Compute the CDF of the theoretical samples and the ECDF of the Belmont winners' data,
    assigning the results to x_theor, y_theor and x, y, respectively.
    Hit submit to plot the CDF of your samples with the ECDF, label your axes and show the plot.

"""
import e26_the_normal_pdf
import e6_computing_the_ecdf
import  matplotlib.pyplot as plt

import numpy as np

belmont_no_outliers = np.array([148.51, 146.65, 148.52, 150.7, 150.42, 150.88, 151.57, 147.54,
                                149.65, 148.74, 147.86, 148.75, 147.5, 148.26, 149.71, 146.56,
                                151.19, 147.88, 149.16, 148.82, 148.96, 152.02, 146.82, 149.97,
                                146.13, 148.1, 147.2, 146., 146.4, 148.2, 149.8, 147.,
                                147.2, 147.8, 148.2, 149., 149.8, 148.6, 146.8, 149.6,
                                149., 148.2, 149.2, 148., 150.4, 148.8, 147.2, 148.8,
                                149.6, 148.4, 148.4, 150.2, 148.8, 149.2, 149.2, 148.4,
                                150.2, 146.6, 149.8, 149., 150.8, 148.6, 150.2, 149.,
                                148.6, 150.2, 148.2, 149.4, 150.8, 150.2, 152.2, 148.2,
                                149.2, 151., 149.6, 149.6, 149.4, 148.6, 150., 150.6,
                                149.2, 152.6, 152.8, 149.6, 151.6, 152.8, 153.2, 152.4,
                                152.2])

# Compute mean and standard deviation: mu, sigma

mu = np.mean(belmont_no_outliers)
sigma = np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples = np.random.normal(mu, sigma, size=10000)

# Get the CDF of the samples and of the data
x_theor, y_theor = e6_computing_the_ecdf.ecdf(e26_the_normal_pdf.samples_std1)
x, y = e6_computing_the_ecdf.ecdf(belmont_no_outliers)



# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()
