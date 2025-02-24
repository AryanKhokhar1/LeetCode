/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int sizeA = 0;
        int sizeB = 0;
        ListNode tempA = headA;
        ListNode tempB = headB;
        while(tempA != null){
            sizeA++;
            tempA = tempA.next;
        }
        while(tempB != null){
            sizeB++;
            tempB = tempB.next;
        }
        while(sizeA > sizeB){
            sizeA--;
            headA = headA.next;
        }
        while(sizeA < sizeB){
            sizeB--;
            headB = headB.next;
        }
        while(headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
}