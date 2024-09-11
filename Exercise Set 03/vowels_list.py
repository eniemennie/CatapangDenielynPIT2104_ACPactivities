def find_vowels(input_string):
    vowels = "aeiouAEIOU" 
    vowel_list = []
    for char in input_string:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list

user_input = input("Enter a string: ")

vowels_in_string = find_vowels(user_input)
print("Vowels in the string:", vowels_in_string)
