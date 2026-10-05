# Character counter without using len()


def char_count(text):
    count = 0 
    if text =="":
        print("Empty string")
    else:    
         text = text.strip(" ")
         for i in text : 
            count+=1
         return count    

      
text = "Machine Learning"
print(char_count(text))