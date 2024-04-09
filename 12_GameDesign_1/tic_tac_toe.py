grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

current_player = "X"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 2:
                print(grid[row][col], end="")            
            else:
                print(grid[row][col])
                
def handle_input(value):
    if(value.__eq__("STOP")):
        return False
    elif(value.__eq__("1")):
        return False
    elif (value.__eq__("2")):
        return False
    elif (value.__eq__("3")):
        return False
    elif(value.__eq__("4")):
        return False
    elif (value.__eq__("5")):
        return False
    elif(value.__eq__("6")):
        return False
    elif(value.__eq__("7")):
        return False
    elif(value.__eq__("8")):
        return False
    elif (value.__eq__("9")):
        return False
    else:
        return True
        

def game_loop():
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while (handle_input(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        print("Game Loop Running")
        user_choice = ""
    print("GAME OVER")
        
game_loop()