def is_palindrome(text):
    # Якщо текст порожній - не паліндром
    if not text:
        return False
    
    # Переводимо у нижній регістр і видаляємо пробіли
    clean_text = ''.join(text.lower().split())
    
    # Порівнюємо текст з його реверсом
    return clean_text == clean_text[::-1]

# Отримуємо введення від користувача
user_input = input("Введіть текст: ")

# Перевіряємо чи є паліндромом
if is_palindrome(user_input):
    print("It's a palindrome")
else:
    print("It's not a palindrome")

# Додатковий спосіб (з використанням циклу)
def is_palindrome_v2(text):
    if not text:
        return False
    
    clean_text = ''.join(text.lower().split())
    length = len(clean_text)
    
    for i in range(length // 2):
        if clean_text[i] != clean_text[length - i - 1]:
            return False
    return True

# Ще один спосіб (з використанням функції all)
def is_palindrome_v3(text):
    if not text:
        return False
    
    clean_text = ''.join(text.lower().split())
    return all(clean_text[i] == clean_text[-(i + 1)] for i in range(len(clean_text) // 2))

# Тестування:
print("\nДодаткові тести:")
test_cases = [
    "А роза упала на лапу Азора",
    "А роза не падала лапу",
    "козак з казок",
    "Мадам",
    "",
    "a",
    "12321"
]

for test in test_cases:
    result = is_palindrome(test)
    print(f"'{test}' -> {result}")