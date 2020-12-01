# x = [1, 3, 5, 7, 8]

x = [3, 5, 6, 7, 4, 0]


def bubble_sort(arr):
    for j in range(len(x)-1):
        for index in range(len(x)-1-j):
            if x[index] > x[index+1]:
                x[index], x[index+1] = x[index+1], x[index]
                print("swapped", x[index], x[index+1])
                print(x)
            else:
                ("no need to swap", x[index], x[index+1])
    return arr


print(bubble_sort(x))

# 3, 5, 6, 4, 0, 7
