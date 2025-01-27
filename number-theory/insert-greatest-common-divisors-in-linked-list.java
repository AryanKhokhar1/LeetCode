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
    static int findHCF(int num1, int num2){
        if(num2 == 0) return num1;
        return findHCF(num2,num1%num2);
    }
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode temp = head;
        while(temp.next != null){
            int hcf = findHCF(temp.val, temp.next.val);
            ListNode node = new ListNode(temp.next.val,temp.next.next);
            temp.next.val = hcf;
            temp.next.next = node;
            temp = temp.next.next;
        }
        return head;
    }
}