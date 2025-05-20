# Завдання 2: Генератор хешів файлів

import hashlib # Імпортуємо стандартний модуль для роботи з криптографічними хешами

def generate_file_hashes(*file_paths): # Функція приймає довільну кількість шляхів до файлів як аргументи
    hashes = {} # Створюємо порожній словник для збереження результатів: {шлях_до_файлу: хеш}

    # Перебираємо кожен шлях до файлу, переданий у функцію
    for path in file_paths:
        try:
            with open(path, 'rb') as file: # Відкриваємо файл у бінарному режимі для читання
                content = file.read() # Зчитуємо весь вміст файлу
                file_hash = hashlib.sha256(content).hexdigest() # Обчислюємо SHA-256 хеш і перетворюємо в рядок hex
                hashes[path] = file_hash # Додаємо результат у словник
        except FileNotFoundError: # Якщо файл не знайдено
            print(f"File not found: {path}")
        except IOError: # Якщо виникає інша помилка читання файлу
            print(f"Error reading file: {path}")
    return hashes # Повертаємо словник з хешами файлів

result = generate_file_hashes('apache_logs.txt', 'apache_logs_error.txt') # Передаємо імена файлів, для яких хочемо обчислити хеш

print(result) # Виводимо отримані хеші