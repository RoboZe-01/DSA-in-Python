  ### Problem statement


"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


"""


   ## Brute force approach ( using timsort )

"""
In this approach i am ignoring the sign ( positive or negative ) then square them and new array will be sorted


   """

nums = 	[-5, -3, -2, -1, 0, 1, 4, 5, 7, 10]       # example array 
# nums.sort(key=abs)
# print(nums)

def square_sort(arr):
    arr.sort(key=abs)
    square_arr = []
    for a in range(0,len(arr)):
        square_arr.append(arr[a]*arr[a])
    return square_arr


print(f'sorted square array is {square_sort(nums)}')



## solution using list comprehension 

def square_arr_compre(arr):
    arr.sort(key=abs)
    arr = [i*i for i in arr]
    return arr

print(f'solution using list comprehenstion : {square_arr_compre(nums)}')


## Solving using square and sort method

def square_and_sort(arr):
    arr = [i*i for i in arr]
    arr.sort()
    return arr

print(f'solution using square and sort method : {square_and_sort(nums)}')



## using Merge sort and two pointer 

def square_merge_sort(arr):
    
    a = [x*x for x in arr if x<0][::-1]  ## Negative arr square
  
    b = [y*y for y in arr if y>=0]     ## positive arr square
    i = 0
    j = 0
    merge_arr=[]
   
    
   
#  # compare the values from a and b at index i and j
    while i < len(a) and j < len(b):
        if a[i]<b[j]:
            merge_arr.append(a[i])
            i+=1
            
        else : 
            merge_arr.append(b[j])
            
            j+=1
           

    # condition when a values are finished 
    while i < len(a) :
        merge_arr.append(a[i])
        
        i+=1
    while j<len(b):
        merge_arr.append(b[j])
        
        j+=1
    return merge_arr               


print(f'using merge sort : {square_merge_sort(nums)}')



 