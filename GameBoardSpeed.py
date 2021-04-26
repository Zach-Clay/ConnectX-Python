from AbsGameBoard import AbsGameBoard

class GameBoardSpeed(AbsGameBoard):
    """
    GameBoardSpeed implements AbsGameBoard using a 2D array 
    for speed efficiency.
    """
    def __init__(self, row, col, win):
        self.row = row
        self.col = col
        self.win = win
        self.board = [[0 for i in range(col)] for j in range(row)]

    #returns the number of rows on the board
    def getNumRows(self) -> int:
        return self.row

    #returns the number of columns on the board
    def getNumColumns(self) -> int:
        return self.col

    #returns the number of tokens in a row needed to win
    def getNumToWin(self) -> int:
        return self.win

    #places a token in the specified column in the lowest row available
    def placeToken(self, player, col) -> None:
        for i in range(self.row-1, -1, -1):
            if self.board[i][col] == 0:
                self.board[i][col] = player
                break

    #returns what token is occupied at position pos, if no token, ' ' is returned
    def whatsAtPos(self, pos) -> str:
        p = self.board[pos.getRow()][pos.getColumn()]
        if p == 0:
            p = ' '
        return p
