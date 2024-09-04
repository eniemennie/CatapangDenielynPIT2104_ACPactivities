user_input = input("Enter two characters separated by a space: ")

char1, char2 = user_input.split()

larger_char = max(char1, char2)


ascii_value = ord(larger_char)


print("-----------------------------------")
print(f"The character with the greater value is: {larger_char}")
print("-----------------------------------")
print(f"The ASCII value of '{larger_char}' is: {ascii_value}")
