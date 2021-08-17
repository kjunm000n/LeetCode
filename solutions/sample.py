# [N] Sample

import random

from solutions.interface import ProblemInterface


class ProblemN(ProblemInterface):
    def __init__(self, debug=False):
        self.debug = debug

    def solution(self):
        return None

    # def comparison_solution(self):
    #     return None

    # def test_one_random(self):
    #     answer1 = self.solution()
    #     answer2 = self.comparison_solution()
    #
    #     print(answer1, answer2)
    #     assert answer1 == answer2

    # def test_runner(self, iters=10):
    #     for i in range(iters):
    #         self.test_one_random(list_size = 10, num_size = 100)
