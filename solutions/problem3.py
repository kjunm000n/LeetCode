# [3] Longest Substring Without Repeating Characters

import string
import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem3(ProblemInterface):
    difficulty = Difficulty.Medium

    def insert(self, dic: Dict[str, int], k: str) -> bool:
        u""" time complexity: O(1) """
        if k not in dic or dic[k] == 0:
            dic[k] = 1
            return False
        elif dic[k] > 0:
            dic[k] += 1
            return True
        else:
            raise ValueError

    def remove(self, dic: Dict[str, int], k: str) -> int:
        u""" time complexity: O(1) """
        if k not in dic or dic[k] < 1:
            raise ValueError
        dic[k] -= 1
        return dic[k]

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s: str) -> int:
        u""" time complexity: O(n) """
        char_dict = dict()
        answer = 0
        front, back = 0, 0
        while back < len(s):
            is_dup = self.insert(char_dict, s[back])
            back += 1
            if is_dup:
                while True:
                    remain = self.remove(char_dict, s[front])
                    front += 1
                    if s[back - 1] == s[front - 1] and remain <= 1 or front >= back:
                        break
            if back - front > answer:
                answer = back - front
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, s: str) -> int:
        u""" time complexity: O(n^2) """
        answer = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(set(list(s[i:j]))) < j - i:
                    continue
                elif len(answer) < j - i:
                    answer = s[i:j]
        return len(answer)


    def test_one_random(self):
        n = random.randint(0, 100)
        s = ''.join([random.choice(string.ascii_lowercase) for _ in range(n)])
        answer1 = self.solution(s)
        answer2 = self.comparison_solution(s)

        print(answer1, answer2)
        assert answer1 == answer2
