# [18] 4Sum

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict
from itertools import combinations, product
from functools import reduce

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem18(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int], target: int) -> List[List[int]]:
        u""" time complexity: O(n^3) """
        answer_set = set()
        nums = sorted(nums)
        for i in range(1, len(nums) - 2):
            for j in range(i+1, len(nums)-1):
                k, l = 0, len(nums) - 1
                while True:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        answer_set.add((nums[k], nums[i], nums[j], nums[l]))
                        l -= 1
                        k += 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    if not k < i < j < l:
                        break
        return [list(answer) for answer in answer_set]

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int], target: int) -> List[List[int]]:
        u""" time complexity: O(n^4) """
        answer_set = set()
        for i, j, k, l in combinations(nums, 4):
            if i + j + k + l == target:
                answer = tuple(sorted([i, j, k, l]))
                if answer not in answer_set:
                    answer_set.add(answer)
        return [list(answer) for answer in answer_set]

    def test_one_random(self, num_length=50, num_size=10**9, target_size=10**9):
        target = random.randint(-target_size, target_size)
        nums = [random.randint(-num_size, num_size) for _ in range(random.randint(3, num_length))]
        answer1 = self.solution(nums, target)
        answer2 = self.comparison_solution(nums, target)

        assert sorted(answer1) == sorted(answer2)
