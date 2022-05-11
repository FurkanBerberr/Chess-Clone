import pygame
from Constants import *
from Board import *
from Piece import *

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Chess")
board = Board()
bo = board.board


def click(location):
    x = location[0]
    y = location[1]
    divX = int(x / (WIDTH/8))
    divY = int(y / (HEIGHT/8))
    chosen = bo[divY][divX]

    for row in bo:
        for piece in row:
            if piece != 0:
                board.moves(piece, divX, divY)
                piece.selected = False
    if chosen != 0:
        # If we have the turn to play we can select the piece
        if board.play_turn == chosen.color:
            chosen.selected = True
    return divX, divY

def draw_window():
    board.draw_squares(WIN)
    board.place_piece()
    board.draw_to_board(WIN)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                divX, divY = click(location)
        draw_window()


    pygame.quit()

if __name__ == "__main__":
    main()
