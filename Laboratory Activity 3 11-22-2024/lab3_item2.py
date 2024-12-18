def is_perfect_number(num):
    
    if num <= 0:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num

def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            if is_perfect_number(number):
                print(f"{number} is a perfect number.")
            else:
                print(f"{number} is not a perfect number.")  
            break  
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()