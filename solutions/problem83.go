package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	for curr := head; curr != nil && curr.Next != nil; curr = curr.Next {
		firstNode := curr
		for curr.Next != nil && curr.Val == curr.Next.Val {
			curr = curr.Next
		}
		firstNode.Next = curr.Next
	}
	return head
}
