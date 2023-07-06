def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero!"
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def main():
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4','5'):
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))

        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))
        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1, n2))
        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1, n2))
        elif choice == '5':
            print(n1, "^", n2, "=", power(n1, n2))
        else:
            print("Invalid choice!")

        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation == "no":
            print("Thank you")
        else:
            main()
    else:
        print("Invalid choice!")

main()
