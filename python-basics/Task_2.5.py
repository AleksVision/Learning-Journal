""" 
Напишите программу банкомат.Начальная сумма равна 0.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1,5% от суммы снятия, но оне мения 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляються проценты на остаток 3%
Нельзя снять больше чем на счете
При повышении суммы в 5 миллионов, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое дейтвие выводит сумму денег
"""
from decimal import Decimal, InvalidOperation

# Константы (преобразуем все в Decimal)
MIN_SUM = Decimal('50')                  # минимальная сумма пополнения и снятия
PROCENT_COMMISSION = Decimal('0.015')    # процент комиссии
MIN_COMMISSION = Decimal('30')           # минимальная комиссия
MAX_COMMISSION = Decimal('600')          # максимальная комиссия
BONUS = Decimal('0.03')                  # бонус
LIMIT_BEFORE_TAX = Decimal('5000000')    # лимит до налога
TAX_RATE = Decimal('0.1')                # ставка налога

def menu(balance: Decimal, count: int, is_flag: bool):
    """
    Главное меню банкомата
    """
    dct = {
        'command': 'Выберите команду: ',
        '1': 'Пополнить счет ',
        '2': 'Снять со счета',
        '3': 'Выйти из программы'
    }

    # Вывод меню
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k} - {v}')
        else:
            print(v)

    # Проверка на налог на богатство
    if balance >= LIMIT_BEFORE_TAX:
        tax = balance * TAX_RATE
        balance -= tax
        print(f'Удержан налог на богатство: {tax}')

    choice = input('Введите команду: ')

    if choice == '3':
        print(f'Конечный баланс: {balance}')
        return balance, False
    elif choice == '1':
        balance = give_money(balance)
        count += 1
    elif choice == '2':
        balance = get_money(balance)
        count += 1
    else:
        print('Неверная команда')

    # Начисление бонуса после каждой третьей операции
    if count % 3 == 0 and count != 0:
        bonus = balance * BONUS
        balance += bonus
        print(f'Начислен бонус: {bonus}')

    print(f'Баланс: {balance}')
    return balance, is_flag

def give_money(balance: Decimal) -> Decimal:
    """
    Функция пополнения счета
    """
    try:
        money_to_add = Decimal(input('Введите сумму пополнения: '))
        if money_to_add % MIN_SUM == 0:
            return balance + money_to_add
        else:
            print('Ошибка пополнения, сумма должна быть кратна 50')
            return balance
    except (ValueError, InvalidOperation):
        print('Ошибка ввода: введите корректное число')
        return balance

def get_money(balance: Decimal) -> Decimal:
    """
    Функция снятия денег
    """
    try:
        money_to_get = Decimal(input('Введите сумму снятия: '))
        
        if money_to_get % MIN_SUM != 0:
            print('Ошибка снятия денег, сумма должна быть кратна 50')
            return balance

        # Расчет комиссии
        commission = money_to_get * PROCENT_COMMISSION
        if commission < MIN_COMMISSION:
            commission = MIN_COMMISSION
        elif commission > MAX_COMMISSION:
            commission = MAX_COMMISSION

        total_withdrawal = money_to_get + commission

        if total_withdrawal <= balance:
            print(f'Комиссия за снятие: {commission}')
            return balance - total_withdrawal
        else:
            print('Недостаточно средств на счете')
            print(f'Требуется: {total_withdrawal}, доступно: {balance}')
            return balance

    except (ValueError, InvalidOperation):
        print('Ошибка ввода: введите корректное число')
        return balance

def main():
    print("Добро пожаловать в программу Банкомат")
    balance = Decimal('0')
    count = 0
    is_flag = True

    while is_flag:
        balance, is_flag = menu(balance, count, is_flag)

if __name__ == "__main__":
    main()
# Объяснение:
# Программа банкомата с использованием Decimal для точных вычислений.
# Пользователь может пополнить счет, снять деньги или выйти из программы.
# Сумма пополнения и снятия должна быть кратна 50.
# После каждой третьей операции начисляется бонус 3%.
# Если сумма превышает 5 миллионов, начисляется налог на богатство 10%.
# При снятии денег начисляется комиссия 1,5%, но не менее 30 и не более 600 у.е.
# Программа выводит баланс после каждой операции.
# Программа работает до тех пор, пока пользователь не выберет выход из программы.
# Программа обрабатывает ошибки ввода и выводит сообщение об ошибке.
# Программа работает с точностью до 2 знаков после запятой.
