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
    public ListNode mergeKLists(ListNode[] lists) {
        
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        ArrayList<Integer> arrayList = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        for(int i = 0; i<lists.length; i++){
            while(lists[i] != null){
                arrayList.add(lists[i].val);
                lists[i] = lists[i].next;
            }
        }
        Integer[] arr = arrayList.toArray(new Integer[0]);
        Arrays.sort(arr);
        for(Integer ele: arr){
            ListNode node = new ListNode(ele);
            dummy.next = node;
            dummy = dummy.next;
        }
        return head.next;
    }
}