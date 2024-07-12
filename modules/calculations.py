#This file will be used to calculate the sum of money (+) and (-)
# And also some other calculations
from datetime import datetime

general_sum = 0  #sum of both incomes and expenses
expenses_sum = 0  #sum of expenses (only negative values)
income_sum = 0  #sum of income (only positive values)

today_general_sum = 0
today_expenses_sum = 0
today_income_sum = 0


def check_date(date):
    date = datetime.strptime(date, '%d-%m-%Y')
    if date.date() == datetime.today().date():
        return 1
    else:
        return 0

def round_everything():
    global variable
    everyting = [general_sum, expenses_sum, income_sum, today_expenses_sum, today_general_sum, today_income_sum]
    for variable in everyting:
        variable = round(variable,2)
        print(variable)


def sum(value, date):
    global general_sum, expenses_sum, income_sum, today_general_sum, today_expenses_sum ,today_income_sum
    is_today_multiplier = check_date(date)
    print(is_today_multiplier)
    try:
        value = float(value)
    except:
        print(f"Sorry, you can't do math on '{value}' because it's {type(value)}. What have you thought?")
        return
    general_sum += value
    today_general_sum += (value*is_today_multiplier)
    print(today_general_sum)
    if value < 0:
        expenses_sum += value
        print(value)
        today_expenses_sum += (value*is_today_multiplier)
    if value > 0:
        income_sum += value
        today_income_sum += (value*is_today_multiplier)
    round_everything()
