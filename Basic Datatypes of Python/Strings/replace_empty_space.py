def empty(text):
    new_text =""
    text = text.strip()
    for i in text :
        if i == " ":
            new_text = new_text+"-"
        else:
            new_text=new_text+i    

    return   new_text 
             

print(empty(" machine  learning  programming "))