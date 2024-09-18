#  Write a Program to create 3 types of file:-
# 1. Jason File
# 2. Excel File
# 3. CSV File
# (read and write your data in all of them)

# taking input from user
name = input("Enter your name")
email = input("Enter your email")
collegeName = input("Enter your college name")
data = name + email + collegeName

# write data into json file :-
f = open("ht.json","w")
f.write(data)
f.close

# write data into Excel File :-
f = open("ht.xlsx","w")
f.write(data)
f.close

# wriet data into CSV file :-
f = open("ht.csv","w")
f.write(data)
f.close


f = open("ht.json","r")
print(f.read())

f = open("ht.xlsx","r")
print(f.read())

f = open("ht.csv","r")
print(f.read())

