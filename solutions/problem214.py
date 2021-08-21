# [214] Shortest Palindrome

import os
import random
import string

from solutions.interface import ProblemInterface
from main import debug_mode


class Problem214(ProblemInterface):
    def is_p(self, s):
        for i in range(len(s) // 2):
            print(len(s) - 1 - i, i)
            if s[-1 - i] != s[i]:
                return False
        return True

    def is_palindrom(self, s):
        return s[:len(s)//2] == s[:(len(s)-1)//2:-1]

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s: str) -> str:
        u"""
        time complexity : O(n^2)
        """
        for i in range(len(s), 0, -1):
            if self.is_palindrom(s[:i]):
                return s[len(s) - 1:i - 1:-1] + s[:i] + s[i:]
        return s


    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, s: str) -> str:
        u"""
        time complexity : O(n^2)
        """
        for i in range(len(s)-1,-1,-1):
            if self.is_palindrom(s[:i:-1]+s):
                return s[:i:-1]+s
        return s

    def test_one_random(self, max_str_size=1000):
        str_size = random.randint(1, max_str_size)
        s = ''.join([random.choice(string.ascii_uppercase) for _ in range(str_size)])

        answer1 = self.solution(s)
        answer2 = self.comparison_solution(s)

        if os.getenv('debug_mode'):
            print(f"input: {s}")
            print(len(answer1), answer1)
            print(len(answer2), answer2)

        assert self.is_palindrom(answer1)
        assert self.is_palindrom(answer2)
        assert len(answer1) == len(answer2)
