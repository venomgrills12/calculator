def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x,y):
    return x ** y
def square(x,y):
    return x ** y
def root(x,y):
    return x ** y
cont = "y"
while cont.lower() == "y":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Square")
    print("7.Root")
    choice = input("Enter choice(1/2/3/4/5/6/7):")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == '1':
                print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '2':
                print(num1,"-",num2,"=", subtract(num1,num2))
    elif choice == '3':
                    print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '4':
                    print(num1,"/",num2,"=", divide(num1,num2))
    elif choice == '5':
                    print(num1,"**",num2,"=", power(num1,num2))
    elif choice == '6':
                    print(num1,"**",2,"=", square(num1,2))
    elif choice =='7':
                    print(num1,"**",0.5,"=", root(num1,0.5))
    else:
                    print("Invalid Output!!!!")
    cont = input("Continue?y/n:")
    if cont == "n":
        break