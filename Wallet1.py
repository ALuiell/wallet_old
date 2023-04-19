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
                             "Отримання статистики прибутків/витрат за певний період по днях,по категоріях",
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

    @staticmethod
    def menu_loop(name_var, num, dictionary):
        func = dictionary.get(name_var)
        if func is None:
            print("Щось пішло не так, введіть число від 1 до", num)
        func()

    @staticmethod
    def the_end():
        quit()

    def main_menu(self):
        print("1.{} \n2.{} \n3.{} \n4.{} \n5.{} \nОберіть потрібну цифру: от 1 до 5: "
              .format(*self.main_menu_options))
        cat = Categories()

        menu_dict = {
            1: cat.categories_one,
            2: cat.categories_two,
            3: cat.categories_three,
            4: cat.categories_four,
            5: self.the_end
        }

        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu_loop(choice, 5, menu_dict)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")
            self.main_menu()


class Categories(Wallet):

    @staticmethod
    def print_subcategory_menu(lst):
        for i, elem in enumerate(lst, start=1):
            print(f"{i}.{elem}")

    def return_to_menu(self):
        print("welcome to the main menu")
        self.main_menu()

    def menu_universal(self, num, functional):
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu_loop(choice, num, functional)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")

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

        functional = {
            1: add_category,
            2: remove_category,
            3: update_category,
            4: list_category,
            5: self.return_to_menu
        }

        def menu_cat1():
            self.print_subcategory_menu(self.menu_categories)
            self.menu_universal(5, functional)

        while True:
            menu_cat1()

    def categories_two(self):
        print("welcome to the categories_two")

        def add_user_acc():
            # выпилить 2 категории, 1 словарь хранящий в себе номер счета который хранит в себе 1)тип счета, 2)деньги
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

        def remove_user_acc():
            print('welcome to the remove_user_acc')

        def change_user_acc():
            print('welcome to the change_user_acc')

        def list_users_acc():
            print('welcome to the list_users_acc')

        def balance_users_acc():
            print("welcome to the balance_users_acc")

        functional = {
            1: add_user_acc,
            2: remove_user_acc,
            3: change_user_acc,
            4: list_users_acc,
            5: balance_users_acc,
            6: self.return_to_menu
        }

        def menu_cat2():
            self.print_subcategory_menu(self.bank_account)
            self.menu_universal(6, functional)

        while True:
            menu_cat2()

    def categories_three(self):
        print("welcome to the categories_three")

        def add_expense():
            print("welcome to the add_expense ")
            pass

        def add_income():
            print("welcome to the add_income ")
            pass

        def transfer_money():
            print("welcome to the transfer_money ")
            pass

        def check_transactions():
            print("welcome to the check_transactions ")
            pass

        def get_statistics():
            print("welcome to the get_statistics ")
            pass

        functional = {
            1: add_expense,
            2: add_income,
            3: transfer_money,
            4: check_transactions,
            5: get_statistics,
            6: self.return_to_menu
        }

        def menu_cat3():
            self.print_subcategory_menu(self.income_expense_management)
            self.menu_universal(6, functional)

        while True:
            menu_cat3()

    def categories_four(self):
        print("welcome to the categories_four")

        def search_by_category():
            print("welcome to the search_by_category ")
            pass

        def search_by_amount_date():
            print("welcome to the search_by_amount_date ")
            pass

        functional = {
            1: search_by_category,
            2: search_by_amount_date,
            3: self.return_to_menu
        }

        def menu_cat4():
            self.print_subcategory_menu(self.income_expense_management)
            self.menu_universal(3, functional)

        while True:
            menu_cat4()


test = Wallet()
test.main_menu()
