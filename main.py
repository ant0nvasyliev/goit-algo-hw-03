from datetime import datetime


def get_days_from_today(date):
    date_difference = datetime.strptime(date, "%Y-%m-%d") - datetime.today()
    return date_difference.days


print(get_days_from_today('2024-10-20'))
