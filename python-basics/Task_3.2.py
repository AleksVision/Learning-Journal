import re

def solve_math_problem(problem):
    def extract_numbers(text):
        return [float(num) for num in re.findall(r'\d+\.?\d*', text)]
    
    def extract_fractions(text):
        fractions = re.findall(r'(\d+)/(\d+)', text)
        if fractions:
            return [float(f[0]) / float(f[1]) for f in fractions]
        return []

    # Задача 84
    if 'принтер' in problem:
        speeds = extract_numbers(problem)[:2]
        times = extract_numbers(problem)[2:]
        total_pages = speeds[0] * times[0] + speeds[1] * times[1]
        return f"Всего страниц отпечатано: {total_pages} страниц"

    # Задача 85
    elif 'деталей' in problem:
        total_details = extract_numbers(problem)[0]
        hours_sasha = 4 * 8
        hours_misha = 5 * 7
        total_hours = hours_sasha + hours_misha
        details_per_hour = total_details / total_hours
        sasha_details = details_per_hour * hours_sasha
        misha_details = details_per_hour * hours_misha
        return f"Саша изготовил {sasha_details} деталей, Миша изготовил {misha_details} деталей"

    # Задача 86
    elif 'вафлями' in problem:
        weights = extract_numbers(problem)
        waffles_weight = 7 * weights[0]
        bagels_weight = 3 * weights[1]
        difference = waffles_weight - bagels_weight
        heavier = "вафель" if difference > 0 else "сушек"  
        return f"7 пакетов {heavier} тяжелее на {abs(difference)} г"

    # Задача 87
    elif 'свеклы' in problem:
        day1 = extract_numbers(problem)[0] * 1000 + extract_numbers(problem)[1]
        day2 = day1 + (extract_numbers(problem)[2] * 1000 + extract_numbers(problem)[3])
        day3 = day2 / 2
        total = day1 + day2 + day3
        return f"Всего свеклы собрано: {total / 1000} т {total % 1000} кг"

    # Задача 88
    elif 'луковиц' in problem:
        total_bulbs = extract_numbers(problem)[0]
        additional_bulbs = extract_numbers(problem)[1]
        bulbs_per_bed = (total_bulbs - additional_bulbs * 9) / 9
        return f"На каждой клумбе посадили {bulbs_per_bed} луковиц"

    # Задача 89
    elif 'краски' in problem:
        brown_cost = extract_numbers(problem)[0] * 9
        white_cost = extract_numbers(problem)[1] * 9
        total_cost = brown_cost + white_cost
        return f"Всего на покраску потребуется: {total_cost} руб."

    # Задача 90
    elif 'Санкт-Петербурга' in problem:
        distance = extract_numbers(problem)[0]
        fuel_consumption = extract_numbers(problem)[1]
        fuel_price = extract_numbers(problem)[2]
        total_cost = (distance / 100) * fuel_consumption * fuel_price
        return f"Общая стоимость бензина: {total_cost} руб."

    # Задача 91
    elif 'поездку' in problem:
        distance = extract_numbers(problem)[0]
        fuel_consumption = extract_numbers(problem)[1]
        fuel_price = extract_numbers(problem)[2]
        total_cost = 2 * (distance / 100) * fuel_consumption * fuel_price
        return f"Общая стоимость поездки туда и обратно: {total_cost} руб."

    # Задача 92
    elif 'цемента' in problem:
        gravel_cost = extract_numbers(problem)[0] * 560
        cement_cost = extract_numbers(problem)[1] * 180
        total_cost = gravel_cost + cement_cost
        return f"Общая сумма на материалы: {total_cost} руб."

    # Задача 93
    elif 'выручка' in problem:
        knitwear_income = extract_numbers(problem)[0]
        shoe_income = knitwear_income * 4
        total_income = knitwear_income + shoe_income
        return f"Общая выручка: {total_income} руб."

    # Задача 94
    elif 'кинотеатра' in problem:
        large_hall_seats = extract_numbers(problem)[0]
        small_hall_seats = large_hall_seats / 4
        total_seats = large_hall_seats + small_hall_seats
        return f"Всего мест в кинотеатре: {total_seats}"

    # Задача 95
    elif 'абонемент' in problem:
        museum_cost = extract_numbers(problem)[0]
        theatre_cost = extract_numbers(problem)[1]
        students = extract_numbers(problem)[2]
        total_cost = (museum_cost + theatre_cost) * students
        return f"Общая сумма: {total_cost} руб."

    # Задача 96
    elif 'баке' in problem:
        bucket1 = extract_numbers(problem)[0]
        bucket2 = bucket1 + extract_numbers(problem)[1]
        bucket3 = bucket1 * 5
        total_water = bucket1 + bucket2 + bucket3
        return f"Всего воды в баках: {total_water} л"

    # Задача 97
    elif 'театр' in problem:
        ticket_cost = extract_numbers(problem)[0]
        family_members = extract_numbers(problem)[1]
        total_cost = ticket_cost * family_members
        return f"Стоимость посещения театра: {total_cost} руб."

    # Задача 98
    elif 'кураги' in problem:
        kuraga_weight = extract_numbers(problem)[0]
        raisin_weight = kuraga_weight / 4
        apple_weight = kuraga_weight / 2
        prune_weight = raisin_weight + 120
        total_weight = kuraga_weight + raisin_weight + apple_weight + prune_weight
        return f"Всего куплено сухофруктов: {total_weight} г"

    # Задача 588
    elif 'туристы' in problem:
        traveled_distance = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        total_distance = traveled_distance / (fraction[0])
        remaining_distance = total_distance - traveled_distance
        return f"Осталось пройти туристам: {remaining_distance} км"

    # Задача 590
    elif 'автомобилей' in problem:
        cars_shown = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        total_cars = cars_shown / (fraction[0])
        return f"Всего автомобилей в автосалоне: {total_cars}"

    # Задача 592
    elif 'геологи' in problem:
        remaining_distance = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        traveled_distance = remaining_distance / (1 - (fraction[0]))
        return f"Геологи уже прошли: {traveled_distance} км"

    # Задача 594
    elif 'обувь' in problem:
        sold_shoes = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        total_shoes = sold_shoes / (fraction[0])
        remaining_shoes = total_shoes - sold_shoes
        return f"Осталось обуви в магазине: {remaining_shoes} пары"

    # Задача 596
    elif 'вспахали' in problem:
        plowed_area = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        total_area = plowed_area / (fraction[0])
        remaining_area = total_area - plowed_area
        return f"Осталось вспахать: {remaining_area} га"

    # Задача 598
    elif 'телефон' in problem:
        phone_payment = extract_numbers(problem)[0]
        fraction = extract_fractions(problem)
        total_payments = phone_payment / (fraction[0])
        return f"Общая сумма коммунальных платежей: {total_payments} руб."

    else:
        return "Не удалось распознать задачу. Пожалуйста, попробуйте другую формулировку."

# Примеры использования
problem = "На строительство бетонного фундамента для гаража ушло 4 т щебня и 30 мешков цемента. Цена щебня - 560 руб. за 1 т, а мешок цемента стоит 180 руб. Какая сумма была потрачена на эти материалы для фундамента?"
print(solve_math_problem(problem))

