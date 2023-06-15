
FPS = 5


WHITE = 'white'
BLACK = 'black'


OPPOSITE_SIDE = {WHITE: BLACK, BLACK: WHITE}


CELL_SIZE = 50


WHITE_CELL_COLOR = (230, 230, 230)
BLACK_CELL_COLOR = (150, 150, 150)


MSG_COLOR = (255, 10, 10)


SELECTED_CELL_COLOR = (120, 120, 255)


KING_ON_SHAH_COLOR = (255, 0, 0)


AVL_MOVE_CELL_COLOR = (255, 120, 120)


PAWN_MOVES = 'pawn_moves'
PAWN_TAKES = 'pawn_takes'


NORMAL_MOVE = 'normal_move'  # Обычный ход
TAKE_MOVE = 'take_move'      # Ход-взятие
CASTLING = 'castling'        # Рокировка
CONVERSION = 'conversion'    # Превращение пешки в другую фигуру
PASSED_TAKE = 'passed_take'  # Взятие на проходе

# Приоритеты ходов
priority_list = [TAKE_MOVE, CONVERSION, PASSED_TAKE, CASTLING, NORMAL_MOVE]



def key_func_for_moves(move):
    return priority_list.index(move.m_type, 0, 5)



MAT = 'mat'  # Игра завершилась матом
PAT = 'pat'  # Игра завершилась патом
