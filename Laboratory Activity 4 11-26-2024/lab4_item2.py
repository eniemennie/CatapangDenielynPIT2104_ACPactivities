def main():
    try:
        size = int(input("Enter the size of the array: "))
        arr = [0.0] * size  # Initialize the array with zeros

        for i in range(size):
            arr[i] = float(input(f"Enter the element of the array:\n"))  # Fixed here
        
        index = int(input("Enter the index of the element to print: "))

        if index < 0 or index >= size:
            raise IndexError(f"Index {index} is invalid.")

        print(f"Element at index {index}: {arr[index]:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()