

def check_levels(board, m, x, y):
    if m < 0:
        return False
    for j in range(m+1):
        # print("Checking Level {}".format(j))
        for k in range(len(board)):
            if board[j][k] == 1 and can_attack(x,y,j,k):
                # print(board[j])
                return True
    return False


def can_attack(x,y,a,b):
    if x == a:
        # print("{} {} can be attacked by {} {}".format(x, y, a, b))
        return True
    elif y == b:
        # print("{} {} can be attacked by {} {}".format(x, y, a, b))
        return True
    elif abs(x-a) == abs(y-b):
        # print("{} {} can be attacked by {} {}".format(x, y, a, b))
        return True
    # print("{} {} CANNOT be attacked by {} {}".format(x, y, a, b))
    return False

def move_queen(board, i):
    if i >= len(board):
        print("\nSucceeded in placing queens!")
        print("Board => {}\n".format(board))
        return
    for j in range(len(board)):
        if not check_levels(board,i - 1, i,j):
            board[i] = [0] * len(board)
            board[i][j] = 1
            # print("Board => {}".format(board))
            move_queen(board, i + 1)
        else:
            continue

def place_queens(n=4):
    board = []
    for i in range(n):
        t = [0]*n
        board.append(t)

    move_queen(board, 0)
    # print(board)


def test():
    place_queens()