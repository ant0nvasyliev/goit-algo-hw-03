from datetime import datetime


def get_days_from_today(date):
    today = datetime.today().date()
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Формат дати має бути 'YYYY-MM-DD'.")
        return

    date_difference = input_date - today
    return date_difference.days


print(get_days_from_today('202-12-31'))
print(get_days_from_today('2024-09-22'))
print(get_days_from_today('2024-10-22'))
