# Count Words


# ------ Basic Solution ------
# text = "Machine learning is good"
# text = text.split()
# count = 0
# for word in text : 
#     count+=1
# print(count)


# ----- Profesional Solution ------- # 

def count_words(text:str)->int:
    """ 
    Function to count the words in the sentence
    Args : 
          text : str : text to count the words 
    Returns : 
          The (int) as the count of the words in sentence 
    Raises : 
        TypeError: If input text is not string            
    Working : 
        - Convert the given string to the list of words using inbuilt split() function 
        - Use for loop to count the words 
        - Returns the output as a count of words 

    """
    # Validate the string
    if not isinstance(text,str):
        raise TypeError("Input must be a string ")
    # Initial count
    count = 0
    text = text.strip()
    text = text.split()
    for word in text:
        count+=1

    return count

# --- Main Excecution ---
if __name__ == "__main__":
    try :
        # Taking input from the user 
        user_input = input("Enter Your string : ")
        # Calling the function 
        result = count_words(user_input)
        # Print the result 
        print(f'The count of words is : {result}')

    except TypeError as e:
        print(e)


    

        
