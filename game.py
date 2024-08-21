from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if (row < 0 or row >= game.field_size):
                    raise FieldIndexError

                col = int(input('Введите номер столбца: '))
                if (col < 0 or col >= game.field_size):
                    raise FieldIndexError

                if game.board[row][col] != ' ':
                    raise CellOccupiedError

            except FieldIndexError:
                print(f'Значение должно быть неотрицательным и меньше {game.field_size}.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue

            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue

            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')

            else:
                break

        game.make_move(row, col, current_player)
        game.make_move(row, col, current_player)
        print('Ход сделан!')
        game.display()

        if game.check_win(current_player):
            print(f'Победили {current_player}.')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            running = False

        if current_player == 'X':
            current_player = '0'
        else:
            current_player = 'X'



if __name__ == '__main__':
    main()

