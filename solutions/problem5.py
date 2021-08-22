# [5] Longest Palindromic Substring

import string
import random
from typing import Optional, Union, Any, List

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem5(ProblemInterface):
    @staticmethod
    def is_palindrom(self, s):
        u""" time complexity: O(n) """
        return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s: str) -> str:
        u""" time complexity: O() """
        return ''


    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, s: str) -> str:
        u""" time complexity: O(n^2) """
        answer = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                curr = s[i:j]
                if self.is_palindrom(curr) and len(curr) > len(answer):
                        answer = curr
        return answer

    def test_one_random(self, max_str_size=1000):
        str_size = random.randint(1, max_str_size+1)
        s = ''.join([random.choice(string.ascii_uppercase) for _ in range(str_size)])

        answer1 = self.solution(s)
        answer2 = self.comparison_solution(s)

        print(answer1, answer2)
        assert self.is_p(answer1)
        assert self.is_p(answer2)
        assert len(answer1) == len(answer2)
