import random

# функция отвечающая за вывод команд

def helpme():
        print("\nВот команды которые Вы можете использовать:")
        print("\n1) Правила - введи эту команду если Вы хотите прочитать правила игры.")
        print("2) Кубики - введи эту команду если Вы хотите кинуть кубики.")
        print("3) Обмен - введи эту команду если Вы хотите обменять своих животных на других.")
        print("ВАЖНО: При обмене Вы можете обменять животных, которые только на",
              " одну ячейку выше (т.е. Вы не можете обменять кроликов на свинью).")
        print("4) Таблица - введи эту команду если ты хочешь посмотреть таблицу обмена животных.")
        print("5) Животные - введи эту команду если ты хочешь посмотреть своих животных")
        print("6) Help - введи эту команду если забыл команды")
        print("ВАЖНО: Ты можешь ввести как название команды, так и её номер.")
        
# функция отвечающая за вывод животных игрока

def yourani():
        print("Ваши кролики: ", player_ani.count("Кролик"))
        print("Ваши овцы: ", player_ani.count("Овца"))
        print("Ваши свиньи: ", player_ani.count("Свинья"))
        print("Ваши коровы: ", player_ani.count("Корова"))
        print("Ваши кони: ", player_ani.count("Конь"))
        
        # !!! тут могли бы быть Ваши собаки но их пока нет

# функция отвечающая за ответ игрока

def answer():
    otvet = input("Введите команду: ").upper()
    
    if otvet == "ПРАВИЛА" or otvet == "1":
        print("\nВ игре есть 5 видов животных: кролик, овца, свинья, корова, конь.")
        print("Ваша задача собрать все виды животных хотя бы в одном экземпляре (кто первый собрал, тот и выиграл).")
        print("Получить животное вы можете если:")
        
        print("\n1) На кубике выпала пара одинаковых животных.")
        print("ВАЖНО: На обоих кубиках есть только кролики, овцы и свиньи",
              " (корова и конь есть в одном экземпляре на одном из кубиков).",
              " так что победить в игре только бросая кубики не получится!")
        print("Пример №1: У вас пока нет никакого животного и вам выпадает",
              " на первом и втором кубике кролик - вы получаете одного кролика.")
        print("Пример №2: У вас пока нет никакого животного и вам выпадает",
              " на первом кубике кролик, а на втором овца - вы ничего не получаете.")
        
        print("\n2) Если у вас уже есть хотя бы одно животное и на кубике(ах) выпало это же животное.")
        print("ВАЖНО: Если у вас больше одного животного и оно же выпало на кубике(ах),",
              " то Вы получаете столько животных, сколько у вас пар получилось вместе с животными на кубике(ах).")
        print("Пример: У вас есть три кролика, а на кубике выпадает ещё один кролик и какое-то животное -",
              " т.к. у вас уже есть 3 кролика и 1 выпал то у Вас 2 пары ((3+1):2=2) соответственно вы получаете 2 кролика.")
        
        print("\n3) Вы можете обменять один вид животных на другой (все виды обменов Вы можете посмотреть написав команду 'Таблица')")
        print("ВАЖНО: Вы можете обмениваться только в свой ход и перед броском кубиков, но зато количество обменов неограниченно.")
        print("ВАЖНО: Животных вы можете обменивать только в одну сторону (на более дорогих).")
        print("Пример №1: У Вас есть 7 кроликов, вы хотите получить одного барана", 
              " - в свой ход вы производите обмен и получаете одну овцу, а ещё у вас остаётся один кролик (одна овца стоит 6 кроликов).")
        print("Пример №2: У Вас есть 1 овца, вы хотите получить 6 кроликов",
              " - к сожалению у вас ничего не получится, потому что овца дороже кроликов.")
        
        answer()
        
    elif otvet == "КУБИКИ" or otvet == "2":
        app = 0
        cube_TR = cube_R[random.randint(0, 11)]
        cube_TY = cube_Y[random.randint(0, 11)]
        
        print("\nНа красном кубике выпало: ", cube_TR)
        print("На жёлтом кубике выпало: ", cube_TY)
        
        if cube_TR == cube_TY:
            app = 1 + player_ani.count(cube_TR) // 2
            print("\nВы получили: ", cube_TR, app, "x")
            
            for i in range(app):
                player_ani.append(cube_TR)
                
            print("\nТеперь у вас:")
            yourani()
            
        else:
            app = (player_ani.count(cube_TR) + 1) // 2
            print("\nВы получили: ", cube_TR, app, "x")
            
            for i in range(app):
                player_ani.append(cube_TR)
                
            app = (player_ani.count(cube_TY) + 1) // 2
            print("Вы получили: ", cube_TY, app, "x")
            
            for i in range(app):
                player_ani.append(cube_TY)
                
            print("\nТеперь у вас:")
            yourani()
            
        dli = 0
        
        if cube_TR == "Лиса":
            print("\nО нет! Вам выпала лиса! Она съедает всех ваших кроликов!")
            dli = bot_ani.count("Кролик")
            for i in range(dli):
                bot_ani.remove("Кролик")
            
            print("Теперь у Вас остались эти животные:")
            yourani()
            
        elif cube_TY == "Волк":
            print("\nО Боже! Вам выпал волк! Он съедает всех Ваших животных кроме коня!")
            
            dli = player_ani.count("Кролик")
            for i in range(dli):
                player_ani.remove("Кролик")
            
            dli = player_ani.count("Овца")
            for i in range(dli):
                player_ani.remove("Овца")
            
            dli = player_ani.count("Свинья")
            for i in range(dli):
                player_ani.remove("Свинья")
            
            dli = player_ani.count("Корова")
            for i in range(dli):
                player_ani.remove("Корова")
            
            print("Теперь у Вас остались только эти животные:")
            yourani()
                
    elif otvet == "ОБМЕН" or otvet == "3":
        print("\nДля выхода из режима обмена напишите 'выход'." )
        print("Введите имя животного, которого вы хотите получить и его количество через пробел:")
        obm = ["no", "none"]
        
        while(obm[0] != "ВЫХОД"):
            obm = input().upper().split()
            obm.append("666")
            obm[1] = int(obm[1])
            
            if obm[0] == "ОВЦА":
                if player_ani.count("Кролик") // 6 >= obm[1]:
                    for i in range(obm[1]):
                        player_ani.append("Овца")
                    for i in range(obm[1] * 6):
                        player_ani.remove("Кролик")
                        print("Операция прошла успешно!")
                        
                else:
                    print("Операция отменилась! У Вас не хватает животных! Проробуйте ещё раз: ")
                
            elif obm[0] == "СВИНЬЯ":
                if player_ani.count("Овца") // 2 >= obm[1]:
                    for i in range(obm[1]):
                        player_ani.append("Свинья")
                    for i in range(obm[1] * 2):
                        player_ani.remove("Овца")
                        print("Операция прошла успешно!")
                        
                else:
                    print("Операция отменилась! У Вас не хватает животных! Проробуйте ещё раз: ")
                        
            elif obm[0] == "КОРОВА":
                if player_ani.count("Свинья") // 3 >= obm[1]:
                    for i in range(obm[1]):
                        player_ani.append("Корова")
                    for i in range(obm[1] * 3):
                        player_ani.remove("Свинья")
                        print("Операция прошла успешно!")
                        
                else:
                    print("Операция отменилась! У Вас не хватает животных! Проробуйте ещё раз: ")
                        
            elif obm[0] == "КОНЬ":
                if player_ani.count("Корова") // 2 >= obm[1]:
                    for i in range(obm[1]):
                        player_ani.append("Конь")
                    for i in range(obm[1] * 2):
                        player_ani.remove("Корова")    
                    print("Операция прошла успешно!")
                    
                else:
                    print("Операция отменилась! У Вас не хватает животных! Проробуйте ещё раз: ")
                    
            elif obm[0] == "ВЫХОД":
                print("\nХорошо!")
                        
            else:
                print("\nЯ тебя не понимаю! Попробуй ещё раз!")
            
        
        answer()
        
    elif otvet == "ТАБЛИЦА" or otvet == "4":
        print("\nВы можете обменять:")
        print("\n6 кроликов на овцу")
        print("2 овец на свинью")
        print("3 свиньи на корову")
        print("2 коровы на коня")
        answer()
    
    elif otvet == "ЖИВОТНЫЕ" or otvet == "5":
        yourani()
        
    elif otvet == "HELP" or otvet == "6":
        helpme()
        
    else:
        print("\nЯ тебя не понимаю! Попробуй ввести ответ снова!")
        answer() 

# функция отвечающая за вывод животных компьютера

def botani():
        print("Ваши кролики: ", bot_ani.count("Кролик"))
        print("Ваши овцы: ", bot_ani.count("Овца"))
        print("Ваши свиньи: ", bot_ani.count("Свинья"))
        print("Ваши коровы: ", bot_ani.count("Корова"))
        print("Ваши кони: ", bot_ani.count("Конь"))
        
# функция отвечающая за ход компьютера
        
def bot_move():
    print("\nХод компьютера!")
    delim = 0
    while(True):
        if bot_ani.count("Конь") < 1:
            if bot_ani.count("Кролик") >= 6:
                delim = bot_ani.count("Кролик") // 6
                for i in range(delim):
                    bot_ani.append("Овца")
                for i in range(delim * 6):
                    bot_ani.remove("Кролик")
                    
            elif bot_ani.count("Овца") >= 2:
                delim = bot_ani.count("Овца") // 2
                for i in range(delim):
                    bot_ani.append("Свинья")
                for i in range(delim * 2):
                    bot_ani.remove("Овца")
                    
            elif bot_ani.count("Свинья") >= 6:
                delim = bot_ani.count("Свинья") // 3
                for i in range(delim):
                    bot_ani.append("Корова")
                for i in range(delim * 3):
                    bot_ani.remove("Свинья")
            
            elif bot_ani.count("Корова") >= 2:
                delim = bot_ani.count("Корова") // 2
                for i in range(delim):
                    bot_ani.append("Конь")
                for i in range(delim * 2):
                    bot_ani.remove("Корова")
            else:
                break
        else:
            if bot_ani.count("Кролик") >= 6 and (bot_ani.count("Корова") == 0 or bot_ani.count("Свинья") == 0 or bot_ani.count("Овца") == 0):
                delim = bot_ani.count("Кролик") // 6
                for i in range(delim):
                    bot_ani.append("Овца")
                for i in range(delim * 6):
                    bot_ani.remove("Кролик")
                    
            elif bot_ani.count("Овца") >= 2 and (bot_ani.count("Корова") == 0 or bot_ani.count("Свинья") == 0):
                delim = bot_ani.count("Овца") // 2
                for i in range(delim):
                    bot_ani.append("Свинья")
                for i in range(delim * 2):
                    bot_ani.remove("Овца")
                    
            elif bot_ani.count("Свинья") >= 3 and bot_ani.count("Корова") == 0:
                delim = bot_ani.count("Свинья") // 3
                for i in range(delim):
                    bot_ani.append("Корова")
                for i in range(delim * 3):
                    bot_ani.remove("Свинья")

            else:
                break
                
    print("\nКомпьютер произвёл обмен! Теперь у него:")
    botani()    
    
    print("\nБот кидает кубики!")
    
    cube_TR = cube_R[random.randint(0, 11)]
    cube_TY = cube_Y[random.randint(0, 11)]
        
    print("\nНа красном кубике выпало: ", cube_TR)
    print("На жёлтом кубике выпало: ", cube_TY)
    
    if cube_TR == cube_TY:
        app = 1 + bot_ani.count(cube_TR) // 2
        print("\nБот получил: ", cube_TR, app, "x")
            
        for i in range(app):
            bot_ani.append(cube_TR)
                
        print("\nТеперь у компьютера:")
        botani()
            
    else:
        app = (bot_ani.count(cube_TR) + 1) // 2
        print("\nБот получили: ", cube_TR, app, "x")
            
        for i in range(app):
            bot_ani.append(cube_TR)
                
        app = (bot_ani.count(cube_TY) + 1) // 2
        print("Бот получил: ", cube_TY, app, "x")
            
        for i in range(app):
            bot_ani.append(cube_TY)
            
        print("\nТеперь у компьютера:")
        botani()
    
    dli = 0
        
    if cube_TR == "Лиса":
        print("\nХа! Боту выпала лиса! Она съедает всех его кроликов!") 
        dli = bot_ani.count("Кролик")
        for i in range(dli):
            bot_ani.remove("Кролик")
            
        print("Теперь у бота остались эти животные:")
        botani()
        
    elif cube_TY == "Волк":
        print("\nАхаха! Боту выпал волк! Он съедает всех его животных кроме коня!")
        dli = bot_ani.count("Кролик")
        for i in range(dli):
            bot_ani.remove("Кролик")
            
        dli = bot_ani.count("Овца")
        for i in range(dli):
            bot_ani.remove("Овца")
            
        dli = bot_ani.count("Свинья")
        for i in range(dli):
            bot_ani.remove("Свинья")
            
        dli = bot_ani.count("Корова")
        for i in range(dli):
            bot_ani.remove("Корова")
            
        print("Теперь у бота остались только эти животные:")
        botani()
        
# животные которые есть на жёлтом и красном кубике

cube_Y = ["Волк", "Кролик", "Овца", "Кролик", "Кролик", "Овца", "Кролик",
          "Кролик", "Кролик", "Свинья", "Овца", "Корова"]
cube_R = ["Лиса", "Свинья", "Кролик", "Овца", "Кролик",
          "Кролик", "Кролик", "Свинья", "Кролик", "Кролик", "Овца", "Конь"]

# животные которые есть у игрока и компьютера

player_ani = ["Корова", "Корова"]
bot_ani = []

# корпус
    
print("                            SUPER FARMER")
print("Version: Pre-alpha")
print("\n\nПривет!") 

while(True):
    print("\nХотите сыграть в игру Супер Фермер (Да/Нет)? ")
    ans = input().upper()
    
    if ans == "ДА":
        print("\nВеликолепно!\nИтак начнём!")
        helpme()
        
        print("\nНАЧАЛО ИГРЫ")
        print("\n======================================================")
        print("\nТвой ход!")        
        
        win_pl = player_ani.count("Кролик") and player_ani.count("Овца") and player_ani.count("Свинья") and player_ani.count("Корова") and player_ani.count("Конь")
        win_bot = bot_ani.count("Кролик") and bot_ani.count("Овца") and bot_ani.count("Свинья") and bot_ani.count("Корова") and bot_ani.count("Конь")
        
        while(not(win_pl) or not(win_bot)):
            answer()
            bot_move()
            
        if win_pl:
            print("\nПоздравляю с победой!\n Хорошая игра!")
            
        elif win_bot:
            print("\nВы проиграли( \nВ другой раз повезёт!")
        
    elif ans == "НЕТ":
        print("\nЖаль! Тогда пока!")
        break
    
    else:
        print("\nЯ тебя не понимаю! Попробуй ввести ответ снова!")
        
# ROAD MAP
# Исправить ошибку в обмене DONE
# Дабавить бросок кубиков игрока DONE
# Добавить отбражение количества животных игрока после обена и броска кубиков DONE
# Добавить ход ИИ DONE
# Добавить собак
# Добавить режим для нескольких игроков
# Оптимизировать