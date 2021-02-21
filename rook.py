class Rook():

    def __init__(self, color, position):
        self.position = position
        self.hasMoved = False
        self.validMoves = []
        self.code = 2
        self.color = color
        self.possibleDirectionsTuple = [(1,0), (0,1), (-1,0), (0,-1)]
    
    def calculateValidMoves(self, board):

        self.validMoves = []

        for directionTuple in self.possibleDirectionsTuple:
            possiblePosition = self.position

            
            while (0 <= possiblePosition[0] <= 7) and (0 <= possiblePosition[1] <= 7):

                possibleY = possiblePosition[0] + directionTuple[0]
                possibleX = possiblePosition[1] + directionTuple[1]

                if (possibleY in board.retrieveClosestYPieceCoordinate(self.position)):
                    break
                
                if (possibleX in board.retrieveClosestXPieceCoordinate(self.position)):
                    break

                if (possibleX != -1 and possibleX != 8) and (possibleY != -1 and possibleY != 8):
                    self.validMoves.append((possibleY, possibleX))

                possiblePosition = (possibleY, possibleX)
                print(possiblePosition)