# Завдання 3: Фільтрація IP-адрес з файлу

def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counter = {} # Словник для підрахунку кількості входжень дозволених IP-адрес

    try:
        with open(input_file_path, 'r') as file:  # Відкриваємо файл у режимі читання
            for line in file: # Читаємо кожен рядок логу
                parts = line.strip().split() # Розбиваємо рядок по пробілах
                ip = parts[0] # 1-й елемент — IP-адреса
                if ip in allowed_ips: # Якщо IP-адреса є у списку дозволених
                    if ip in ip_counter: # Підраховуємо кількість входжень для цієї IP-адреси
                        ip_counter[ip] += 1
                    else:
                        ip_counter[ip] = 1 # Якщо нова адреса
    except FileNotFoundError: # Виняток якщо input файл не знайдено
        print(f"File {input_file_path} not found.")
        return {}
    try:
            with open(output_file_path, 'w') as outfile: # Відкриваємо output файл у режимі запису
                for ip, count in ip_counter.items():
                    outfile.write(f"{ip} - {count}\n") # Записуємо у форматі <IP> - <кількість входжень>
            print(f"Result from file '{output_file_path}':")
            with open(output_file_path, 'r') as outfile: # Виводимо вміст результатного файлу
                print(outfile.read())
    except IOError:
        print(f"Unable to edit file : '{output_file_path}'.") # Якщо сталася помилка при записі у файл
allowed_ips = ['83.149.9.216', '66.249.73.185' , '208.115.111.72', '97.116.185.190', '100.43.83.137']
ip_filt = filter_ips('apache_logs.txt', 'output_log.txt', allowed_ips) # Викликаємо функцію фільту з переданими файлами