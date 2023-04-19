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
                             "Отримання статистики прибутків/витрат за певний період по днях, по категоріях",
                             "Назад"]
search_transactions_op = ["Можливість пошуку категорій, витрат прибутків за категорією",
                          "Можливість пошуку прибутку витрати за сумою датою", "Назад"]
main_menu_options = ["Управління категоріями витрат та доходів", "Управління рахунками",
                     "Управління витратами та доходами", "Пошук", "Вихід"]


class Menu:

    def __init__(self):
        self.main_menu_options = main_menu_options
        self.cat1 = CategoryOne
        self.cat2 = CategoryTwo
        self.cat3 = CategoryThree
        self.cat4 = CategoryFour

    @staticmethod
    def menu_loop(name_var, end, dictionary, menu_name=None):
        if name_var > end:
            print("Ви ввели неправильне значення. Спробуйте ще раз")
            menu_name()
        elif name_var <= end:
            func = dictionary.get(name_var)
            func()

    @staticmethod
    def the_end():
        quit()

    def main_menu(self):
        print("1.{} \n2.{} \n3.{} \n4.{} \n5.{} \nОберіть потрібну цифру: от 1 до 5: "
              .format(*self.main_menu_options))
        menu_dict = {
            1: self.cat1().menu_cat1,
            2: self.cat2().menu_cat2,
            3: self.cat3().menu_cat3,
            4: self.cat4().menu_cat4,
            5: self.the_end
        }
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu_loop(choice, 5, menu_dict, self.main_menu)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")
            self.main_menu()


class Categories:

    def __init__(self):
        # class Menu
        self.menu = Menu()

        # CategoryOne
        self.menu_categories = menu_categories
        self.user_categories = []

        # CategoryTwo
        self.bank_account = bank_account
        self.user_accounts = user_accounts

        # CategoryThree
        self.income_expense_management = income_expense_management

        # 4 CategoryFour
        self.search_transactions_op = search_transactions_op

        # 5 main_menu
        self.main_menu_options = main_menu_options

    @staticmethod
    def print_subcategory_menu(lst):
        for i, elem in enumerate(lst, start=1):
            print(f"{i}.{elem}")

    def return_to_menu(self):
        self.menu.main_menu()

    def menu_universal(self, num, functional, menu_name):
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu.menu_loop(choice, num, functional, menu_name)
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

    def menu_cat1(self):
        functional = {
            1: self.add_category,
            2: self.remove_category,
            3: self.update_category,
            4: self.list_category,
            5: self.menu.main_menu
        }
        while True:
            self.print_subcategory_menu(self.menu_categories)
            self.menu_universal(5, functional, self.menu_cat1)


class CategoryTwo(Categories):

    def add_user_acc(self):
       print("welcome to the add_user_acc")

    def remove_user_acc(self):
        print('welcome to the remove_user_acc')

    def change_user_acc(self):
        print('welcome to the change_user_acc')

    def list_users_acc(self):
        print('welcome to the list_users_acc')

    def balance_users_acc(self):
        print("welcome to the balance_users_acc")

    def menu_cat2(self):
        functional = {
            1: self.add_user_acc,
            2: self.remove_user_acc,
            3: self.change_user_acc,
            4: self.list_users_acc,
            5: self.balance_users_acc,
            6: self.menu.main_menu
        }
        while True:
            self.print_subcategory_menu(self.bank_account)
            self.menu_universal(6, functional, self.menu_cat2)


class CategoryThree(Categories):

    def add_expense(self):
        print("welcome to the add_expense ")
        pass

    def add_income(self):
        print("welcome to the add_income ")
        pass

    def transfer_money(self):
        print("welcome to the transfer_money ")
        pass

    def check_transactions(self):
        print("welcome to the check_transactions ")
        pass

    def get_statistics(self):
        print("welcome to the get_statistics ")
        pass

    def menu_cat3(self):
        functional = {
            1: self.add_expense,
            2: self.add_income,
            3: self.transfer_money,
            4: self.check_transactions,
            5: self.get_statistics,
            6: self.menu.main_menu
        }
        while True:
            self.print_subcategory_menu(self.income_expense_management)
            self.menu_universal(6, functional, self.menu_cat3)


class CategoryFour(Categories):

    def search_by_category(self):
        print("welcome to the search_by_category ")
        pass

    def search_by_amount_date(self):
        print("welcome to the search_by_amount_date ")
        pass

    def menu_cat4(self):
        functional = {
            1: self.search_by_category,
            2: self.search_by_amount_date,
            3: self.return_to_menu
        }
        while True:
            self.print_subcategory_menu(self.income_expense_management)
            self.menu_universal(3, functional, self.menu_cat4)


test = Menu()
test.main_menu()
