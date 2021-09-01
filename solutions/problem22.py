# [22] Generate Parentheses

import random
from typing import Optional, Union, Any, List, Dict, Set
from functools import cache

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem22(ProblemInterface):
    difficulty = Difficulty.Medium

    @cache
    def generateParenthesis(self, n: int) -> Set[str]:
        if n == 1:
            return {"()"}
        else:
            curr_set = set()
            for i in range(1, (n + 1) // 2 + 1):
                front = self.generateParenthesis(i)
                back = self.generateParenthesis(n - i)
                for f in front:
                    for b in back:
                        curr_set.add(f"{f}{b}")
                        curr_set.add(f"{b}{f}")
                        if i == 1:
                            curr_set.add(f"({b})")
            return curr_set

    @ProblemInterface.time_check(debug_mode)
    def solution(self, n: int) -> List[str]:
        u""" time complexity: O(4^n) """
        return list(self.generateParenthesis(n))

    @cache
    def generateParenthesis2(self, n: int) -> Set[str]:
        if n == 1:
            return {"()"}
        else:
            prev_set = self.generateParenthesis2(n-1)
            curr_set = set()
            for prev in prev_set:
                for i in range(len(prev)):
                    curr_set.add(prev[:i]+"()"+prev[i:])
            return curr_set

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, n: int) -> List[str]:
        u""" time complexity: O(2n*n!) """
        return list(self.generateParenthesis(n))

    def test_one_random(self, num_size=8):
        n = random.randint(1, num_size)
        answer1 = self.solution(n)
        answer2 = self.comparison_solution(n)

        assert sorted(answer1) == sorted(answer2)
