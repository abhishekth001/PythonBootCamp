# WAP to check the user eligibile for job application
#if gender is female and age is greater then 17
#if gender is male then they can apply for private job


age = int(input("Enter your age "))
gender = input("Enter your Gender ")

# methor 1 :- 

if(age > 17):
    if(gender == 'female'):
        print("You are eligible for Government job")
    elif(gender == 'male'):
        print("You are eligible for private job")
    else:
        print("Your gender is incorrect")
else:
    print("You are not eligible for any job")
    
    
#method 2 :-
if(age > 17 and gender == "female"):
    print("You are eligible for Government job")
elif(age>17 and gender == "male"):
    print("Yor are eligible for private job")
else:
    print("You are not eligible for any job")
