import re
def normalize_phone(phone_number):
    # Видаляємо всі символи, які не є цифрами або знаком "+"
    phone_number = re.sub(r'[^0-9+]', '', phone_number.strip())
    
    # Якщо номер починається з "38" (але без "+"), додаємо "+" на початок
    if phone_number.startswith('38') and not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    # Якщо номер не починається з "+", додаємо код країни "+38"
    if not phone_number.startswith('+'):
        phone_number = '+38' + phone_number.lstrip('0')  # Видаляємо початкові нулі
    
    # Якщо номер починається з "+38", перевіряємо, чи є після нього нуль
    if phone_number.startswith('+38'):
        # Якщо після "+38" немає нуля, додаємо його
        if len(phone_number) == 3 or phone_number[3] != '0':
            phone_number = '+38' + '0' + phone_number[3:].lstrip('0')

    # Переконуємося, що номер має рівно 13 символів
    if len(phone_number) != 13:
        raise ValueError("The phone number must be 13 characters long, including the country code.")

    return phone_number

# print(normalize_phone("    +38(050)123-32-34"))  
# print(normalize_phone("              0503451234"))       
# print(normalize_phone("(050)8889900"))         
# print(normalize_phone("38050-111-22-22"))       
# print(normalize_phone("38050 111 22 11   "))     
# print(normalize_phone("+38 681112211"))          
# print(normalize_phone("+38 50112211"))         
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

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

