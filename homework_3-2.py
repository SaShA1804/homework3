import random

def get_user_input():
    while True:
        
        min_number = int(input("Введіть мінімальний номер лотерейних квитків: "))
        max_number = int(input("Введіть максимальний номер лотерейних квитків: "))
        quantity = int(input("Введіть кількість виграшних лотерейних квитків: "))
        return(min_number,max_number,quantity)
            
def get_numbers_ticket(min_number, max_number, quantity):
    list_ticket={}
    try:
        if min_number < 1:
            return list_ticket
            
        if max_number > 1000:
           return list_ticket 
 
        if quantity > (max_number - min_number + 1):
            return list_ticket

    except ValueError:
        return(print("Введіть ціле число."))

     
    list_ticket = list(range(min_number, max_number + 1))  
    victory_tickets = random.sample(list_ticket, quantity)  
    victory_tickets.sort()  
    return victory_tickets

# Отримання введення від користувача
min_number, max_number, quantity = get_user_input()

# Отримання виграшних номерів квитків
ticket_numbers = get_numbers_ticket(min_number, max_number, quantity)

# Виведення виграшних номерів
print("Виграшні номери квитків:", ticket_numbers)
