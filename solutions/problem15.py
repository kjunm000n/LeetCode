# [15] 3Sum

import random
from typing import Optional, Union, Any, List, Dict

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem15(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int]) -> List[List[int]]:
        u""" time complexity: O() """
        return None

    # @ProblemInterface.time_check(debug_mode)
    # def comparison_solution(self, nums: List[int]) -> List[List[int]]:
    #     u""" time complexity: O() """
    #     return None

    # def test_one_random(self):
    #     answer1 = self.solution()
    #     answer2 = self.comparison_solution()
    #
    #     if debug_mode:
    #        print(answer1, answer2)
    #     assert answer1 == answer2
