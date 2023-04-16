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
        self.cat1 = CategoryOne()
        #self.cat2 = CategoryTwo()
        #self.cat3 = CategoryThree()
        #self.cat4 = CategoryFour()

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

        menu_dict = {
            1: self.cat1.run_menu,
            #2: self.cat2.run_menu(),
            #3: self.cat3.run_menu(),
            #4: self.cat4.run_menu(),
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
        # Category1
        self.menu_categories = menu_categories
        # список созданных пользователем категорий
        self.user_categories = []
        # Category2
        self.bank_account = bank_account
        self.user_accounts = user_accounts
        # Category3
        self.income_expense_management = income_expense_management
        # Category4
        self.search_transactions_op = search_transactions_op
        self.menu = Menu()

    @staticmethod
    def print_subcategory_menu(lst):
        for i, elem in enumerate(lst, start=1):
            print(f"{i}.{elem}")

    def return_to_menu(self):
        print("welcome to the main menu")
        self.menu.main_menu()

    def menu_universal(self, num, functional):
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu.menu_loop(choice, num, functional)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")


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
        5: Categories.return_to_menu
    }

    @staticmethod
    def menu_cat1():
        categories = Categories()
        Categories.print_subcategory_menu(categories.menu_categories)
        categories.menu_universal(5, CategoryOne.functional)

    def run_menu(self):
        while True:
            self.menu_cat1()


test = Menu()
test.main_menu()
