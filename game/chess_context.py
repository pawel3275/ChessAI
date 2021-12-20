import numpy as np
from game.move import Move


class ChessGameContext:
    def __init__(self):
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ])
        self.moveFunctions = {"P": self.get_pawn_moves, "R": self.get_rook_moves, "N": self.get_knight_moves,
                              "B": self.get_bishop_moves, "Q": self.get_queen_moves, "K": self.get_king_moves}
        self.moveLog = []
        self.white_to_move = True
        self.white_king_location = (7, 4)
        self.black_king_location = (0, 4)
        self.checkmate = False
        self.stalemate = False

    def make_move(self, move):
        self.board[move.start_row][move.start_column] = "__"
        self.board[move.end_row][move.end_column] = move.piece_moved
        self.moveLog.append(move)
        self.white_to_move = not self.white_to_move
        if move.piece_moved == "wK":
            self.white_king_location = (move.end_row, move.end_column)
        elif move.piece_moved == "bK":
            self.black_king_location = (move.end_row, move.end_column)

    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.start_row][move.start_column] = move.piece_moved
            self.board[move.end_row][move.end_column] = move.piece_captured
            self.white_to_move = not self.white_to_move
            if move.piece_moved == "wK":
                self.white_king_location = (move.start_row, move.start_column)
            elif move.piece_moved == "bK":
                self.black_king_location = (move.start_row, move.start_column)

    def get_valid_moves(self):
        moves = self.get_possible_moves()

        for i in range(len(moves)-1, -1, -1):
            self.make_move(moves[i])
            self.white_to_move = not self.white_to_move
            if self.in_check():
                moves.remove(moves[i])
            self.white_to_move = not self.white_to_move
            self.undo_move()

        if len(moves) == 0:
            if self.in_check():
                print("CHECKMATE")
                self.checkmate = True
            else:
                print("STALEMATE")
                self.stalemate = True
        else:
            self.stalemate = False
            self.checkmate = False

        return moves

    def in_check(self):
        if self.white_to_move:
            return self.square_attacked(self.white_king_location[0], self.white_king_location[1])
        else:
            return self.square_attacked(self.black_king_location[0], self.black_king_location[1])

    def square_attacked(self, row, column):
        self.white_to_move = not self.white_to_move
        opponent_moves = self.get_possible_moves()
        self.white_to_move = not self.white_to_move
        for move in opponent_moves:
            if move.end_row == row and move.end_column == column:
                return True
        return False

    def get_possible_moves(self):
        moves = [Move((3, 6), (3, 4), self.board)]  # Testing

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                turn = self.board[i][j][0]
                if (turn == "w" and self.white_to_move) or (turn == "b" and not self.white_to_move):
                    piece = self.board[i][j][1]
                    self.moveFunctions[piece](i, j, moves)
        return moves

    def get_pawn_moves(self, row, column, moves_list):
        if self.white_to_move:
            if self.board[row - 1][column] == "__":
                moves_list.append(Move((row, column), (row - 1, column), self.board))
                if row == 6 and self.board[row - 2][column] == "__":
                    moves_list.append(Move((row, column), (row - 2, column), self.board))
            if column - 1 >= 0:
                if self.board[row - 1][column - 1][0] == "b":
                    moves_list.append(Move((row, column), (row - 1, column - 1), self.board))
            if column + 1 <= 7:
                if self.board[row - 1][column + 1][0] == "b":
                    moves_list.append(Move((row, column), (row - 1, column + 1), self.board))
        else:
            if self.board[row + 1][column] == "__":
                moves_list.append(Move((row, column), (row + 1, column), self.board))
                if row == 1 and self.board[row + 2][column] == "__":
                    moves_list.append(Move((row, column), (row + 2, column), self.board))
            if column - 1 >= 0:
                if self.board[row + 1][column - 1][0] == "w":
                    moves_list.append(Move((row, column), (row + 1, column - 1), self.board))
            if column + 1 <= 7:
                if self.board[row + 1][column + 1][0] == "w":
                    moves_list.append(Move((row, column), (row + 1, column + 1), self.board))

    def get_rook_moves(self, row, column, moves_list):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        enemy_color = "b" if self.white_to_move else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = column + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "__":
                        moves_list.append(Move((row, column), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves_list.append(Move((row, column), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def get_knight_moves(self, row, column, moves_list):
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        ally_color = "w" if self.white_to_move else "b"
        for direction in directions:
            end_row = row + direction[0]
            end_col = column + direction[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves_list.append(Move((row, column), (end_row, end_col), self.board))

    def get_bishop_moves(self, row, column, moves_list):
        directions = ((-1, -1), (-1, 1), (1, -1), (0, 1))
        enemy_color = "b" if self.white_to_move else "w"
        for direction in directions:
            for i in range(1, 8):
                end_row = row + direction[0] * i
                end_col = column + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "__":
                        moves_list.append(Move((row, column), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_color:
                        moves_list.append(Move((row, column), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break

    def get_queen_moves(self, row, column, moves_list):
        self.get_rook_moves(row, column, moves_list)
        self.get_bishop_moves(row, column, moves_list)

    def get_king_moves(self, row, column, moves_list):
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        ally_color = "w" if self.white_to_move else "b"
        for i in range(8):
            end_row = row + directions[i][0]
            end_col = column + directions[i][1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = self.board[end_row][end_col]
                if end_piece[0] != ally_color:
                    moves_list.append(Move((row, column), (end_row, end_col), self.board))
