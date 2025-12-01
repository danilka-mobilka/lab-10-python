def calculate_life_number(date_str):
    """
    Обчислює цифру життя з дати народження
    
    Args:
        date_str: Дата у будь-якому форматі (YYYYMMDD, DDMMYYYY, MMDDYYYY)
    
    Returns:
        Цифра життя (одна цифра від 1 до 9)
    """
    # Видаляємо всі нецифрові символи
    digits = ''.join(filter(str.isdigit, date_str))
    
    # Перевіряємо, чи є цифри
    if not digits:
        return 0
    
    # Обчислюємо суму всіх цифр
    digit_sum = sum(int(d) for d in digits)
    
    # Повторюємо додавання, поки не отримаємо одну цифру
    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))
    
    return digit_sum

# Спосіб 2: з використанням рекурсії
def calculate_life_number_recursive(date_str):
    # Видаляємо всі нецифрові символи
    digits = ''.join(filter(str.isdigit, date_str))
    
    if not digits:
        return 0
    
    def recursive_sum(num):
        if num < 10:
            return num
        return recursive_sum(sum(int(d) for d in str(num)))
    
    initial_sum = sum(int(d) for d in digits)
    return recursive_sum(initial_sum)

# Спосіб 3: з використанням математичної властивості цифрового кореня
def calculate_life_number_math(date_str):
    # Видаляємо всі нецифрові символи
    digits = ''.join(filter(str.isdigit, date_str))
    
    if not digits:
        return 0
    
    # Обчислюємо суму всіх цифр
    digit_sum = sum(int(d) for d in digits)
    
    # Використовуємо формулу для цифрового кореня
    if digit_sum == 0:
        return 0
    return digit_sum % 9 or 9

# Основна програма
def main():
    # Запит дати народження користувача
    date = input("Введіть дату народження (у будь-якому форматі, наприклад 19991229, 20000101): ")
    
    # Обчислення цифри життя
    life_number = calculate_life_number(date)
    
    # Виведення результату
    print(f"Цифра життя для дати {date}: {life_number}")

# Тестування
def run_tests():
    """Функція для тестування різних методів"""
    test_cases = [
        ("19991229", 6),
        ("20000101", 4),
        ("19990228", 5),
        ("19850615", 8),
        ("19500422", 3),
        ("", 0),
        ("12/03/1990", 7),  # З роздільниками
        ("03-12-1990", 7),  # З іншими роздільниками
    ]
    
    print("\nТестування трьох методів обчислення цифри життя:")
    print("=" * 60)
    print(f"{'Дата':<15} {'Очікуваний':<12} {'Метод 1':<10} {'Метод 2':<10} {'Метод 3':<10}")
    print("=" * 60)
    
    for date, expected in test_cases:
        result1 = calculate_life_number(date)
        result2 = calculate_life_number_recursive(date)
        result3 = calculate_life_number_math(date)
        
        status1 = "?" if result1 == expected else "?"
        status2 = "?" if result2 == expected else "?"
        status3 = "?" if result3 == expected else "?"
        
        print(f"{date:<15} {expected:<12} {result1:<3}{status1:<7} {result2:<3}{status2:<7} {result3:<3}{status3:<7}")

# Запуск основної програми або тестів
if __name__ == "__main__":
    print("Обчислення цифри життя з дати народження")
    print("-" * 40)
    
    # Запускаємо основну програму
    main()
    
    # Пропонуємо користувачу побачити тести
    choice = input("\nХочете побачити тестові приклади? (так/ні): ")
    if choice.lower() in ['так', 'yes', 'y', 'т']:
        run_tests()