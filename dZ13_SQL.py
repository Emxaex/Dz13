import sqlite3
from warnings import onceregistry

sqlZapros = sqlite3.connect('bank.db')
bank=sqlZapros.cursor()



bank.execute(""" CREATE TABLE IF NOT EXISTS bank(
ph_number INTEGER,
name TEXT,
balance INTEGER);
""")


def add_client():
    name = input('Введите ваше ФИО: ')
    tel_numb = int(input('Введите ваш номер телефона'))
    total = int(input('Введите кол-во денег которое хотите добавить на ваш аккаунт: '))
    return bank.execute(f"""INSERT INTO bank(name,ph_number,balance) VALUES('{name}',{tel_numb},{total});""")


def add_balance():
    name = input('Введите ваше ФИО для пополнения баланса: ')
    summa = int(input('Сколько денег вы хотите добавить? '))

    balance = bank.execute(f"""SELECT balance FROM bank WHERE name='{name}' ;""").fetchone()
    his_balance=balance[0]

    Itog=his_balance+summa
    bank.execute(f"UPDATE bank SET balance='{Itog}' WHERE name='{name}';  ")
#добавление баланса

def minus_balance():
    name = input('Введите ваше ФИО для снятия баланса: ')
    summa = int(input('Сколько денег вы хотите снять? '))

    balance=bank.execute(f"SELECT balance FROM bank  WHERE name='{name}';").fetchone()
    his_balance=balance[0]
    Itog=his_balance-summa
    if Itog>0:
        bank.execute(f"UPDATE bank SET balance='{Itog}' WHERE name='{name}'; ")
    else:
        print('У вас нет такой суммы')
def show_info():
    vivod = bank.execute(f'SELECT name,balance,ph_number FROM bank; ').fetchall()
    for i in vivod:
        name,summa,tel=i
        print(f"""
Абонент: {name}
Телефон: {tel}
Баланс: {summa}
""")

def vklad():
    name = input('Введите ваше ФИО для рассчёта вклада: ')
    balance = bank.execute(f"SELECT balance FROM bank  WHERE name='{name}';").fetchone()
    his_balance=balance[0]
    vklad_1year=his_balance*(1+0.25)**1
    vklad_2year = his_balance * (1 + 0.25) ** 2
    vklad_3year = his_balance * (1 + 0.25) ** 3
    print(f"""С балансом {his_balance} и ставкой финансирования 25%, вы получите
С вкладом на 1 год: {vklad_1year}
С вкладом на 2 года: {vklad_2year}
С вкладом на 3 года: {vklad_3year}
""")

while True:

    print('1 - Добавить клиента')
    print('2 - Добавить сумму')
    print('3 - Снять сумму')
    print('4 - Увидеть данные')
    print('5 - Рассчитать вклад')
    print('6 - Закончить')
    action=int(input())
    if action == 1:
        add_client()
        sqlZapros.commit()
    elif action==2:
        add_balance()
        sqlZapros.commit()
    elif action==3:
        minus_balance()
        sqlZapros.commit()
    elif action==4:
        show_info()
    elif action==5:
        vklad()
    elif action==6:
        break
sqlZapros.close()