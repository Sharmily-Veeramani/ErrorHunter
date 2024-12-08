def array_operations_menu():
    print("1. Sum of Array")
    print("2. Largest Element")
    print("3. Smallest Element")
    print("4. Sort Array")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 4.")

    arr = list(map(int, input("Enter array elements separated by space: ").split()))

    if choice == 1:
        print("Sum:", sum(arr))   
    elif choice == 2:
        print("Largest Element:", max(arr))  
    elif choice == 3:
        print("Smallest Element:", min(arr))   
    elif choice == 4:
        arr.sort()
 
        print("Sorted Array:", arr) 
    else:
        print("Invalid option")
array_operations_menu()
 
        
       
 
