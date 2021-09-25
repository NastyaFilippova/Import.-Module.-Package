import requests
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

today = date.today()

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Today: {today}')
