import unittest
from ai import Ai
from board import Board


class TestAi(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board()
        self._ai = Ai(self._board)

    def tearDown(self) -> None:
        pass

    def test_get_current_wdt(self):
        self.assertEqual(self._ai.get_current_wdt(), -1)

    def test_get_current_lnt(self):
        self.assertEqual(self._ai.get_current_lnt(), -1)

    def test_set_lnt_wdt(self):
        self._ai.set_wdt_lnt(3, 4)
        self.assertEqual(self._ai.get_current_wdt(), 3)
        self.assertEqual(self._ai.get_current_lnt(), 4)

    def test_make_move(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 6)
        self._ai.make_move()
        self.assertEqual(self._ai.get_maximum_sequence(), 4)

    def test_do_best_move1(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.do_best_move()
        self.assertEqual(self._ai.get_current_wdt(), 4)
        self.assertEqual(self._ai.get_current_lnt(), 5)

    def test_do_best_move2(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.set_wdt_lnt(4, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 4)
        self._ai.do_best_move()
        self.assertEqual(self._ai.get_current_wdt(), 2)
        self.assertEqual(self._ai.get_current_lnt(), 5)

    def test_do_best_move3(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.set_wdt_lnt(4, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(2, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 4)
        self._ai.do_best_move()
        self.assertEqual(self._ai.get_current_wdt(), 2)
        self.assertEqual(self._ai.get_current_lnt(), 3)

    def test_do_best_move4(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.set_wdt_lnt(4, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(2, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(2, 3)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 4)
        self._ai.do_best_move()
        self.assertEqual(self._ai.get_current_wdt(), 4)
        self.assertEqual(self._ai.get_current_lnt(), 3)

    def test_do_best_move5(self):
        self._ai.set_wdt_lnt(3, 4)
        self._ai.make_move()
        self._ai.set_wdt_lnt(4, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(2, 5)
        self._ai.make_move()
        self._ai.set_wdt_lnt(2, 3)
        self._ai.make_move()
        self._ai.set_wdt_lnt(4, 3)
        self._ai.make_move()
        self._ai.set_wdt_lnt(3, 4)
        self._ai.do_best_move()
        self.assertEqual(self._ai.get_current_wdt(), 7)
        self.assertEqual(self._ai.get_current_lnt(), 7)

    def test_get_maximum_sequence(self):
        self.assertEqual(self._ai.get_maximum_sequence(), 4)

    def test_scenario_1(self):
        self._ai._board.add_element(1, 3, 4)
        self._ai._board.add_element(1, 3, 5)
        self._ai._board.add_element(1, 3, 6)
        self._ai.do_scenario_1()
        self._ai.set_wdt_lnt(3, 7)
        self.assertEqual(self._ai.get_current_wdt(), 3)
        self.assertEqual(self._ai.get_current_lnt(), 7)

    def test_scenario_2(self):
        self._ai._board.add_element(1, 4, 3)
        self._ai._board.add_element(1, 5, 3)
        self._ai._board.add_element(1, 6, 3)
        self._ai.do_scenario_2()
        self._ai.set_wdt_lnt(7, 3)
        self.assertEqual(self._ai.get_current_wdt(), 7)
        self.assertEqual(self._ai.get_current_lnt(), 3)


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board()

    def tearDown(self) -> None:
        pass

    def test_add_element(self):
        self._board.add_element(1, 3, 3)
        self.assertEqual(self._board.validate_move(3, 3), False)

    def test_validate_move(self):
        self.assertEqual(self._board.validate_move(-1, 1), False)
        self.assertEqual(self._board.validate_move(1, -1), False)

    def test_get_len_diagonal1(self):
        self._board.add_element(1, 1, 1)
        self._board.add_element(1, 2, 2)
        diags = self._board.get_len_diag()
        self.assertEqual(diags[0], 2)

    def test_get_len_diagonal2(self):
        self._board.add_element(1, 1, 2)
        self._board.add_element(1, 2, 1)
        diags = self._board.get_len_diag()
        self.assertEqual(diags[0], 0)

    def test_won_rows(self):
        self._board.add_element(1, 1, 1)
        self._board.add_element(1, 1, 2)
        self._board.add_element(1, 1, 3)
        self._board.add_element(1, 1, 4)
        self._board.add_element(1, 1, 5)
        self.assertEqual(self._board.check_if_won_rows(), True)

    def test_won_cols(self):
        self._board.add_element(1, 1, 1)
        self._board.add_element(1, 2, 1)
        self._board.add_element(1, 3, 1)
        self._board.add_element(1, 4, 1)
        self._board.add_element(1, 5, 1)
        self.assertEqual(self._board.check_if_won_cols(), True)

    def test_won_diags1(self):
        self._board.add_element(1, 1, 1)
        self._board.add_element(1, 2, 2)
        self._board.add_element(1, 3, 3)
        self._board.add_element(1, 4, 4)
        self._board.add_element(1, 5, 5)
        self.assertEqual(self._board.check_if_won_diags(), True)

    def test_won_diags2(self):
        self._board.add_element(1, 1, 4)
        self._board.add_element(1, 2, 3)
        self._board.add_element(1, 3, 2)
        self._board.add_element(1, 4, 1)
        self._board.add_element(1, 5, 0)
        self.assertEqual(self._board.check_if_won_diags(), True)
