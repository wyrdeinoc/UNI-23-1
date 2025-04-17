# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # Завдання 1 : Робота з текстом

# def dictGen (text):
#     words = text.lower().replace(",", "").replace(".", "").split()
#     # Видаляємо розділові знаки та розбиваємо рядок на слова
#     word_counts = {}
#     for word in words: # Підраховуємо кількість повторень слів
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts

# text = "Text example, that includes repeated words. Words words words."
# print(text)

# countDict = {}
# countDict = dictGen(text)
# frequent_words = []

# # # .items() повертає пари (ключ, значення) у вигляді ітератора, де:
# # # ключ — це слово
# # значення — це кількість його повторень
# for word, count in countDict.items():
#     if count > 3:
#         frequent_words.append(word)

# for word in frequent_words:
#     print(f"Words that are repeated more than 3 times : {word}")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # Завдання 2 : Інвентаризація продуктів

# products = {"Milk":100, "Banana":50, "Apple":250}
# def productUpd (name, amount):
#     if name in products:
#         products[name] += amount
#         if products[name] < 0:
#             del products[name]
#     else:
#         if amount > 0:
#             products[name] = amount
#     print (products)
# productUpd("Kiwi", 50)
# productUpd("Avocado", 2)
# productUpd("Banana", -30)
# productUpd("Banana", -50) # Зменшуємо кількість продукту до < 0

# productCount = []
# for name, amount in products.items ():
#     if amount < 5:
#         productCount.append(name)
# print("Products with less than 5 items in stock : ", productCount)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # Задача 3 : Статистика продажів

# ProductList = [{"Product":"Milk", "Amount":15, "Price" : 60}, {"Product":"Banana","Amount":50, "Price" : 40}, {"Product":"Banana","Amount":60, "Price" : 40}]

# def Profit () :
#     # Словник в якому зберігається назва продукту (Key) і загальний дохід (Value)
#     ProfitCount = {}
#     for product in ProductList:
#         GeneralProfit = product["Amount"] * product["Price"]
#         ProductName = product["Product"]
#         # Перевіряємо чи існує продукт в словнику
#         if ProductName in ProfitCount:
#             ProfitCount[ProductName] += GeneralProfit       # Додаємо загальний дохід до існуючого продукту
#         else:
#             ProfitCount[ProductName] = GeneralProfit        # Додаємо новий продукт та його загальний дохід
#     return ProfitCount

# ProfitCount = Profit()
# print(ProfitCount)

# # Словник в якому зберігаються назви продуктів з доходом більше 1000
# ProfitableProd = []
# for prodName, generalProfit in ProfitCount.items () :
#     if generalProfit > 1000:
#         ProfitableProd.append(prodName)
# print("Products with profit over 1000 : ", ProfitableProd)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # Завдання 4 : Система управління задачами
# taskStatus = {}

# def taskAdd ():
#     task = input ("Type in the task name : ")
#     status = input ("Type in the task status : ")
#     taskStatus [task] = status
#     print (taskStatus)

# def taskDel ():
#     task = input ("Type in the task name you would like to delete: ")
#     if task in taskStatus :
#         del taskStatus[task]
#     else :
#         "Provided task name is incorrect."
#     print (taskStatus)

# def statusUpd ():
#     task = input ("Type in the task name you would like to edit: ")
#     if task in taskStatus :
#         taskStatus[task] = input ("Type in the new status of the task: ")
#     else :
#         "Provided task name is incorrect."
#     print (taskStatus)

# taskAdd()
# taskAdd()
# taskDel ()
# statusUpd ()

# taskList = []
# for task,status in taskStatus.items():
#     if status == "In progress":
#         taskList.append(task)

# print("Tasks in progress : ", taskList)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # Задача 5 : Аутентифікація користувачів

# import hashlib

# # Створюємо словник користувачів (логін -> {пароль, ПІБ})
# users = {
#     "user1": {"password": hashlib.md5("password123".encode()).hexdigest(), "full_name": "Sergii Kh"},
#     "user2": {"password": hashlib.md5("qwerty".encode()).hexdigest(), "full_name": "Petro Ivanov"},
# }

# def check_password(login, password):# Функція для перевірки пароля
#     if login in users:
#         hashed_input = hashlib.md5(password.encode()).hexdigest()
#         if users[login]["password"] == hashed_input:
#             return True
#     return False

# # Введення логіна і пароля
# login = input("Input login: ")
# password = input("Input password: ")

# # Перевірка
# if check_password(login, password):
#     print(f"Access granted , {users[login]['full_name']}!")
# else:
#     print("Access denied")
#     print("Incorrect login or password !")