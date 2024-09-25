def is_palindrome(number):
    str_number = str(number)
    return str_number == str_number[::-1]

try:
    user_input = int(input("Enter an integer: "))
    if is_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not a Palindrome")
except ValueError:
    print("Please enter a valid integer.")
