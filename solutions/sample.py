# [N] Sample

import os
import random

from solutions.interface import ProblemInterface
from main import debug_mode


class ProblemN(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self):
        return None

    # @ProblemInterface.time_check(debug_mode)
    # def comparison_solution(self):
    #     return None

    # def test_one_random(self):
    #     answer1 = self.solution()
    #     answer2 = self.comparison_solution()
    #
    #     if os.getenv('debug_mode'):
    #     print(answer1, answer2)
    #     assert answer1 == answer2
