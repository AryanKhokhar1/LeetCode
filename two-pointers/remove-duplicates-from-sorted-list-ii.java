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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode temp = head;
        ListNode dummy = new ListNode(0);
        ListNode answer = dummy;
        int number = 200;
        while(temp != null && temp.next != null){
            if(temp.val == temp.next.val || temp.val == number){
                number = temp.val;
                temp = temp.next;
            }else{
                ListNode node = new ListNode(temp.val);
                dummy.next = node;
                dummy = dummy.next;
                temp = temp.next;
            }
        }
        if(temp != null && temp.val != number){
            ListNode node = new ListNode(temp.val);
            dummy.next = node;
        }
        ListNode ans = answer.next;
        return ans;
    }
}