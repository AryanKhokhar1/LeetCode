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
    public ListNode swapNodes(ListNode head, int k) {
        ArrayList<Integer> arrList = new ArrayList<>();
        while(head != null){
            arrList.add(head.val);
            head = head.next;
        }
        Integer c = arrList.get(k-1);
        arrList.set(k-1,arrList.get(arrList.size()-k));
        arrList.set(arrList.size()-k,c);
        
        ListNode dummy = new ListNode();
        ListNode temp = dummy;
        for(int element: arrList){
            ListNode node = new ListNode(element);
            temp.next = node;
            temp = temp.next;
        }
        return dummy.next;
    }
}