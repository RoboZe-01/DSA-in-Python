# Reverse the string using for loop 

# ----- Basic Version ------


def reversed_string(input_string):
    reverserd_str = " "
    for char in input_string : 
        reverserd_str=char+reverserd_str
    return reverserd_str
print(reversed_string("Python"))

    
# ----- Professional Version -----

