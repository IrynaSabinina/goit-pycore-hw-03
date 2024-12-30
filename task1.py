from datetime import datetime

def get_days_from_today(date):
    # Перетворення рядка на об'єкт datetime
    input_date = datetime.strptime(date, '%Y-%m-%d')
    # Поточна дата
    today = datetime.today().date()
    # Різниця між датами
    delta = today - input_date.date()
    # Повернення кількості днів
    return delta.days

# Приклад використання
print(get_days_from_today('2024-01-01'))