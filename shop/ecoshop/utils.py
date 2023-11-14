# import time
#

import time
#
# def add_friend(name,age):
#     if name in friends:
#         return friends[name]
#     else:
#         time.sleep(5)
#         friends[name]=age
#         return friends[name]
#
# print(add_friend("Max",22))
#
# print(add_friend("Kate", 23))
#
# print(add_friend("Max", 23))
from functools import lru_cache

# friends = {}


# @lru_cache
# def add_friend(name):
#     if name not in friends:
#         time.sleep(5)
#         friends["name"] = 0
#     return name
#
# print(add_friend("Max"))
# print(add_friend("Kate"))
# print(add_friend("Max"))
# import random
# import datetime

# @lru_cache
# def add_number(number,*args):
#     time.sleep(5)
#     return number + random.randint(1,10)

# print(add_number(3))
# print(add_number(3,12))
# print(add_number(1))
# print(add_number(1,9))
# print(add_number(3,45))
# print(add_number(3,12))
#
# @lru_cache
# def get_current_time(current_time):
#     time.sleep(7)
#     return current_time
#
# print(get_current_time(datetime.datetime.utcnow()))
# print(get_current_time(datetime.datetime.utcnow()))
# print(get_current_time(datetime.datetime.utcnow()))
# print(get_current_time(datetime.datetime.utcnow()))
# print(get_current_time(datetime.datetime.utcnow()))