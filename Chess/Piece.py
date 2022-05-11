import pygame
import os
import operator
from Constants import *


class Piece:
    def __init__(self, row, column, color, name):
        self.row = row
        self.column = column
        self.color = color
        self.name = name
        self.selected = False

    def draw(self, win, board):
        piece = pygame.Rect(self.column * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        if self.selected:
            # Shows the selected piece
            pygame.draw.rect(win, (0, 0, 255), (self.column*SQUARE_SIZE, self.row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
            moves = self.valid_moves(board)
            for move in moves:
                x = (move[0]*SQUARE_SIZE)
                y = (move[1]*SQUARE_SIZE)
                pygame.draw.rect(win, (0, 0, 255), (x, y, SQUARE_SIZE, SQUARE_SIZE), 3)
        return piece.x, piece.y


class Rook(Piece):
    def valid_moves(self, board):
        moves = []
        if self.selected:
            # Right
            right = self.column
            right += 1
            while 0 <= right < 8:
                piece = board[self.row][right]
                if piece == 0:
                    moves.append((right, self.row))
                else:
                    if piece.color != self.color:
                        moves.append((right, self.row))
                    break
                right += 1

            # Left
            left = self.column
            left -= 1
            while 0 <= left < 8:
                piece = board[self.row][left]
                if piece == 0:
                    moves.append((left, self.row))
                else:
                    if piece.color != self.color:
                        moves.append((left, self.row))
                    break
                left -= 1

            # Up
            up = self.row
            up -= 1
            while 0 <= up < 8:
                piece = board[up][self.column]
                if piece == 0:
                    moves.append((self.column, up))
                else:
                    if piece.color != self.color:
                        moves.append((self.column, up))
                    break
                up -= 1

            # Down
            down = self.row
            down += 1
            while 0 <= down < 8:
                piece = board[down][self.column]
                if piece == 0:
                    moves.append((self.column, down))
                else:
                    if piece.color != self.color:
                        moves.append((self.column, down))
                    break
                down += 1

        return moves


class Knight(Piece):
    # Knight has two type of valid move
    # Short one is first move two place vertically and go one horizontally up
    # Long one is first move two place horizontally and go one vertically
    def valid_moves(self, board):
        moves = []

        # Up and right
        # Short
        up_UR = self.row
        right_UR = self.column
        up_UR -= 1
        right_UR += 2
        if 0 <= right_UR < 8 and 0 <= up_UR < 8:
            piece = board[up_UR][right_UR]
            if piece == 0:
                moves.append((right_UR, up_UR))
            else:
                if piece.color != self.color:
                    moves.append((right_UR, up_UR))
        # Long
        up_UR = self.row
        right_UR = self.column
        up_UR -= 2
        right_UR += 1
        if 0 <= right_UR < 8 and 0 <= up_UR < 8:
            piece = board[up_UR][right_UR]
            if piece == 0:
                moves.append((right_UR, up_UR))
            else:
                if piece.color != self.color:
                    moves.append((right_UR, up_UR))

        # Up and left
        # Short
        up_UL = self.row
        right_UL = self.column
        up_UL -= 1
        right_UL -= 2
        if 0 <= right_UL < 8 and 0 <= up_UL < 8:
            piece = board[up_UL][right_UL]
            if piece == 0:
                moves.append((right_UL, up_UL))
            else:
                if piece.color != self.color:
                    moves.append((right_UL, up_UL))
        # Long
        up_UL = self.row
        right_UL = self.column
        up_UL -= 2
        right_UL -= 1
        if 0 <= right_UL < 8 and 0 <= up_UL < 8:
            piece = board[up_UL][right_UL]
            if piece == 0:
                moves.append((right_UL, up_UL))
            else:
                if piece.color != self.color:
                    moves.append((right_UL, up_UL))

        # Down and left
        # Short
        down_DL = self.row
        right_DL = self.column
        down_DL += 1
        right_DL -= 2
        if 0 <= down_DL < 8 and 0 <= right_DL < 8:
            piece = board[down_DL][right_DL]
            if piece == 0:
                moves.append((right_DL, down_DL))
            else:
                if piece.color != self.color:
                    moves.append((right_DL, down_DL))
        # Long
        down_DL = self.row
        right_DL = self.column
        down_DL += 2
        right_DL -= 1
        if 0 <= down_DL < 8 and 0 <= right_DL < 8:
            piece = board[down_DL][right_DL]
            if piece == 0:
                moves.append((right_DL, down_DL))
            else:
                if piece.color != self.color:
                    moves.append((right_DL, down_DL))

        # Down and right
        # Short
        down_DR = self.row
        right_DR = self.column
        down_DR += 1
        right_DR += 2
        if 0 <= down_DR < 8 and 0 <= right_DR < 8:
            piece = board[down_DR][right_DR]
            if piece == 0:
                moves.append((right_DR, down_DR))
            else:
                if piece.color != self.color:
                    moves.append((right_DR, down_DR))
        # Long
        down_DR = self.row
        right_DR = self.column
        down_DR += 2
        right_DR += 1
        if 0 <= down_DR < 8 and 0 <= right_DR < 8:
            piece = board[down_DR][right_DR]
            if piece == 0:
                moves.append((right_DR, down_DR))
            else:
                if piece.color != self.color:
                    moves.append((right_DR, down_DR))

        return moves



class Bishop(Piece):
    def valid_moves(self, board):
        moves = []

        # Up and right
        up_UR = self.row
        right_UR = self.column
        up_UR -= 1
        right_UR += 1
        while 0 <= right_UR < 8 and 0 <= up_UR < 8:
            piece = board[up_UR][right_UR]
            if piece == 0:
                moves.append((right_UR, up_UR))
            else:
                if piece.color != self.color:
                    moves.append((right_UR, up_UR))
                break
            up_UR -= 1
            right_UR += 1

        # Up and left
        up_UL = self.row
        right_UL = self.column
        up_UL -= 1
        right_UL -= 1
        while 0 <= right_UL < 8 and 0 <= up_UL < 8:
            piece = board[up_UL][right_UL]
            if piece == 0:
                moves.append((right_UL, up_UL))
            else:
                if piece.color != self.color:
                    moves.append((right_UL, up_UL))
                break
            up_UL -= 1
            right_UL -= 1

        # Down and left
        down_DL = self.row
        right_DL = self.column
        down_DL += 1
        right_DL -= 1
        while 0 <= down_DL < 8 and 0 <= right_DL < 8:
            piece = board[down_DL][right_DL]
            if piece == 0:
                moves.append((right_DL, down_DL))
            else:
                if piece.color != self.color:
                    moves.append((right_DL, down_DL))
                break
            down_DL += 1
            right_DL -= 1

        # Down and right
        down_DR = self.row
        right_DR = self.column
        down_DR += 1
        right_DR += 1
        while 0 <= down_DR < 8 and 0 <= right_DR < 8:
            piece = board[down_DR][right_DR]
            if piece == 0:
                moves.append((right_DR, down_DR))
            else:
                if piece.color != self.color:
                    moves.append((right_DR, down_DR))
                break
            down_DR += 1
            right_DR += 1

        return moves


class Queen(Piece):
    def valid_moves(self, board):
        moves = []

        # Up and right
        up_UR = self.row
        right_UR = self.column
        up_UR -= 1
        right_UR += 1
        while 0 <= right_UR < 8 and 0 <= up_UR < 8:
            piece = board[up_UR][right_UR]
            if piece == 0:
                moves.append((right_UR, up_UR))
            else:
                if piece.color != self.color:
                    moves.append((right_UR, up_UR))
                break
            up_UR -= 1
            right_UR += 1

        # Up and left
        up_UL = self.row
        right_UL = self.column
        up_UL -= 1
        right_UL -= 1
        while 0 <= right_UL < 8 and 0 <= up_UL < 8:
            piece = board[up_UL][right_UL]
            if piece == 0:
                moves.append((right_UL, up_UL))
            else:
                if piece.color != self.color:
                    moves.append((right_UL, up_UL))
                break
            up_UL -= 1
            right_UL -= 1

        # Down and left
        down_DL = self.row
        right_DL = self.column
        down_DL += 1
        right_DL -= 1
        while 0 <= down_DL < 8 and 0 <= right_DL < 8:
            piece = board[down_DL][right_DL]
            if piece == 0:
                moves.append((right_DL, down_DL))
            else:
                if piece.color != self.color:
                    moves.append((right_DL, down_DL))
                break
            down_DL += 1
            right_DL -= 1

        # Down and right
        down_DR = self.row
        right_DR = self.column
        down_DR += 1
        right_DR += 1
        while 0 <= down_DR < 8 and 0 <= right_DR < 8:
            piece = board[down_DR][right_DR]
            if piece == 0:
                moves.append((right_DR, down_DR))
            else:
                if piece.color != self.color:
                    moves.append((right_DR, down_DR))
                break
            down_DR += 1
            right_DR += 1

        # Right
        right = self.column
        right += 1
        while 0 <= right < 8:
            piece = board[self.row][right]
            if piece == 0:
                moves.append((right, self.row))
            else:
                if piece.color != self.color:
                    moves.append((right, self.row))
                break
            right += 1

        # Left
        left = self.column
        left -= 1
        while 0 <= left < 8:
            piece = board[self.row][left]
            if piece == 0:
                moves.append((left, self.row))
            else:
                if piece.color != self.color:
                    moves.append((left, self.row))
                break
            left -= 1

        # Up
        up = self.row
        up -= 1
        while 0 <= up < 8:
            piece = board[up][self.column]
            if piece == 0:
                moves.append((self.column, up))
            else:
                if piece.color != self.color:
                    moves.append((self.column, up))
                break
            up -= 1

        # Down
        down = self.row
        down += 1
        while 0 <= down < 8:
            piece = board[down][self.column]
            if piece == 0:
                moves.append((self.column, down))
            else:
                if piece.color != self.color:
                    moves.append((self.column, down))
                break
            down += 1

        return moves


class King(Piece):
    def valid_moves(self, board):
        moves = []

        # Up and right
        up_UR = self.row
        right_UR = self.column
        up_UR -= 1
        right_UR += 1
        if 0 <= right_UR < 8 and 0 <= up_UR < 8:
            piece = board[up_UR][right_UR]
            if piece == 0:
                moves.append((right_UR, up_UR))
            else:
                if piece.color != self.color:
                    moves.append((right_UR, up_UR))

        # Up and left
        up_UL = self.row
        right_UL = self.column
        up_UL -= 1
        right_UL -= 1
        if 0 <= right_UL < 8 and 0 <= up_UL < 8:
            piece = board[up_UL][right_UL]
            if piece == 0:
                moves.append((right_UL, up_UL))
            else:
                if piece.color != self.color:
                    moves.append((right_UL, up_UL))

        # Down and left
        down_DL = self.row
        right_DL = self.column
        down_DL += 1
        right_DL -= 1
        if 0 <= down_DL < 8 and 0 <= right_DL < 8:
            piece = board[down_DL][right_DL]
            if piece == 0:
                moves.append((right_DL, down_DL))
            else:
                if piece.color != self.color:
                    moves.append((right_DL, down_DL))

        # Down and right
        down_DR = self.row
        right_DR = self.column
        down_DR += 1
        right_DR += 1
        if 0 <= down_DR < 8 and 0 <= right_DR < 8:
            piece = board[down_DR][right_DR]
            if piece == 0:
                moves.append((right_DR, down_DR))
            else:
                if piece.color != self.color:
                    moves.append((right_DR, down_DR))

        # Right
        right = self.column
        right += 1
        if 0 <= right < 8:
            piece = board[self.row][right]
            if piece == 0:
                moves.append((right, self.row))
            else:
                if piece.color != self.color:
                    moves.append((right, self.row))

        # Left
        left = self.column
        left -= 1
        if 0 <= left < 8:
            piece = board[self.row][left]
            if piece == 0:
                moves.append((left, self.row))
            else:
                if piece.color != self.color:
                    moves.append((left, self.row))

        # Up
        up = self.row
        up -= 1
        if 0 <= up < 8:
            piece = board[up][self.column]
            if piece == 0:
                moves.append((self.column, up))
            else:
                if piece.color != self.color:
                    moves.append((self.column, up))

        # Down
        down = self.row
        down += 1
        if 0 <= down < 8:
            piece = board[down][self.column]
            if piece == 0:
                moves.append((self.column, down))
            else:
                if piece.color != self.color:
                    moves.append((self.column, down))

        return moves


class Pawn(Piece):
    def __init__(self, row, column, color, name):
        super().__init__(row, column, color, name)
        self.queen = False

    def valid_moves(self, board):
        moves = []
        if self.selected:
            ops = {"+": operator.add, "-": operator.sub}
            # For black pawns
            if self.color == "b" and self.row < 7:
                # Capturing the opponent
                eliminate_piece = board[self.row+1][self.column-1]
                if eliminate_piece != 0 and eliminate_piece.color == "w":
                    moves.append((self.column-1, self.row+1))
                eliminate_piece = board[self.row + 1][self.column + 1]
                if eliminate_piece != 0 and eliminate_piece.color == "w":
                    moves.append((self.column + 1, self.row + 1))
                sign = ops["+"]
                start_pos = 1
            # For white pawns
            else:
                # Capturing the opponent
                eliminate_piece = board[self.row-1][self.column-1]
                if eliminate_piece != 0 and eliminate_piece.color == "b":
                    moves.append((self.column-1, self.row-1))
                eliminate_piece = board[self.row - 1][self.column + 1]
                if eliminate_piece != 0 and eliminate_piece.color == "b":
                    moves.append((self.column + 1, self.row - 1))
                start_pos = 6
                sign = ops["-"]

            # First opening and normal moves
            first_p = board[sign(self.row, 1)][self.column]
            if first_p == 0:
                moves.append((self.column, sign(self.row, 1)))
            # If pawn has not been moved player can move two square
            # Player can not move two squares if there is a piece
            if self.row == start_pos and first_p == 0:
                p = board[sign(self.row, 2)][self.column]
                if p == 0:
                    moves.append((self.column, sign(self.row, 2)))
        return moves


def load_piece_image():
    """Load images and return them as a dict."""
    image_dict = {}
    for filename in os.listdir(os.path.join("Pieces")):
        if filename.endswith('.png'):
            path = os.path.join(os.path.join("Pieces"), filename)
            key = filename[:-4]
            image_dict[key] = pygame.image.load(path).convert_alpha()
            image_dict[key] = pygame.transform.scale(image_dict[key], (SQUARE_SIZE, SQUARE_SIZE))
    return image_dict

