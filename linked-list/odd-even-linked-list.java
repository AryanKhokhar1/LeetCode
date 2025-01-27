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
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode dummy1 = head;
        ListNode ans = dummy1;
        ListNode dummy2 = head.next;
        ListNode d2 = dummy2;
        while(dummy1.next != null && dummy2.next != null){
            dummy1.next = dummy2.next;
            dummy1 = dummy1.next;
            dummy2.next = dummy1.next;
            dummy2 = dummy2.next;
        }
        dummy1.next = d2;
        return ans;
    }
}