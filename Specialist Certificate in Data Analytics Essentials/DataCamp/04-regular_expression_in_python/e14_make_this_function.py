"""
The variables number1, number2,string1, and list_links have already been pre-loaded.
If you want to explore the variables, you can use print() to view them in the IPython Shell.

Inside the f-string, include number1,number2 and the result of dividing number1 by number2 rounded to one decimal.

Inside the f-string, use .replace() to replace the substring https with an empty substring in string1.

Inside the f-string, get list_links length, multiply it by 100 and divide it by 120. Round the result to two decimals.
"""
number1 = 120
number2 = 7
string1 = "httpswww.datacamp.com"
list_links = ['www.news.com', 'www.google.com', 'www.yahoo.com',
              'www.bbc.com', 'www.msn.com', 'www.facebook.com', 'www.news.google.com'
              ]

# Include both variables and the result of dividing them
print(
    f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1 / number2:.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Divide the length of list by 120 rounded to two decimals
print(f"Only {(len(list_links)*100)/120:.2f}% of the posts contain links")
