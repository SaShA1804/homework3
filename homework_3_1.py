from datetime import datetime

def get_date_input():
    while True:
        try:
            date_string = input("Будь ласка, введіть дату у форматі рік-місяць-день (наприклад, 2024-06-26): ")
            datetime.strptime(date_string, "%Y-%m-%d")
            return date_string
        except ValueError:
            print("Дата введена неправильно, спробуйте ще раз.")

def get_days_from_today(date):
    try:
        date_time_input = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = date_time_input - today
        return difference.days
    except ValueError:
        print("Формат дати невірний. Будь ласка, введіть дату у форматі рік-місяць-день (наприклад, 2024-06-26).")
        return None

date = get_date_input()

difference_result = get_days_from_today(date)

if difference_result is not None:
    print(f"Різниця між датами: {difference_result} днів")
