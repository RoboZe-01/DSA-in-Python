

# Problem statement : User will input (3ages).Find the oldest one


                       ### Method 1 :  MAnual simple way  ####

# Using hard coded values 

# age_1 = input("Enter the age of person 1 : ")
# age_2 = input("Enter the age of person 2 : ")     # initialising the values 
# age_3 = input("Enter the age of person 3 : ")

# if age_1 > age_2 and age_1 >age_3:
#     print("Person 1 is oldest : ", age_1)
# elif age_2 > age_1 and age_2 > age_3:
#     print("second person is oldest :", age_2)  
# else:
#     print("Third person is oldest : ", age_3)
  

                     ### Method 2 ; Using a function ### 

# Function definition

def find_oldest ():

    # Taking input from the user
    age_1 = int(input("Enter the age of person 1 : "))
    age_2 = int(input("Enter the age of person 2 : "))
    age_3 = int(input("Enter the age of person 3 : "))
   
   # Condition for finding the oldest age
    if age_1 > age_2 and age_1 >age_3:
     print("Person 1 is oldest : ", age_1)
    elif age_2 > age_1 and age_2 > age_3:
        print("second person is oldest :", age_2)  
    else:
        print("Third person is oldest : ", age_3)

#Calling the function 

find_oldest()    