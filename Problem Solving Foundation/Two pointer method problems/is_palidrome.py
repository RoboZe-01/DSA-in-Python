
                               ### Problem statement ###

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.  """    





### Method 1 : By reversing the string 

# def palindrome_reverse(inpt_str):

#     # using slicing / indexing reverse the string 
#     if inpt_str.lower() == inpt_str[::-1].lower():
#         return True 
#     else:
#         return False
    

# strr= input('Enter Your string here : ')

# print(f'{palindrome_reverse(strr)}')


"""
Above code can only handle the small words 
it do not handle : edge cases , alpahnumeric filtering 
"""


             ### Using two pointer method 
class Solution : 
    def valid_palindrome( self , inpt_str:str)->bool:

        left , right = 0 , len(inpt_str)-1

        while left<right:


        # ignore alphanum from left 
            while left<right and not inpt_str[left].isalnum():
                left+=1
            # ignore alnum from right 
            while left <right and not inpt_str[right].isalnum():
                right -= 1


            # check right and left letters
            if inpt_str[left].lower() != inpt_str[right].lower():
                return False
            
            left +=1
            right -=1

        return True  

# Get the input from the user 
if __name__ == '__main__':
    # create a instance of the solution class
    solution = Solution()

    # get the input string from the user 
    user_str = input("Enter a String to check it it's palindrome : ")

    # check if it's palindrom 
    result = solution.valid_palindrome(user_str)

    # display the results 
    print(f' is "{user_str}" a palindrome? {result} ')




    
    



