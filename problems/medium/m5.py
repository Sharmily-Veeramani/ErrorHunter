def matrix_operations_menu():
    print("1. Add Matrices")
    print("2. Multiply Matrices")
    print("3. Transpose Matrix")
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 3:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid choice! Please enter a number between 1 and 3.")
    if choice == 1 or choice == 2:
        while True:
            try:
                rows, cols = map(int, input("Enter rows and columns: ").split())
                if rows > 0 and cols > 0:
                    break
                else:
                    print("Invalid input! Please enter positive integers for rows and columns.")
            except ValueError:
                print("Invalid input! Please enter integers for rows and columns.")

        mat1 = []
        for i in range(rows):
            while True:
                try:
                    row = list(map(int, input(f"Enter row {i+1}: ").split()))
                    if len(row) == cols:
                        mat1.append(row)
                        break
                    else:
                        print(f"Invalid input! Please enter {cols} integers for row {i+1}.")
                except ValueError:
                    print(f"Invalid input! Please enter integers for row {i+1}.")

        mat2 = []
        for i in range(rows):
            while True:
                try:
                    row = list(map(int, input(f"Enter row {i+1} of second matrix: ").split()))
                    if len(row) == cols:
                        mat2.append(row)
                        break
                    else:
                        print(f"Invalid input! Please enter {cols} integers for row {i+1}.")
                except ValueError:
                    print(f"Invalid input! Please enter integers for row {i+1}.")

        if choice == 1:
            result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
            print("Resultant Matrix:")
            for row in result:
                print(row)
        else:
            result = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    for k in range(cols):
                        result[i][j] += mat1[i][k] * mat2[k][j]
            print("Resultant Matrix:")
            for row in result:
                print(row)

    elif choice == 3:
        while True:
            try:
                rows, cols = map(int, input("Enter rows and columns: ").split())
                if rows > 0 and cols > 0:
                    break
                else:
                    print("Invalid input! Please enter positive integers for rows and columns.")
            except ValueError:
                print("Invalid input! Please enter integers for rows and columns.")

        mat = []
        for i in range(rows):
            while True:
                try:
                    row = list(map(int, input(f"Enter row {i+1}: ").split()))
                    if len(row) == cols:
                        mat.append(row)
                        break
                    else:
                        print(f"Invalid input! Please enter {cols} integers for row {i+1}.")
                except ValueError:
                    print(f"Invalid input! Please enter integers for row {i+1}.")

        transpose = [[mat[j][i] for j in range(rows)] for i in range(cols)]
        print("Transpose:")
        for row in transpose:
            print(row)

    else:
        print("Invalid option")

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() == "yes":
        matrix_operations_menu()

matrix_operations_menu()

        
