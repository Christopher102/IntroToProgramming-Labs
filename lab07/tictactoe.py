# This program plays tictactoe between two players!


def printRow(row):
    print("|", end="")
    for square in row:
        if square == 0:
            print("   ", end='|')
        if square == 1:
            print(" X ",  end='|')
        if square == 2:
            print(" O ", end='|')
        else:
            pass


def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)
        print("\n+-----------+")
    pass


def markBoard(board, row, col, player):
    try:
        if board[row][col] == 0:
            board[row][col] = player
            return board
        elif board[row][col] == 1 or 2:
            print("That space is already used!\n")
            return board
        pass
    except IndexError:
        print("Only values between 1 and 3 please.")
        pass


def getPlayerMove():
    while True:
        try:
            row = int(input("\nPlease input a row: "))
            col = int(input("\nPlease input a column: "))
            break
        except ValueError:
            print("Please only input numbers.")
    return (row, col)


def hasBlanks(board):
    for row in board:
        for square in row:
            if square == 0:
                return True


def main():
    board = ([0, 0, 0],
             [0, 0, 0],
             [0, 0, 0])
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        row -= 1
        col -= 1
        markBoard(board, row, col, player)
        player = player % 2 + 1


main()
