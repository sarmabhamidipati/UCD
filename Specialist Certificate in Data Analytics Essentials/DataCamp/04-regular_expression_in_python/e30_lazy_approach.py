"""
Lazy Approach
The re module and the variable sentiment_analysis are already loaded in your session.

Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.

Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
"""

import re

sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget " \
                     "the name of the site (I'm crying)."

# Write a greedy regex expression to match
sentences_found_greedy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)