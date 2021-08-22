# [367] Valid Perfect Square

import random
from typing import Optional, Union, Any, List

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem367(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, num: int) -> bool:
        u""" time complexity: O(log(n)) """
        max_sqrt = 2 ** 16
        curr = max_sqrt // 2 - 1
        step_size = max_sqrt // 4
        while True:
            if num < curr * curr:
                curr -= step_size
            elif num > (curr + 1) * (curr + 1):
                curr += step_size
            elif curr * curr == num or (curr + 1) * (curr + 1) == num:
                return True
            if step_size == 0:
                return False
            step_size //= 2

    def comparison_solution(self, x: int) -> bool:
        u""" time complexity: O(1) """
        from math import sqrt
        return int(sqrt(x)) ** 2 == x

    def test_one_random(self, num_size=2 ** 31):
        num = random.randint(0, num_size)
        answer1 = self.solution(num)
        answer2 = self.comparison_solution(num)

        print(answer1, answer2)
        assert answer1 == answer2

