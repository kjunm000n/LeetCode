# [N] **Sample Text**

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class ProblemN(ProblemInterface):
    difficulty = Difficulty.Easy

    @ProblemInterface.time_check(debug_mode)
    def solution(self):
        u""" time complexity: O() """
        return None

    # @ProblemInterface.time_check(debug_mode)
    # def comparison_solution(self):
    #     u""" time complexity: O() """
    #     return None

    # def test_one_random(self):
    #     answer1 = self.solution()
    #     answer2 = self.comparison_solution()
    #
    #     assert answer1 == answer2
