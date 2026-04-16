
# Problem statement : 

"""
Code a program which checks if someone is on the list or not , and what is there status 

if some is on the list then greet them and aknowledge there status 
else , let them know that they are not on the list
"""


import time
import sys

# Initilise the the guest list 
roster = {
    "Prem": "VIP",
    "Priya": "Member",
    "Ishaan": "Guest",
    "Subha": "VIP",
    "Rohan": "Member",
    "Saanvi": "Guest",
    "Rahul": "VIP",
    "Diya": "Member",
    "Advait": "Guest",
    "Om": "VIP",
    "Kabir": "Member",
    "Anika": "Guest",
    "Arjun": "VIP",
    "Kiara": "Member",
    "Sai": "Guest",
    "Ira": "VIP",
    "Reyansh": "Member",
    "Tara": "Guest",
    "Dhruv": "VIP",
    "Meera": "Member"
}


# Typewriter effect 
def typewriter_effect(text, delay=0.1):
    for char in text:
        # sys.stdout.write ensures it prints without adding a new line
        sys.stdout.write(char)
        # flush ensures the character appears immediately
        sys.stdout.flush()
        # Sleep for the duration of the delay
        time.sleep(delay)
    # Print a new line at the very end
    print()


while True :
    person = input("What is your good name Sir/Mam : ")
    typewriter_effect("wait a sec , Checking your name on the list .... ")


    # Condition for cheking if the name on the list or not 
    if person in roster:
        print(f'Hello {person} , your are allowed , have a nice day !! ')
    else:
        print("sorry sir your not on the list")    


  