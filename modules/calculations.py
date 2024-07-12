#This file will be used to calculate the sum of money (+) and (-)
# And also some other calculations
from datetime import datetime
from constants import ROUND_TO_DIGIT

class Calculator:
    general_sum = 0  #sum of both incomes and expenses
    expenses_sum = 0  #sum of expenses (only negative values)
    income_sum = 0  #sum of income (only positive values)
    today_general_sum = 0
    today_expenses_sum = 0
    today_income_sum = 0

    def __init__(self) -> None:
        pass

    @staticmethod
    def check_date(date):
        date = datetime.strptime(date, '%d-%m-%Y')
        if date.date() == datetime.today().date():
            return 1
        else:
            return 0
    @staticmethod
    def round_everything():
        everyting = [Calculator.general_sum,
                     Calculator.expenses_sum,
                     Calculator.income_sum, 
                     Calculator.today_expenses_sum,
                     Calculator.today_general_sum,
                     Calculator.today_income_sum]
        rounded_values = [round(variable, ROUND_TO_DIGIT) for variable in everyting]
        variable_names = ["general_sum", "expenses_sum", "income_sum", "today_expenses_sum", "today_general_sum", "today_income_sum"]
        for i, variable in enumerate(variable_names):
            globals()[variable] = rounded_values[i]

    @staticmethod
    def sum(value, date):
        is_today_multiplier = Calculator.check_date(date)
        print(is_today_multiplier)
        try:
            value = float(value)
        except:
            print(f"Sorry, you can't do math on '{value}' because it's {type(value)}. What have you thought?")
            return
        Calculator.general_sum += value
        Calculator.today_general_sum += (value*is_today_multiplier)
        if value < 0:
            Calculator.expenses_sum += value
            print(value)
            Calculator.today_expenses_sum += (value*is_today_multiplier)
        if value > 0:
            Calculator.income_sum += value
            Calculator.today_income_sum += (value*is_today_multiplier)
        Calculator.round_everything()
