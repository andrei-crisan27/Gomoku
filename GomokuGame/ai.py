import random

class Ai:
    def __init__(self, board):
        self._board = board
        self._current_wdt = -1
        self._current_lnt = -1
        self._move_cnt = 0

    def get_current_wdt(self):
        """
        :return: the value of the current ai row position
        """
        return self._current_wdt

    def get_current_lnt(self):
        """
        :return: the value of the current ai column position
        """
        return self._current_lnt

    def set_wdt_lnt(self, wdt, lnt):
        """
         sets the ai current position
        """
        self._current_wdt = wdt
        self._current_lnt = lnt
        self._move_cnt += 1

    def make_move(self):
        """
        makes an ai move
        """
        self._board.add_element(2, self._current_wdt, self._current_lnt)

    def do_best_move(self):
        """
        tries multiple move scenarios for the ai, proceeds to only do the most suitable one
        """
        if self._board.validate_move(self._current_wdt, self._current_lnt) is True:
            self.make_move()
        elif self._board.validate_move(self._current_wdt + 1, self._current_lnt + 1) is True:
            self._current_wdt += 1
            self._current_lnt += 1
            self.make_move()
        elif self._board.validate_move(self._current_wdt - 1, self._current_lnt + 1) is True:
            self._current_wdt -= 1
            self._current_lnt += 1
            self.make_move()
        elif self._board.validate_move(self._current_wdt - 1, self._current_lnt - 1) is True:
            self._current_wdt -= 1
            self._current_lnt -= 1
            self.make_move()
        elif self._board.validate_move(self._current_wdt + 1, self._current_lnt - 1) is True:
            self._current_wdt += 1
            self._current_lnt -= 1
            self.make_move()
        else:
            self._current_wdt = 7
            self._current_lnt = 7
            while self._board.validate_move(self._current_wdt, self._current_lnt) is False:
                self._current_lnt += 1
            self.make_move()

    def get_maximum_sequence(self):
        """
        :return: 1 if the maximum sequence is on a row, 2 if it is on a column or 4 if there is not a maximum sequence
        """
        on_rows = self._board.get_len_row()
        on_cols = self._board.get_len_col()
        max1 = on_rows[0]
        max2 = on_cols[0]
        if max1 >= max2 and max1 >= 3:
            return 1
        elif max2 >= max1 and max2 >= 3:
            return 2
        else:
            return 4

    def do_scenario_1(self):
        """
        tries to block the player on row
        """
        on_rows = self._board.get_len_row()
        store_wdt = self._current_wdt
        store_lnt = self._current_lnt
        if self._board.validate_move(on_rows[1], on_rows[2] + 1) is True:
            self._current_wdt = on_rows[1]
            self._current_lnt = on_rows[2] + 1
            self.do_best_move()
        elif self._board.validate_move(on_rows[1], self._current_lnt - on_rows[0] - 1) is True:
            self._current_lnt -= on_rows[0]
            self._current_lnt -= 1
            self._current_wdt = on_rows[1]
            self.do_best_move()
        else:
            self.do_best_move()
        self._current_wdt = store_wdt
        self._current_lnt = store_lnt

    def do_scenario_2(self):
        """
        tries to block the player on column
        """
        on_cols = self._board.get_len_col()
        store_wdt = self._current_wdt
        store_lnt = self._current_lnt
        if self._board.validate_move(on_cols[1] + 1, on_cols[2]) is True:
            self._current_wdt = on_cols[1] + 1
            self._current_lnt = on_cols[2]
            self.do_best_move()
        elif self._board.validate_move(self._current_wdt - on_cols[0] - 1, on_cols[2]) is True:
            self._current_wdt -= on_cols[0]
            self._current_wdt -= 1
            self._current_lnt = on_cols[2]
            self.do_best_move()
        else:
            self.do_best_move()
        self._current_wdt = store_wdt
        self._current_lnt = store_lnt

