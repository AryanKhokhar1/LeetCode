# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        ans = temp
        while head != None:
            if head.val not in nums:
                node = ListNode(head.val)
                temp.next = node
                temp = temp.next
            head = head.next
        return ans.next