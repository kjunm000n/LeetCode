# [17] Letter Combinations of a Phone Number

import random
from typing import Optional, Union, Any, List, Dict, Set
import itertools

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem17(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, digits: str) -> List[str]:
        u""" time complexity: O(n^k) """
        answer = []
        letter_dic = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z'],
                      }
        for digit in digits:
            if not answer:
                answer = letter_dic[digit]
            else:
                temp, answer = answer, []
                for s in temp:
                    for s2 in letter_dic[digit]:
                        answer.append(s + s2)
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, digits: str) -> List[str]:
        u""" time complexity: O(n^k) """
        answer = []
        letter_dic = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z'],
                      }
        if not digits:
            return answer
        vectors = [letter_dic[digit] for digit in digits]
        answer = [''.join(comb) for comb in itertools.product(*vectors)]
        return answer

    def test_one_random(self):
        digits_str = "23456789"
        digits = ''.join([random.choice(digits_str) for _ in range(random.randint(0,4))])

        answer1 = self.solution(digits)
        answer2 = self.comparison_solution(digits)

        assert set(answer1) == set(answer2)
