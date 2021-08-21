# [2] Add Two Numbers 2

import os
import random
from typing import Optional

from solutions.interface import ProblemInterface
from main import debug_mode


class Problem2(ProblemInterface):
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            if not 0 <= val <= 9:
                raise ValueError

        def to_int(self):
            sum_val = self.val
            next_node = self.next
            while next_node:
                sum_val = sum_val*10 + next_node.val
                next_node = next_node.next
            return sum_val

        def __eq__(self, other):
            if self.val != other.val:
                return False
            else:
                if self.next is None and other.next is None:
                    return True
                elif self.next is None or other.next is None:
                    return False
                else:
                    return self.next.__eq__(other.next)

    def sum_ListNode(self, n1: ListNode, n2: ListNode, carry=0) -> (ListNode, int):
        sum_val = (n1.val + n2.val + carry)
        return self.ListNode(val=sum_val%10), sum_val//10

    @ProblemInterface.time_check(debug_mode)
    def solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        curr_node1, curr_node2 = l1, l2
        while curr_node1 is not None or curr_node2 is not None:
            if curr_node1 is not None:
                s1.append(curr_node1)
                curr_node1 = curr_node1.next
            if curr_node2 is not None:
                s2.append(curr_node2)
                curr_node2 = curr_node2.next
        next_node, carry = None, 0
        while s1 and s2:
            prev_node, carry = self.sum_ListNode(s1.pop(), s2.pop(), carry=carry)
            prev_node.next = next_node
            next_node = prev_node
        while s1:
            prev_node, carry = self.sum_ListNode(s1.pop(), self.ListNode(val=0), carry=carry)
            prev_node.next = next_node
            next_node = prev_node
        while s2:
            prev_node, carry = self.sum_ListNode(s2.pop(), self.ListNode(val=0), carry=carry)
            prev_node.next = next_node
            next_node = prev_node
        if carry != 0:
            prev_node, carry = self.sum_ListNode(self.ListNode(val=0), self.ListNode(val=0), carry=carry)
            prev_node.next = next_node
            next_node = prev_node
        return next_node

    def int_to_ListNode(self, val):
        next_node = None
        while True:
            prev_node = self.ListNode(val=val%10)
            prev_node.next = next_node
            next_node = prev_node
            val //= 10
            if val <= 0:
                break
        return next_node

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.int_to_ListNode((l1.to_int() + l2.to_int()))

    def test_one_random(self, max_list_length=10):
        l1 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))
        l2 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))

        answer1 = self.solution(l1, l2)
        answer2 = self.comparison_solution(l1, l2)

        print(f"l1: {l1.to_int()}, l2: {l2.to_int()}, sum: {l1.to_int()+l2.to_int()}")
        print(f"solution: {answer1.to_int()} / comparison_solution: {answer2.to_int()}")
        assert answer1 == answer2
