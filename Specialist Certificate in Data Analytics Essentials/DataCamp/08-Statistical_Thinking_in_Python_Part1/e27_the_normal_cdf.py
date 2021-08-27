"""
The Normal CDF
Using the samples you generated in the last exercise (in your namespace as samples_std1, samples_std3,
and samples_std10), generate and plot the CDFs.


    Use your ecdf() function to generate x and y values for CDFs: x_std1, y_std1, x_std3, y_std3 and x_std10, y_std10,
    respectively.
    Plot all three CDFs as dots (do not forget the marker and linestyle keyword arguments!).
    Hit submit to make a legend, showing which standard deviations you used, and to show your plot.
    There is no need to label the axes because we have not defined what is being described by the Normal distribution;
    we are just looking at shapes of CDFs.

"""
import e26_the_normal_pdf
import e6_computing_the_ecdf
import  matplotlib.pyplot as plt

# Generate CDFs

x_std1, y_std1 = e6_computing_the_ecdf.ecdf(e26_the_normal_pdf.samples_std1)
x_std3, y_std3 = e6_computing_the_ecdf.ecdf(e26_the_normal_pdf.samples_std3)
x_std10, y_std10 = e6_computing_the_ecdf.ecdf(e26_the_normal_pdf.samples_std10)



# Plot CDFs
# Plot CDFs
_ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
_ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')
_ = plt.plot(x_std10, y_std10, marker='.', linestyle='none')



# Make a legend and show the plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'), loc='lower right')
plt.show()
