"""
Calling by its name

The variable courses containing one tool and one field name has been saved. You can use print(courses) to view
the variable in the IPython Shell.

Instructions 1/2
    Create a dictionary assigning the first and second element appearing in the list courses to the
    keys "field" and "tool" respectively.

    Complete the placeholders accessing inside to the elements linked with the keys field and tool
    in the dictionary data.
    Print out the resulting message using the .format() method,
    passing the plan dictionary to replace the data placeholders.

"""
# Create a dictionary
courses = ['artificial intelligence', 'neural networks']
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }
print(plan)

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))
