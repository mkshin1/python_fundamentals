'''
Countdown - Create a function that accepts a number as an input.
Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
Example: countdown(5) should return [5,4,3,2,1,0]
'''


# def count_down(x):
#     for n in range(x, 0, -1):
#         print(n)


# count_down(5)

# if you assign a variable to a function that does not have a return statement (value) it will cause a "syntax error" but still run your code.
# also any function that does not have a return statement that you assign to will be interpreted as None by python.


'''Print and Return - Create a function that will receive a list with two numbers.
Print the first value and return the second.
Example: print_and_return([1,2]) should print 1 and return 2.'''


# def print_and_return(x, y):
#     print(x)
#     return y


# # --> returns 10 which is the whatever is being printed
# # print_and_return(10, 15)
# a = print_and_return(10, 15)
# print(a)

'''
First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
'''


# def first_plus_length(x):
#     return x[0] + len(x)


# print(first_plus_length([1, 2, 3, 4, 5]))
# x = first_plus_length([1, 2, 3, 4, 5])
# print(x)


'''
Values Greater than Second - Write a function that accepts a list and creates a new list containing
only the values from the original list that are greater than its 2nd value.
Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
Example: values_greater_than_second([3]) should return False
'''


# def values_greater_than_second(old_list):
#     print(old_list)
#     if len(old_list) < 2:
#         return False
#     new_list = []
#     second_value = old_list[1]
#     print(second_value)
#     for n in range(len(old_list)):
#         # converted list into a range object by calling the range function and passing the length of the old list..?
#         if old_list[n] > second_value:
#             new_list.append(old_list[n])
#             print(old_list[n])
#     return new_list


# x = values_greater_than_second([5, 10, 8, 3, 4, 9])
# print(x)

def values_greater_than_second(old_list):
    old_list
    if len(old_list) < 2:
        return False
    new_list = []
    second_value = old_list[1]
    print(second_value)
    for n in old_list:
        print(n)
        print(old_list[n])
        # ^ IndexError: list index out of range
        # converted list into a range object by calling the range function and passing the length of the old list..?
        if old_list[n] > second_value:
            new_list.append(old_list[n])
            print(old_list[n])
    return new_list


x = values_greater_than_second([5, 10, 8, 3, 4, 9])
print(x)


'''
This Length, That Value - Write a function that accepts two integers as parameters: size and value.
The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
Example: length_and_value(4,7) should return [7,7,7,7]
Example: length_and_value(6,2) should return [2,2,2,2,2,2]
'''


# def length_and_value(size, value):
#     new_list = list(range(size))
#     # range function does not return list types.
#     # must convert the range object/type to an list object/type
#     print(new_list)
#     for n in new_list:
#         new_list[n] = value
#     return new_list


# x = length_and_value(4, 7)
# print(x)
