def file_handling_menu():
    print("1. Write to File")
    print("2. Read File")
    print("3. Count Lines, Words, Characters")
    print("4. Append to File")
    choice = int(input("Enter your choice: "))

    filename = input("Enter the file name: ")

    if choice == 1:
        data = input("Enter data to write: ")
        with open(filename, "w") as f:  
            f.write(data)
    elif choice == 2:
        with open(filename, "r") as f:
            print(f.read())  
    elif choice == 3:
        with open(filename, "r") as f:
            lines = len(f.read().split("\n"))
            words = len(f.read().split()) 
            chars = sum(len(line) for line in f.readlines())  
            print("Lines:", lines, "Words:", words, "Characters:", chars)
    elif choice == 4:
        data = input("Enter data to append: ")
        with open(filename, "w") as f:  
            f.write(data)
    else:
        print("Invalid option")
