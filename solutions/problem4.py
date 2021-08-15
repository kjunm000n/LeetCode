# [4] Median of Two Sorted Arrays

import random

from solutions.interface import *


class Problem4(ProblemInterface):
    def __init__(self, debug=False):
        self.debug = debug

    def avg(self, nums):
        return sum(nums)/len(nums)

    def divide_according_to_median(self, lst):
        assert lst
        if len(lst) % 2 == 1:
            return lst[:len(lst) // 2], lst[len(lst) // 2:len(lst) // 2 + 1], lst[len(lst) // 2 + 1:]
        else:
            return lst[:len(lst) // 2 - 1], lst[len(lst) // 2 - 1:len(lst) // 2 + 1], lst[len(lst) // 2 + 1:]

    def median(self, nums, with_arr=False):
        u"""
        Get median of single array. If with_arr is True, return list with median values.
        """
        answer = self.divide_according_to_median(nums)[1]
        return answer if with_arr else self.avg(answer)

    def solution(self, nums1, nums2, debug=False):
        u"""
        time complexity: O(log (m+n))
        """
        if self.debug:
            print(f"func({nums1},{nums2})")

        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)
        if len(nums1) == 1 and len(nums2) == 1:
            return self.avg(nums1+nums2)
        if len(nums1) == 1 and len(nums2) == 2:
            if nums1[0] > nums2[1]:
                return nums2[1]
            elif nums1[0] < nums2[0]:
                return nums2[0]
            else:
                return nums1[0]
        if len(nums1) == 2 and len(nums2) == 1:
            if nums2[0] > nums1[1]:
                return nums1[1]
            elif nums2[0] < nums1[0]:
                return nums1[0]
            else:
                return nums2[0]
        if len(nums1) == 2 and len(nums2) == 2:
            if nums1[1] <= nums2[0]:
                return self.avg([nums1[1], nums2[0]])
            elif nums1[0] >= nums2[1]:
                return self.avg([nums1[0], nums2[1]])
            elif nums1[0] <= nums2[0] <= nums2[1] <= nums1[1]:
                return self.avg(nums2)
            elif nums2[0] <= nums1[0] <= nums1[1] <= nums2[1]:
                return self.avg(nums1)
            elif nums2[0] <= nums1[0] <= nums2[1] <= nums1[1]:
                return self.avg([nums1[0], nums2[1]])
            elif nums1[0] <= nums2[0] <= nums1[1] <= nums2[1]:
                return self.avg([nums1[1], nums2[0]])
            else:
                raise

        front1, mid1, back1 = self.divide_according_to_median(nums1)
        front2, mid2, back2 = self.divide_according_to_median(nums2)

        assert len(mid1) in [1, 2] and len(mid2) in [1, 2]
        assert len(front1) == len(back1) and len(front2) == len(back2)

        if len(mid1) == 1 and len(mid2) == 1:
            if mid1[0] == mid2[0]:
                return mid1[0]
            elif mid1[0] > mid2[0]:
                if (len(nums1) + len(nums2) + len(front1) + len(back2)) % 2 == 1:
                    if len(front1) > len(back2):
                        front1 = front1[:-1]
                    else:
                        back2 = back2[1:]
                next_nums1, next_nums2 = front1, back2
            elif mid1[0] < mid2[0]:
                if (len(nums1) + len(nums2) + len(front2) + len(back1)) % 2 == 1:
                    if len(front2) > len(back1):
                        front2 = front2[:-1]
                    else:
                        back1 = back1[1:]
                next_nums1, next_nums2 = back1, front2
        elif len(mid1) == 1 and len(mid2) == 2:
            if mid2[0] <= mid1[0] <= mid2[1]:
                return mid1[0]
            elif mid1[0] > mid2[0]:
                if (len(nums1) + len(nums2) + len(front1) + len(back2)) % 2 == 1:
                    if len(front1) > len(back2):
                        front1 = front1[:-1]
                    else:
                        back2 = back2[1:]
                next_nums1, next_nums2 = front1, back2
            elif mid1[0] < mid2[0]:
                if (len(nums1) + len(nums2) + len(front2) + len(back1)) % 2 == 1:
                    if len(front2) > len(back1):
                        front2 = front2[:-1]
                    else:
                        back1 = back1[1:]
                next_nums1, next_nums2 = back1, front2
        elif len(mid1) == 2 and len(mid2) == 1:
            next_nums1, next_nums2 = nums2, nums1
        elif len(mid1) == 2 and len(mid2) == 2:
            if mid1[0] <= mid2[0] <= mid2[1] <= mid1[0]:
                return self.avg(mid2)
            elif mid2[0] <= mid1[0] <= mid1[1] <= mid2[0]:
                return self.avg(mid1)
            elif mid1[0] >= mid2[1]:
                if (len(nums1) + len(nums2) + len(front1) + len(back2)) % 2 == 1:
                    if len(front1) > len(back2):
                        front1 = front1[:-1]
                    else:
                        back2 = back2[1:]
                next_nums1, next_nums2 = front1, back2
            elif mid1[1] <= mid2[0]:
                if (len(nums1) + len(nums2) + len(front2) + len(back1)) % 2 == 1:
                    if len(front2) > len(back1):
                        front2 = front2[:-1]
                    else:
                        back1 = back1[1:]
                next_nums1, next_nums2 = back1, front2
            else:
                next_nums1, next_nums2 = nums1, nums2
                if next_nums1[0] < next_nums2[0]:
                    next_nums1 = next_nums1[:1]
                else:
                    next_nums2 = next_nums2[:1]
                if next_nums1[-1] > next_nums2[-1]:
                    next_nums1 = next_nums1[:-1]
                else:
                    next_nums2 = next_nums2[:-1]

        return self.solution(next_nums1, next_nums2, debug=debug)

    def comparison_solution(self, nums1, nums2):
        u"""
        time complexity: O((m+n) log (m+n))
        """
        nums = sorted(nums1+nums2)
        return self.median(nums)

    def test_one_random(self, list_size = 10, num_size = 100, debug = False):
        nums1 = sorted([random.randint(1, num_size) for _ in range(random.randint(1, list_size))])
        nums2 = sorted([random.randint(1, num_size) for _ in range(random.randint(1, list_size))])

        answer1 = self.solution(nums1, nums2, debug=self.debug)
        answer2 = self.comparison_solution(nums1, nums2)

        print(answer1, answer2)
        assert answer1 == answer2

    def test_runner(self, iters=10):
        for i in range(iters):
            self.test_one_random(list_size = 10, num_size = 100, debug = False)
