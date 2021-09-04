# [48] Rotate Image

import copy
import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem48(ProblemInterface):
    difficulty = Difficulty.Medium
    name = 'rotate-image'

    @ProblemInterface.time_check(debug_mode)
    def solution(self, matrix: List[List[int]]) -> None:
        u""" time complexity: O(n^2) """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(i, n - i - 1):
                matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i], matrix[i][j] \
                    = matrix[i][j], matrix[j][-i-1], matrix[-i-1][-j-1], matrix[-j-1][i]

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, matrix: List[List[int]]) -> None:
        u""" time complexity: O(n^2) """
        temp_matrix = copy.deepcopy(matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp_matrix[n-j-1][i]
        del temp_matrix

    def test_one_random(self, size=20, num_size=1000):
        n = random.randint(1, 20)
        answer1 = [[random.randint(-num_size, num_size) for _ in range(n)] for _ in range(n)]
        answer2 = copy.deepcopy(answer1)
        self.solution(answer1)
        self.comparison_solution(answer2)

        assert answer1 == answer2
