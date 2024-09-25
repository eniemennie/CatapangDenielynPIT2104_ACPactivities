def calculate_discount(purchase_amount):
    if purchase_amount > 5000:
        discount_percentage = 10
    else:
        discount_percentage = 5
    
    discount_amount = (discount_percentage / 100) * purchase_amount
    final_amount = purchase_amount - discount_amount
    return final_amount, discount_amount, discount_percentage

def main():
    while True:
        try:
            purchase_amount = float(input("Enter the total purchase amount: P"))
            print(f"Initial Purchase Amount: P{purchase_amount:.2f}")
            final_amount, discount_amount, discount_percentage = calculate_discount(purchase_amount)
            print(f"Discount: P{discount_amount:.2f}")
            print(f"Final Amount after Discount: P{final_amount:.2f}")
        except ValueError:
            print("Please enter a valid number.")
        
        try_again = input("Would you like to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you!")
            break

if __name__ == "__main__":
    main()
