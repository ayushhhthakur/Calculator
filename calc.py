def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    if 0 in numbers[1:]:
        return "Cannot divide by zero"
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

while True:
    print("Welcome to Mini Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Select an operation: ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4'):
        num_count = int(input("Enter the number of values: "))
        numbers = []
        for i in range(num_count):
            num = float(input(f"Enter number {i + 1}: "))
            numbers.append(num)

        if choice == '1':
            result = add(numbers)
            print(f"Result of addition: {result}")
        elif choice == '2':
            result = subtract(numbers)
            print(f"Result of subtraction: {result}")
        elif choice == '3':
            result = multiply(numbers)
            print(f"Result of multiplication: {result}")
        elif choice == '4':
            result = divide(numbers)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result of division: {result}")
        else:
            print("Invalid choice")
    else:
        print("Invalid input. Please enter a valid option (1/2/3/4/5)")
