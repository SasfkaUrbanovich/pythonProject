def draw_board(board):
    for i in range(3):
        print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])


def play(xo):
    correct = False
    while not correct:
        answer = input(f'Куда поставим {xo} ')
        try:
            answer = int(answer)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число? ')
            continue
        if int(answer) in range(10):
            if board[answer - 1] != 'X' and board[answer - 1] != 'O':
                board[answer - 1] = xo
                draw_board(board)
                correct = True
            else:
                print('Место занято')
        else:
            print('Введите число от 1 до 9')


def cheak_win(board):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    print('Проверка')
    for elem in win:
        if board[elem[0]] == board[elem[1]] == board[elem[2]]:
            print('Победил', board[elem[0]])
            return True
    return False


def main():
    draw_board(board)
    count = 0
    win = False
    while not win:
        if count % 2 == 0:
            play(xo='X')
            count += 1
        else:
            play(xo='O')
            count += 1
        if count > 4:
            if cheak_win(board):
                win = True
                break
    return print('ПОБЕДА')


if __name__ == '__main__':
    board = list(range(1, 10))
    main()
