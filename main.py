from pawn import Pawn
from board import Board
from rook import Rook

board = Board() 
piao = Pawn(0, (5,4))
piao.code = 4
piao2 = Pawn(0, (2,4))
piao2.code = 4
piao3 = Pawn(0, (4,2))
piao3.code = 4
piao4 = Pawn(0, (4,6))
piao4.code = 4
torre = Rook(0, (4,4))
board.createBoard()
board.addPieceToBoard(piao)
board.addPieceToBoard(piao2)
board.addPieceToBoard(piao3)
board.addPieceToBoard(piao4)
board.addPieceToBoard(torre)

for chessFile in board.board:
    print(chessFile)

for pieceOnBoard in board.piecesOnBoard:
    print(pieceOnBoard)

torre.calculateValidMoves(board)
print(torre.validMoves)

for validRookMove in torre.validMoves:
    board.addPieceToBoard(Pawn(0, validRookMove))

board.board.reverse()
for chessFile in board.board:
    print(chessFile)