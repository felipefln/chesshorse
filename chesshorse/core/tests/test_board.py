from chesshorse.core.board import Board
from django.test import TestCase


class TestBoard(TestCase):
    def test_parameters(self):
        with self.assertRaises(TypeError):
            Board.get_result()

    def test_board_should_return_correct_response(self):
        position = 'd5'
        assert Board.get_result(position) == ['b6', 'c7', 'e7', 'f6', 'f4', 'e3', 'c3', 'b4']
