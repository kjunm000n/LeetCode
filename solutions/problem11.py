# [N] Sample
import itertools
import random
from typing import Optional, Union, Any, List

from main import debug_mode
from solutions.interface import ProblemInterface


class Problem11(ProblemInterface):
    @ProblemInterface.time_check(debug_mode)
    def solution(self, height: List[int]) -> int:
        u""" time complexity: O(n) """
        answer = 0
        front_iter, back_iter = 0, len(height) - 1
        while True:
            if front_iter >= back_iter:
                break
            h1, h2 = height[front_iter], height[back_iter]
            answer = max(answer, (back_iter-front_iter)*min(h1, h2))
            prev_front_iter, prev_back_iter = front_iter, back_iter
            if h1 >= h2:
                while back_iter > 0 and h2 >= height[back_iter]:
                    back_iter -= 1
            if h1 <= h2:
                while front_iter < len(height) - 1 and h1 >= height[front_iter]:
                    front_iter += 1
            if h1 == h2:
                if front_iter >= back_iter or back_iter < 0 or front_iter > len(height) - 1:
                    break
                if height[front_iter] > height[back_iter]:
                    back_iter = prev_back_iter
                elif height[front_iter] < height[back_iter]:
                    front_iter = prev_front_iter
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, height: List[int]) -> int:
        u""" time complexity: O(n) """
        answer, i, j = 0, 0, len(height)-1
        while True:
            if i >= j:
                return answer
            answer = max(answer, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return answer

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution2(self, height: List[int]) -> int:
        u""" time complexity: O(n^2) """
        answer = 0
        for i, h1 in enumerate(height[:-1]):
            for j, h2 in enumerate(height[i + 1:], i + 1):
                answer = max(answer, (j - i) * min(h1, h2))
        return answer

    @staticmethod
    def get_area(front_info, back_info):
        return (back_info[0] - front_info[0]) * min(front_info[1], back_info[1])

    @ProblemInterface.time_check(debug_mode)
    def failed_solution1(self, height: List[int]) -> int:
        u""" Idea: 앞에서한칸, 뒤에서한칸씩 땡기기 / time complexity: O(n) """
        answer = 0
        front_iter, back_iter = 0, len(height) - 1
        prev_front_iter, prev_back_iter = 0, len(height) - 1
        prev_h1, prev_h2 = 0, 0

        while True:
            if front_iter >= back_iter:
                break
            h1, h2 = height[front_iter], height[back_iter]
            answer = max([answer] + [self.get_area(f, b) for f, b in list(
                itertools.product([[prev_front_iter, prev_h1], [front_iter, h1]],
                                  [[prev_back_iter, prev_h2], [back_iter, h2]]))])
            prev_h1, prev_h2, prev_front_iter, prev_back_iter = h1, h2, front_iter, back_iter
            front_iter, back_iter = front_iter + 1, back_iter - 1
            while front_iter < len(height) - 1 and height[front_iter] <= prev_h1:
                front_iter += 1
            while back_iter > 0 and height[back_iter] <= prev_h2:
                back_iter -= 1
        return answer

    @ProblemInterface.time_check(debug_mode)
    def failed_solution2(self, height: List[int]) -> int:
        u""" time complexity: O(n^2) """
        answer = 0
        front_iter = 0
        while True:
            if front_iter >= len(height) - 1:
                break
            h1 = height[front_iter]
            back_iter = len(height) - 1
            while True:
                h2 = height[back_iter]
                answer = max(answer, self.get_area([front_iter, h1], [back_iter, h2]))
                back_iter = back_iter - 1
                while back_iter > 0 and height[back_iter] <= h2:
                    back_iter -= 1
                if back_iter <= 0 or h2 >= h1:
                    break
            while front_iter < len(height) - 1 and height[front_iter] <= h1:
                front_iter += 1
        return answer

    def test_one_random(self, num_len=10 ** 5, max_height=10 ** 4):
        n = random.randint(2, num_len)
        height = [random.randint(0, max_height) for _ in range(n)]
        answer1 = self.solution(height)
        answer2 = self.comparison_solution(height)

        if debug_mode:
            print(answer1, answer2)
        assert answer1 == answer2
