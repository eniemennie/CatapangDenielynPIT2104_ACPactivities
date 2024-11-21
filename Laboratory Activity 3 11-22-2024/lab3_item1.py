def roman_to_integer(r):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0

    for char in r[::-1]:
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

def main():
    roman_numeral = input("Enter a Roman numeral: ")
    integer_value = roman_to_integer(roman_numeral.upper())
    print(f"The integer value of {roman_numeral} is {integer_value}")

if __name__ == "__main__":
    main()