# Завдання 2 : Інвентаризація продуктів

products = {"Milk":100, "Banana":50, "Apple":250} # Створення словника з продуктами та їх кількостями
def productUpd (name, amount):
    if name in products:
        products[name] += amount # Якщо продукт є в інвентарі, додаємо до його поточної кількості значення amount
        if products[name] < 0: # Якщо після оновлення кількість продукту стає меншою за 0, видаляємо цей продукт зі списку
            del products[name]
    else:
        if amount > 0: # Якщо продукт відсутній в інвентарі і кількість більше 0, додаємо його до інвентарю
            products[name] = amount
    print (products)
productUpd("Kiwi", 50)
productUpd("Avocado", 2)
productUpd("Banana", -30)
productUpd("Banana", -50) # Зменшуємо кількість продукту до < 0

productCount = [] # Створення списку для збереження продуктів, кількість яких менша за 5
for name, amount in products.items (): # Перебір продуктів у словнику і додавання їх до списку, якщо кількість менша за 5
    if amount < 5:
        productCount.append(name)
print("Products with less than 5 items in stock : ", productCount) # Виведення результату: список продуктів, кількість яких менша за 5
