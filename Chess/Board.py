import pygame
from Piece import *
from Constants import *


class Board:
    def __init__(self):
        self.board = [[] for _ in range(ROWS)]
        self.play_turn = "w"
        self.check = False

    def place_piece(self):
        # Creating the piece objects
        # Locating to proper order in board list
        self.board[0].append(Rook(0, 0, "b", "bR"))
        self.board[0].append(Knight(0, 1, "b", "bN"))
        self.board[0].append(Bishop(0, 2, "b", "bB"))
        self.board[0].append(Queen(0, 3, "b", "bQ"))
        self.board[0].append(King(0, 4, "b", "bK"))
        self.board[0].append(Bishop(0, 5, "b", "bB"))
        self.board[0].append(Knight(0, 6, "b", "bN"))
        self.board[0].append(Rook(0, 7, "b", "bR"))

        self.board[7].append(Rook(7, 0, "w", "wR"))
        self.board[7].append(Knight(7, 1, "w", "wN"))
        self.board[7].append(Bishop(7, 2, "w", "wB"))
        self.board[7].append(Queen(7, 3, "w", "wQ"))
        self.board[7].append(King(7, 4, "w", "wK"))
        self.board[7].append(Bishop(7, 5, "w", "wB"))
        self.board[7].append(Knight(7, 6, "w", "wN"))
        self.board[7].append(Rook(7, 7, "w", "wR"))

        # Creating pawns
        for row in range(ROWS):
            for column in range(COLUMNS):
                if row == 1:
                    self.board[row].append(Pawn(row, column, "b", "bP"))
                elif row == 6:
                    self.board[row].append(Pawn(row, column, "w", "wP"))
                elif row != 1 or row != 6:
                    self.board[row].append(0)

    def draw_to_board(self, win):
        # Locating the piece objects in the window
        piece_dic = load_piece_image()
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] != 0:
                    piece_obj = self.board[row][column]
                    pieceX, pieceY = piece_obj.draw(win, self.board)
                    win.blit(piece_dic[piece_obj.name], (pieceX, pieceY))

    # Creating the board with drawing squares to the screen
    # Filling the all background with the green
    # Draw cream squares starting with (0, 0) point
    def draw_squares(self, win):
        win.fill(GREEN)
        for row in range(ROWS):
            for column in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, CREAM, (column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Chancing the board after making valid move
    def moves(self, piece, divX, divY):
        if piece != 0 and piece.selected:
            # Looking for a valid move
            val_mov = piece.valid_moves(self.board)
            for moves in val_mov:
                # Checking second click is in the valid moves
                if divX == moves[0] and divY == moves[1]:
                    n_board = self.board[:]
                    # Taking the piece in the second click location
                    n_board[divY][divX] = n_board[piece.row][piece.column]
                    # Making precious location blank
                    n_board[piece.row][piece.column] = 0
                    # Chancing the Piece location
                    piece.row = moves[1]
                    piece.column = moves[0]
                    self.board = n_board
                    # When white makes the move we chance the player turn
                    if self.play_turn == "w":
                        self.play_turn = "b"
                    else:
                        self.play_turn = "w"
