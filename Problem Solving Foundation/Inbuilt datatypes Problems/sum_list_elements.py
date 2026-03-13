

# Sum of List Elements

# Write a Python function that calculates the sum of all elements in a given list of integers.

# Parameters:

# numbers (List of integers): The input list containing integers.

# Returns:

# An integer representing the sum of all elements in the input list.

# Example:

# Input: numbers = [1, 2, 3, 4, 5]
# Output: 15

# Input: numbers = [10, -5, 7, 8, -2]
# Output: 18




### Solution ### 


def sum_list(numbers):
    # Your code goes here
    sum = 0
    for num in numbers:
        sum = sum + num
        
    return sum    
        
        
    pass

numbers = [1, 2, 3, 4, 5]

sum_list(numbers)