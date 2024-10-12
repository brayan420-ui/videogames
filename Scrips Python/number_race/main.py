from random import randint
import os
status_menu = True


def main_menu():
    global status_opt
    status_opt = True
    print ("=== Main Menu ===")
    print("[1]. Start game")
    print("[2]. Help")
    print("[3]. Exit")
    opt = int(input("Press any option: "))
    
    while status_opt:
        opt = int(input("Press any option: "))
        if opt < 1 or opt > 3:
            print("Error, press any option between 1 and 3")
        else:
            status_opt = False
        return opt
    
while status_menu:
    op = main_menu()
    if op == 1:
        os.system('clear')
        print("===WELCOME TO NUMBER RACE===")
        
        players = int(input("Press number of players [1-4]: "))
        print("=== Level Menu ===")
        
        print("[1]. Basic")
        print("[2]. Intermediate")
        print("[3]. Advance")
        print("[4]. Expert")
        opt = int(input("Press any option: "))
        
        if opt == 1:
            pos = 20
        elif opt == 2:
            pos = 30
        elif opt == 3:
            pos = 50
        else:
            pos = 100
        
        # START GAME
        status_game = True
        roll_count = 0
        roll_acum = 0
        while status_game:
            os.system("clear")
            input("Press any key to roll dice..")  
                
            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(f"Dice 1: {dice1}")
            print(f"Dice 2: {dice2}")
            total = dice1 + dice2
            print(f"Total roll = {total}")
            
            roll_count += 1
            roll_acum += total
            print(f"Total game score = {roll_acum}")
            
            if roll_acum >= 50:  # Se gana al alcanzar 50 puntos acumulados
                print(": : : YOU WIN : : :") 
                status_game = False
                
            os.system("pause")
            
        print("INFO")
        print(f"Total rolls: {roll_count}")
        print(f"Total dice sum: {roll_acum}")
        
        input("Press any key to go to the main menu.. ")
    elif op == 2:
        print("Help under construction")
        input("Press any key to go to the main menu.. ")
    else:
        print("See you later!")
        input("Press any key to exit.. ")
