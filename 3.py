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


print(format_phone_number("+380 44 123 4567"))
