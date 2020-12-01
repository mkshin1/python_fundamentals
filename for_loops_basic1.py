# # # The break statement exits the current loop prematurely,
# # # resuming execution at the first post-loop statement.
# # # The break statement can be used in both while and for loops.
# # 1. Basic - Print all integers from 0 to 150.


# # Basic - Print all integers from 0 to 150.
# x = range(0, 151, 1)
# print(x)

# for y in range(0, 151):
#     print(y)

# # Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for y in range(5, 1005, 5):
#     print(y)
# for y in range(5, 1005):
#     if y % 5 == 0:
#         print(y)

# # Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for y in range(1, 101):
#     if y % 5 == 0:
#         print("coding")
#     elif y % 10 == 0 or y % 2 == 0:
#         print("Coding Dojo")

# # Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
# sum = 0
# for n in range(0, 500000):
#     if n % 2 != 0:
#         sum += n
# print(sum)

# # Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# for y in range(2018, 0, -4):
#     print(y)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
# print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# low_num = 2
# high_num = 9
# mult = 3

# for y in range(low_num, high_num+1):
#     if y % mult == 0:
#         print(y)
