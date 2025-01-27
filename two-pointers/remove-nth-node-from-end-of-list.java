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
    static int getSize(ListNode temp){
        int size = 0;
        while(temp != null){
            size++;
            temp = temp.next;
        }
        return size;
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp = head;
        int size = getSize(temp);   
        int index = size - n;
        if(index == 0){
            head = head.next;
        }else{
            ListNode node = head;
            for(int i = 1; i<index; i++){
                node  = node.next;
            }
            ListNode middleNode = node.next;
            if(middleNode.next == null){
                node.next = null;
            }else{
                node.next = middleNode.next;
            }
        }
        return head;
    }
}