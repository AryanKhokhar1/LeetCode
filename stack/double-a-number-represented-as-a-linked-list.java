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
    public ListNode doubleIt(ListNode head) {
        ListNode temp = head;
        int firstElement = (temp.val*2);
        temp.val = firstElement%10;
        if(firstElement/10 == 1){
            ListNode node = new ListNode(1,head);
            head = node;
        }
        while(temp.next != null){
            int mult = temp.next.val*2;
            temp.next.val = mult%10;
            if(mult/10 == 1){
                temp.val++;
            }
            temp = temp.next;
        }
        return head;
    }
}