import hashlib

class User:
    def __init__(self, username, password_hash, is_active): 
        self.__username = username  # Приватне поле з ім’ям користувача
        self.__password_hash = hashlib.md5(password_hash.encode()).hexdigest() # Хешування паролю
        self.__is_active = is_active # Статус активності аккаунту

    def verify_password(self, password): 
        hashed_input = hashlib.md5(password.encode()).hexdigest() # Хешування введеного паролю
        if hashed_input == self.__password_hash: # Перевіряє чи відповідає введений пароль збереженому хешу
            return True
        else:
            return False

    def get_username(self): # Геттер юзеру
        return self.__username
    
    def get_is_active(self): # Геттер активності
        return self.__is_active

class Administrator(User): # Підклас що успадковує User
    def __init__(self, username, password_hash): 
        super().__init__(username, password_hash, True) # Адміністратор завжди активний, тому is_active = True
        self.__permission_list = [] # Список дозволів

    def add_permission(self, permission):
        self.__permission_list.append(permission) # Додати дозвіл

    def remove_permission(self, permission):
        self.__permission_list.remove(permission) # Видалити дозвіл

    def print_permissions(self):
        print(self.__permission_list) # Вивести всі дозволи


class RegularUser(User): # Підклас що успадковує User
    def __init__(self, username, password_hash, last_dateLogin):
        super().__init__(username, password_hash, True) # Звичайний користувач активний за замовчуванням
        self.__last_dateLogin = last_dateLogin # Дата останнього входу

    def print_lastDateLogin(self):
        print(f"Login date: {self.__last_dateLogin} ")


class GuestUser(User):
      def __init__(self, username, password_hash): 
        super().__init__(username, password_hash, False) # Гість завжди неактивний

class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user): # Додаємо користувача до системи за його логіном
        self.users[user.get_username()] = user

    def authenticate_user(self, username, password): # Перевіряє ім’я користувача та пароль
        if username in self.users and self.users[username].verify_password(password):
            return self.users[username] # Повертаємо об’єкт користувача при успішній перевірці
        else: 
            return None

# Створюємо об'єкти трьох типів користувачів
admin_user  = Administrator("Kir", "12345")
regular_user = RegularUser("ABCD", "password123", "12.03.2025")
guest_user =  GuestUser("Anton", "pass123")

# Створюємо об'єкт класу AccessControl і додаємо користувачів
access = AccessControl()
access.add_user(admin_user)
access.add_user(regular_user)
access.add_user(guest_user)

print("\n--- Administrator Login ---")
user = access.authenticate_user("Kir", "12345")
if user:
    print(f"Access granted: {user.get_username()} | Active: {user.get_is_active()}")
    if isinstance(user, Administrator): # Перевірка типу користувача
        user.add_permission("Perm1")
        user.add_permission("Perm2")
        user.remove_permission("Perm1")
        user.print_permissions()
else:
    print("Access denied")

print("\n--- Regular User Login ---")
user = access.authenticate_user("ABCD", "password123")
if user:
    print(f"Access granted: {user.get_username()} | Active: {user.get_is_active()}")
    if isinstance(user, RegularUser):
        user.print_lastDateLogin() # Виводимо останню дату входу
else:
    print("Access denied")

print("\n--- Guest User Login ---")
user = access.authenticate_user("Anton", "pass123")
if user:
    print(f"Access granted: {user.get_username()} | Active: {user.get_is_active()}")
else:
    print("Access denied")