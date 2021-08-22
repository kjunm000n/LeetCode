# [1] Two Sum

import os
import random

from solutions.interface import ProblemInterface
from main import debug_mode

class Problem1(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums, target):
        u"""
        sort first, and match target values within one iteration.
        expected time complexity = O(nlogn)
        """
        answer = []
        num_dict = dict()
        for i, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(i)
            else:
                num_dict[num] = [i]
        nums = sorted(nums)
        back_index = len(nums) - 1
        for front_index, num in enumerate(nums):
            if front_index >= back_index:
                break
            while num + nums[back_index] >= target and front_index < back_index:
                if num + nums[back_index] == target:
                    if num != nums[back_index]:
                        return [num_dict[num][0], num_dict[nums[back_index]][0]]
                    else:
                        return num_dict[num][:2]
                back_index -= 1
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums, target):
        u"""
        expected time complexity = O(n^2)
        """
        for i, num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if num1 + num2 == target:
                    return [i, j]
        return []

    def test_one_random(self, list_size=5, num_size=20):
        while True:
            nums = [random.randint(1, num_size) for _ in range(random.randint(1, list_size))]
            target = random.randint(1, num_size//2)
            answer2 = self.comparison_solution(nums, target)
            if not answer2:
                continue
            else:
                answer1 = self.solution(nums, target)
                break

        print(answer1, answer2)
        assert sum([nums[i] for i in answer1]) == target
        assert answer1[0] != answer1[1]
        assert sum([nums[i] for i in answer2]) == target
        assert answer2[0] != answer2[1]
