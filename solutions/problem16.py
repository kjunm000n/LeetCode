# [16] 3Sum Closest

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict
from itertools import combinations, product
from functools import reduce

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem16(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int], target: int) -> List[List[int]]:
        u""" time complexity: O(n^2) """
        answer = 103001
        nums = sorted(nums)
        for i in range(1, len(nums)-1):
            j, k = 0, len(nums)-1
            while True:
                if abs((nums[i]+nums[j]+nums[k]) - target) < abs(answer - target):
                    answer = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < target:
                    j += 1
                else:
                    return answer
                if not j < i < k:
                    break
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int], target: int) -> List[List[int]]:
        u""" time complexity: O(n^3) """
        answer = 103001
        for i, j, k in combinations(nums, 3):
            if abs(i + j + k - target) < abs(answer - target):
                answer = i + j + k
                if answer == target:
                    return answer
        return answer

    def test_one_random(self, num_length=10, num_size=1000, target_size=100000):
        target = random.randint(-target_size, target_size)
        nums = [random.randint(-num_size, num_size) for _ in range(random.randint(3, num_length))]
        answer1 = self.solution(nums, target)
        answer2 = self.comparison_solution(nums, target)

        assert abs(target - answer1) == abs(target - answer2)
