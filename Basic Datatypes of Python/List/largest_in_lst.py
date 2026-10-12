# ----- Find the largest number in the list ----- # 

#   -------- Basic Version --------

# number_lst = [1,2,44,18,55,16,64,15]
# largest_num = number_lst[0]
# for num in number_lst : 
#     if num > largest_num:
#         largest_num = num
# print(largest_num)        



# ------ Professional Version ------
"""This version is professional as we are :
1. Using functional methods
2. Handling edge cases as : Empty list , list with single element , list with different datatype 
3. Handling proper export """


def find_largest(user_list:list[float,int])->float:

    """
    Function to find the largest number in the list 
    args : User_list - Consist of the list of float and int 

    returns : float -> largest number in the list 

    raises : TypeError: If input is not list or contain numeric value
             ValueError: If empty list appeared
    """

    # Validate  the input of the list 
    if not isinstance(user_list,list):
        raise TypeError("Input must be the list of number int or float")

    # Validate for empty list
    if not user_list:
        raise ValueError("List cannot be empty")

    # validate for the element in the list to be int float 
    for item in user_list:
        if not isinstance(item,(int,float)):
            raise TypeError("All element must be numeric")

    # Applying main logic of the function    
    largest_num = user_list[0]
    for num in user_list:    
        if num > largest_num:
         largest_num = num
    return largest_num 

# Main excecution of the function 
if __name__ == "__main__":

    try:
        # take input from the user 
        user_input = input("Enter the numeric value seperated by space (int/float) : ")
        # Convert user input to the list of numbers 
        number_list = [float(item) for item in user_input.split()]
        # call the function and store the result in the variable 
        result = find_largest(number_list)
        # Print the result 
        print(f'Largest Number from this list is : {result}')

    # Handling the exception 
    except (TypeError,ValueError)    as error:
        print(error)
    except Exception as e:
        print(e)





