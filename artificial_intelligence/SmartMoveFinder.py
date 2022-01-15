import random

piece_score = {"K": 0, "Q": 10, "R": 5, "B": 3, "N": 3, "P": 1}
CHECKMATE_SCORE = 1000
STALEMATE_SCORE = 0
DEPTH = 4

'''
    Returns the random move from available moves in the log
'''


def find_random_move(valid_moves):
    return valid_moves[random.randint(0, len(valid_moves)-1)]


'''
    Finds the best possible move by the given values of the chess pieces
'''


def find_best_move(game_context, valid_moves):
    turn_multiplier = 1 if game_context.white_to_move else -1
    opponent_min_max_score = -CHECKMATE_SCORE
    best_move = None
    for player_move in valid_moves:
        game_context.make_move(player_move)
        opponent_moves = game_context.get_valid_moves()

        if game_context.checkmate:
            opponent_max_score = -CHECKMATE_SCORE
        elif game_context.stalemate:
            opponent_max_score = STALEMATE_SCORE
        else:
            opponent_max_score = -CHECKMATE_SCORE
            for opponent_move in opponent_moves:
                game_context.make_move(opponent_move)
                if game_context.checkmate:
                    score = -turn_multiplier * CHECKMATE_SCORE
                elif game_context.stalemate:
                    score = STALEMATE_SCORE
                else:
                    score = -turn_multiplier * score_material(game_context.board)
                if score > opponent_max_score:
                    opponent_max_score = score
                game_context.undo_move()
        if opponent_max_score < opponent_min_max_score:
            opponent_min_max_score = opponent_max_score
            best_move = player_move

        game_context.undo_move()
    return best_move


'''
    Calculates the score for the each move given
'''


def score_material(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                score += piece_score[square[1]]
            elif square[0] == "b":
                score -= piece_score[square[1]]

    return score


'''
    Min max (non-recurse) to find the best available move
'''


def find_best_move_min_max(game_context, valid_moves):
    global next_move
    next_move = None
    find_move_min_max(game_context, valid_moves, DEPTH)
    return next_move


'''
    Min max (recurse) to find the best available move
'''


def find_move_min_max(game_context, valid_moves, depth, white_moving):
    global next_move
    if depth == 0:
        return score_material(game_context.board)

    if white_moving:
        max_score = -CHECKMATE_SCORE
        for move in valid_moves:
            game_context.make_move()
            next_moves = game_context.get_valid_moves()
            score = find_move_min_max(game_context, next_moves, depth-1, False)
            if score > max_score:
                max_score = score
                if depth == DEPTH:
                    next_move = move
            game_context.undo_move()
        return max_score
    else:
        min_score = CHECKMATE_SCORE
        for move in valid_moves:
            next_moves = game_context.get_valid_moves()
            score = find_move_min_max(game_context, next_moves, depth - 1, True)
            if score > min_score:
                min_score = score
                if depth == DEPTH:
                    next_move = move
            game_context.undo_move()
        return min_score


'''
    Adjust the score if the checkmate is possible to do. Returns MAX score for checkmate possibility
'''


def score_board(game_context):
    if game_context.checkmate:
        if game_context.white_to_move:
            return -CHECKMATE_SCORE
        else:
            return CHECKMATE_SCORE
    elif game_context.stalemate:
        return STALEMATE_SCORE

    score = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                score += piece_score[square[1]]
            elif square[0] == "b":
                score -= piece_score[square[1]]

    return score
