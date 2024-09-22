import re


def format_phone_number(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number)

    if phone_number.startswith('380'):
        return '+' + phone_number

    elif phone_number.startswith('0'):
        return '+380' + phone_number[1:]

    elif phone_number.startswith('+'):
        return phone_number

    else:
        return '+380' + phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [format_phone_number(
    phone_number) for phone_number in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567',
#  '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
