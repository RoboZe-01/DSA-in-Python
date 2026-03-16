      ### Problem ### 


# Find the Largest Element in a List

# Write a Python function that finds and returns the largest element in a given list of integers.

# Parameters:

# numbers (List of integers): The input list containing integers.

# Returns:

# An integer representing the largest element in the input list.

# Example:

# Input: numbers = [3, 8, 2, 10, 5]
# Output: 10

# Input: numbers = [-5, -10, -2, -1, -7]
# Output: -1




                      ### Solution ###


# Method 1 : Brute logic method

def largest_num(numbers):
    order = numbers
    order = set(order)
    order = list(order)
    order_sorted = sorted(order)
    print(order_sorted[-1])
  

numbers =[-5, -10, -2, -1, -7]
largest_num(numbers)  


# Using inbuilt Function MAX

def find_largest(numbers):
    if not numbers:
        return None
    else : 
        return max(numbers)
    
print(f'Solution using inbuilt function : {find_largest(numbers)}')    