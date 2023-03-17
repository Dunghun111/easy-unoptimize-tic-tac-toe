import getPosition
import checkConditional
import curses
import time


def Player_1_Move(P1_in):
    position = getPosition.Position(P1_in)
    get_position = position.GetPosition()
    p1_vertical = get_position[1]
    p1_horizontal = get_position[0]

    if boardMatrix[p1_horizontal][p1_vertical] == ' ':
        boardMatrix[p1_horizontal][p1_vertical] = 'x'
        return True

    else:
        return False


def Player_2_Move(P2_in):
    position = getPosition.Position(P2_in)
    get_position = position.GetPosition()
    p2_vertical = get_position[1]
    p2_horizontal = get_position[0]

    if boardMatrix[p2_horizontal][p2_vertical] == ' ':
        boardMatrix[p2_horizontal][p2_vertical] = 'o'
        return True

    else:
        return False


boardMatrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def main(console):
    turn = 0
    game_end = False

    while not game_end:
        valid = False
        while not valid:
            console.erase()
            console.addstr(0, 0, f'''
 - - -
|{boardMatrix[0][0]}|{boardMatrix[0][1]}|{boardMatrix[0][2]}|
|- - -|
|{boardMatrix[1][0]}|{boardMatrix[1][1]}|{boardMatrix[1][2]}|
|- - -|
|{boardMatrix[2][0]}|{boardMatrix[2][1]}|{boardMatrix[2][2]}|
 - - -
        ''')
            console.refresh()
            console.addstr(9, 0, 'Which cells do you want to choose?(x): ')
            get_p1_in = console.getch()
            console.addstr(9, 39, chr(get_p1_in))
            console.refresh()
            p1_input = chr(get_p1_in)
            valid = Player_1_Move(int(p1_input))
            time.sleep(0.2)

            if not valid:
                console.addstr(9, 0, 'That cells has another mark!            ')
                console.refresh()
                time.sleep(0.5)

        checker = checkConditional.Checking(boardMatrix)
        checker_return = checker.boardCheck()

        if checker_return == 'x' or checker_return == 'o':
            console.erase()
            console.addstr(0, 0, f'''
 - - -
|{boardMatrix[0][0]}|{boardMatrix[0][1]}|{boardMatrix[0][2]}|
|- - -|
|{boardMatrix[1][0]}|{boardMatrix[1][1]}|{boardMatrix[1][2]}|
|- - -|
|{boardMatrix[2][0]}|{boardMatrix[2][1]}|{boardMatrix[2][2]}|
 - - -
            ''')
            console.addstr(9, 0, f'{checker_return} win!')
            console.refresh()
            time.sleep(5)
            break

        turn += 1

        if turn == 9:
            console.erase()
            console.addstr(0, 0, f'''
 - - -
|{boardMatrix[0][0]}|{boardMatrix[0][1]}|{boardMatrix[0][2]}|
|- - -|
|{boardMatrix[1][0]}|{boardMatrix[1][1]}|{boardMatrix[1][2]}|
|- - -|
|{boardMatrix[2][0]}|{boardMatrix[2][1]}|{boardMatrix[2][2]}|
 - - -
                    ''')
            console.addstr(9, 0, "Draw!")
            console.refresh()
            time.sleep(5)
            break

        valid = False

        while not valid:
            console.erase()
            console.addstr(0, 0, f'''
 - - -
|{boardMatrix[0][0]}|{boardMatrix[0][1]}|{boardMatrix[0][2]}|
|- - -|
|{boardMatrix[1][0]}|{boardMatrix[1][1]}|{boardMatrix[1][2]}|
|- - -|
|{boardMatrix[2][0]}|{boardMatrix[2][1]}|{boardMatrix[2][2]}|
 - - -
            ''')
            console.refresh()
            console.addstr(9, 0, 'Which cells do you want to choose?(o): ')
            get_p2_in = console.getch()
            console.addstr(9, 39, chr(get_p2_in))
            console.refresh()
            p2_input = chr(get_p2_in)
            valid = Player_2_Move(int(p2_input))
            time.sleep(0.2)

            if not valid:
                console.addstr(9, 0, 'That cells has another mark!            ')
                console.refresh()
                time.sleep(0.5)

        checker = checkConditional.Checking(boardMatrix)
        checker_return = checker.boardCheck()

        if checker_return == 'x' or checker_return == 'o':
            console.erase()
            console.addstr(0, 0, f'''
 - - -
|{boardMatrix[0][0]}|{boardMatrix[0][1]}|{boardMatrix[0][2]}|
|- - -|
|{boardMatrix[1][0]}|{boardMatrix[1][1]}|{boardMatrix[1][2]}|
|- - -|
|{boardMatrix[2][0]}|{boardMatrix[2][1]}|{boardMatrix[2][2]}|
 - - -
            ''')
            console.addstr(0, 0, f'{checker_return} win!')
            console.refresh()
            time.sleep(5)
            break

        turn += 1
        console.erase()
    curses.endwin()


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt as e:
        print("Bye!")
    except ValueError as ee:
        print("Err: Value Error! Quitting!")
