# Print X N Times
def print_x_n_times(x, n):
    for i in range(n):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
    x=input("Enter a character:")
    n=int(input("enter the number of times to loop:"))
    print_x_n_times(x,n)