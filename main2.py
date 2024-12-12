from re import match

mercedes_Benz=[{"Stamp":"E-Class","price":100000000},
               {"Stamp":"GLC Coupe","price":12000000},
               {"Stamp":"GLS","price":15000000},
               {"Stamp":"S-Class","price":16000000},
               {"Stamp":"G-Class AMG","price":25000000},
               {"Stamp":"GLE","price":20000000},
               {"Stamp":"Maybach GLS","price":100000000},
               {"Stamp": "V-Класс", "price": 5000000},
               {"Stamp": "GLC", "price": 10000000},
               {"Stamp": "GLE Coupe", "price": 80000000},
               {"Stamp": "Maybach S-Класс", "price": 800000000},
               {"Stamp": "GLA", "price": 250000500},
               {"Stamp": "GLE Coupe AMG", "price": 300000000},
               {"Stamp": "E-Класс AMG", "price": 5634300},
               {"Stamp": "S-Класс AMG", "price": 6000000},
               {"Stamp": "GLS AMG", "price": 8000000}]

users = [
    {
        'username': 'john_doe', # Логин пользователя
        'password': 'password', # Пароль
        'role': 'user',
    },
    {
        'username': 'admin_user',
        'password': 'password',
        'role': 'admin'
    }
]
def add_mers(): #Добавление
    print("Напишите данные")
    stamp = input()
    price = int(input())
    new_car = {"Stamp": stamp, "price": price}
    mercedes_Benz.append(new_car)

def delete_mers():#Удаление
    print("Удаление данных")
    stamp = input()
    for i in mercedes_Benz:
        if i["Stamp"] == stamp:
            mercedes_Benz.remove(i)
            print("Удаление прошло успешно")
            break
def editing_mers():#Редактирование
    print("Редактирование данных")
    print("======================================")
    mercedes_Benz_print(text="Все машины: ", elements=mercedes_Benz)
    print("======================================")
    old_stamp = input("Введите модель: ")
    for i in range(len(mercedes_Benz)+1):
        if mercedes_Benz[i]["Stamp"] == old_stamp:
            new_stamp = input("Введите новую модель: ")
            price = int(input("Введите новую цену: "))
            mercedes_Benz[i]["Stamp"] = new_stamp
            mercedes_Benz[i]["price"] = price
            print("Изменение прошло успешно")
            break



def mercedes_Benz_print(text, elements):
    print(text)
    for i, element in enumerate(elements, start=1):
        print(f"{i}.", end="")
        for key, value in element.items():
            print(f"{key}:{value}", end=" ")
            if key == 'price':
                print()

def auth(username,password): #Регистрация
    for i in users:
        if i["username"] == username and i["password"] == password:
            print("Авторизация прошла успешно")
            return i["role"]
    return False



def main(): #Начало
    print("Добро пожаловать в Автосалон, пройдите авторизацию")
    user_name = input("Введите логин: ")
    password =  input("Введите пароль: ")
    role = auth(user_name, password)

    if role == "user":
        while True:
            try:
                action = int(input("Выберите действие: \n1. Посмотреть машины.\n2. Купить.\n3. Отсортировать.\n4. Отфильтровать.\n5.Выйти.\n"))
                match action:
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        exit()
            except Exception as e:
                print(f" Ошибка: {e}")

    elif role == "admin":
        while True:
            try:
                action = int(input("Выберите действие: \n1. Добавить машину.\n2. Удалить.\n3. Редактировать.\n4. Просмотр.\n5.Выйти.\n"))
                match action:
                    case 1:
                        add_mers()
                    case 2:
                        delete_mers()
                    case 3:
                        editing_mers()
                    case 4:
                        mercedes_Benz_print(text="Все машины: ", elements=mercedes_Benz)
                    case 5:
                        exit()
            except Exception as e:
                print(f" Ошибка: {e}")



if __name__ == "__main__":
    main()

#ошибки  сортировка вывод