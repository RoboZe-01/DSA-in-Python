# # 
# Check if all elements in a list are Unique
# Check if All Elements in a List are Unique

# You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

# Parameters:

# lst (List of integers): The list of integers to check for uniqueness.

# Returns:

# A boolean value True if all elements in the list are unique, False otherwise.

# Example:

# Input: lst = [1, 2, 3, 4, 5]
# Output: True

# Input: lst = [1, 2, 3, 3, 4, 5]
# Output: False



                                  ### Solution ### 


## Method 1 : Using Set conversion 

def unique_or_not(lst):
    order = set(lst)
    order = list(order)
    if lst != order:
        print("False")
    else:
        print("True")
    
lst = [1,2,3,4,5,6]
unique_or_not(lst)


# Method 2 : Using opttimised set conversion 

def unique_or_not_optimized(lst):
    if len(lst)!= len(set(lst)):
        return False
    else:
        return True
    


print(f'Finding unique or not unsing oplimised method : {unique_or_not_optimized(lst)}')    


