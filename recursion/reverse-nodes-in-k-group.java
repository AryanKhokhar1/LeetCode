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
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head == null || head.next == null){
            return head;
        }
        int a = k;
        Stack<Integer> stack = new Stack<>();
        ListNode dummy = new ListNode(0);
        ListNode ans = dummy;
        while(head != null){
            if(a == 0){
                while(!stack.empty()){
                    ListNode node = new ListNode(stack.pop());
                    dummy.next = node;
                    dummy = dummy.next;
                }
                dummy.next = head;
                a = k;

            }else{
                stack.push(head.val);
                head = head.next;
                a--;
            }
        }
        if(a == 0 ){
            while(!stack.empty()){
                ListNode node = new ListNode(stack.pop());
                dummy.next = node;
                dummy = dummy.next;
            }
            dummy.next = head;
        }
        return ans.next;
    }
}