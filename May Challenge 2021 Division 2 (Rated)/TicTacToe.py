# https://www.codechef.com/MAY21B/problems/TCTCTOE

# Solution in Python


def CheckKeyAllSides(key,Grid):
    if Grid[0][0] == key and Grid[1][0] == key and Grid[2][0] == key:
        return True
    elif Grid[0][1] == key and Grid[1][1] == key and Grid[2][1] == key:
        return True
    elif Grid[0][2] == key and Grid[1][2] == key and Grid[2][2] == key:
        return True
    elif Grid[0][0] == key and Grid[0][1] == key and Grid[0][2] == key:
        return True
    elif Grid[1][0] == key and Grid[1][1] == key and Grid[1][2] == key:
        return True
    elif Grid[2][0] == key and Grid[2][1] == key and Grid[2][2] == key:
        return True
    elif Grid[0][0] == key and Grid[1][1] == key and Grid[2][2] == key:
        return True
    elif Grid[2][0] == key and Grid[1][1] == key and Grid[0][2] == key:
        return True
    else:
        return False
    # if Grid[1][1] == key or Grid[0][0] == key or Grid[2][2] == key:
    #     if Grid[2][0] == key and Grid[0][2] == key:
    #         return True
    #     elif Grid[0][0] == key and Grid[2][2] == key:
    #         return True
    #     elif Grid[0][1] == key and Grid[2][1] == key:
    #         return True
    #     elif Grid[1][0] == key and Grid[1][2] == key:
    #         return True
    #     elif Grid[1][0] == key and Grid[2][0] == key:
    #         return True
    #     elif Grid[0][1] == key and Grid[0][2] == key:
    #         return True
    #     elif Grid[2][0] == key and Grid[2][1] == key:
    #         return True
    #     elif Grid[0][2] == key and Grid[1][2] == key:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False
            
    
    
    
def CountKeys(Grid):
    X = 0
    O = 0
    empty = 0
    for i in range(3):
        for j in range(3):
            if Grid[i][j] == 'X':
                X = X+1
            elif Grid[i][j] == 'O':
                O = O+1
            else:
                empty = empty + 1
    return X,O,empty
        
        
def TICTACTOE(Grid):
    playerX_won = CheckKeyAllSides('X',Grid) 
    playerO_won = CheckKeyAllSides('O',Grid) 
    playerX_cnt,playerO_cnt,empty_cnt = CountKeys(Grid)
    if (playerX_won == True and playerO_won == True) or (playerX_cnt < playerO_cnt) or (playerX_cnt > playerO_cnt+1):
        print(3)
    elif (playerX_won == True and playerO_won == False) and (playerX_cnt > playerO_cnt):
        print(1)
    elif (playerX_won == False and playerO_won == True) and (playerX_cnt == playerO_cnt):
        print(1)
    elif (playerX_won == False and playerO_won == False) and empty_cnt == 0:
        print(1)
    elif (playerX_won == False and playerO_won == False) and empty_cnt == 9:
        print(2)
    elif (playerX_won == False and playerO_won == False) and empty_cnt > 0:
        print(2)
    else:
        print(3)
        
        
        
for _ in range(int(input())):
    Grid = []
    for _ in range(3):
        temp = input()
        Grid.append(list(temp))
    TICTACTOE(Grid)
        
        
    
    
    
