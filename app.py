# Given two integer numbers return their product. If the product is greater than 1000, then return their sum

a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
if (a*b > 1000):
    print("Sum = ", a+b)
else:
    print("Nothing to print")