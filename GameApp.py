from GameBoardSpeed import GameBoardSpeed
from GameBoardMem import GameBoardMem

"""
Receives input from the user specifying the number of players
in the game and returns a list of each character playing
"""
def getPlayers() -> 'list':
    #min and max number of players
    min, max = 2, 10
    list = []
    num = 0
    while num < min or num > max:
        str = input(f"How many players? ({min}-{max}): ")
        num = int(str)
        if num < min:
            print(f"Must be at least {min} players")
        elif num > max:
            print(f"Cannot be more than {max} players")

    for i in range(1, num+1):
        str = input(f"Enter the character to represent player {i}: ")
        str = str.upper()
        #if the character has not been used
        if list.count(str) == 0:
            list.append(str)
        #prompt user this token is taken then ask again
        else:
            while list.count(str) != 0:
                print(f"{str} is already taken as a player token!")
                str = input(f"Enter the character to represent player {i}: ")
                str = str.upper()
            list.append(str)
    return list

#returns the number of rows on the board, specified by the user
def howManyRows() -> int:
    #min and max number of rows
    min, max = 3, 100
    row = 0
    while row < min or row > max:
        str = input(f"How many rows should be on the board? ({min}-{max}): ")
        row = int(str)
        if row < min:
            print(f"Must be at least {min} rows")
        elif row > max:
            print(f"Rows cannot be greater than {max}")
    return row

#returns the number of columns on the board, specified by the user
def howManyCols() -> int:
    #min and max number of cols
    min, max = 3, 100
    col = 0
    while col < min or col > max:
        str = input(f"How many columns should be on the board? ({min}-{max}): ")
        col = int(str)
        if col < min:
            print(f"Must be at least {min} columns")
        elif col > max:
            print(f"Columns cannot be greater than {max}")
    return col

#returns the number to win, specified by the user
def howManyToWin(row, col) -> int:
    #min and max number to win
    min, max = 3, 25
    win = 0
    while win < min or win > max or win > row or win > col:
        str = input(f"How many in a row to win? ({min}-{max}): ")
        win = int(str)
        if win < min:
            print(f"Must be at least {min} to win")
        elif win > max:
            print(f"Number to win cannot be greater than {max}")
        elif win > row:
            print(f"Number to win cannot be greater than the number of rows: ({row})")
        elif win > col:
            print(f"Number to win cannot be greater than the number of columns: ({col})")
    return win

#returns the column # that the player wants to place their token in
def getPlayersCol(board, player) -> int:
    getCol = True
    col = 0
    maxCol = board.getNumColumns()-1
    while getCol:
        str = input(f"Player {player}, what column do you want to place your token in?: ")
        col = int(str)
        if col < 0:
            print("Column cannot be less than 0")
        elif col > maxCol:
            print(f"Column cannot be greater than {maxCol}")
        elif col >= 0 and col <= maxCol:
            if board.checkIfFree(col):
                getCol = False
                break
            else:
                print("Column is full")
    return col

#returns true if the user wants to play another game
def askToPlayAgain() -> bool:
    askAgain = True
    while askAgain:
        str = input("Would you like to play again? Y/N: ")
        str = str.upper()
        if str == "N":
            return False
        elif str == "Y":
            return True
        else:
            print("Invalid character!")

    return False

#controls the flow of the game
def main():
    #bool to know when to stop the game
    playGame = True
    #bool to know if we need to create a new board
    playAgain = True
    #board will hold the state of the GameBoard
    board = None
    #players will hold the players specified by the user
    players = None

    #this loop will iterate until the user doesn't want to play anymore
    while playGame:
        
        #if we need to create a new board
        if playAgain:
            players = getPlayers()
            row = howManyRows()
            col = howManyCols()
            win = howManyToWin(row, col)
            #determine which AbsGameBoard implementation to use
            ask = True
            while ask:
                str = input("Would you like a Fast Game(F/f) or a Memory,"
                " Efficient Game(M/m)?: ")
                str = str.upper()
                if str == "F":
                    board = GameBoardSpeed(row, col, win)
                    ask = False
                elif str == "M":
                    board = GameBoardMem(row, col, win)
                    ask = False
                else:
                    print("Please enter F or M")
        
        playAgain = False

        #each player will place their token as many times as needed
        for i in range(len(players)):
            print(board)
            p = players[i]
            c = getPlayersCol(board, p)
            board.placeToken(p, c)
            #check if the placement resulted in a win
            if board.checkForWin(c):
                print(board)
                print(f"Player {p} Won!")
                #user wants to play again
                if askToPlayAgain():
                    playAgain = True
                    break
                else:
                    playGame = False
                    break
            #check if placement resulted in a tie
            if board.checkTie():
                print(board)
                print("It's a tie!")
                #user wants to play again
                if askToPlayAgain():
                    playAgain = True
                    break
                else:
                    playGame = False
                    break
main()
