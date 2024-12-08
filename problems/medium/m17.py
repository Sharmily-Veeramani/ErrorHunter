'''Write a program to reverse a given list without using built-in functions'''
def reverse_list(lst):
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst
 
input_list = input("Enter elements sep by commas : ")
re_list=list(map(int, input_list.split(',')))
print("Original list:", re_list)

reversed_list = reverse_list(re_list)
print("Reversed list:", reversed_list)