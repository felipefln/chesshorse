class Board(object):
    @staticmethod
    def get_result(pos):
        def get_board_algebraic():
            board_head = list(map(chr, range(ord('a'), ord('h') + 1)))
            board_lines = list(reversed(range(1, 9)))
            board_algebraic = [[''] * 8 for i in range(8)]
            for x in range(8):
                for y in range(0, 8):
                    board_algebraic[x][y] = board_head[y] + str(board_lines[x])
            return board_algebraic

        def get_index(pos, board):
            for r in range(0, 8):
                if pos in board[r]:
                    return list([r, board[r].index(pos)])
            return None

        result = []

        movement_horse = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
        board = get_board_algebraic()
        posi = get_index(pos, board)
        for m in movement_horse:
            x = posi[0] + m[0]
            y = posi[1] + m[1]
            if (x >= 0 and y >= 0) and (x < 8 and y < 8):
                result.append(board[x][y])
        return result
