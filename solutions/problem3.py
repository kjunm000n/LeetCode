# [3] Longest Substring Without Repeating Characters

import os
import random, string

from solutions.interface import ProblemInterface
from main import debug_mode

class Problem3(ProblemInterface):
    def insert(self, dic, k):
        if k not in dic or dic[k] == 0:
            dic[k] = 1
            return False
        elif dic[k] > 0:
            dic[k] += 1
            return True
        else:
            raise

    def remove(self, dic, k):
        if k not in dic or dic[k] < 1:
            raise
        dic[k] -= 1
        return dic[k]

    @ProblemInterface.time_check(debug_mode)
    def solution(self, s):
        s_dict = dict()
        answer, answer_s = 0, ''
        front, back = 0, 0
        while back < len(s):
            is_dup = self.insert(s_dict, s[back])
            back += 1
            if os.getenv('debug_mode'):
                print(front, back, s_dict, is_dup)
            if is_dup:
                while True:
                    remain = self.remove(s_dict, s[front])
                    front += 1
                    if os.getenv('debug_mode'):
                        print('  ', front, back, s_dict)
                    if s[back - 1] == s[front - 1] and remain <= 1 or front >= back:
                        break
            if back - front > answer:
                answer = back - front
                answer_s = s[front:back]
                if os.getenv('debug_mode'):
                    print(answer_s, answer)
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, s):
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
