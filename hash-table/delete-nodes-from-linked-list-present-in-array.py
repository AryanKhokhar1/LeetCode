# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        d = dict()
        for ele in nums:
            if d.get(ele) == None:
                d[ele] = True
        prev = ListNode(0)
        main = prev
        
        while head!= None:
            if d.get(head.val):
                prev.next = head.next
            else:
                prev.next = head
                prev = head
            head = head.next
        return main.next