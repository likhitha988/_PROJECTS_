#Assignment 1
import math

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        return "Division by zero not possible"
    return a / b
def mod(a, b): return a % b
def power(a, b): return a ** b
def square(a): return a * a
def sqrt(a): return math.sqrt(a)
def fact(a): return math.factorial(a)

while True:
    print("\n***** CALCULATOR *****")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Square")
    print("8.Square Root")
    print("9.Factorial")
    print("10.Exit")

    ch = int(input("Enter choice: "))

    if ch == 10:
        print("Thank You")
        break

    if ch in [1,2,3,4,5,6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if ch == 1:
            print(add(a,b))
        elif ch == 2:
            print(sub(a,b))
        elif ch == 3:
            print(mul(a,b))
        elif ch == 4:
            print(div(a,b))
        elif ch == 5:
            print(mod(a,b))
        elif ch == 6:
            print(power(a,b))

    elif ch == 7:

        print(square(a))

    elif ch == 8:
        a = float(input("Enter number: "))
        print(sqrt(a))

    elif ch == 9:
        a = int(input("Enter number: "))
        print(fact(a))

    else:
        print("Invalid Choice")








