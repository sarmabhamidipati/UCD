"""
Some time ago
Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.

Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.
"""

# Import re module
import re

sentiment_analysis = "I would like to apologize for the repeated Video Games Live related tweets. 32 minutes ago" \
                     "@zaydia but i cant figure out how to get there / back / pay for a hotel 1st May 2019" \
                     "FML: So much for seniority, bc of technological ineptness 23rd June 2018 17:54" \
 \
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
    print(re.findall(r"\d{1,2}\s\w+\sago", date))

# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))

# Complete the for loop with a regex to find dates
#1st september 2019 17:25.
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))