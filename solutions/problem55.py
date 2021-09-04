# [55] Jump Game

import random
from typing import Optional, Union, Any, List, Tuple, Set, Dict

from definitions import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem55(ProblemInterface):
    difficulty = Difficulty.Medium
    name = 'jump-game'

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums: List[int]) -> bool:
        u""" time complexity: O(n) """
        curr_pos = 0
        while True:
            if curr_pos == len(nums) - 1 or nums[curr_pos] + curr_pos >= len(nums) - 1:
                break
            next_pos = curr_pos
            for i in range(1, min(nums[curr_pos] + 1, len(nums) - curr_pos)):
                if nums[next_pos] + next_pos < nums[curr_pos + i] + curr_pos + i:
                    next_pos = curr_pos + i
            if next_pos == curr_pos:
                return False
            curr_pos = next_pos
        return True

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums: List[int]) -> bool:
        u""" time complexity: O(n^2) """
        min_jump = [len(nums) for _ in nums]
        min_jump[0] = 0
        visited = set()
        pos_queue = [0]
        for i in range(len(nums)):
            if not pos_queue:
                return False
            curr = pos_queue.pop(0)
            for j in range(max(0, curr - nums[curr]), min(len(nums), curr + nums[curr] + 1)):
                if j not in visited:
                    visited.add(j)
                    pos_queue.append(j)
                    min_jump[j] = min_jump[curr]
                    if j == len(nums) - 1:
                        return True
        return False

    def test_one_random(self, num_length_size=10**4, num_size=10**5):
        num_length = random.randint(1, num_length_size)
        nums = [random.randint(0, num_size) for _ in range(num_length)]
        answer1 = self.solution(nums)
        answer2 = self.comparison_solution(nums)

        assert answer1 == answer2
