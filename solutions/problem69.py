# [69] Sqrt(x)

import os
import random

from solutions.interface import ProblemInterface
from main import debug_mode


class Problem69(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, x: int) -> int:
        max_sqrt = 2 ** 16
        curr = max_sqrt // 2 - 1
        step_size = max_sqrt // 4
        while True:
            if x < curr * curr:
                curr -= step_size
            elif x > (curr + 1) * (curr + 1):
                curr += step_size
            elif (curr+1)*(curr+1) == x:
                return curr+1
            else:
                return curr
            step_size //= 2

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, x: int) -> int:
        from math import sqrt
        return int(sqrt(x))

    def test_one_random(self, num_size=2**31):

        num = random.randint(0, num_size)
        answer1 = self.solution(num)
        answer2 = self.comparison_solution(num)

        print(answer1, answer2)
        assert answer1 == answer2
