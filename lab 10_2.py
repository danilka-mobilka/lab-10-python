def are_anagrams(text1, text2):
    # Якщо обидва рядки порожні - не анаграми
    if not text1 and not text2:
        return False
    
    # Очищаємо текст: переводимо в нижній регістр і видаляємо пробіли
    clean_text1 = ''.join(text1.lower().split())
    clean_text2 = ''.join(text2.lower().split())
    
    # Сортуємо символи і порівнюємо
    return sorted(clean_text1) == sorted(clean_text2)

# Спосіб 2: використання словника для підрахунку символів
def are_anagrams_dict(text1, text2):
    if not text1 and not text2:
        return False
    
    clean_text1 = ''.join(text1.lower().split())
    clean_text2 = ''.join(text2.lower().split())
    
    # Якщо довжини не співпадають - точно не анаграми
    if len(clean_text1) != len(clean_text2):
        return False
    
    # Створюємо словники для підрахунку символів
    count1 = {}
    count2 = {}
    
    for char in clean_text1:
        count1[char] = count1.get(char, 0) + 1
    
    for char in clean_text2:
        count2[char] = count2.get(char, 0) + 1
    
    return count1 == count2

# Спосіб 3: використання collections.Counter
from collections import Counter

def are_anagrams_counter(text1, text2):
    if not text1 and not text2:
        return False
    
    clean_text1 = ''.join(text1.lower().split())
    clean_text2 = ''.join(text2.lower().split())
    
    return Counter(clean_text1) == Counter(clean_text2)

# Отримуємо введення від користувача
text1 = input("Введіть перше слово: ")
text2 = input("Введіть друге слово: ")

# Використовуємо перший спосіб для перевірки
if are_anagrams(text1, text2):
    print("Anagrams")
else:
    print("Not anagrams")

# Тестування різних методів
print("\nДодаткові тести різними методами:")
test_pairs = [
    ("Listen", "Silent"),
    ("modern", "norman"),
    ("Апельсин", "Спаниель"),
    ("", ""),
    ("a", "A"),
    ("Dormitory", "Dirty room"),
    ("School master", "The classroom")
]

print("\n" + "="*40)
print(f"{'Перше слово':<20} {'Друге слово':<20} {'Результат':<15}")
print("="*40)

for t1, t2 in test_pairs:
    result = are_anagrams(t1, t2)
    print(f"{t1:<20} {t2:<20} {'Anagrams' if result else 'Not anagrams':<15}")