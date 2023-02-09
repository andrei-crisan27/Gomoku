class Board:
    def __init__(self):
        self._data = [[0] * 15 for i in range(15)]

    def add_element(self, inst, lnt, wdt):
        """
        makes a move on the board; 1 is for the player, 2 is for the computer
        """
        if inst == 1:
            self._data[lnt][wdt] = 1
        elif inst == 2:
            self._data[lnt][wdt] = 2

    def validate_move(self, lnt, wdt):
        """
        :return: true if a move can be done, and false otherwise
        """
        if wdt < 0 or wdt > 14:
            return False
        elif lnt < 0 or lnt > 14:
            return False
        elif self._data[lnt][wdt] != 0:
            return False
        return True

    def get_len_row(self):
        """
        :return: the maximum length of similar elements on a row, and coordinates from one of those elements
        """
        maxcnt = 0
        the_row = 0
        the_col = 0
        for i in range(0, 15):
            cnt = 0
            for j in range(0, 15):
                if self._data[i][j] == 0:
                    cnt -= cnt
                if self._data[i][j] == self._data[i][j - 1] and self._data[i][j] == 1:
                    cnt += 1
                elif self._data[i][j] != self._data[i][j - 1] and self._data[i][j] == 1:
                    cnt = 1
                else:
                    cnt = 0
                if cnt > maxcnt:
                    maxcnt -= maxcnt
                    maxcnt += cnt
                    the_row -= the_row
                    the_row += i
                    the_col -= the_col
                    the_col += j
        return maxcnt, the_row, the_col

    def get_len_col(self):
        """
        :return: the maximum length of similar elements on a column, and coordinates from one of those elements
        """
        maxcnt = 0
        the_row = 0
        the_col = 0
        for j in range(0, 15):
            cnt = 0
            for i in range(0, 15):
                if self._data[i][j] == 0:
                    cnt -= cnt
                if self._data[i][j] == self._data[i - 1][j] and self._data[i][j] == 1:
                    cnt += 1
                elif self._data[i][j] != self._data[i - 1][j] and self._data[i][j] == 1:
                    cnt = 1
                else:
                    cnt = 0
                if cnt > maxcnt:
                    maxcnt -= maxcnt
                    maxcnt += cnt
                    the_row -= the_row
                    the_row += i
                    the_col -= the_col
                    the_col += j
        return maxcnt, the_row, the_col

    def get_len_diag(self):
        """
        :return: the maximum length of similar elements on a diagonal, and coordinates from one of those elements
        """
        maxcnt = 0
        the_row = 0
        the_col = 0
        for i in range(0, 11):
            for j in range(0, 11):
                item = self._data[i][j]
                ok = 0
                if item != 0:
                    for k in range(1, 5):
                        if item == self._data[i+k][j+k]:
                            ok += 1
                if ok > maxcnt:
                    maxcnt -= maxcnt
                    the_row -= the_row
                    the_col -= the_col
                    maxcnt += ok + 1
                    the_row += i
                    the_col += j

        for i in range(0, 11):
            for j in range(4, 15):
                item = self._data[i][j]
                ok = 0
                if item != 0:
                    for k in range(1, 5):
                        if item == self._data[i+k][j-k]:
                            ok += 1
                if ok > maxcnt:
                    maxcnt -= maxcnt
                    the_row -= the_row
                    the_col -= the_col
                    maxcnt += ok + 1
                    the_row += i
                    the_col += j
        return maxcnt, the_row, the_col

    def check_if_won_rows(self):
        """
        :return: true if there is a winner on rows, false otherwise
        """
        for i in range(0, 15):
            cnt = 0
            for j in range(0, 15):
                if self._data[i][j] == 0:
                    cnt -= cnt
                if self._data[i][j] == self._data[i][j - 1]:
                    cnt += 1
                elif self._data[i][j] != self._data[i][j - 1] and self._data[i][j] != 0:
                    cnt = 1
                else:
                    cnt = 0
                if cnt == 5:
                    return True
        return False

    def check_if_won_cols(self):
        """
        :return: true if there is a winner on columns, false otherwise
        """
        for j in range(0, 15):
            cnt = 0
            for i in range(0, 15):
                if self._data[i][j] == 0:
                    cnt -= cnt
                if self._data[i][j] == self._data[i - 1][j]:
                    cnt += 1
                elif self._data[i][j] != self._data[i - 1][j] and self._data[i][j] != 0:
                    cnt = 1
                else:
                    cnt = 0
                if cnt == 5:
                    return True
        return False

    def check_if_won_diags(self):
        """
        :return: true if there is a winner on diagonals, false otherwise
        """
        for i in range(0, 11):
            for j in range(0, 11):
                item = self._data[i][j]
                ok = 0
                if item != 0:
                    for k in range(1, 5):
                        if item == self._data[i+k][j+k]:
                            ok += 1
                if ok == 4:
                    return True

        for i in range(0, 11):
            for j in range(4, 15):
                item = self._data[i][j]
                ok = 0
                if item != 0:
                    for k in range(1, 5):
                        if item == self._data[i+k][j-k]:
                            ok += 1
                if ok == 4:
                    return True

        return False

    def print_table(self):
        """
        prints the table in its current form
        """
        for i in range(15):
            display_row = []
            for j in range(15):
                val = self._data[i][j]
                display_row.append(val)
            print(display_row)