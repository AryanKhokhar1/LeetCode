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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        ListNode prev = head;
        ListNode temp = head.next;
        if(prev == null || temp == null || temp.next == null){
            return new int[]{-1,-1};
        }
        int position = 2;
        while(temp.next != null){
            if(temp.val > prev.val && temp.val > temp.next.val){
                arrayList.add(position);
            }else if(temp.val < prev.val && temp.val < temp.next.val){
                arrayList.add(position);
            }
            position++;
            prev = prev.next;
            temp = temp.next;
        }
        if(arrayList.size() <= 1){
            return new int[]{-1,-1};
        }else{
            int firstval = Integer.MAX_VALUE;
            for(int i = 1; i<arrayList.size(); i++){
                firstval = Math.min(firstval, arrayList.get(i) - arrayList.get(i-1));
            }
            return new int[]{firstval, arrayList.get(arrayList.size() -1) - arrayList.get(0)};
        }
    }
}