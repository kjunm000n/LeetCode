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
            i = 1
            while next_node:
                sum_val += next_node.val*10**i
                next_node = next_node.next
                i += 1
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

    def sum_ListNode_to_ListNode(self, n1: ListNode, n2: ListNode, carry=0) -> (ListNode, int):
        sum_val = (n1.val + n2.val + carry)
        return self.ListNode(val=sum_val%10), sum_val//10

    def sum_ListNode_to_int(self, n1: ListNode, n2: ListNode, carry=0) -> (int, int):
        sum_val = (n1.val + n2.val + carry)
        return sum_val%10, sum_val//10

    @ProblemInterface.time_check(debug_mode)
    def solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node1, curr_node2, carry = l1, l2, 0
        head_node, next_carry = self.sum_ListNode_to_ListNode(curr_node1, curr_node2, carry)
        prev_node = head_node
        curr_node1, curr_node2, carry = curr_node1.next, curr_node2.next, next_carry
        while curr_node1 is not None and curr_node2 is not None:
            next_node, next_carry = self.sum_ListNode_to_ListNode(curr_node1, curr_node2, carry)
            prev_node.next, prev_node = next_node, next_node
            curr_node1, curr_node2, carry = curr_node1.next, curr_node2.next, next_carry

        curr_node = curr_node1 or curr_node2
        if curr_node:
            while curr_node is not None:
                next_node, next_carry = self.sum_ListNode_to_ListNode(curr_node, self.ListNode(0), carry)
                prev_node.next, prev_node = next_node, next_node
                curr_node, carry = curr_node.next, next_carry

        if carry:
            prev_node.next = self.ListNode(carry)

        return head_node

    def int_to_ListNode(self, val):
        head_node = self.ListNode(val=val%10)
        prev_node = head_node
        while True:
            val //= 10
            if val <= 0:
                break
            next_node = self.ListNode(val=val%10)
            prev_node.next = next_node
            prev_node = next_node
        prev_node.next = None
        return head_node

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.int_to_ListNode((l1.to_int() + l2.to_int()))

    def list_to_ListNode(self, lst):
        next_node = self.ListNode(lst.pop())
        while lst:
            prev_node = self.ListNode(lst.pop())
            prev_node.next, next_node = next_node, prev_node
        return next_node

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node1, curr_node2, sums, carry = l1, l2, [], 0
        while curr_node1 or curr_node2 or carry:
            curr_node1 = curr_node1 or self.ListNode(0)
            curr_node2 = curr_node2 or self.ListNode(0)
            sum_val, carry = self.sum_ListNode_to_int(curr_node1, curr_node2, carry)
            sums.append(sum_val)
            curr_node1, curr_node2 = curr_node1.next, curr_node2.next
        return self.list_to_ListNode(sums)

    def test_one_random(self, max_list_length=10):
        l1 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))
        l2 = self.int_to_ListNode(random.randint(1, 10**random.randint(1, max_list_length + 1) + 1))

        answer1 = self.solution(l1, l2)
        answer2 = self.comparison_solution2(l1, l2)

        print(f"l1: {l1.to_int()}, l2: {l2.to_int()}, sum: {l1.to_int()+l2.to_int()}")
        print(f"solution: {answer1.to_int()} / comparison_solution: {answer2.to_int()}")
        assert answer1 == answer2
