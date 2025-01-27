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
    public ListNode removeNodes(ListNode head) {
        ListNode temp = head;
        Stack<Integer> stack = new Stack<>();
        int value;
        while(temp != null){
            if(stack.empty()){
                stack.push(temp.val);
            }else{
                // value = stack.peek();
                if(!stack.empty() && temp.val>stack.peek()){
                    while(!stack.empty() && temp.val>stack.peek()){
                        stack.pop();
                    }
                    stack.push(temp.val);
                }else{
                    stack.push(temp.val);
                }
            }
            // System.out.println(stack);
            temp =temp.next;
        }
        ListNode dummy = new ListNode();
        // ListNode answer;
        boolean a = true;
        while(!stack.empty()){
            ListNode node = new ListNode(stack.pop());
            if(a){
                node.next = null;
                a = false;
            }else{
                node.next = dummy;
            }
            dummy = node;
        }
        return dummy;
    }
}