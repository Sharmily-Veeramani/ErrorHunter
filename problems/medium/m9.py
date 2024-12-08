def set_operations_menu():
    while True:
        print("\n1. Union of Two Sets")
        print("2. Intersection of Two Sets")
        print("3. Difference of Two Sets")
        print("4. Check Subset")
        print("5. Exit")
        choice = int(input("Enter your choice between 1 to 5 : "))

        set1 = set(input("Enter elements of Set 1 separated by space: ").split())
        set2 = set(input("Enter elements of Set 2 separated by space: ").split())

        if choice == 1:
            print("Union:", set1 | set2)  
        elif choice == 2:
            print("Intersection:", set1 & set2)  
        elif choice == 3:
            print("Difference:", set1 - set2)   
        elif choice == 4:
            if set1.issubset(set2):
                print("Set 1 is a subset of Set 2")
            elif set2.issubset(set1):
                print("Set 2 is a subset of Set 1")
            else:
                print("Neither set is a subset of the other")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
set_operations_menu()