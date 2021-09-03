# [36] Valid Sudoku

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem36(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, board: List[List[str]]) -> bool:
        u""" time complexity: O() """
        sets = [set() for _ in range(27)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in sets[i]:
                        return False
                    else:
                        sets[i].add(board[i][j])
                    if board[i][j] in sets[9+j]:
                        return False
                    else:
                        sets[9+j].add(board[i][j])
                    if board[i][j] in sets[18+i//3*3+j//3]:
                        return False
                    else:
                        sets[18+i//3*3+j//3].add(board[i][j])
        return True

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, board: List[List[str]]) -> bool:
        u""" time complexity: O(n^2) """
        for horizon in board:
            for num in range(1, 10):
                if horizon.count(str(num)) > 1:
                    return False
        for j in range(9):
            vertical = [horizon[j] for horizon in board]
            for num in range(1, 10):
                if vertical.count(str(num)) > 1:
                    return False
        for i in range(3):
            for j in range(3):
                rectangle = [board[3 * i + k][3 * j + l] for k in range(3) for l in range(3)]
                for num in range(1, 10):
                    if rectangle.count(str(num)) > 1:
                        return False
        return True

    def test_one_random(self):
        s = '123456789' + '.' * 80
        board = [[random.choice(s) for _ in range(9)] for _ in range(9)]
        answer1 = self.solution(board)
        answer2 = self.comparison_solution(board)

        assert answer1 == answer2
