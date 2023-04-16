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


class Menu:

    def __init__(self):
        self.main_menu_options = main_menu_options

    @staticmethod
    def menu_loop(name_var, num, dictionary):
        while True:
            if name_var <= num and name_var != 0:
                for key, val in dictionary.items():
                    if name_var == key:
                        val()
                break
            else:
                print("Щось пішло не так, введіть число від 1 до", num)
                break

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


class Categories:

    def __init__(self):
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

    @staticmethod
    def print_subcategory_menu(lst):
        for i, elem in enumerate(lst, start=1):
            print(f"{i}.{elem}")

    def return_to_menu(self):
        print("welcome to the main menu")
        self.main_menu()

    def menu_universal(self, menu_cat, num, functional):
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu_loop(choice, num, functional)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")
            menu_cat(num, functional)


class CategoryOne(Categories):

    def add_category(self):
        name = input("Введіть назву нової категорії: ")
        self.user_categories.append(name)
        if name in self.user_categories:
            print("Категорію додано")

    def remove_category(self):
        name = input("Введіть назву категорії: ")
        if name in self.user_categories:
            for elem in self.user_categories:
                if name == elem:
                    self.user_categories.remove(elem)
                    if name not in self.user_categories:
                        print("Категорія видалена")
        elif name not in self.user_categories:
            print("Категорію не знайдено")

    def update_category(self):
        name = input("Введіть назву категорії, яку потрібно змінити: ")
        if name in self.user_categories:
            index = self.user_categories.index(name)
            new_name = input("Введіть назву категорії: ")
            self.user_categories[index] = new_name
            print("Назван категорії оновлена")
        else:
            print("Категорія не знайдена")

    def list_category(self):
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

class CategoryTwo(Categories):

    def add_user_acc(self):
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


class CategoryThree(Categories):
    pass


class CategoryFour(Categories):
    pass




