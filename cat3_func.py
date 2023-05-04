import datetime
import random
from datetime import datetime

user_accounts = {
    "12345678": {"type": "Дебетовий", "name": "John Smith", "transactions": [], "balance": 0.0},
    "87654321": {"type": "Кредитний", "name": "Jane Doe", "transactions": [], "balance": 0.0},
    "65432198": {"type": "Дебетовий", "name": "Michael Johnson", "transactions": [], "balance": 0.0}
}

lst_accounts = ["12345678", "87654321", "65432198"]

user_categories = ["Їжа", "Одяг і взуття", "Розваги", "Транспорт", "Комунальні послуги", "Оплата житла",
                   "Здоров'я та медицина", "Подарунки та благодійність", "Краса та гігієна",
                   "Офісні витрати", "Домашні тварини", "Подорожі", "Освіта та розвиток", "Перекази", "Інші витрати"]

lst_transfer = {}


def generate_random_date():
    """Генерация даты"""
    current_time = datetime.datetime.now()
    time_speed = random.uniform(0, 400)  # случайное значение скорости времени
    step = datetime.timedelta(days=1)
    current_time += step * time_speed
    year = current_time.year
    month = current_time.month
    day = current_time.day
    return f"{day:02d}.{month:02d}.{year}"


def generate_transaction_id():
    """Генерация id"""
    rand_num = random.randint(100000, 999999)
    new_transaction_id = f"TRX{rand_num}"
    return new_transaction_id


def display_balance(account_num):
    """Отображение баланса"""
    balance_info = user_accounts.get(account_num)
    print("Баланс: {:,.2f} грн".format(balance_info.get("balance")))


def display_account_info(account_num):
    """Отображение информации конкретного счета"""
    print("Номер Рахунку: {}".format(account_num))
    print(f"ПІБ: {user_accounts[account_num]['name']}")
    print(f"Тип: {user_accounts[account_num]['type']}")
    display_balance(account_num)
    print()


def display_transactions(account_num):
    """Отображение транзакций"""
    transactions = user_accounts[account_num]["transactions"]
    if len(transactions) != 0:
        display_account_info(account_num)
        print("Транзакції: ")
        for i, transaction in enumerate(transactions):
            print(
                f"{i + 1}. {transaction['date']} | {transaction['category']} | {transaction['transaction']}"
                f" | id:{transaction['transaction_id']}")
        print("-------------------------------------------------------------------------------------------------------")
    else:
        print("Транзакцій на рахунку: {} не знайдено".format(account_num))


def lst_user_acc():
    """Список транзакций"""
    if len(user_accounts) == 0:
        print("Рахунків нема")
    else:
        print("Список рахунків:\n")
        for elem, info in user_accounts.items():
            display_account_info(elem)

    print("----------------------------------------------------------------------------------------------------------")


def add_trans(arg1, arg3, arg4):
    """Добавление Транзакции"""
    trans_id = generate_transaction_id()
    account_num = arg1
    date, category, transaction = generate_random_date(), arg3, arg4
    lst_user_acc()
    transactions = user_accounts[account_num]["transactions"]
    balance = user_accounts[account_num]["balance"]
    transactions.append({"transaction_id": trans_id, "date": date, "category": category, "transaction": transaction})
    balance += float(transaction)
    user_accounts[account_num]["transactions"] = transactions
    user_accounts[account_num]["balance"] = balance
    print("Транзакцію додано")
    print("{} | {} | {} | id:{}\n".format(date, category, transaction, trans_id))
    display_account_info(account_num)


def delete_transfer_transaction(account_num, transaction_id):
    """Удаление перевода со второго счета"""
    transaction_info = lst_transfer[transaction_id]
    account_num1 = transaction_info["to_account"]  # если удаляется транзакция со счета получателя True
    account_num2 = transaction_info["from_account"]  # если удаляется транзакция со счета отправителя False

    verify = "2"
    if account_num == account_num2:
        verify = "1"

    def delete(account_number):
        transactions = user_accounts[account_number]["transactions"]
        for elem in transactions:
            if transaction_id == elem["transaction_id"]:
                print("id транзакции на втором счету найден")
                transaction_amount = float(elem["transaction"])
                if transaction_amount > 0:
                    balance = user_accounts[account_number]["balance"] - transaction_amount
                else:
                    balance = user_accounts[account_number]["balance"] + abs(transaction_amount)
                transactions.remove(elem)
                user_accounts[account_number]["transactions"] = transactions
                user_accounts[account_number]["balance"] = balance
                break

    if verify == "1":
        delete(account_num1)
    elif verify == "2":
        delete(account_num2)

    del lst_transfer[transaction_id]


def delete_transaction(account_num, transaction, transactions):
    """Удаление обычной транзакции"""
    """account_num: номер счета, transaction: словарь транзакции в списке,
    transactions: список транзакций указанного счета """

    transaction_amount = float(transaction["transaction"])
    if transaction_amount > 0:
        balance = user_accounts[account_num]["balance"] - transaction_amount
    else:
        balance = user_accounts[account_num]["balance"] + abs(transaction_amount)
    transactions.remove(transaction)
    user_accounts[account_num]["transactions"] = transactions
    user_accounts[account_num]["balance"] = balance


def delete_transactions(arg1):
    """Удаление Транзакций"""
    account_num = arg1
    transactions = user_accounts[account_num]["transactions"]
    display_transactions(account_num)
    transaction_id = input("Введіть id транзакції: ")
    for elem in transactions:
        if transaction_id == elem["transaction_id"]:
            if elem["category"] == "Перекази":
                transfer_transaction = elem
                delete_transaction(account_num, transfer_transaction, transactions)
                delete_transfer_transaction(account_num, transaction_id)
            else:
                transaction = elem
                delete_transaction(account_num, transaction, transactions)
    print("Транзакція видалена")


def transfer_money(num1, num2):
    """Перевод денег между счетами"""
    # from num1 = input_num()
    # to num2 = input_num()
    transfer_id = generate_transaction_id()
    date1 = generate_random_date()
    category = "Перекази"
    if user_accounts[num1]["balance"] != 0.0:
        display_account_info(num1)
        amount = float(input("Введіть суму для переводу: "))

        trans1 = "-{:.2f}".format(amount)
        trans2 = "+{:.2f}".format(amount)

        if user_accounts[num1]["balance"] >= amount:
            user_accounts[num1]["balance"] -= amount
            user_accounts[num2]["balance"] += amount
            user_accounts[num1]["transactions"].append(
                {"transaction_id": transfer_id, "date": date1, "category": category, "transaction": trans1})

            user_accounts[num2]["transactions"].append(
                {"transaction_id": transfer_id, "date": date1, "category": category, "transaction": trans2})
            print("\nПереказ виконано\n")

            lst_transfer[transfer_id] = {"date": date1, "from_account": num1, "to_account": num2, "amount": amount}
            print("---------------------------------------------------------------------------------------------------")

        else:
            print("Недостатньо коштів на рахунку")
    else:
        print("Баланс рахунку: {} пустий".format(num1))

    def get_expenses_income_by_period(self):
        self.display_all_num()
        num = self.input_num()
        print("""Для перевірки витрат і прибутків за певний період, будь ласка, введіть дату початку періоду та дату 
        його завершення. Формат дати має бути наступним: день.місяць.рік (наприклад, 01.05.2023)""")

        start_date_input = input("Введіть дату початку періоду: ")
        date_end_input = input("Введіть дату кінця періоду: ")

        start_date = datetime.strptime(start_date_input, "%d.%m.%Y")
        end_date = datetime.strptime(date_end_input, "%d.%m.%Y")
        income = 0
        expense = 0
        transactions = self.user_accounts[num]["transactions"]
        for transaction in transactions:
            transaction_date = datetime.strptime(transaction['date'], "%d.%m.%Y")
            transaction_amount = float(transaction['transaction'][1:])
            transaction_type = transaction['transaction'][0]
            if start_date <= transaction_date <= end_date:
                if transaction_type == '+':
                    income += transaction_amount
                elif transaction_type == '-':
                    expense += transaction_amount
        return f"Для введеного Вами періоду часу, загальна сума витрат становить {expense:,.2f} гривень. " \
               f"Також, загальний прибуток за цей період склав {income:,.2f} гривень. " \
               "Дякую, що користуєтесь нашим сервісом!"


add_trans("12345678", "Їжа", "+150")
display_transactions("12345678")
transfer_money("12345678", "65432198")
print(
    "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(user_accounts["12345678"]["transactions"])
print(user_accounts["65432198"]["transactions"])
print(lst_transfer)
