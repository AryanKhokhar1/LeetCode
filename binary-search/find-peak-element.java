class Solution {
    public int findPeakElement(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<>();
        for(int ele:nums){
            arr.add(ele);
        }
        if(arr.size() == 1){
            return 0;
        }
        arr.add(0,Integer.MIN_VALUE);
        arr.add(arr.size(),Integer.MIN_VALUE);
        for(int i = 0,j= 2; j<=arr.size(); i++,j++){
            if(arr.get(i+1)>arr.get(i) && arr.get(i+1)>arr.get(j)){
                return i;
            }
        }
        return -1;
    }
}