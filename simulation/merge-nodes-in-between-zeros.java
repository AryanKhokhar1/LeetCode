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
    public ListNode mergeNodes(ListNode head) {
        ListNode ans = new ListNode(0);
        ListNode answer = ans;
        int val = 0;
        head = head.next;
        while(head != null){
            if(head.val == 0){
                ListNode node = new ListNode(val);
                ans.next = node;
                ans = ans.next;
                val = 0;
            }else{
                val += head.val;
            }
            head = head.next;
        }
        return answer.next;
    }
}