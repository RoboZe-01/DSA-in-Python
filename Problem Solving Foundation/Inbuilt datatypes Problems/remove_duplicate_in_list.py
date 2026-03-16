# Remove Duplicate in a List


# Remove Duplicates from a List

# You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

# Parameters:

# lst (List of integers): The list of integers from which duplicates should be removed.

# Returns:

# A list of integers where all duplicates have been removed, preserving the original order.

# Example:

# Input: lst = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Input: lst = [4, 5, 5, 4, 6, 7]
# Output: [4, 5, 6, 7]


### Solution ## 

# Using set conversion

def remove_duplicates(lst):
    lst = set(lst)
    lst = list(lst)

    return lst

lst = [4, 5, 5, 4, 6, 7]
print(f'Removed duplicates using set conversion : {remove_duplicates(lst)}')


# Using Python Loop 

def remove_duplicates_loop(lst):
    new_lst = []
    for num in lst : 
        
        if num not in new_lst :
            new_lst.append(num)
    return new_lst

print(f'Removed duplicates using set Loop : {remove_duplicates_loop(lst)}')        

