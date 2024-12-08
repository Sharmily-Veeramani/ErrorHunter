def conversion_menu():
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Decimal to Binary, Octal, Hexadecimal")
        print("4. Kilometers to Miles and Vice Versa")
        print("5. Exit")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 5:
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid choice! Please enter a number between 1 and 5.")
        if choice == 1:
            celsius = int(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32   
            print("Temperature in Fahrenheit:", fahrenheit)
        elif choice == 2:
            fahrenheit = int(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print("Temperature in Celsius:", celsius)
        elif choice == 3:
            decimal = int(input("Enter a decimal number: "))
            print(f"Binary: {bin(decimal)[2:]}, Octal: {oct(decimal)[2:]}, Hexadecimal: {hex(decimal)[2:]}")   
        elif choice == 4:
            km = float(input("Enter distance in kilometers: "))
            miles = km * 0.621371  
            print("Distance in Miles:", miles)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
conversion_menu()