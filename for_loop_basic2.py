'''Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]'''


# def biggie_size(x):
#     for n in range(len(x)):
#         if x[n] > 0:
#             x[n] = "big"
#     return x


# y = biggie_size([-1, 3, 5, -5])
# print(y)

# # listx = [1, 2, 3, 4, 5]
# # for n in range(len(listx)):
# #     y = listx[n]
# #     print(y)

'''Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it'''


# def count_positives(arr):
#     count = 0
#     for n in range(len(arr)):
#         if arr[n] > 0:
#             count += 1
#     arr[-1] = count
#     print(count)
#     return arr


# solution = count_positives([0, 2, 3, 4, 5, 7])
# print(solution)

'''Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7'''


# def sum_total(x):
#     sum = 0
#     for n in x:
#         sum += n
#     print(sum)
#     return sum


# print(sum_total([1, 2, 3, 4]))
# solution = sum_total([1, 2, 3, 4])
# print(solution)


''' Average - Create a function that takes a list and returns the average of all the values.x
Example: average([1,2,3,4]) should return 2.5 '''


# def average(x):
#     sum = 0
#     for n in range(len(x)):
#         sum += x[n]
#     return sum / len(x)


# print(average([1, 2, 3, 4]))
# solution = average([1, 2, 3, 4])
# print(solution)
# print(average)  # --> <function average at 0x000001DA3B5BA430>


'''Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0'''


# def length(x):
#     count = 0
#     for n in range(len(x)):
#         count += 1
#     return count


# print(length([0, 1, 2, 3, 5, 6, 7]))

'''Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False'''


# def minimum(arr):
#     if len(arr) == 0:
#         return False
#     min = arr[0]
#     for n in range(len(arr)):
#         if arr[n] < min:
#             min = arr[n]
#     return min


# print(minimum([]))


'''
Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False
'''


# def maximum(arr):
#     if len(arr) == 0:
#         return False
#     max = arr[0]
#     for n in range(len(arr)):
#         if arr[n] > max:
#             max = arr[n]
#     return max


# print(maximum([100, 1, 2, 3, -500, 6, 7]))

'''
Ultimate Analysis - Create a function that takes a list and returns a dictionary
that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should return
{'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
'''


# def ultimate_analysis(arr):
#     new_dic = dict()

#     sum_total = 0
#     for n in range(len(arr)):
#         sum_total = sum_total + arr[n]
#         # print(sum_total)

#     average = sum_total / len(arr)
#     # print(average)

#     max = arr[0]
#     for n in range(len(arr)):
#         if arr[n] > max:
#             max = arr[n]
#     # print(max)

#     min = arr[0]
#     for n in range(len(arr)):
#         if arr[n] < min:
#             min = arr[n]
#     # print(min)

#     new_dic["sum_total"] = sum_total
#     new_dic["average"] = average
#     new_dic["max"] = max
#     new_dic["min"] = min
#     # print(new_dic)

#     return new_dic


# print(ultimate_analysis([1, 2, 3, 4, 5]))

'''
Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
(This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]'''


def reverse_list(arr):
    for n in range(len(arr) // 2):
        # arr[n], arr[-n-1] = arr[-n-1], arr[n]
        print(arr[n])
        temp = arr[n]
        arr[n] = arr[-n-1]
        # the key is the -n
        arr[-n-1] = temp
    return arr


# def reverse_list2(arr):
#     arr = arr[::-1]
#     return arr
# this method is using the slice method on lists


print(reverse_list([4, 3, 2, 1]))
# TypeError: unsupported operand type(s) for /: 'list' and 'int'

# random_list = [1, 2, 3, 4, 5]
# temp = random_list[0]
# random_list[0] = random_list[-1]
# random_list[-1] = temp

# print(random_list)
