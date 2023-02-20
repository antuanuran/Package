from application.salary import calculate_salary
from application.db.people import get_employees
from colorama import Fore, Style


if __name__ == '__main__':
    a = input(Fore.BLUE + '\nХотите рассчитать зарплату сотрудников? (y/n)')
    if (a == 'y'):
        calculate_salary()

        b = input(Style.BRIGHT + Fore.GREEN + '\nХотите получить список всех сотрудников? (y/n)')
        if (b == 'y'):
            get_employees()


    else:
        b = input(Style.RESET_ALL + '\nХотите получить список всех сотрудников? (y/n)')
        if (b == 'y'):
            get_employees()

