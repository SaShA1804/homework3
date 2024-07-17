from datetime import datetime

def get_date_input():
    while True:
        try:
            date_string = input("Будь ласка, введіть дату у форматі день-місяць-рік (наприклад,2024-06-26 ): ")
            datetime.strptime(date_string, "%Y-%m-%d")
            return date_string
        except ValueError:
            print("Дата введена неправильно, спробуйте ще раз")
       
def get_days_from_today(date):
    # Преобразование строки даты в объект datetime
    date_time_input = datetime.strptime(date, "%Y-%m-%d").date()
    today = datetime.today().date()
    # Вычисление разницы в днях
    difference = date_time_input - today
    return difference.days

# Отримання дати від користувача
date = get_date_input()
# Обчислення різниці в днях
difference_result = get_days_from_today(date)
# Виведення результату
print(f"Різниця між датами: {difference_result} днів")

