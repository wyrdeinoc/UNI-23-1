# Задача 3 : Статистика продажів

ProductList = [{"Product":"Milk", "Amount":15, "Price" : 60}, {"Product":"Banana","Amount":50, "Price" : 40}, {"Product":"Banana","Amount":60, "Price" : 40}]

def Profit () : # Функція для обчислення загального доходу від продажу кожного продукту
    ProfitCount = {} # Словник в якому зберігається назва продукту (Key) і загальний дохід (Value)
    for product in ProductList: # Перебір кожного продукту в списку ProductList
        GeneralProfit = product["Amount"] * product["Price"] # Обчислення загального доходу для поточного продукту: кількість * ціна
        ProductName = product["Product"] # Отримуємо назву продукту
        if ProductName in ProfitCount: # Перевіряємо чи існує продукт в словнику
            ProfitCount[ProductName] += GeneralProfit # Додаємо загальний дохід до існуючого продукту
        else:
            ProfitCount[ProductName] = GeneralProfit  # Якщо продукту немає в словнику, додаємо його та встановлюємо його загальний дохід
    return ProfitCount # Повертаємо словник з назвою продукту та його загальним доходом

ProfitCount = Profit() # Викликаємо функцію Profit і зберігаємо результат у ProfitCount
print(ProfitCount)

ProfitableProd = [] # Словник в якому зберігаються назви продуктів з доходом більше 1000
for prodName, generalProfit in ProfitCount.items () : # Якщо загальний дохід продукту більше 1000, додаємо його до списку ProfitableProd
    if generalProfit > 1000:
        ProfitableProd.append(prodName)
print("Products with profit over 1000 : ", ProfitableProd)
