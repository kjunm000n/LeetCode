# [14] Longest Common Prefix

import random
import string
from typing import Optional, Union, Any, List, Dict, Set

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem14(ProblemInterface):
    difficulty = Difficulty.Easy

    @ProblemInterface.time_check(debug_mode)
    def solution(self, strs: List[str]) -> str:
        u""" time complexity: O(mn) """
        answer = ''
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            answer += chars[0]
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, strs: List[str]) -> str:
        u""" time complexity: O(mn) """
        answer = ''
        pos = 0
        while strs:
            prev = None
            for i in range(len(strs)):
                if pos >= len(strs[i]):
                    return answer
                if i == 0:
                    prev = strs[i][pos]
                elif strs[i][pos] != prev:
                    return answer
            answer += strs[0][pos]
            pos += 1
        return answer

    def test_one_random(self, num_str=200, num_length=200):
        strs = [''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(1, num_length))])
                for _ in range(random.randint(1, num_str))]

        answer1 = self.solution(strs)
        answer2 = self.comparison_solution(strs)

        if debug_mode:
           print(answer1, answer2)
        assert answer1 == answer2
