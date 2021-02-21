class Pawn():

    def __init__(self, color, position):
        self.position = position
        self.hasMoved = False
        self.validMoves = []
        self.code = 9
        self.color = color
        self.possibleDirectionsTuple = []
    
    def calculateValidMoves(self, board):

        self.validMoves = []

        if self.hasMoved == False:
            self.validMoves.append((self.position[0] + 1, self.position[1]))
            self.validMoves.append((self.position[0] + 2, self.position[1]))
        elif self.hasMoved == True:
            self.validMoves.append((self.position[0]+ 1, self.position[1]))