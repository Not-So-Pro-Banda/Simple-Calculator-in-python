start = input("Enter y to start calculator or n to exit ")
while start == "y":
    a = eval(input("Enter a number: "))
    b = eval(input("Enter another number: "))
    operator = input("What do you want to do? + , - , * , / ")
    if operator == "+":
        print(a+b)
    elif operator == "-":
        print(a-b)
    elif operator == "*":
        print(a*b)
    elif operator == "/":
        print(a/b)
    elif operator == "%":
        print(a%b)
    else:
        print("Invalid operator.")
    start = input("Enter y to start calculator or n to exit ")
