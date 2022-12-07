def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter the number for finding factorial= "))
result = factorial(num)
print(f"Factorial of a number ={result}")
