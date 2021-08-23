# [15] 3Sum

import random
from typing import Optional, Union, Any, List, Dict
from itertools import combinations, product

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem15(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int]) -> List[List[int]]:
        u""" time complexity: O(n^2) """
        answer, num_dict = [], {}
        for n in nums:
            num_dict.setdefault(n, 0)
            num_dict[n] += 1

        if 0 in num_dict:
            if num_dict[0] >= 3:  # three zero
                answer.append([0, 0, 0])
            num_dict.pop(0)
            for k, v in num_dict.items():
                if k > 0 and -k in num_dict:  # one positive, one negative and zero
                    answer.append([-k, 0, k])
        print(answer)

        for k, v in num_dict.items():
            if v >= 2 and -2 * k in num_dict:  # two same positive or negative and the other
                if k > 0:
                    answer.append([-2 * k, k, k])
                else:
                    answer.append([k, k, -2 * k])

        for k1, k2 in combinations([k for k in num_dict.keys() if k > 0], 2):
            if -(k1 + k2) in num_dict:  # two different positive and one negative
                if k1 > k2:
                    answer.append([-(k1 + k2), k2, k1])
                else:
                    answer.append([-(k1 + k2), k1, k2])

        for k1, k2 in combinations([k for k in num_dict.keys() if k < 0], 2):
            if -(k1 + k2) in num_dict:  # two different negative and one positive
                if k1 > k2:
                    answer.append([k2, k1, -(k1 + k2)])
                else:
                    answer.append([k1, k2, -(k1 + k2)])

        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int]) -> List[List[int]]:
        u""" time complexity: O(n^3) """
        answer, prev_set = [], set()
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        case = sorted([nums[i], nums[j], nums[k]])
                        if tuple(case) not in prev_set:
                            prev_set.add(tuple(case))
                            answer.append(case)
        return answer

    def test_one_random(self, num_length=3000, num_size=10000):
        nums = [random.randint(-num_size, num_size) for _ in range(random.randint(0, num_length))]
        answer1 = self.solution(nums)
        answer2 = self.comparison_solution(nums)

        assert sorted(answer1) == sorted(answer2)
