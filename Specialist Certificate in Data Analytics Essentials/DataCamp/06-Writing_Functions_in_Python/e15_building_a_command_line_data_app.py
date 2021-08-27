"""
Building a command line data app

    Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
    The name of the function the user wants to call is stored in func_name. Use the dictionary of functions,
    function_map, to call the chosen function and pass data as an argument.

"""
# Add the missing function references to the function map
function_map = {
    'mean': mean,
    'std': std,
    'minimum': minimum,
    'maximum': maximum
}

data = load_data()
print(data)


def get_user_input(function__main__=None):
    return function__main__.get_user_input


func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map['mean'](data)
function_map['std'](data)
function_map['minimum'](data)
function_map['maximum'](data)
