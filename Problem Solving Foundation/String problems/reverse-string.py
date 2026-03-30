"""

                    ### Problem solving ###
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""





## Method 1  : using simple slicing 

def reverse_string(s):
    s=s[::-1]
    return s


s = ["H","a","n","n","a","h"]

print(f'reversed string is : {reverse_string(s)}')

## Method 2 : using two pointer method 

class Solution:
    def reverse_string(self,s):
        
        # initializing the index
        left , right= 0,len(s)-1
        while left < right :
            # swaping the string using two pointer in place 
            s[left],s[right]=s[right],s[left]
            left +=1
            right -=1
        return s
    
if __name__ == '__main__':
    solution = Solution()
    print(f'reversed using two pointer : {solution.reverse_string(s)}')

