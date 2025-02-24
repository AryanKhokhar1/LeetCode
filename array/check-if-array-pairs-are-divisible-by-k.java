class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] keys = new int[k];

        for(int ele: arr){
            int remainder = ((ele % k) + k) % k;
            keys[remainder]++;
        }

        if(keys[0] % 2 != 0) return false;
        if(k % 2 == 0){
            if(keys[k/2] % 2 != 0){
                return false;
            }
        }
        for(int i = 1, j = k -1; i<j ; i++, j--){
            if(keys[i]  != keys[j]){
                return false;
            }
        }
        return true;
    }
}