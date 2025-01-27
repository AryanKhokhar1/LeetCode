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
    public int getDecimalValue(ListNode head) {
        StringBuilder str = new StringBuilder();
        while(head != null){
            str.append(head.val);
            head = head.next;
        }
        int answer = 0;
        int a = 0;
        for(int i = str.length()-1; i>= 0; i--){
            answer += (str.charAt(i) - '0')*Math.pow(2,a++);
        }
        return answer;
    }
}