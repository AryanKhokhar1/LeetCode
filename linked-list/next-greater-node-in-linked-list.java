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
    public int[] nextLargerNodes(ListNode head) {
        ListNode ans = head;
        int size = 1;
        while(head != null){
            ListNode temp = head.next;
            boolean check = false;
            while(temp!= null){
                if(head.val<temp.val){
                    head.val = temp.val;
                    check = true;
                    break;
                }
                temp = temp.next;
            }
            if(!check){
                head.val = 0;
            }
            head = head.next;
            size++;
        }
        int[] arr = new int[size-1];
        int i = 0;
        while(ans != null){
            arr[i++] = ans.val;
            ans = ans.next;
        }
        return arr;
    }
}