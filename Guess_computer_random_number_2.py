import random


def guess(x):
    random_number = random.randint(1, x)
    random_number = 753
    guess = 0
    while guess:
        guess = int(input(f"guess a number: "))


guess(100)