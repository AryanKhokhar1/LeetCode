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
    public ListNode modifiedList(int[] nums, ListNode head) {
        HashMap<Integer, Boolean> map = new HashMap<>();
        for(int element: nums){
            if(map.get(element) == null){
                map.put(element,true);
            }
        }
        ListNode dummy = new ListNode(0);
        ListNode ans = dummy;
        while(head != null){
            if(map.get(head.val) == null){
                ListNode node = new ListNode(head.val);
                dummy.next = node;
                dummy = dummy.next;
            }
            head = head.next;
        }
        return ans.next;
    }
}