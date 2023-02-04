#calculator
print("***Calculator***")

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

print("Choose operation: ")
print("1.Add ")
print("2.Subtract")
print("3.Multiply ")
print("4.Division ")


while True:
    choice = input("Enter choice: ")
    if choice in ("1" , "2" , "3" , "4"):
        try:
            num1=float(input("Enter 1st number: "))
            num2=float(input("Enter 2nd number:"))
        except NameError or ValueError:
            print("Enter valid option!")
            continue
    
        if choice == "1":
            print(num1 , "+" , num2 , "=" , add(num1, num2) )
        if choice == "2":
            print(num1 , "-" , num2 , "=" , subtract(num1, num2) )
        if choice == "3":
            print(num1 , "*" , num2 , "=" , multiply(num1, num2) )
        if choice == "4":
            try:
                print(num1 , "/" , num2 , "=" , division(num1, num2) )
            except ZeroDivisionError:
                print("Oops! Cannot divide zero")
                
        try_again = input("Do you want to try again? y/n: ")
        if try_again == "n":
            break
        else:
           continue
    else:
        print("Invalid choice!")
print("Closed!")