# [7] Reverse Integer

import random
import time
import timeit

from solutions.interface import ProblemInterface
from main import debug_mode


class Problem7(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def get_reverse(self, x: int, digit=0) -> int:
        if x < 0:
            answer = list(self.get_reverse(-x))
            answer[0] = -1 * answer[0]
            return tuple(answer)
        if x < 10:
            return x, digit+1
        else:
            head = x % 10
            tail, digit = self.get_reverse(x // 10)
            return head * 10**digit + tail, digit+1

    @ProblemInterface.time_check(debug_mode)
    def solution(self, x: int) -> int:
        answer =  self.get_reverse(x)[0]
        return answer if -(2 ** 31) <= answer < 2 ** 31 else 0

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, x: int) -> int:
        if x < 0:
            return -self.comparison_solution(-x)
        else:
            answer = int(str(x)[::-1])
            return answer if -(2 ** 31) <= answer < 2 ** 31 else 0

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution2(self, x: int) -> int:
        if x < 0:
            return -self.comparison_solution2(-x)
        else:
            answer = int(''.join(reversed(str(x))))
            return answer if -(2 ** 31) <= answer < 2 ** 31 else 0

    def test_one_random(self, num_max=2 ** 31):
        num = random.randint(-num_max, num_max)

        answer1 = self.solution(num)
        answer2 = self.comparison_solution(num)

        print(answer1, answer2)
        assert answer1 == answer2