# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next # temp pointer for slow.next
        slow.next = None # break the middle link
        prev = None
        while second:
            temp = second.next
            second.next = prev # reverse the link
            prev = second
            second = temp

        # merge two halves
        firstHalf, secondHalf = head, prev
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2
