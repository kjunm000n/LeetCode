# [33] Search in Rotated Sorted Array

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem33(ProblemInterface):
    difficulty = Difficulty.Medium

    def bisection(self, nums, target, base):
        u""" time complexity: O(log(n)) """
        if not nums:
            return -1
        index = (len(nums) - 1) // 2
        if nums[index] == target:
            return base + index
        if nums[0] == target:
            return base
        if nums[-1] == target:
            return base + len(nums) - 1
        if nums[0] < target < nums[index] or target < nums[index] < nums[0] or nums[index] < nums[0] < target:
            return self.bisection(nums[1:index], target, base + 1)
        if nums[index] < target < nums[-1] or target < nums[-1] < nums[index] or nums[-1] < nums[index] < target:
            return self.bisection(nums[index + 1:-1], target, base + index + 1)
        return -1

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int], target: int) -> int:
        u""" time complexity: O(log(n)) """
        return self.bisection(nums, target, 0)

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int], target: int) -> int:
        u""" time complexity: O(n) """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

    def test_one_random(self, num_size=10**4, num_len_size=5000):
        num_length = random.randint(1, num_len_size)
        nums = sorted(random.sample(range(1, num_size), num_length))
        rotate_index = random.randint(0, len(nums)-1)
        nums = nums[rotate_index:] + nums[:rotate_index]
        target = random.sample(nums, 1)[0]
        answer1 = self.solution(nums, target)
        answer2 = self.comparison_solution(nums, target)

        assert answer1 == answer2
