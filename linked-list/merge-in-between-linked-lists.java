/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode temp = list1;
        ListNode firstNode = list1;
        ListNode lastNode = list1.next;
        for(int i = 0; b > -2; a--, b--){
            if(a == 1){
                firstNode = temp;
            }else if(b == -1){
                lastNode = temp;
            }
            temp = temp.next;
        }
        firstNode.next = list2;
        ListNode temp2 = list2;
        while(temp2.next != null){
            temp2 = temp2.next;
        }
        temp2.next = lastNode;

    return list1;
    }
}