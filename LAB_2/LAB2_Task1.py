# Завдання 1: Аналізатор лог-файлів

def analyze_log_file(log_file_path): # Словник для збереження кількостей HTTP-кодів
    status_codes = {}
    try:
        with open(log_file_path, 'r') as file: # Відкриваємо файл у режимі читання
            for line in file: # Читаємо кожен рядок файлу
                parts = line.strip().split() # Розбиваємо рядок по пробілах
                if len(parts) >= 9: # Перевірка, чи є достатньо елементів
                    status_code = parts[8] # 9-й елемент — HTTP статус-код
                    if status_code.isdigit(): # Перевірка, чи це число
                        if status_code in status_codes: # Якщо статус вже є в словнику — збільшуємо кількість
                            status_codes[status_code] += 1
                        else:
                            status_codes[status_code] = 1 # Інакше додаємо новий код
            print(parts[0]) # Виводимо IP-адресу з останнього обробленого рядка
    except FileNotFoundError:
        print(f"File {log_file_path} not found.") # Якщо файл не знайдено — виводимо повідомлення
        return {}
    except IOError as e:
        print(f"Error occured: {e}") # Інші помилки читання файлу
        return {}

    return status_codes # Повертаємо словник


st_code  = analyze_log_file("apache_logs.txt") # Виклик функції та вивід результатів

for code, count in st_code.items():
    print(f"Status-code {code}: {count} times")