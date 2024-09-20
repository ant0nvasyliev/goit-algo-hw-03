import random


def get_numbers_ticket(min, max, quantity):
    numbers = []
    if min >= 1 and max <= 1000 and quantity <= (max - min):
        numbers = random.sample(range(min, max), quantity)
        print("Ваші лотерейні числа:", sorted(numbers))
    else:
        print("Empty list")
        return []


get_numbers_ticket(1, 49, 6)
