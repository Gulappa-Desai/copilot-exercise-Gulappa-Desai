def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Testing the function
num = int(input("Enter a number: "))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
