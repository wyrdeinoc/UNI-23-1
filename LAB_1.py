# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # �������� 1 : ������ � �������

# def dictGen (text):
#     words = text.lower().replace(",", "").replace(".", "").split()
#     # ��������� ������� ����� �� ��������� ����� �� �����
#     word_counts = {}
#     for word in words: # ϳ��������� ������� ��������� ���
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

# # # .items() ������� ���� (����, ��������) � ������ ���������, ��:
# # # ���� � �� �����
# # �������� � �� ������� ���� ���������
# for word, count in countDict.items():
#     if count > 3:
#         frequent_words.append(word)

# for word in frequent_words:
#     print(f"Words that are repeated more than 3 times : {word}")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # �������� 2 : �������������� ��������

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
# productUpd("Banana", -50) # �������� ������� �������� �� < 0

# productCount = []
# for name, amount in products.items ():
#     if amount < 5:
#         productCount.append(name)
# print("Products with less than 5 items in stock : ", productCount)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # ������ 3 : ���������� �������

# ProductList = [{"Product":"Milk", "Amount":15, "Price" : 60}, {"Product":"Banana","Amount":50, "Price" : 40}, {"Product":"Banana","Amount":60, "Price" : 40}]

# def Profit () :
#     # ������� � ����� ���������� ����� �������� (Key) � ��������� ����� (Value)
#     ProfitCount = {}
#     for product in ProductList:
#         GeneralProfit = product["Amount"] * product["Price"]
#         ProductName = product["Product"]
#         # ���������� �� ���� ������� � ��������
#         if ProductName in ProfitCount:
#             ProfitCount[ProductName] += GeneralProfit       # ������ ��������� ����� �� ��������� ��������
#         else:
#             ProfitCount[ProductName] = GeneralProfit        # ������ ����� ������� �� ���� ��������� �����
#     return ProfitCount

# ProfitCount = Profit()
# print(ProfitCount)

# # ������� � ����� ����������� ����� �������� � ������� ����� 1000
# ProfitableProd = []
# for prodName, generalProfit in ProfitCount.items () :
#     if generalProfit > 1000:
#         ProfitableProd.append(prodName)
# print("Products with profit over 1000 : ", ProfitableProd)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# # �������� 4 : ������� ��������� ��������
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

# # ������ 5 : �������������� ������������

# import hashlib

# # ��������� ������� ������������ (���� -> {������, ϲ�})
# users = {
#     "user1": {"password": hashlib.md5("password123".encode()).hexdigest(), "full_name": "Sergii Kh"},
#     "user2": {"password": hashlib.md5("qwerty".encode()).hexdigest(), "full_name": "Petro Ivanov"},
# }

# def check_password(login, password):# ������� ��� �������� ������
#     if login in users:
#         hashed_input = hashlib.md5(password.encode()).hexdigest()
#         if users[login]["password"] == hashed_input:
#             return True
#     return False

# # �������� ����� � ������
# login = input("Input login: ")
# password = input("Input password: ")

# # ��������
# if check_password(login, password):
#     print(f"Access granted , {users[login]['full_name']}!")
# else:
#     print("Access denied")
#     print("Incorrect login or password !")