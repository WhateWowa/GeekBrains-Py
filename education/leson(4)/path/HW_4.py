# 2
# my_list = [1, 9, 1, 42, 4, 5, 2]
# new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i-1] and i !=0]
# print(new_list)
# 3
# 4

my_list = [1, 1, 2, 2, 3, 3, 4, 5, 6, 8, 1, 4, 10, 11, 1]
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)
# 5

from functools import reduce

def mel_f()

# 6