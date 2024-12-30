import datetime

def get_upcoming_birthdays(users):
    today = datetime.date.today()  
    upcoming_birthdays = []

 
    for user in users:
       
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()

    
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday.replace(year=today.year)

        # високосний рік
        if birthday.month == 2 and birthday.day == 29:
            
            if not (today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)):
                # Якщо сьогодні не високосний рік, перенесіть день народження на наступний високосний рік
                birthday = birthday.replace(year=today.year + 4)

        # різниця в днях між сьогоднішнім днем і датою народження
        delta = (birthday - today).days

        if 0 <= delta <= 7 or delta == 365 or delta == 366:
            
            if birthday.weekday() == 5:  # Субота
                birthday = birthday + datetime.timedelta(days=2)  # Move to Monday
            elif birthday.weekday() == 6:  #Неділя
                birthday = birthday + datetime.timedelta(days=1)  # Move to Monday

           
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays



users = [ 
    {"name": "John Doe", "birthday": "1985.12.31"},
    {"name": "Jane Smith", "birthday": "1990.01.02"},
    {"name": "John Doe2", "birthday": "1990.12.25"},
    {"name": "John Doe3", "birthday": "1985.12.30"},
    {"name": "John Doe4", "birthday": "1992.12.31"},
    {"name": "John Doe5", "birthday": "1987.01.01"},
    {"name": "John Doe6", "birthday": "1995.12.29"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
