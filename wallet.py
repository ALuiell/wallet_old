import os
import re

menu_categories = ["Додати категорію", "Видалити категорію", "Змінити дані про категорію",
                   "Перегляд списку категорій", "Назад"]
user_categories = []
bank_account = ["Створити новий рахунок", "Видалити рахунок", "Змінити дані рахунку",
                "Переглянути список рахунків", "Переглянути кошти на рахунку", "Назад"]

user_accounts = {}

income_expense_management = ["Додавання/видалення витрат до певного рахунку",
                             "Додавання/видалення прибутків до певного рахунку",
                             "Переведення грошей з рахунку на рахунок",
                             "Перевірка витрат/прибутків за певний період",
                             " Отримання статистики прибутків/витрат за певний період по днях, по категоріях",
                             "Назад"]
search_transactions_op = ["Можливість пошуку категорій, витрат прибутків за категорією",
                          "Можливість пошуку прибутку витрати за сумою датою", "Назад"]
main_menu_options = ["Управління категоріями витрат та доходів", "Управління рахунками",
                     "Управління витратами та доходами", "Пошук", "Вихід"]


class Wallet:

    def __init__(self):
        # 1 Управління категоріями витрат та доходів
        self.menu_categories = menu_categories
        # список созданных пользователем категорий
        self.user_categories = []
        # 2 Управління рахунками
        self.bank_account = bank_account
        # список созданных пользователем счетов
        self.user_accounts = user_accounts
        # 3 Управління витратами та доходами
        self.income_expense_management = income_expense_management
        # 4 Пошук
        self.search_transactions_op = search_transactions_op
        # 5 Головне меню
        self.main_menu_options = main_menu_options

    def return_to_menu(self):
        self.main_menu()

    def main_menu(self):

        try:
            menu_num = int(input("1.{} \n2.{} \n3.{} \n4.{} \n5.{} \nОберіть потрібну цифру: от 1 до 5: "
                                 .format(*self.main_menu_options)))

            if menu_num == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ви перейшли в меню '{}', що далі?".format(self.main_menu_options[0]))
                cat1 = Category()
                cat1.categories_one()

            elif menu_num == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ви перейшли в меню '{}', що далі?".format(self.main_menu_options[1]))
                bank_choice_score = int(input("1.{} \n2.{} \n3.{} \n4.{} \n5.{} \n6.{}: ".format(*self.bank_account)))

            elif menu_num == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ви перейшли в меню '{}', що далі?".format(self.main_menu_options[2]))
                management_category = int(input("1.{} \n2.{} \n3.{} \n4.{} \n5.{} \n6.{}: "
                                                .format(*self.income_expense_management)))


            elif menu_num == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ви перейшли в меню '{}', що далі?".format(self.main_menu_options[3]))
                search_transactions_options = int(input("1.{} \n2.{} \n{} : ".format(*self.search_transactions_op)))


            elif menu_num == 5:
                print("Гарного дня!.")
                quit()

        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")


class Category(Wallet):

    def menu_loop(self, name_var, num, dictionary):
        while True:
            if name_var <= num and name_var != 0:
                for key, val in dictionary.items():
                    if name_var == key:
                        val()
                break
            else:
                print("введіть число від 1 до", num)

    def categories_one(self):

        def add_category():
            name = input("Введіть назву нової категорії: ")
            self.user_categories.append(name)
            if name in self.user_categories:
                print("Категорію додано")

        def remove_category():
            name = input("Введіть назву категорії: ")
            if name in self.user_categories:
                for elem in self.user_categories:
                    if name == elem:
                        self.user_categories.remove(elem)
                        if name not in self.user_categories:
                            print("Категорія видалена")
            elif name not in self.user_categories:
                print("Категорію не знайдено")

        def update_category():
            name = input("Введіть назву категорії, яку потрібно змінити: ")
            if name in self.user_categories:
                index = self.user_categories.index(name)
                new_name = input("Введіть назву категорії: ")
                self.user_categories[index] = new_name
                print("Назван категорії оновлена")
            else:
                print("Категорія не знайдена")

        def list_category():
            print("Список категорій:")
            for elem in self.user_categories:
                print("".join(elem))

        def return_to_menu():
            self.main_menu()

        functional = {
            1: add_category,
            2: remove_category,
            3: update_category,
            4: list_category,
            5: return_to_menu
        }

        def menu_cat1():
            print("1.{} \n2.{} \n3.{} \n4.{} \n5.{}".format(*self.menu_categories))
            try:
                choice = int(input("Введіть потрібний пункт: "))
                self.menu_loop(choice, 5, functional)
            except ValueError:
                print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")
                menu_cat1()

        while True:
            menu_cat1()

    def categories_two(self):
        #выпилить 2 категории, 1 словарь хранящий в себе номер счета который хранит в себе 1)тип счета, 2)деньги
        def add_user_account():
            pattern = r'^\d{8}$'
            account_num = input("Номер рахунку має складатися з 8 цифр. Приклад: 12345678 \nВведіть номер рахунку: ")
            if re.match(pattern, account_num):
                account_type = int(input("Оберіть тип: \n1.дебетовий \n2.кредитний \nВведіть цифру 1 або 2: "))
                if account_type == "1":
                    user_accounts[account_num] = {"type": "debit", "transactions": []}
                elif account_type == "2":
                    user_accounts[account_num] = {"type": "credit", "transactions": []}
            else:
                print("Неправильный формат номера счета")

menu = Wallet()
menu.main_menu()
