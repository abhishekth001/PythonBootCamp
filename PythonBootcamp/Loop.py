# Use while loop to print 1 to 10
i=1
while i<5:
    print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1

i=10
while i>0:
    print(i)
    break
    i-=1

#continue is use for escape
i=10
while i>0:
    print(i)
    i-=1
    continue




# Find the Factorial of a number by taking from user
num = int(input(" Enter a number to find its Factorial : "))

factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i
    
print(f"The factorial of {num} is {factorial}")

#for loop :-
# print the number 1 to 10
for i in range(1,11,1):
    print(i)

#print even number
# method 1 :-
for i in range(1,11,1):
    if(i%2==0):
        print(i)
        
#method 2 :-
for evenNo in range(2,11,2):
    print(evenNo)


