# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Noelle", "Hello")  # with a comma
print("Hello" + "Noelle")  # with a +
# 3. print "Hello 42!" with the number in a variable
name = "forty-two"
print("Hello" + name)  # with a comma
# TypeError: can only concatenate str (not "int") to str
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
# with a +	-- this one should give us an error!
print("I love to eat" + fave_food1 + "and" + fave_food2)
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}")  # with an f string

name2 = "michael shin"
print(f"hello {name2}")
print("hello", name2)
print("hello" + name2)
num = 42
print("hello", num)

print(f"hello  {num}")
print("hello {}".format(num))
# print("hello" + num)
# can only concatenate str (not "int") to str
