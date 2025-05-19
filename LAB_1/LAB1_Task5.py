# Задача 5: Аутентифікація користувачів

import hashlib  # Імпортуємо модуль для хешування паролів

users = { # Створення словник, ключ — логін, значення — словник з хешованим паролем та повним ім’ям
    "user1": {"password": hashlib.md5("password123".encode()).hexdigest(), "full_name": "Anna Kir"},
    "user2": {"password": hashlib.md5("qwerty".encode()).hexdigest(), "full_name": "ABCD"}
}

# Функція перевірки правильності пароля користувача
def check_password(login, password):
    # Перевіряємо, чи існує логін у базі
    if login in users:
        # Хешуємо введений пароль
        hashed_input = hashlib.md5(password.encode()).hexdigest()
        # Порівнюємо збережений хеш із хешем введеного пароля
        if users[login]["password"] == hashed_input:
            return True  # Якщо збігається — доступ дозволено
    return False  # Якщо логін не існує або пароль неправильний

# Введення облікових даних користувачем
login = input("Input login: ")
password = input("Input password: ")

# Аутентифікація
if check_password(login, password):
    # Якщо успішно — виводимо привітання з повним ім’ям
    print(f"Access granted , {users[login]['full_name']} !")
    # Якщо невірні дані — виводимо повідомлення про відмову
else:
    print("Access denied")
    print("Incorrect login or password !")