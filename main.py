import json #Подключение модуля json
#Создание переменной для меню
menu=("""Доступные операции:  
      1. Вывести все записи.  
      2. Вывести запись по полю.  
      3. Добавить запись.  
      4. Удалить запись по полю.  
      5. Выйти из программы. """)  
print(menu) #Вывод на консоль
count = 0 #Создание переменной для счета кол-ва операций
num = int(input("Введите номер пункта который хотите выполнить: ")) #Ввод желаемого пункта с клавиатуры

with open("stars.json", 'r', encoding='utf-8') as file: #Открытие файла и присваивание его переменной
    data = json.load(file) #Преобразование файла с помощью функции load()
    while num > 0 and num <= 5: #Цикл while для проверки является ли введенные с клавиатуры данные числом от 1 до 5
        #Цикл if-elif-else для выполнения пунктов от 1 до 5
        if num == 1: #Вывод всех записей
            print()
            for star in data: #Цикл for для получение данных каждой звезды из файла и присваивание их переменным для вывода
                star_id = star.get("id") 
                star_name = star.get("name") 
                star_constellation = star.get("constellation") 
                star_is_visible = bool(star.get("is_visible")) 
                star_radius = star.get("radius") 
                if star_is_visible == True: 
                    visible = "Да" 
                else: 
                    visible = "Нет" 
                print(f"""------------------------------------------------------------- 
Номер звезды в списке: {star_id} 
Название звезды: {star_name} 
Созвездие, частью которого является звезда: {star_constellation} 
Видно ли звезду невооруженным взглядом: {visible} 
Солнечный радиус звезды: {star_radius} 
""") 
 
            print()  
            print(menu) #Повторный вызов меню
            num = int(input("Введите номер пункта который хотите выполнить: ")) #Повторный ввод цифры с клавиатуры
            count += 1
 
        elif num == 2: #Вывод записи по полю
            print() 
            find = False #Создание булевой переменной
            id = int(input("Введите номер поля: ")) #Ввод номера поля
            for star in data:  #Цикл for для получение данных звезды из файла и присваивание их переменным для вывода
                search_id = star.get("id") 
                if id == search_id: #Проверка нахождения верного номера поля
                    find = True #Изменение булевой переменной
                    star_id = star.get("id") 
                    star_name = star.get("name") 
                    star_constellation = star.get("constellation") 
                    star_is_visible = bool(star.get("is_visible")) 
                    star_radius = star.get("radius") 
                    if star_is_visible == True: 
                        visible = "Да" 
                    else: 
                        visible = "Нет" 
                    print(f"""------------------------------------------------------------- 
Номер звезды в списке: {star_id} 
Название звезды: {star_name} 
Созвездие, частью которого является звезда: {star_constellation} 
Видно ли звезду невооруженным взглядом: {visible} 
Солнечный радиус звезды: {star_radius} 
""") 
            if not find: #Цикл if в случае если запись не найдена
                print() 
                print("Запись не найдена.") 
            print()  
            print(menu) #Повторный вызов меню
            count += 1
            num = int(input("Введите номер пункта который хотите выполнить: ")) #Повторный ввод цифры с клавиатуры
      
        elif num == 3: #Добавление записи
            print()  
 
            new_id = len(data) + 1 #Присваивание нового номера поля, следующего за последним 
            new_name = input("Введите название звезды: ") #Ввод данных с клавиатуры
            new_constellation = input("Введите название созвездия: ") #Ввод данных с клавиатуры
            new_is_visible = input("Видно ли звезду невооруженным глазом: ") #Ввод данных с клавиатуры
            new_radius = input("Введите солнечный радиус: ") #Ввод данных с клавиатуры

            #Создание нового элемента для файла
            new_star = { 
            "id": new_id, 
            "name": new_name, 
            "constellation": new_constellation, 
            "is_": True if new_is_visible.lower() == "да" else False, 
            "radius": new_radius 
            } 
 
            data.append(new_star) #Добавление элемента в файл
            with open("stars.json", 'w', encoding='utf-8') as out_file: #Открытие файла и присваивание его переменной
                json.dump(data, out_file, ensure_ascii = False, indent = 2) 
             
 
            print(menu) #Повторный вызов меню
            count += 1
            num = int(input("Введите номер пункта который хотите выполнить: ")) #Повторный ввод цифры с клавиатуры
 
        elif num == 4: #Удаление записи по полю
            print()  
 
            delete_id = int(input("Введите номер записи, которую желаете удалить: ")) #Ввод номера поля
            find = False #Создание булевой переменной
            for star in data: #Цикл for для получение данных звезды из файла и присваивание их переменным для удаления
                sought_for_id = star.get("id") 
                if delete_id == sought_for_id: #Проверка нахождения верного номера поля 
                    find = True #Изменение булевой переменной
                    data.remove(star) #Удаление данных звезды из файла
                    with open("stars.json", "w",encoding="utf-8") as new_file:
                        json.dump(data, new_file, ensure_ascii = False, indent = 4) 
                    break #Остановка цикла в случае нахождения нужной звезды
                 
            if not find: #Цикл if в случае если запись не найдена
                print() 
                print("Запись не найдена.") 
 
            print()  
            print(menu) #Повторный вызов меню
            count += 1
            num = int(input("Введите номер пункта который хотите выполнить: ")) #Повторный ввод цифры с клавиатуры
 
        elif num == 5: #Выход из программы
            print()  
            print(f"Выход из программы. Кол-во операций: {count}")  
            print()  
            break  
    else:  
        print("Ввведено неверное число.")