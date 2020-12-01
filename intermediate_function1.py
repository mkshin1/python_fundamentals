import random


def randInt(min=None, max=None):
    # print(min, max)
    if min is not None and max is None:
        print("the min is printing:", min)
        return random.uniform(min, 100)
    elif max is not None and min is None:
        print("the max is printing:", max)
        return random.random() * max
    elif min and max is not None:
        print("the min and max is printing:", min, max)
        return random.uniform(min, max)
    else:
        random_number = random.random()
        print("the min and max is not printing:", random_number)
        return random_number


    # min = random.random(0, min)
    # both = random.random(min, max)
    # num = random.random()
    # return num
print(randInt(min=105))

# default = random.randint(0, 100)
# if max:
#     return random.randint(0, max)
# print("here is the printed:" + max)
# if min:
#     return random.randint(min, 100)
#     print("here is the printed:" + min)
# elif max and min:
#     return random.randint(max, min)
#     print("here is the printed max and min:" + (max, min))
# else:
#     return default
# print("here is the printed:" + default)
'''reference'''
# def default(x=10, y=20):
#     # print(x)
#     return f"hello there {x}. I am {y}"


# print(default("michael", "Python"))
