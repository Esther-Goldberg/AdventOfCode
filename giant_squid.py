def is_win(board):
    for line in board:
        all_x = True
        for element in line:
            if element != 'X':
                all_x = False
                break
        if all_x:
            return True

    for column in range(5):
        all_x = True
        for line in board:
            if line[column] != 'X':
                all_x = False
                break
        if all_x:
            return True

    return False


def get_score(board, number):
    sum = 0
    for line in board:
        for element in line:
            if element != 'X':
                sum += element
    return sum * number


def print_board(board):
    for line in board:
        print(line)
    print()


def main():
    with open('inputs/giant_squid_input.txt') as infile:
        bingo_numbers = list(map(int, infile.readline().split(',')))

        bingo_boards = []

        line = infile.readline()

        while line:
            new_board = []
            for i in range(5):
                new_board.append(list(map(int, infile.readline().split())))
            bingo_boards.append(new_board)
            line = infile.readline()

        for number in bingo_numbers:
            for board in bingo_boards:
                for line in board:
                    if number in line:
                        line[line.index(number)] = 'X'
                        break

                if is_win(board):
                    print(get_score(board, number))
                    return


if __name__ == "__main__":
    main()
