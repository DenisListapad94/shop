# import time
#

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


#
# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )
#
import unittest


# class Fox:
#     pass

class Queue:
    POSSIBLE_STRATEGIES = ["FIFO","LIFO"]
    def __init__(self, strategy = "FIFO"):
        if strategy not in self.POSSIBLE_STRATEGIES:
            raise ValueError
        self.strategy = strategy


class TestQueue(unittest.TestCase):
    def test_queue_exist(self):
        queue = Queue()
        self.assertIsInstance(queue, Queue)

    def test_set_wrong_strategy(self):
        with self.assertRaises(ValueError):
            wrong_strategy = "FIFA"
            queue = Queue(wrong_strategy)


# class TestMethods(unittest.TestCase):
#
#
#     def test_mul(self):
#         val_1,val_2 = 3,4
#         mul = val_1 * val_2
#         self.assertEqual(mul ,12)
#
#     def test_summa(self):
#         val_1,val_2 = 3,4
#         summa = val_1 + val_2
#         self.assertEqual(summa ,6)


if __name__ == '__main__':
    unittest.main()
