from board import Board
from ai import Ai


class Ui:
    def __init__(self):
        self._board = Board()
        self._ai = Ai(self._board)
        self._counter = 0

    def start(self):
        while True:
            try:
                self._board.print_table()
                row = int(input("Give row: "))
                col = int(input("Give col: "))
                if self._board.validate_move(row, col) is True:
                    self._board.add_element(1, row, col)
                else:
                    raise Exception("Invalid input!")
                if self._board.check_if_won_rows() is True or self._board.check_if_won_cols() is True or self._board.check_if_won_diags() is True:
                    self._board.print_table()
                    print("Game ended! You won!")
                    return
                if self._counter == 0:
                    self._ai.set_wdt_lnt(row, col)
                    self._ai.do_best_move()
                    self._counter += 1
                else:
                    if self._ai.get_maximum_sequence() == 4:
                        self._ai.do_best_move()
                    elif self._ai.get_maximum_sequence() == 1:
                        self._ai.do_scenario_1()
                    elif self._ai.get_maximum_sequence() == 2:
                        self._ai.do_scenario_2()
                if self._board.check_if_won_rows() is True or self._board.check_if_won_cols() is True or self._board.check_if_won_diags() is True:
                    self._board.print_table()
                    print("Game ended! Computer won!")
                    return
            except Exception as ve:
                print(ve)


ui = Ui()
ui.start()
