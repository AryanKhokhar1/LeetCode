# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        temp = head
        while temp != None:
            lis.append(temp.val)
            temp = temp.next
        
        for i in range(1,len(lis)):
            for j in range(i-1,-1,-1):
                if lis[i] < lis[j]:
                    extra = lis[i]
                    lis[i] = lis[j]
                    lis[j] = extra
                    i -= 1
                else:
                    break
        
        # new linkedlist
        newhead = ListNode()
        newtemp = newhead
        for ele in lis:
            node = ListNode(ele)
            newhead.next = node
            newhead = newhead.next
        
        return newtemp.next