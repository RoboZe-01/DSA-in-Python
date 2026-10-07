# Count Words


# ------ Basic Solution ------
text = "Machine learning is good"
text = text.split()
count = 0
for word in text : 
    count+=1
print(count)


# ----- Profesional Solution ------- # 

def count_words(text:str)->int:
    
        
