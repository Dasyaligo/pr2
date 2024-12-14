from re import match

mercedes_Benz = [
    {"Stamp": "E-Class", "price": 100000000, "stock": 10},
    {"Stamp": "GLC Coupe", "price": 12000000, "stock": 5},
    {"Stamp": "GLS", "price": 15000000, "stock": 3},
    {"Stamp": "S-Class", "price": 16000000, "stock": 7},
    {"Stamp": "G-Class AMG", "price": 25000000, "stock": 2},
    {"Stamp": "GLE", "price": 20000000, "stock": 4},
    {"Stamp": "Maybach GLS", "price": 100000000, "stock": 1},
    {"Stamp": "V-Класс", "price": 5000000, "stock": 8},
    {"Stamp": "GLC", "price": 10000000, "stock": 6},
    {"Stamp": "GLE Coupe", "price": 80000000, "stock": 2},
    {"Stamp": "Maybach S-Класс", "price": 800000000, "stock": 1},
    {"Stamp": "GLA", "price": 250000500, "stock": 5},
    {"Stamp": "GLE Coupe AMG", "price": 300000000, "stock": 1},
    {"Stamp": "E-Класс AMG", "price": 5634300, "stock": 3},
    {"Stamp": "S-Класс AMG", "price": 6000000, "stock": 2},
    {"Stamp": "GLS AMG", "price": 8000000, "stock": 3}
]

users = [
    {
        'username': 'john_doe',  # Логин пользователя
        'password': 'password',  # Пароль
        'role': 'user',
    },
    {
        'username': 'admin_user',
        'password': 'password',
        'role': 'admin'
    }
]

def add_mers():  # Добавление
    print("Напишите данные")
    stamp = input("Введите модель: ")
    price = int(input("Введите цену: "))
    stock = int(input("Введите количество: "))  # Добавляем ввод для stock
    new_car = {"Stamp": stamp, "price": price, "stock": stock}
    mercedes_Benz.append(new_car)

def purchase_mers():
    print("Все машины: ", mercedes_Benz)
    selected_stamp = input("Введите модель автомобиля, который хотите купить: ")
    quantity = int(input("Введите количество: "))

    for car in mercedes_Benz:
        if car["Stamp"] == selected_stamp:
            if quantity <= car["stock"]:
                total_cost = car["price"] * quantity
                car["stock"] -= quantity
                print(f"Вы успешно купили {quantity} {selected_stamp}(ов) за {total_cost} рублей.")
                return
            else:
                print(f"Недостаточно автомобилей в наличии. Доступно: {car['stock']}")
                return

    print("Модель не найдена.")

def sort_mers(order='asc'):
    if order == 'asc':
        sorted_cars = sorted(mercedes_Benz, key=lambda x: x['price'])
    else:
        sorted_cars = sorted(mercedes_Benz, key=lambda x: x['price'], reverse=True)
    print("Отсортированные машины: ", sorted_cars)

def delete_mers():  # Удаление
    print("Удаление данных")
    stamp = input("Введите модель для удаления: ")
    for i in mercedes_Benz:
        if i["Stamp"] == stamp:
            mercedes_Benz.remove(i)
            print("Удаление прошло успешно")
            break
    else:
        print("Модель не найдена.")

def editing_mers():  # Редактирование
    print("Редактирование данных")
    print("======================================")
    print("Все машины: ", mercedes_Benz)
    print("======================================")
    old_stamp = input("Введите модель для редактирования: ")
    for i in range(len(mercedes_Benz)):
        if mercedes_Benz[i]["Stamp"] == old_stamp:
            new_stamp = input("Введите новую модель: ")
            price = int(input("Введите новую цену: "))
            mercedes_Benz[i]["Stamp"] = new_stamp
            mercedes_Benz[i]["price"] = price
            print("Изменение прошло успешно")
            break
    else:
        print("Модель не найдена.")

def auth(username, password):  # Авторизация
    for i in users:
        if i["username"] == username and i["password"] == password:
            print("Авторизация прошла успешно")
            return i["role"]
    return False

def main():  # Начало
    print("Добро пожаловать в Автосалон, пройдите авторизацию")
    user_name = input("Введите логин: ")
    password = input("Введите пароль: ")
    role = auth(user_name, password)

    if role == "user":
        while True:
            try:
                action = int(input("Выберите действие: \n1. Посмотреть машины.\n2. Купить.\n3. Отсортировать.\n4. Выйти.\n"))
                match action:
                    case 1:
                        print("Все машины: ", mercedes_Benz)
                    case 2:
                        purchase_mers()
                    case 3:
                        sort_order = input("Выберите порядок сортировки (asc/desc): ")
                        sort_mers(order=sort_order)
                    case 4:
                        exit()
            except ValueError as e:
                print(f"Ошибка: {e}. Пожалуйста, введите число.")

    elif role == "admin":
        while True:
            try:
                action = int(input("Выберите действие: \n1. Добавить машину.\n2. Удалить.\n3. Редактировать.\n4. Просмотр.\n5. Выйти.\n"))
                match action:
                    case 1:
                        add_mers()
                    case 2:
                        delete_mers()
                    case 3:
                        editing_mers()
                    case 4:
                        print("Все машины: ", mercedes_Benz)
                    case 5:
                        exit()
            except ValueError as e:
                print(f"Ошибка: {e}. Пожалуйста, введите число.")

if __name__ == "__main__":
    main()
