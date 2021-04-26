class BoardPosition:
    """
    BoardPosition is used to represent a player's token on the ConnectX
    Board. This is a very simple class, it only contains the row number and
    column number.
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other)  -> bool:
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self)  -> str:
        return str(self.row) + "," + str(self.col)
    
    def getRow(self) -> int:
        return self.row

    def getColumn(self) -> int:
        return self.col