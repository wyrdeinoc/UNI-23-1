# Завдання 4 : Система управління задачами
taskStatus = {} # Створення словника з ключами - назви задач, значення - статус

def taskAdd (): # Функція додавання нової задачі
    task = input ("Type in the task name : ")
    status = input ("Type in the task status : ")
    taskStatus [task] = status # Додаємо задачу та її статус до словника taskStatus
    print (taskStatus)

def taskDel (): # Функція для видалення задач
    task = input ("Type in the task name you would like to delete: ") # Отримання назви задачі яку потрібно видалити
    if task in taskStatus : # Перевіряємо, чи існує така задача в словнику
        del taskStatus[task]
    else : # Якщо задача не знайдена, виводимо повідомлення про помилку
        "Provided task name is incorrect."
    print (taskStatus)

def statusUpd (): # Функція для оновлення статусу задачі
    task = input ("Type in the task name you would like to edit: ")
    if task in taskStatus : # Перевіряємо, чи існує така задача в словнику
        taskStatus[task] = input ("Type in the new status of the task: ") # Якщо задача є, запитуємо новий статус та оновлюємо його
    else : # Якщо задача не знайдена, виводимо повідомлення про помилку
        "Provided task name is incorrect."
    print (taskStatus)

# Викликаємо функції для додавання, видалення та оновлення статусу задач
taskAdd()
taskAdd()
taskDel ()
statusUpd ()

taskList = [] # Створюємо список для збереження задач, які знаходяться в статусі "In progress"
for task,status in taskStatus.items():
    if status == "In progress": # Якщо статус задачі "In progress", додаємо її до списку taskList
        taskList.append(task)

print("Tasks in progress : ", taskList) # Виводимо список задач, які знаходяться в статусі "In progress"
