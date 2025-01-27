class Solution {
    public int findKthPositive(int[] arr, int k) {
        ArrayList<Integer> arl = new ArrayList<>();
        int index = 0;
        int miss = 0;
        for(int i = 1; i<arr[arr.length-1]; i++){
            if(arr[index] == i){
                index++;
            }else{
                arl.add(i);
                miss++;
            }
            if(k == miss){
                return i;
            }
        }
        return (arr[arr.length-1] + (k-arl.size()));
    }
}