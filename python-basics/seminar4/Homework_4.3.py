from decimal import Decimal, InvalidOperation
from datetime import datetime

# Константы (преобразуем все в Decimal для точных вычислений с деньгами)
MIN_SUM = Decimal('50')                  # минимальная сумма пополнения и снятия
PROCENT_COMMISSION = Decimal('0.015')    # процент комиссии (1.5%)
MIN_COMMISSION = Decimal('30')           # минимальная комиссия
MAX_COMMISSION = Decimal('600')          # максимальная комиссия
BONUS = Decimal('0.03')                  # бонус (3%)
LIMIT_BEFORE_TAX = Decimal('5000000')    # лимит до налога
TAX_RATE = Decimal('0.1')                # ставка налога (10%)

def format_decimal(value):
    """
    Форматирует Decimal значение в строку с двумя знаками после запятой.
    
    Аргументы:
        value: Decimal значение для форматирования
        
    Возвращает:
        Отформатированную строку
    """
    return f"{value:.2f}"

def add_transaction_to_history(transaction_history, operation_type, amount, commission=None, balance_before=None, balance_after=None):
    """
    Добавляет новую операцию в историю транзакций.
    
    Аргументы:
        transaction_history: список истории транзакций
        operation_type: тип операции ('Пополнение', 'Снятие', 'Налог', 'Бонус')
        amount: сумма операции
        commission: комиссия (если применимо)
        balance_before: баланс до операции
        balance_after: баланс после операции
        
    Возвращает:
        Обновленный список истории транзакций
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    transaction = {
        'timestamp': timestamp,
        'operation': operation_type,
        'amount': amount,
        'commission': commission,
        'balance_before': balance_before,
        'balance_after': balance_after
    }
    
    transaction_history.append(transaction)
    return transaction_history

def check_wealth_tax(balance, transaction_history):
    """
    Проверяет и применяет налог на богатство, если баланс превышает лимит.
    
    Аргументы:
        balance: текущий баланс счета
        transaction_history: список истории транзакций
        
    Возвращает:
        Кортеж (новый баланс, обновленный список истории)
    """
    if balance >= LIMIT_BEFORE_TAX:
        balance_before = balance
        tax = balance * TAX_RATE
        balance -= tax
        print(f'Удержан налог на богатство: {format_decimal(tax)} у.е.')
        
        # Добавляем операцию налога в историю
        transaction_history = add_transaction_to_history(
            transaction_history, 
            'Налог на богатство', 
            tax, 
            None, 
            balance_before, 
            balance
        )
        
    return balance, transaction_history

def give_money(balance, transaction_history):
    """
    Функция пополнения счета.
    
    Аргументы:
        balance: текущий баланс счета
        transaction_history: список истории транзакций
        
    Возвращает:
        Кортеж (новый баланс, обновленный список истории)
    """
    try:
        money_to_add = Decimal(input('Введите сумму пополнения: '))
        if money_to_add % MIN_SUM == 0:
            balance_before = balance
            balance += money_to_add
            print(f'Счет пополнен на: {format_decimal(money_to_add)} у.е.')
            
            # Добавляем операцию пополнения в историю
            transaction_history = add_transaction_to_history(
                transaction_history, 
                'Пополнение', 
                money_to_add, 
                None, 
                balance_before, 
                balance
            )
        else:
            print(f'Ошибка пополнения, сумма должна быть кратна {MIN_SUM} у.е.')
    except (ValueError, InvalidOperation):
        print('Ошибка ввода: введите корректное число')
        
    return balance, transaction_history

def get_money(balance, transaction_history):
    """
    Функция снятия денег со счета.
    
    Аргументы:
        balance: текущий баланс счета
        transaction_history: список истории транзакций
        
    Возвращает:
        Кортеж (новый баланс, обновленный список истории)
    """
    try:
        money_to_get = Decimal(input('Введите сумму снятия: '))
        
        if money_to_get % MIN_SUM != 0:
            print(f'Ошибка снятия денег, сумма должна быть кратна {MIN_SUM} у.е.')
            return balance, transaction_history

        # Расчет комиссии
        commission = money_to_get * PROCENT_COMMISSION
        
        # Проверяем, что комиссия не меньше минимальной и не больше максимальной
        if commission < MIN_COMMISSION:
            commission = MIN_COMMISSION
        elif commission > MAX_COMMISSION:
            commission = MAX_COMMISSION

        total_withdrawal = money_to_get + commission

        if total_withdrawal <= balance:
            balance_before = balance
            balance -= total_withdrawal
            print(f'Сумма снятия: {format_decimal(money_to_get)} у.е.')
            print(f'Комиссия за снятие: {format_decimal(commission)} у.е.')
            
            # Добавляем операцию снятия в историю
            transaction_history = add_transaction_to_history(
                transaction_history, 
                'Снятие', 
                money_to_get, 
                commission, 
                balance_before, 
                balance
            )
        else:
            print('Недостаточно средств на счете')
            print(f'Требуется: {format_decimal(total_withdrawal)} у.е., доступно: {format_decimal(balance)} у.е.')
            
    except (ValueError, InvalidOperation):
        print('Ошибка ввода: введите корректное число')
        
    return balance, transaction_history

def apply_bonus(balance, transaction_history):
    """
    Начисляет бонус на остаток средств.
    
    Аргументы:
        balance: текущий баланс счета
        transaction_history: список истории транзакций
        
    Возвращает:
        Кортеж (новый баланс, обновленный список истории)
    """
    balance_before = balance
    bonus = balance * BONUS
    balance += bonus
    print(f'Начислен бонус: {format_decimal(bonus)} у.е.')
    
    # Добавляем операцию бонуса в историю
    transaction_history = add_transaction_to_history(
        transaction_history, 
        'Бонус', 
        bonus, 
        None, 
        balance_before, 
        balance
    )
    
    return balance, transaction_history

def print_transaction_history(transaction_history):
    """
    Выводит историю транзакций в удобном формате.
    
    Аргументы:
        transaction_history: список истории транзакций
    """
    if not transaction_history:
        print("История операций пуста.")
        return
    
    print("\n===== ИСТОРИЯ ОПЕРАЦИЙ =====")
    print("Дата и время       | Операция          | Сумма      | Комиссия   | Баланс до  | Баланс после")
    print("-" * 93)
    
    for transaction in transaction_history:
        # Форматируем значения для вывода
        timestamp = transaction['timestamp']
        operation = transaction['operation']
        amount = format_decimal(transaction['amount']) if transaction['amount'] else "-"
        commission = format_decimal(transaction['commission']) if transaction['commission'] else "-"
        balance_before = format_decimal(transaction['balance_before']) if transaction['balance_before'] else "-"
        balance_after = format_decimal(transaction['balance_after']) if transaction['balance_after'] else "-"
        
        # Форматируем строку вывода
        print(f"{timestamp} | {operation:<17} | {amount:<10} | {commission:<10} | {balance_before:<10} | {balance_after:<10}")
    
    print("=" * 93)

def menu(balance, transaction_history, operation_count):
    """
    Главное меню банкомата.
    
    Аргументы:
        balance: текущий баланс счета
        transaction_history: список истории транзакций
        operation_count: счетчик операций
        
    Возвращает:
        Кортеж (новый баланс, обновленный список истории, новый счетчик операций, флаг продолжения работы)
    """
    print("\n===== МЕНЮ БАНКОМАТА =====")
    print("1 - Пополнить счет")
    print("2 - Снять со счета")
    print("3 - Показать историю операций")
    print("4 - Выйти из программы")
    
    # Проверка на налог на богатство перед любой операцией
    balance, transaction_history = check_wealth_tax(balance, transaction_history)
    
    print(f'\nТекущий баланс: {format_decimal(balance)} у.е.')
    
    choice = input('\nВведите номер команды: ')
    
    is_flag = True  # Флаг для продолжения работы программы
    
    if choice == '4':
        print(f'Спасибо за использование нашего банкомата!')
        print(f'Конечный баланс: {format_decimal(balance)} у.е.')
        is_flag = False
    elif choice == '1':
        balance, transaction_history = give_money(balance, transaction_history)
        operation_count += 1
    elif choice == '2':
        balance, transaction_history = get_money(balance, transaction_history)
        operation_count += 1
    elif choice == '3':
        print_transaction_history(transaction_history)
    else:
        print('Неверная команда. Пожалуйста, выберите один из пунктов меню.')
    
    # Начисление бонуса после каждой третьей операции пополнения или снятия
    if operation_count > 0 and operation_count % 3 == 0:
        balance, transaction_history = apply_bonus(balance, transaction_history)
    
    return balance, transaction_history, operation_count, is_flag

def main():
    """
    Основная функция программы.
    """
    print("=" * 50)
    print("Добро пожаловать в программу Банкомат!")
    print("=" * 50)
    
    # Инициализация переменных
    balance = Decimal('0')          # Начальный баланс
    transaction_history = []        # Пустой список для истории операций
    operation_count = 0             # Счетчик операций
    is_flag = True                  # Флаг для продолжения работы программы
    
    # Основной цикл программы
    while is_flag:
        balance, transaction_history, operation_count, is_flag = menu(balance, transaction_history, operation_count)

if __name__ == "__main__":
    main()
