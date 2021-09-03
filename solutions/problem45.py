# [45] Jump Game II

import random
from typing import Optional, Union, Any, List, Dict, Set

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem45(ProblemInterface):
    difficulty = Difficulty.Medium

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int]) -> int:
        u""" time complexity: O(n) """
        min_jump, curr_pos = 0, 0
        while True:
            if curr_pos == len(nums)-1:
                break
            if nums[curr_pos] + curr_pos >= len(nums)-1:
                min_jump += 1
                break
            next_pos = curr_pos
            for i in range(1, min(nums[curr_pos] + 1, len(nums) - curr_pos)):
                if nums[next_pos] + next_pos < nums[curr_pos + i] + curr_pos + i:
                    next_pos = curr_pos + i
            curr_pos = next_pos
            min_jump += 1
        return min_jump



    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int]) -> int:
        u""" time complexity: O(n^2) """
        min_jump = [len(nums) for _ in nums]
        min_jump[0] = 0
        pos_queue = [0]
        visited = {0}
        while pos_queue:
            curr = pos_queue.pop(0)
            for i in range(max(curr-nums[curr], 0), min(curr+nums[curr]+1, len(nums))):
                if i not in visited:
                    visited.add(i)
                    min_jump[i] = min_jump[curr] + 1
                    pos_queue.append(i)
                if i == len(nums)-1:
                    return min_jump[i]

    def test_one_random(self, num_length_size=10**4, num_size=10**3):
        num_length = random.randint(1, num_length_size)
        nums = [random.randint(0, num_size) for _ in range(num_length)]
        answer1 = self.solution(nums)
        answer2 = self.comparison_solution(nums)

        assert answer1 == answer2
