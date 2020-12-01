# Practice writing functions and looping over dictionaries
# Achieve a better understanding of how to traverse through a list of dictionaries or through a dictionary of lists
# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]


# 1.Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# x[1][0] = 15
# print(x)

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"] = "Bryant"
# print(students)


# 3 In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0] = "Andres"
# print(sports_directory)

# # 4 Change the value 20 in z to 30
# z[0]["y"] = 30
# print(z)


'''
Create a function iterateDictionary(some_list) that, given a list of dictionaries,
the function loops through each dictionary in the list and prints each key and the associated value.
For example, given the following list: '''

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# def iterateDictionary(full_names):
#     for name in full_names:
#         # loop through the list of items that are stored as dictionary items
#         # print(lists)
#         for key in name:
#             # create an inner loop to grab the key for each dictionary item
#             print(f"{key} - {name[key]}")
#         # use a formated string to print out the key of the each dictionary item and as well as the value.
#             # print(key)
#             # print(lists[key])


''' to get the value of a dictionary item - one way is to write the syntax like this : dict["key"] (will grant u access the value to that specific key)'''


# iterateDictionary(students)


'''
Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
the function prints the value stored in that key for each dictionary. 
For example, iterateDictionary2('first_name', students) should output:
'''


# def iterateDictionary2(key_name, full_names):
#     for name in full_names:
#         # iterates through the list that contains dictionary items
#         for key in name:
#             # iterates through each dictionary item which has 2 key, value pairs fo each item
#             if key_name == key:
#                 # do a validation here to check to see if the key_name which is the argument passed in matches a key
#                 print(name[key])
#             # else:
#             #     print("not found")


# iterateDictionary2("last_name", students)


'''
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 
For example:
'''

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(coding):
    # for key, value in coding.items():
    #     print(key, value)
    for key in coding:
        print(key, len(coding[key]))
        for value in coding[key]:
            print(value)
        # print(coding[key])

    # print(dojo["locations"])
    # print(dojo["instructors"])
    # print(dojo["instructors"][0])


print_info(dojo)
