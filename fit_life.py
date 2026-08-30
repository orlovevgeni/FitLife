# Проект FitLife - MVP версия 2.0

WATER_REC = 30  # мл воды на 1 кг веса
WATER_PER_KG = 1000  # мл в 1 литре

# Возвращает оценку ИМТ (упрощенный вариант с 3 зонами).
def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Недостаточный вес (рекомендуется набрать массу)'
    elif 18.5 <= bmi < 25:
        return 'Нормальный вес (так держать!)'
    else:  # bmi >= 25
        return 'Избыточный вес (рекомендуется скорректировать питание)'

# Возвращает правильное склонение слова 'год'.
def get_years_word(age):
    if 11 <= age % 100 <= 14:
        return 'лет'
    last_digit = age % 10
    if last_digit == 1:
        return 'год'
    elif 2 <= last_digit <= 4:
        return 'года'
    else:
        return 'лет'

# Возвращает правильное склонение слова 'литр'.
def get_liters_word(liters):
    int_part = int(liters)
    if 11 <= int_part % 100 <= 14:
        return 'литров'
    last_digit = int_part % 10
    if last_digit == 1:
        return 'литр'
    elif 2 <= last_digit <= 4:
        return 'литра'
    else:
        return 'литров'


# 1. Знакомство - получаем имя с проверкой
while True:
    user_name = input('Привет, как тебя зовут? ').strip()
    if user_name:
        break
    print('Имя не может быть пустым. Попробуйте снова.')

# 2. Сбор данных с проверками на разумные диапазоны

# Возраст
while True:
    try:
        user_age = int(input('Сколько тебе лет? '))
        if 1 <= user_age <= 120:
            break
        print('Возраст должен быть от 1 до 120 лет. Попробуйте снова.')
    except ValueError:
        print('Ошибка! Нужно ввести целое число. Попробуйте снова.')

# Вес
while True:
    try:
        user_weight = float(input('Сколько весишь в килограммах (например, 60.3)? '))
        if 10 <= user_weight <= 300:
            break
        print('Вес должен быть от 10 до 300 кг. Попробуйте снова.')
    except ValueError:
        print('Ошибка! Нужно ввести число. Попробуйте снова.')

# Рост
while True:
    try:
        user_height = float(input('Какой у тебя рост в метрах (например, 1.75)? '))
        if 0.5 <= user_height <= 2.8:
            break
        print('Рост должен быть от 0.5 до 2.8 м. Попробуйте снова.')
    except ValueError:
        print('Ошибка! Нужно ввести число. Попробуйте снова.')

# 3. Расчеты

# Рассчет ИМТ (индекса массы тела: вес разделить на (рост в квадрате))
bmi = round(user_weight / (user_height ** 2), 1)

# WATER_REC = 30 мл на 1 кг веса, WATER_PER_KG = 1000 мл в 1 литре
# Итоговая норма в литрах с округлением до 1 знака
water_needed = round(user_weight * WATER_REC / WATER_PER_KG, 1)

# 4. Подготовка склонений
years_text = get_years_word(user_age)
liters_text = get_liters_word(water_needed)
bmi_comment = get_bmi_category(bmi)

# 5. Вывод результата
print('-----------------------------------------------------')
print(f'Отчет для пользователя: {user_name} ({user_age} {years_text})')
print('-----------------------------------------------------')
print(f'Твой Индекс Массы Тела: {bmi} — {bmi_comment}')
print(f'Рекомендуемая норма воды: {water_needed} {liters_text} в день')
print('-----------------------------------------------------')
print()
print('Расчет окончен. Будь здоров!')