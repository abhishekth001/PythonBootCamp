# WAP to Check the greatest number among 3 numbers

a = int(input(" Enter first value "))
b = int(input(" Enter second value "))
c = int(input(" Enter third value "))

if(a>b and a>c):
    print(a,"is greater then" , b ,"and" , c)
elif(b>c and b>a):
    print(b,"is greater then",a, "and", c)
else:
    print(c,"is greater then",a, "and",b)