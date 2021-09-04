# [49] Group Anagrams

import random
import string
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem49(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, strs: List[str]) -> List[List[str]]:
        u""" time complexity: O(mn) """
        answer_dict = {}
        for s in strs:
            h = hash(tuple(sorted(s)))
            answer_dict.setdefault(h, [])
            answer_dict[h].append(s)
        return list(answer_dict.values())

    def to_hash(self, s: str) -> int:
        u""" time complexity: O(m) """
        alphabets = [0 for i in range(26)]
        for c in s:
            alphabets[ord(c) - 97] += 1
        return hash(tuple(alphabets))

    def to_tuple(self, s):
        s_dict = {}
        for c in s:
            s_dict.setdefault(c, 0)
            s_dict[c] += 1
        return tuple(sorted([(k, v) for k, v in s_dict.items()]))

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, strs: List[str]) -> List[List[str]]:
        u""" time complexity: O(mn) """
        answer_dict = {}
        for s in strs:
            tup = self.to_tuple(s)
            answer_dict.setdefault(tup, [])
            answer_dict[tup].append(s)
        return list(answer_dict.values())

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution2(self, strs: List[str]) -> List[List[str]]:
        u""" time complexity: O(mn) """
        answer_dict = {}
        for s in strs:
            tup = self.to_tuple(s)
            answer_dict.setdefault(tup, [])
            answer_dict[tup].append(s)
        return list(answer_dict.values())

    def test_one_random(self, str_length=100, num_length_size=10**4):
        strs = [''.join([random.choice(string.ascii_lowercase) for _ in range(1, str_length)]) for _ in range(random.randint(1,num_length_size))]
        answer1 = self.solution(strs)
        answer2 = self.comparison_solution(strs)

        assert answer1 == answer2
