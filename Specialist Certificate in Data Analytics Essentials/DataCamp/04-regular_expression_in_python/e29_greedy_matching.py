"""
Greedy matching
The re module as well as the variable sentiment_analysis are already loaded in your session.
 You can use print(sentiment_analysis) to view it in the IPython Shell.

 Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.
 Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.
"""
import re

sentiment_analysis = "Was intending to finish editing my 536-page novel manuscript tonight, but that will probably " \
                     "not happen. And only 12 pages are left "
print(sentiment_analysis)
# Write a lazy regex expression
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Write a greedy regex expression
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)
