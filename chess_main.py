"This is responsible for handling the user inputs"
import chess_engine
import pygame as pg


WIDTH = HEIGHT = 800
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}  # This dictionary stores images for pieces

def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wp", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load(piece+".png"), (SQ_SIZE, SQ_SIZE))

def main():
    pg.init()  # Initializes all the Pygame modules
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = chess_engine.GameState()
    load_images()  # Loads images only once
    running = True
    sqSelected=()
    playerClicks=[]
    
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type== pg.MOUSEBUTTONDOWN:
                location=pg.mouse.get_pos() #(x,y) location of mouse
                col=location[0]//SQ_SIZE
                row=location[1]//SQ_SIZE
                
                if sqSelected==(row,col): #clicking the same square twice
                    sqSelected=()#deselect the click
                    playerClicks=[] #clear the player clicks list
                else:
                    sqSelected=(row,col)
                    playerClicks.append(sqSelected)#append for 1 and 2 clicks
                if len(playerClicks) ==2: #after 2nd click
                    move=chess_engine.Move(playerClicks[0],playerClicks[1],gs.board)
                    gs.makeMove(move)
                    sqSelected=()#resetting clicks
                    playerClicks =[]# resetting for the next move
                    
                     
        
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()  # Updates the display window

def draw_game_state(screen, gs):
    draw_board(screen)  # Draw squares  on the board
    draw_pieces(screen, gs.board)  # Draw pieces on top of the squares

def draw_board(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if (r + c) % 2 == 0:
                color = pg.Color("white")
            else:
                color = pg.Color("darkgreen")
            pg.draw.rect(screen, color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()


