# [9] Palindrome Number

import math
import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem9(ProblemInterface):
    difficulty = Difficulty.Easy

    @ProblemInterface.time_check(debug_mode)
    def solution(self, x: int) -> bool:
        u""" time complexity: O(n) """
        if x < 0:
            return False
        digit = int(math.log10(x))+1
        for i in range(digit//2):
            if (x // (10**i)) % 10 != (x // (10**(digit-1-i))) % 10:
                return False
        return True

    @staticmethod
    def is_palindrom(s: str) -> bool:
        u""" time complexity: O(n) """
        return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, x: int) -> bool:
        u""" time complexity: O(n) """
        return self.is_palindrom(str(x))

    def test_one_random(self):
        num = random.randint(-2**31, 2**31-1)
        answer1 = self.solution(num)
        answer2 = self.comparison_solution(num)

        if debug_mode:
            print(answer1, answer2)
        assert answer1 == answer2
