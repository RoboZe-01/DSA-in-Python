

"""
Project details : 
Concepts: Nested loops, range(), formatting

Build: Generate customizable multiplication tables

Features:
- Ask: "Which table?" and "Up to which number?"
- Display formatted table
- Option to save to file
- Generate multiple tables in one run

"""
"""
Imp questions to ask : 

1. What are the inputs we are taking from the user : table of what number , upto to what 
2. what is the output : table in column format

"""

def table_generator(table , upto):
    
    for num in range(1,upto+1):
        print(table*num)



table = int(input("What table you want to generate : "))
upto = int(input("Enter what upto table : "))

table_generator(table,upto)
