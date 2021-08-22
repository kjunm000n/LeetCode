# [1] Two Sum

import random
from typing import Optional, Union, Any, List

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem1(ProblemInterface):
    def get_num_dict(self, nums):
        u"""save indexes for each value / time complexity: O(n) """
        num_dict = dict()
        for i, num in enumerate(nums):
            if num in num_dict:
                num_dict[num].append(i)
            else:
                num_dict[num] = [i]
        return num_dict

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums, target):
        u""" time complexity: O(nlog(n)) """
        answer = []
        num_dict = self.get_num_dict(nums)
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
        u""" time complexity: O(n^2) """
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
