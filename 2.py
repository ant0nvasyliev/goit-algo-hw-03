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
# Ваші лотерейні числа: [15, 16, 17, 21, 22, 44]

get_numbers_ticket(0, 49, 6)
# Empty list
