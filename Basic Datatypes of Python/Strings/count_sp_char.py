# Count specific character 

text = "programming"   # main text 
sp_char = "g"          # character that we want to find count of 

# Function to create the count specific character 



def count_sp_char(text,sp_char):
    j=0
    for i in text:
     if i==sp_char:
      j+=1
    print(j)

count_sp_char(text,sp_char)


