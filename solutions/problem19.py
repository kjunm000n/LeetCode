# [19] Remove Nth Node From End of List

import random
from typing import Optional, Union, Any, List, Dict, Set

from main import debug_mode
from solutions.interface import ProblemInterface, Difficulty


class Problem19(ProblemInterface):
    difficulty = Difficulty.Medium

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            if not 0 <= val <= 100:
                raise ValueError

        def copy(self):
            head = self.__class__(val=self.val)
            curr_this, curr_other = self.next, head
            while curr_this:
                curr_other.next = self.__class__(curr_this.val)
                curr_this, curr_other = curr_this.next, curr_other.next
            return head

        def __eq__(self, other):
            if other is None:
                return False
            if self.val != other.val:
                return False
            if self.next is None and other.next is None:
                return True
            if self.next is None or other.next is None:
                return False
            return self.next.__eq__(other.next)


    @ProblemInterface.time_check(debug_mode)
    def solution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        curr_node = head
        len_list = 0
        while curr_node:
            len_list += 1
            curr_node = curr_node.next
        if len_list == n:
            return head.next
        curr_node = head
        for _ in range(len_list - n - 1):
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        return head

    @ProblemInterface.time_check(debug_mode)
    def comparison_solution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        u""" time complexity: O(n) """
        node_list = []
        curr_node = head
        while curr_node:
            node_list.append(curr_node)
            curr_node = curr_node.next
        del_node = node_list[len(node_list) - n]
        if n != len(node_list):
            prev_node = node_list[len(node_list) - n - 1]
            prev_node.next = del_node.next
            del del_node
            return head
        else:
            next_node = head.next
            del head
            return next_node

    def test_one_random(self, sz_size=30, val_size=100):
        sz = random.randint(1, sz_size)
        n = random.randint(1, sz)
        head = self.ListNode(random.randint(1, val_size))
        curr = head
        for i in range(sz):
            next_node = self.ListNode(random.randint(1, val_size))
            curr.next, curr = next_node, next_node
        answer1 = self.solution(head.copy(), n)
        answer2 = self.comparison_solution(head.copy(), n)

        assert answer1 == answer2
