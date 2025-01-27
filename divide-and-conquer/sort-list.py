# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def mergeSort(self,arr):
        if(len(arr) == 1):
            return arr
        
        mid = (len(arr)//2)
        left = self.mergeSort(arr[0:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left,right)
    def merge(self,left, right):
        mergedArr = list()
        i = 0
        j = 0
        while(i<len(left) and j<len(right)):
            if(left[i] < right[j]):
                mergedArr.append(left[i])
                i+=1
            else:
                mergedArr.append(right[j])
                j+=1
        
        while(i<len(left)):
            mergedArr.append(left[i])
            i+=1

        while(j<len(right)):
            mergedArr.append(right[j])
            j+=1

        return mergedArr
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(head == None or head.next == None):
            return head
        temp = head
        lis = list()
        while temp:
            lis.append(temp.val)
            temp = temp.next

        sorted_list = self.mergeSort(lis)

        answer = ListNode(0)
        temp = answer
        for element in sorted_list:
            temp.next = ListNode(element)
            temp = temp.next

        return answer.next