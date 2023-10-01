import queue

def is_solved(board):
    for i in range(len(board) - 1):
        if board[i] != i + 1:
            return False
    return True

def move(board, i, j):
    new_board = board.copy()
    temp = new_board[i]
    new_board[i] = new_board[j]
    new_board[j] = temp
    return new_board

def create_node(board, moves):
    return (board, moves)

def get_possible_moves(board):
    empty_index = board.index(0)
    possible_moves = []

    if empty_index % 4 > 0:
        possible_moves.append(move(board, empty_index, empty_index - 1))

    if empty_index % 4 < 3:
        possible_moves.append(move(board, empty_index, empty_index + 1))

    if empty_index // 4 > 0:
        possible_moves.append(move(board, empty_index, empty_index - 4))

    if empty_index // 4 < 3:
        possible_moves.append(move(board, empty_index, empty_index + 4))

    return possible_moves

def solve_puzzle(start_board):
    visited = set()
    q = queue.Queue()

    q.put(create_node(start_board, ""))
    visited.add(tuple(start_board))

    while not q.empty():
        current_node = q.get()
        current_board, moves = current_node

    if is_solved(current_board):
        return moves

    possible_moves = get_possible_moves(current_board)

    for move in possible_moves:
        if tuple(move) not in visited:
            q.put(create_node(move, moves + str(move.index(0))))
    visited.add(tuple(move))

    return None

start_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

import random
random.shuffle(start_board)

print("Start:")
for i in range(0, 16, 4):
    print(start_board[i:i+4])
    print()

solution = solve_puzzle(start_board)

if solution:
    print("solve seek!")
    print("way:", solution)
else:
    print("don't solve.")