# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else: 
#         max = find_max(lst[1:])
#         return max if max > lst[0] else lst[0]
#     pass


# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

import math

def find_max(l, current_max = -math.inf):
    if len(l) == 0:
        return current_max
    if l[0] > current_max:
        print(f"inside the if statement: the current max is {current_max}. The current value is {l}")
        new_current_max = l[0]
    else: 
        print(f"inside the else statement: The current max is {current_max}. The current value is {l}")
 
        new_current_max = current_max

    return find_max(l[1:], new_current_max)

print(find_max([1, 4, 45, 6, -50, 10, 2]))