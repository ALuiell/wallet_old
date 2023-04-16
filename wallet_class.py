
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

class Categories:

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


class CategoryOne(Categories):
    print("welcome to the categories_two")

    def add_category(self):
        print("add_category")

    def remove_category(self):
        print("remove_cat")

    def update_category(self):
        print("welcome to the update_category")

    def list_category(self):
        print("welcome to the list_category")

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
       print("welcome to the add_user_acc")

    def remove_user_acc(self):
        print('welcome to the remove_user_acc')

    def change_user_acc(self):
        print('welcome to the change_user_acc')

    def list_users_acc(self):
        print('welcome to the list_users_acc')

    def balance_users_acc(self):
        print("welcome to the balance_users_acc")

    functional = {
        1: add_user_acc,
        2: remove_user_acc,
        3: change_user_acc,
        4: list_users_acc,
        5: balance_users_acc,
        6: self.return_to_menu
    }

    def menu_cat2(self):
        self.print_subcategory_menu(self.bank_account)
        self.menu_universal(6, functional)

    while True:
        menu_cat2()


class CategoryThree(Categories):
    print("welcome to the categories_three")

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

    functional = {
        1: add_expense,
        2: add_income,
        3: transfer_money,
        4: check_transactions,
        5: get_statistics,
        6: self.return_to_menu
    }

    def menu_cat3(self):
        self.print_subcategory_menu(self.income_expense_management)
        self.menu_universal(6, functional)

    while True:
        menu_cat3()


class CategoryFour(Categories):
    print("welcome to the categories_four")

    def search_by_category(self):
        print("welcome to the search_by_category ")
        pass

    def search_by_amount_date(self):
        print("welcome to the search_by_amount_date ")
        pass

    functional = {
        1: search_by_category,
        2: search_by_amount_date,
        3: self.return_to_menu
    }

    def menu_cat4(self):
        self.print_subcategory_menu(self.income_expense_management)
        self.menu_universal(3, functional)

    while True:
        menu_cat4()


class Menu:

    def __init__(self):
        self.main_menu_options = main_menu_options
        self.cat1 = CategoryOne()
        self.cat2 = CategoryTwo()
        self.cat3 = CategoryThree()
        self.cat4 = CategoryFour()

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
            1: None,
            2: None,
            3: None,
            4: None,
            5: None
        }
        try:
            choice = int(input("Введіть потрібний пункт: "))
            self.menu_loop(choice, 5, menu_dict)
        except ValueError:
            print("\nВи ввели неправильне значення. Спробуйте ще раз.\n")
            self.main_menu()

test = Menu()
test.main_menu()
