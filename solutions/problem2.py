# [2] Add Two Numbers 2

import random
from typing import Optional, Union, Any, List, Dict

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem2(ProblemInterface):
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
                if not self.next and not other.next:
                    return True
                elif not self.next or not other.next:
                    return False
                else:
                    return self.next.__eq__(other.next)

        def __repr__(self):
            return (self.next.__repr__() + str(self.val)) if self.next else str(self.val)

    def sum_ListNode(self, n1: ListNode, n2: ListNode, carry: int, return_type: Any) -> (Union[ListNode, int], int):
        u""" time complexity: O(1) """
        sum_val = (n1.val + n2.val + carry)
        if return_type == self.ListNode:
            return self.ListNode(val=sum_val % 10), sum_val // 10
        elif return_type == int:
            return sum_val % 10, sum_val // 10
        else:
            raise ValueError

    @ProblemInterface.time_check(debug_mode)
    def solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        curr_node1, curr_node2, carry = l1, l2, 0
        head_node, next_carry = self.sum_ListNode(curr_node1, curr_node2, carry, self.ListNode)
        prev_node = head_node
        curr_node1, curr_node2, carry = curr_node1.next, curr_node2.next, next_carry
        while curr_node1 is not None and curr_node2 is not None:
            next_node, next_carry = self.sum_ListNode(curr_node1, curr_node2, carry, self.ListNode)
            prev_node.next, prev_node = next_node, next_node
            curr_node1, curr_node2, carry = curr_node1.next, curr_node2.next, next_carry

        curr_node = curr_node1 or curr_node2
        if curr_node:
            while curr_node is not None:
                next_node, next_carry = self.sum_ListNode(curr_node, self.ListNode(0), carry, self.ListNode)
                prev_node.next, prev_node = next_node, next_node
                curr_node, carry = curr_node.next, next_carry

        if carry:
            prev_node.next = self.ListNode(carry)

        return head_node

    def int_to_ListNode(self, val: int) -> ListNode:
        u""" time complexity: O(n) """
        head_node = self.ListNode(val=val % 10)
        prev_node = head_node
        while True:
            val //= 10
            if val <= 0:
                break
            next_node = self.ListNode(val=val % 10)
            prev_node.next = next_node
            prev_node = next_node
        prev_node.next = None
        return head_node

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        return self.int_to_ListNode((self.ListNode_to_int(l1) + self.ListNode_to_int(l2)))

    def ListNode_to_int(self, curr_node: ListNode) -> int:
        u""" time complexity: O(n) """
        sum_val = curr_node.val
        next_node = curr_node.next
        i = 1
        while next_node:
            sum_val += next_node.val * 10 ** i
            next_node = next_node.next
            i += 1
        return sum_val

    def int_list_to_ListNode(self, lst: List[int]) -> ListNode:
        u""" time complexity: O(n) """
        next_node = self.ListNode(lst.pop())
        while lst:
            prev_node = self.ListNode(lst.pop())
            prev_node.next, next_node = next_node, prev_node
        return next_node

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        curr_node1, curr_node2, sums, carry = l1, l2, [], 0
        while curr_node1 or curr_node2 or carry:
            curr_node1 = curr_node1 or self.ListNode(0)
            curr_node2 = curr_node2 or self.ListNode(0)
            sum_val, carry = self.sum_ListNode(curr_node1, curr_node2, carry, int)
            sums.append(sum_val)
            curr_node1, curr_node2 = curr_node1.next, curr_node2.next
        return self.int_list_to_ListNode(sums)

    def test_one_random(self, max_list_length=10):
        n1, n2 = [random.randint(1, 10 ** random.randint(1, max_list_length + 1) + 1) for _ in range(2)]
        l1, l2 = self.int_to_ListNode(n1), self.int_to_ListNode(n2)

        answer1 = self.solution(l1, l2)
        answer2 = self.comparison_solution2(l1, l2)

        assert answer1 == answer2
