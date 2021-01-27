# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a function that accepts a complex dictionary and prints out all of it's keys and all of its values. 
# The dictionary can have dictionaries nested inside of it
# 'dictionary' is the dictionary that's currently being iterated over.
# 'indent' is a string representing the current level of indentation
# ...
# pretty_print(inner_dictionary, indent + '..');
# ...

# def pretty_print(dictionary, indent, level=1):
#     for key, value in dictionary.items():
#         print(f"This is the key: {key}. \nThis is the value: {value}")
#         # print(f"Dictionary items are following: {dictionary.items()}")
#         if type(value) == dict:
#             print(indent * level, key, ":")
#             print(f"This is the current level: {level}")
#             pretty_print(value, indent, level+1)
#         else: 
#             print(f"This is the indentation: {indent}")
#             print(indent * level, key, ":", value)
#     pass

# o1 = {"a": 1, "b": 2}
# o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
# o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

# # print(pretty_print(o1, "-"))
# # print(pretty_print(o2, " "))
# print(pretty_print(o3, ".."))
# ..a: 1
# ..b: 2
# ..c:
# ....name: Bruce Wayne
# ....occupation: Hero
# ....friends: 
# ......spiderman:
# ........name: Peter Parker
# ......superman: 
# ........name: Clark Kent
# ..d: 4

def pretty_print1(dictionary, indent, level = 1):
	for key in dictionary:
            value = dictionary[key]

            if type(value) is dict:
                print((indent * level) + key + ': ')
                pretty_print1(value, indent, level + 1)
            else:
                print(indent + key + ': ' + str(value))

        
o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

print(pretty_print1(o1, "-"))
print(pretty_print1(o2, " "))
print(pretty_print1(o3, ".."))