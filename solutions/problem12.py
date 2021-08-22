# [12] Integer to Roman

import random
from typing import Optional, Union, Any, List, Dict

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem12(ProblemInterface):
    @staticmethod
    def generate_Roman(digit: int, char1: str, char5: str, char10: str) -> str:
        if digit == 9:
            return char1 + char10
        elif digit == 4:
            return char1 + char5
        elif digit < 4:
            return char1 * digit
        elif digit > 4:
            return char5 + char1 * (digit - 5)

    @ProblemInterface.time_check(debug_mode)
    def solution(self, num: int) -> str:
        u""" time complexity: O(1) """
        answer = ''
        digit4 = num // 1000
        answer += self.generate_Roman(digit4, 'M', '!', '!')

        digit3 = (num % 1000) // 100
        answer += self.generate_Roman(digit3, 'C', 'D', 'M')

        digit2 = (num % 100) // 10
        answer += self.generate_Roman(digit2, 'X', 'L', 'C')

        digit1 = num % 10
        answer += self.generate_Roman(digit1, 'I', 'V', 'X')

        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, num: int) -> str:
        u""" time complexity: O(1) """
        return self.solution(num)

    def test_one_random(self, num_size=3999):
        n = random.randint(1,3999)

        answer1 = self.solution(n)
        answer2 = self.comparison_solution(n)

        if debug_mode:
           print(answer1, answer2)
        assert answer1 == answer2
