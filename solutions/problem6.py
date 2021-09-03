# [6] ZigZag Conversion

import string
import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem6(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s: str, numRows: int) -> str:
        u""" time complexity: O(n) """
        answer = ''
        if numRows == 1:
            return s
        for i in range(numRows):
            if i in [0, numRows-1]:
                line = s[i::2*(numRows-1)]
            else:
                line1, line2 = s[i::2*(numRows-1)], s[2*(numRows-1)-i::2*(numRows-1)]
                line = [None] * (len(line1)+len(line2))
                line[0::2], line[1::2] = line1, line2
                line = ''.join(line)
            answer += line
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, s: str, numRows: int) -> str:
        u""" time complexity: O(n) """
        if numRows == 1:
            return s
        line_dict = {i: [] for i in range(numRows)}
        for i, c in enumerate(s):
            line = min(i%((numRows-1)*2), ((numRows-1)*2)-i%((numRows-1)*2))
            line_dict[line].append(c)
        answer = ''
        for i in range(numRows):
            answer += ''.join(line_dict[i])
        return answer

    def test_one_random(self, str_len=1000):
        n = random.randint(1,str_len)
        numRows = random.randint(1, n)
        s = ''.join([random.choice(string.ascii_lowercase) for _ in range(str_len)])

        answer1 = self.solution(s, numRows)
        answer2 = self.comparison_solution(s, numRows)

        if debug_mode:
            print(answer1, answer2)
        assert answer1 == answer2
