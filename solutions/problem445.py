# [445] Add Two Numbers 2

import random
from typing import Optional, Union, Any, List, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem445(ProblemInterface):
    difficulty = Difficulty.Medium

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            if not 0 <= val <= 9:
                raise ValueError

        def __eq__(self, other: 'ListNode') -> bool:
            if self.val != other.val:
                return False
            else:
                if self.next is None and other.next is None:
                    return True
                elif self.next is None or other.next is None:
                    return False
                else:
                    return self.next.__eq__(other.next)

        def __repr__(self) -> str:
            return str(self.val) + self.next.__repr__() if self.next else ''

    def sum_ListNode(self, n1: ListNode, n2: ListNode, carry=0) -> (ListNode, int):
        u""" time complexity: O(1) """
        sum_val = (n1.val + n2.val + carry)
        return self.ListNode(val=sum_val%10), sum_val//10

    @ProblemInterface.time_check(debug_mode)
    def solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        u""" time complexity: O(n) """
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

    def int_to_ListNode(self, val: int) -> ListNode:
        u""" time complexity: O(n) """
        next_node = None
        while True:
            prev_node = self.ListNode(val=val%10)
            prev_node.next = next_node
            next_node = prev_node
            val //= 10
            if val <= 0:
                break
        return next_node

    def ListNode_to_int(self, curr_node: ListNode) -> int:
        u""" time complexity: O(n) """
        sum_val = curr_node.val
        next_node = curr_node.next
        while next_node:
            sum_val = sum_val * 10 + next_node.val
            next_node = next_node.next
        return sum_val

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        return self.int_to_ListNode((self.ListNode_to_int(l1) + self.ListNode_to_int(l2)))

    def test_one_random(self, max_list_length=10):
        l1 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))
        l2 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))

        answer1 = self.solution(l1, l2)
        answer2 = self.comparison_solution(l1, l2)

        assert answer1 == answer2
