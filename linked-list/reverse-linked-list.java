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
    public ListNode reverseList(ListNode head) {
        
        ListNode temp = head;
        if(temp == null || temp.next == null){
            return head;
        }
        ListNode previous = head;
        ListNode current = head.next;
        ListNode n = head.next.next;
        previous.next = null;
        while(n != null){
            current.next = previous;
            previous = current;
            current = n;
            n = n.next;
        }
        current.next = previous;
        previous = current;
        return previous;
    }
}