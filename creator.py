import pathlib
from pathlib import Path
import random


def vale(msg):
    while True:
        try:
            x = int(input(msg))
            return x
            break
        except ValueError:
            print("wrong")


def perfect():
    return 1


def pos():
    return 2


def neg():
    return 3


def pos_neg():
    return 4


path = pathlib.Path().absolute()

path_instances = pathlib.PurePath(path, Path("instances_created"))

alpha = ['A', 'C', 'G', 'T']
instant = []
words = []

msg = "Length of generated instance: "
value1 = vale(msg)
msg = "Length of generated words "
value2 = vale(msg)
msg = "1 for perfect\n 2 for negative \n 3 for positive \n 4 for neg and pos "
chosen_one = vale(msg)

for i in range(value1):
    instant.append(alpha[random.randint(0, 3)])

switcher = {
    1: perfect,
    2: neg,
    3: pos,
    4: pos_neg
}
print(switcher[chosen_one]())