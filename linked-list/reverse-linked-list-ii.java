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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        Stack<Integer> stack = new Stack<>();
        ListNode temp = head;
        ListNode first = head;
        for(int i = 1; i<=right; i++){
            if(left == i){
                first = temp;
            }

            temp = temp.next;
        }
        // ListNode last = temp;
        ListNode it = first;
        while(it != temp){
            stack.push(it.val);
            it = it.next;
        }
        while(!stack.empty() ){
            first.val = stack.pop();
            first = first.next;
        }
        return head;
    }
}