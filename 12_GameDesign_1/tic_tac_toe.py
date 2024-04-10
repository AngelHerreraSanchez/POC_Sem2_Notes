grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 2:
                print(grid[row][col], end="")            
            else:
                print(grid[row][col])
                
       

def game_loop():
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        print("Game Loop Running")
        user_choice = ""
    print("GAME OVER")
        
game_loop()