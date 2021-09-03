# [13] Roman to Integer

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem13(ProblemInterface):
    difficulty = Difficulty.Easy

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s: str) -> int:
        u""" time complexity: O(1) """
        answer = 0
        roman_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                      'D': 500, 'CM': 900, 'M': 1000}
        parse_order = ['M', 'CM', 'CD', 'D', 'C', 'XC', 'XL', 'L', 'X', 'IX', 'IV', 'V', 'I']
        for symbol in parse_order:
            while s.startswith(symbol):
                answer += roman_dict[symbol]
                s = s[len(symbol):]
        return answer

    @staticmethod
    def generate_Roman(digit: int, char1: str, char5: str, char10: str) -> str:
        u""" time complexity: O(1) """
        if digit == 9:
            return char1 + char10
        elif digit == 4:
            return char1 + char5
        elif digit < 4:
            return char1 * digit
        elif digit > 4:
            return char5 + char1 * (digit - 5)

    def int_to_Roman(self, num: int) -> str:
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
    def comparison_solution(self, s: str) -> int:
        u""" time complexity: O(1) """
        return self.solution(s)

    def test_one_random(self, num_size=3999):
        n = random.randint(1, 3999)
        s = self.int_to_Roman(n)

        answer1 = self.solution(s)

        if debug_mode:
            print(answer1, answer1)
        assert answer1 == n
