'''
Let's build a Calculator

a+b
a-b
a*b
a/b
a%b

'''

first_number=input("Enter the first number : ")
operators=input("The operators are(+,-,*,/,%) : ")
Second_number=input("Enter the Second number : ")

first_number=int(first_number)
Second_number=int(Second_number)



if operators=="+":
    print(first_number+Second_number)
elif operators=="-":
    print(first_number-Second_number)
elif operators=="*":
    print(first_number*Second_number)
elif operators=="/":
    print(first_number/Second_number)
elif operators=="%":
    print(first_number%Second_number)
else:
    print("Invalid Operators")

