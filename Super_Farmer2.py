import random

def answer():
    otvet = input().upper()
    
    if otvet == "ПРАВИЛА" or otvet == "1":
        print("Fig tebe")
        
    elif otvet == "КУБИКИ" or otvet == "2":
        print("Ок")
        
    elif otvet == "ОБМЕН" or otvet == "3":
        print("Кек")
    
    else:
        print("\nЯ тебя не понимаю! Попробуй ввести ответ снова!")
        answer()
        

cube_ani1 = ["Кролик", "Овца", "Свинья", "Корова", "Волк"]
cube_ani2 = ["Кролик", "Овца", "Свинья", "Конь", "Лиса"]
player_ani = []
bot_ani = []
    
print("                            SUPER FARMER")
print("\nПривет!") 

while(True):
    print("\nХочешь сыграть в игру Супер Фермер (Да/Нет)? ")
    ans = input().upper()
    
    if ans == "ДА":
        print("\nВеликолепно!\nИтак начнём!\nВот команды которые ты можешь использовать:")
        print("1) Правила - введи эту команду если ты хочешь прочитать правила игры.")
        print("2) Кубики - введи эту команду если ты хочешь кинуть кубики.")
        print("3) Обмен - введи эту команду если ты хочешь обменять своих животных на других.")
        
        
    elif ans == "НЕТ":
        print("\nЖаль! Тогда пока!")
        break
    
    else:
        print("\nЯ тебя не понимаю! Попробуй ввести ответ снова!")