import sqlite3
import hashlib

# Підключення до БД (створюється файл users.db)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Створення таблиці users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    full_name TEXT NOT NULL
)
''')

def add_user(login, password, full_name): # Функція для додавання користувача
    password_hash = hashlib.sha256(password.encode()).hexdigest() # Хешування паролю
    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)", (login, password_hash, full_name))
        conn.commit() # Коммітимо зміни
        print(f"Користувача '{login}' додано.")
    except sqlite3.IntegrityError: # Перевірка на наявність логіну
        print(f"Користувач з логіном '{login}' вже існує.")

def delete_user(login):
    cursor.execute("DELETE FROM users WHERE login = ?", (login,))
    if cursor.rowcount: # Перевіряє, чи була змінена хоча б одна строка в результаті останнього SQL-запиту (UPDATE, DELETE, тощо).
        print(f"Користувача '{login}' видалено.")
    else:
        print(f"Користувача '{login}' не знайдено.")
    conn.commit()

def update_password(login, new_password): # Оновлення паролю користувачів
    hashed = hashlib.sha256(new_password.encode()).hexdigest()
    cursor.execute("UPDATE users SET password = ? WHERE login = ?", (hashed, login))
    conn.commit()
    print(f"Пароль для '{login}' оновлено.")

def authenticate_user(login): # Перевірка автентифікації, тобто введеного паролю користувача. пароль користувач вводить з консолі, зчитування за допомогою методу input() 
    cursor.execute("SELECT password FROM users WHERE login = ?", (login,))
    row = cursor.fetchone() # Бере один рядок результату
    if row: # Перевіряє: чи є такий користувач у базі
        entered_password = input("Введіть пароль: ")
        hashed_input = hashlib.sha256(entered_password.encode()).hexdigest()
        if hashed_input == row[0]: # Порівнюємо з паролем із бази
            print("Автентифікація успішна.")
            return True
        else:
            print("Невірний пароль.")
            return False
    else: # Якщо логін відсутній у базі
        print("Користувача не знайдено.")
        return False

# Приклад використання:
if __name__ == "__main__":
    add_user("admin", "securepassword", "ABCD EFG")
    add_user("admin1", "securepassword", "EFG DCBA")
    add_user("admin2", "securepassword", "Kir ABC")
    delete_user("admin")

    login = input("Введіть логін користувача: ")

    if authenticate_user(login):
        new_pass = input("Введіть новий пароль: ")
        update_password(login, new_pass)

    conn.close()
