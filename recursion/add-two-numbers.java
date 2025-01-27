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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode dummy = head;
        int carry = 0;
        while(l1 != null || l2 != null){
            int num1 = (l1 != null) ? l1.val : 0;
            int num2 = (l2 != null) ? l2.val : 0;
            int value = (carry+num1+num2)%10;
            ListNode node = new ListNode(value);
            dummy.next = node;
            dummy = dummy.next;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
            carry = (carry+num1+num2)/10;
        }
        if(carry == 1){
            ListNode node = new ListNode(1);
            dummy.next  = node;
            dummy = dummy.next;
        }
        return head.next;
    }
}