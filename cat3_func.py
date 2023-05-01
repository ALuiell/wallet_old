
import datetime
import random

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
    current_time = datetime.datetime.now()
    time_speed = random.uniform(0, 400)  # случайное значение скорости времени
    step = datetime.timedelta(days=1)
    current_time += step * time_speed
    year = current_time.year
    month = current_time.month
    day = current_time.day
    return f"{day:02d}.{month:02d}.{year}"


def display_balance(account_num):
    balance_info = user_accounts.get(account_num)
    print("Баланс: {:,.2f} грн".format(balance_info.get("balance")))


def display_account_info(account_num):
    print("Номер Рахунку: {}".format(account_num))
    print(f"ПІБ: {user_accounts[account_num]['name']}")
    print(f"Тип: {user_accounts[account_num]['type']}")
    display_balance(account_num)
    print()


def lst_user_acc():
    if len(user_accounts) == 0:
        print("Рахунків нема")
    else:
        print("Список рахунків:\n")
        for elem, info in user_accounts.items():
            display_account_info(elem)

    print("----------------------------------------------------------------------------------------------------------")


def display_transactions(account_num):
    transactions = user_accounts[account_num]["transactions"]
    if len(transactions) != 0:
        display_account_info(account_num)
        print("Транзакції: ")
        for i, transaction in enumerate(transactions):
            print(f"{i + 1}. {transaction['date']} | {transaction['category']} | {transaction['transaction']}")
        print("-------------------------------------------------------------------------------------------------------")
    else:
        print("Транзакцій не знайдено")


def add_trans(arg1, arg2, arg3, arg4):
    account_num = arg1
    date, category, transaction = arg2, arg3, arg4
    lst_user_acc()
    transactions = user_accounts[account_num]["transactions"]
    balance = user_accounts[account_num]["balance"]
    transactions.append({"date": date, "category": category, "transaction": transaction})
    balance += float(transaction)
    user_accounts[account_num]["transactions"] = transactions
    user_accounts[account_num]["balance"] = balance
    print("Транзакцію додано")
    print("{} | {} | {}\n".format(date, category, transaction))
    display_account_info(account_num)


def generate_transaction_id():
    rand_num = random.randint(100000, 999999)
    new_transaction_id = f"TRX{rand_num}"
    return new_transaction_id


def delete_transaction1(arg1):
    account_num = arg1
    transactions = user_accounts[account_num]["transactions"]
    display_transactions(account_num)
    transaction_index = int(input("Enter the number of the transaction to delete: ")) - 1
    transaction = transactions[transaction_index]
    transaction_amount = float(transaction["transaction"])
    if transaction_amount > 0:
        balance = user_accounts[account_num]["balance"] - transaction_amount
    else:
        balance = user_accounts[account_num]["balance"] + abs(transaction_amount)
    del transactions[transaction_index]
    user_accounts[account_num]["transactions"] = transactions
    user_accounts[account_num]["balance"] = balance
    print("Транзакція видалена")
    display_account_info(account_num)


def transfer_money(num1, num2):
    # from num1 = input_num()
    # to num2 = input_num()
    transfer_id = generate_transaction_id()
    date1 = generate_random_date()
    category = "Перекази"
    if user_accounts[num1]["balance"] != 0.0:
        display_account_info(num1)
        amount = float(input("Введіть суму для переводу: "))
        trans1 = -amount
        trans2 = "+{}".format(amount)
        if user_accounts[num1]["balance"] >= amount:
            user_accounts[num1]["balance"] -= amount
            user_accounts[num2]["balance"] += amount
            user_accounts[num1]["transactions"].append(
                {"transactions_id": transfer_id, "date": date1, "category": category, "transaction": trans1})

            user_accounts[num2]["transactions"].append(
                {"transactions_id": transfer_id, "date": date1, "category": category, "transaction": trans2})
            print("\nПереказ виконано\n")

            lst_transfer[transfer_id] = {"date": date1, "from_account": num1, "to_account": num2, "amount": amount}
            print("---------------------------------------------------------------------------------------------------")

        else:
            print("Недостатньо коштів на рахунку")
    else:
        print("Баланс рахунку: {} пустий".format(num1))


add_trans("12345678", "31.04.2023", "Їжа", "+150")
print("---------------------------------------------------------------------------------------------------")
transfer_money("12345678", "65432198")
print("---------------------------------------------------------------------------------------------------")

display_transactions("12345678")
display_transactions("65432198")
lst_user_acc()
delete_transaction1("12345678")
lst_user_acc()
