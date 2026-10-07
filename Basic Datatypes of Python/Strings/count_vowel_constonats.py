# Count Vowels and Consonants Separately

# Problem statement : Count vowels in the words 

"""Count the number of vowels in the text

Keyword arguments:Text : str
argument -- User will put the string to the input 
Return: Output should be int of how many vowels are there
"""

# Function to count the vowels
def count_vowels(text : str)->int:
    # Define vowels
    vowels = ['a','e','i','o','u']
    # Handling cases ( Convert the text to lower case)
    text = text.lower()
    vowel_count = 0
    consonant_count=0

    # Condition to check if number is vowels
    for char in text:
        if char in vowels:
            vowel_count+=1
        elif char ==" ":
            vowel_count
        else:
            consonant_count +=1
    return vowel_count , consonant_count

print(count_vowels("Prem"))    
print(count_vowels("Subhashin"))    
print(count_vowels(""))    
print(count_vowels("Rahul"))    
print(count_vowels("om"))    
print(count_vowels("Prem Subha"))    


    