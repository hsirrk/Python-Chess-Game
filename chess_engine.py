"This is responsible for storing the current state of the chess game, also determines the valid moves in the chess game"

class GameState():
    def __init__(self):
        #b denotes black, w is white
        #R denotes rook, B denotes bishop, etc
        #-- denotes empty squares
        self.board =[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
            ]
        
        self.WhiteToMove=True# tracks if its white turn to move
        self.MoveLog=[]#tracks how the pieces are moving
        
    def makeMove(self, move):
        
        self.board[move.startRow][move.startCol]="--"
        self.board[move.endRow][move.endCol]=move.pieceMoved
        self.MoveLog.append(move)#log the move so we can undo later???
        self.WhiteToMove= False # other players turn to move

            
    
class Move():
    
    def __init__(self, startSq, endSq, board):
        self.startRow=startSq[0]
        self.startCol=startSq[1]
        self.endRow=endSq[0]
        self.endCol=endSq[1]
        self.pieceMoved=board[self.startRow][self.startCol]
        self.pieceCaptured=board[self.endRow][self.endCol]
        