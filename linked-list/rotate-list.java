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
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode temp = head;
        int size = 0;
        while(temp != null){
            size++;
            temp = temp.next;
        }
        int rotation = k%size;
        if(head.next.next == null){
            if(rotation == 1){
                ListNode ans = head.next;
                head.next.next = head;
                head.next = null;
                return ans;
            }
        }
        while(rotation != 0){
            temp = head;
            while(temp.next.next != null){
                temp = temp.next;
            }
            ListNode node = new ListNode(temp.next.val);
            temp.next = null;
            node.next = head;
            head = node;
            rotation--;
        }
        return head;
    }
}