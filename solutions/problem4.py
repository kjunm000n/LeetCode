# [4] Median of Two Sorted Arrays

import os
import random

from solutions.interface import ProblemInterface
from main import debug_mode


class Problem4(ProblemInterface):
    def avg(self, nums):
        return sum(nums)/len(nums)

    def median(self, nums, with_arr=False):
        u"""
        Get median of single array. If with_arr is True, return list with median values.
        """
        answer = [num for i, num in enumerate(nums) if i == len(nums)//2 or (len(nums)%2==0 and i == len(nums)//2-1)]
        return answer if with_arr else self.avg(answer)

    @ProblemInterface.time_check(debug_mode)
    def solution(self, nums1, nums2):
        u"""
        time complexity: O(log (m+n))
        """
        if os.getenv('debug_mode'):
            print(f"func({nums1},{nums2})")

        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)
        if len(nums1) == 1 and len(nums2) == 1:
            return self.avg(nums1+nums2)
        if len(nums1) == 1 or len(nums2) == 1:
            return self.median(nums1+nums2)

        mid1, mid2 = nums1[len(nums1)//2], nums2[len(nums2)//2]
        skip = max(min(len(nums1) // 2-1, len(nums2) // 2-1), 1)
        if os.getenv('debug_mode'):
            print(f"  mid1:{mid1}, mid2:{mid2}, skip: {skip}")
        if mid1 > mid2:
            next_nums1, next_nums2 = nums1[:-skip], nums2[skip:]
        elif mid1 == mid2:
            return mid1
        elif mid1 < mid2:
            next_nums1, next_nums2 = nums1[skip:], nums2[:-skip]

        if os.getenv('debug_mode'):
            print(f"    l1:{len(nums1)}, l2:{len(nums2)} / "
                  f"mid1:{len(next_nums1)}, mid2:{len(next_nums2)}")

        return self.solution(next_nums1, next_nums2)

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, nums1, nums2):
        u"""
        time complexity: O((m+n) log (m+n))
        """
        nums = sorted(nums1+nums2)
        return self.median(nums)

    def test_one_random(self, list_size = 10, num_size = 100):
        nums1 = sorted([random.randint(1, num_size) for _ in range(random.randint(1, list_size))])
        nums2 = sorted([random.randint(1, num_size) for _ in range(random.randint(1, list_size))])

        answer1 = self.solution(nums1, nums2)
        answer2 = self.comparison_solution(nums1, nums2)

        print(answer1, answer2)
        assert answer1 == answer2
