"""
Distribution of no-hitters and cycles

    Use your successive_poisson() function to draw 100,000 out of the distribution of waiting times
    for observing a no-hitter and a hitting of the cycle.
    Plot the PDF of the waiting times using the step histogram technique of a previous exercise.
    Don't forget the necessary keyword arguments. You should use bins=100, normed=True, and histtype='step'.
    Label the axes.
    Show your plot.

"""
import e31_if_you_have_a_story_you_can_simulate_it
import matplotlib.pyplot as plt

# Draw samples of waiting times: waiting_times
waiting_times = e31_if_you_have_a_story_you_can_simulate_it.successive_poisson(764,715,100000)

# Make the histogram

_= plt.hist(waiting_times, histtype='step', bins=100)

# Label axes
_ = plt.xlabel('time (days)')
_ = plt.ylabel('CDF')


# Show the plot
plt.show()
