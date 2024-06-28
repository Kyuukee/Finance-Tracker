
#first_name = "Que"
#last_name = "Scott"
#full_name = first_name + " " + last_name

#print("Hello " + full_name)

#age = 31
#print(full_name + " You are " + str(age))

#human = True
#print("Are you a human: " + str(human))

#name = input("What is your name?: ")
#age = input("How old are you?: ")
#print("Hello " + name)

#name = input("What is your name?: ")
#age = input("How old are you?: ") 

#print("Hello " + name, "You are " + age, "Years old!")

'''age = int(input("How old are you?: "))

if age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You are a not born yet!")
else:
    print("You are a child!")'''
'''
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'bill': 'javascript',
    'sally': 'HTML'
            }

for name, lang in fav_lang.items():
    print(lang.title())
    '''
'''
def start():
    print("Welcome to my LEFTOVER app")

start()

print("\nPlease enter the following info...")
credit = input("Credit Card Debt: $")
pay = input("Pay: $")
rent = input("Rent: $")
insurance = input("Car Insurance: $")
phone = input("Phone Bill: $")
food = input("Food Expenses: $")
gas = input("Gas: $")

print(f"Credit: ${credit.title()}")
print(f"Pay: ${pay.title()}")
print(f"Rent: ${rent.title()}")
print(f"Car Insurance: ${insurance.title()}")
print(f"Phone Bill: ${phone.title()}")
print(f"Food Expenses: ${food.title()}")
'''



print("Please enter your monthly expenses...")

def expenses_input(prompt):
    user_input = input(prompt)
    if user_input == "":
        print("That is not a valid input!")
    elif user_input < 0.0:
        print("There's no way you're that broke!")
    else:
        pass

    expenses = {
        'Food': int(input("Food: $")),
        'Rent/Utilities': float(input("Rent/Utilities: $")),
        'Car Insurance': float(input("Car Insurance: $")),
        'Phone Bill': float(input("Phone Bill: $")),
        'Credit Card Debt': float(input("Credit Card Debt: $")),
        'Random': float(input("Random: $"))
    }

pay = float(input("Pay: $"))

monthly_expenses = sum(expenses.values())
weekly_expenses = monthly_expenses / 4
yearly_expenses = weekly_expenses * 52
monthly_savings = pay - monthly_expenses
weekly_savings = monthly_savings / 4
yearly_savings = weekly_savings * 52


print(f"\nTotal Weekly Expenses: ${weekly_expenses}")
print("-------------------------------")
print(f"Total Monthly Expenses: ${monthly_expenses}")
print("-------------------------------")
print(f"Total Yearly Expenses: ${yearly_expenses}")
print("-------------------------------")
print(f"Potential Weekly Savings: ${weekly_savings}")
print("-------------------------------")
print(f"Potential Monthly Savings: ${monthly_savings}")
print("-------------------------------")
print(f"Potential Yearly Savings: ${yearly_savings}")

