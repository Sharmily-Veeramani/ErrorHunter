# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    if len(arr)<1:
        return "Array is empty"
    return arr[0] + arr[-1]  
if __name__ == "__main__":
    input_str = input("Enter the array elements separated by space: ")
    arr = [int(x) for x in input_str.split()]
    print(sum_first_last(arr))