import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime

def get_exchange_rate(start_date, end_date, valcode="eur"): # Функція для отримання курсу валют від НБУ (за замовчуванням EUR)
    url = (
        f"https://bank.gov.ua/NBU_Exchange/exchange_site"
        f"?start={start_date}&end={end_date}&valcode={valcode}"
        f"&sort=exchangedate&order=desc&json"
    )
    response = requests.get(url) # Виконання GET-запиту за URL

    if response.status_code == 200: # Успішний запит
        return json.loads(response.content)
    elif response.status_code == 404: # Якщо сервер не знайшов дані
        print("Дані з технічної причини не отримані")
    else:
        print("Помилка отримання даних")
    return None

def exchange_data(data): # Функція для перетворення JSON-даних у словник {дата: курс}
    rates = {} # Порожній словник для результатів
    for item in data:
        rates[item['exchangedate']] = item ['rate'] # Зберігаємо дату як ключ і курс як значення
    return rates # Повертаємо словник з курсами

def plot_rates(date_rate_dict): # Функція для побудови графіка на основі словника
    dates = []
    rates = []
    for item, rate in date_rate_dict.items(): # Ітеруємо словник
        dates.append(item) # Додаємо дату
        rates.append(rate) # Додаємо курс
    plt.xlabel("Дата")
    plt.ylabel("Курс (UAH)")
    plt.title("Офіційний курс EUR/UAH")
    plt.plot(dates, rates) # Побудова лінійного графіка
    plt.show()

# Параметри
start_date = "20240401"
end_date = "20240405"
currency = "eur"

jsondata = get_exchange_rate(start_date, end_date, currency) # Отримуємо JSON-дані з API

if jsondata: # Перевіряємо чи вдалося отримати дані з API
    exchange_rates = exchange_data(jsondata) # Перетворюємо отриманий JSON у словник з датами та курсами

    for date, rate in exchange_rates.items(): # Виводимо кожну дату та курс
        print(f"{date}: {rate} грн") # Форматований вивід

    plot_rates(exchange_rates) # Виклик побудови графіку