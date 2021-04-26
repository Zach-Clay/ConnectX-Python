from abc import ABC, abstractmethod
from BoardPosition import BoardPosition

class AbsGameBoard(ABC):
    """
    AbsGameBoard is abstractly a 2D Grid of characters representing
    a connectX game. This class contains many hook (default) methods
    that do not need to be overridden in subclasses.
    """
    #returns the number of rows on the board
    @abstractmethod
    def getNumRows(self) -> int:
        pass

    #returns the number of columns on the board
    @abstractmethod
    def getNumColumns(self) -> int:
        pass

    #returns the number of tokens in a row needed to win
    @abstractmethod
    def getNumToWin(self) -> int:
        pass

    #places a token in the specified column in the lowest row available
    @abstractmethod
    def placeToken(self, player, col) -> None:
        pass

    #returns what token is occupied at position pos, if no token, ' ' is returned
    @abstractmethod
    def whatsAtPos(self, pos) -> str:
        pass

    #returns a string representation of the GameBoard
    def __str__(self) -> str:
        s = "|"
        #one_space is used to determine if spacing needs to adjust
        #for columns above 10
        one_space = 10

        for i in range(self.getNumColumns()):
            if i >= one_space:
                s += " " + str(i) + " |"
            else:
                s += "  " + str(i) + " |"
        s += "\n"

        for i in range(self.getNumRows()):
            for j in range(self.getNumColumns()):
                pos = BoardPosition(i, j)
                s += "| " + self.whatsAtPos(pos) + "  "
            s += "|\n"
        return s

    #true if column does not contain #getNumRows() characters
    def checkIfFree(self, col) -> bool:
        for i in range(self.getNumRows()-1, -1, -1):
            pos = BoardPosition(i, col)
            if self.whatsAtPos(pos) == ' ':
                return True
        return False

    #true if all positions on the board have been occupied
    def checkTie(self) -> bool:
        for i in range(self.getNumRows()):
            for j in range(self.getNumColumns()):
                pos = BoardPosition(i, j)
                if self.whatsAtPos(pos) == ' ':
                    return False
        return True

    #true if #getNumToWin() equivalent tokens are placed horizontally, vertically, or diagonally
    def checkForWin(self, col) -> bool:
        for i in range(self.getNumRows()-1, -1, -1):
            temp = BoardPosition(i, col)

            if self.whatsAtPos(temp) == ' ':
                pos = BoardPosition(i+1, col)
                player = self.whatsAtPos(pos)
                if self.checkHorizWin(pos, player):
                    return True
                elif self.checkVertWin(pos, player):
                    return True
                elif self.checkDiagWin(pos, player):
                    return True
                else:
                    break
            elif i == 0:
                pos = BoardPosition(i, col)
                player = self.whatsAtPos(pos)
                if self.checkHorizWin(pos, player):
                    return True
                elif self.checkVertWin(pos, player):
                    return True
                elif self.checkDiagWin(pos, player):
                    return True
                else:
                    break
        return False

    #true if player has #getNumToWin() in a row horizontally
    def checkHorizWin(self, pos, player) -> bool:
        r = pos.getRow()
        c = pos.getColumn()-1
        count = 1

        #Searches to the left of the last token
        while c > -1:
            temp = BoardPosition(r, c)
            if self.isPlayerAtPos(temp, player):
                count+=1
            else:
                break
            if count == self.getNumToWin():
                return True
            c-=1
        
        c = pos.getColumn()+1

        #Searches to the right of the last token
        while c < self.getNumColumns():
            temp = BoardPosition(r, c)
            if self.isPlayerAtPos(temp, player):
                count+=1
            else:
                break
            if count == self.getNumToWin():
                return True
            c+=1
        
        return False

    #true if player has #getNumToWin() in a row vertically
    def checkVertWin(self, pos, player) -> bool:
        r = pos.getRow()+1
        c = pos.getColumn()
        count = 1

        #searches down the board
        while r < self.getNumRows():
            temp = BoardPosition(r, c)
            if self.isPlayerAtPos(temp, player):
                count+=1
            else:
                break
            r+=1
        if count >= self.getNumToWin():
            return True
        return False
    
    #true if player has #getNumToWin() in a row diagonally
    def checkDiagWin(self, pos, player) -> bool:
        r = pos.getRow()
        c = pos.getColumn()
        count = 0
        
        #First we look for a \ (SE) direction win
        #this loop traces r and c to the top left of the board
        while r > 0 and c > 0:
            r-=1
            c-=1
        
        #this loop keeps count of diagonal characters
        while r < self.getNumRows() and c < self.getNumColumns():
            temp = BoardPosition(r, c)
            if self.isPlayerAtPos(temp, player):
                count+=1
            if count == self.getNumToWin():
                return True
            if not self.isPlayerAtPos(temp, player):
                count = 0
            r+=1
            c+=1

        #if \ (SE) direction didn't win, this step looks for a / (SW) direction win
        r = pos.getRow()
        c = pos.getColumn()
        count = 0

        #this loop traces to the bottom left of the board
        while r < self.getNumRows()-1 and c > 0:
            r+=1
            c-=1

        #this loop keeps count of diagonal characters
        while r > -1 and c < self.getNumColumns():
            temp = BoardPosition(r, c)
            if self.isPlayerAtPos(temp, player):
                count+=1
            if count == self.getNumToWin():
                return True
            if not self.isPlayerAtPos(temp, player):
                count = 0
            r-=1
            c+=1

        return False

    #true if the token at pos == player
    def isPlayerAtPos(self, pos, player) -> bool:
        c = self.whatsAtPos(pos)
        if c == player:
            return True
        return False
