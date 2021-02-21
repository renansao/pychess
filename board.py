class Board():

    def __init__(self):
        self.board = []
        self.piecesOnBoard = []
    
    def createBoard(self):
        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[i].append(0)

    def addPieceToBoard(self, piece):
        self.piecesOnBoard.append(piece)
        self.board[piece.position[0]][piece.position[1]] = piece.code
    
    def move(self, piece, newPosition):
        if newPosition in piece.validMoves:
            self.board[piece.position[0]][piece.position[1]] = 0
            self.board[newPosition[0]][newPosition[1]] = piece.code
            piece.position = newPosition
            piece.hasMoved = True
        else:
            return False
        
        return True
    
    def retrieveClosestYPieceCoordinate(self, piecePosition):

        closestPiecesPosition = []

        y = piecePosition[0] + 1
        while (y <= 7):
            if self.board[y][piecePosition[1]] != 0:
                closestPiecesPosition.append(y)
            y+=1
        
        y = piecePosition[0] - 1
        while (y >= 0):
            if self.board[y][piecePosition[1]] != 0:
                closestPiecesPosition.append(y)
            y-=1
        
        print("pieces : ", closestPiecesPosition)

        return closestPiecesPosition

    def retrieveClosestXPieceCoordinate(self, piecePosition):
        
        closestPiecesPosition = []

        x = piecePosition[1] + 1
        while (x <= 7):
            if self.board[piecePosition[0]][x] != 0:
                closestPiecesPosition.append(x)
            x+=1
        
        x = piecePosition[1] - 1
        while (x >= 0):
            if self.board[piecePosition[0]][x] != 0:
                closestPiecesPosition.append(x)
            x-=1
        
        print("pieces : ", closestPiecesPosition)

        return closestPiecesPosition