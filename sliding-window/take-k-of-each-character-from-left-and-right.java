class Solution {
    public int takeCharacters(String s, int k) {
        int[] arr = {0, 0, 0};
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == 'a'){
                arr[0]++;
            }else if(s.charAt(i) == 'b'){
                arr[1]++;
            }else if(s.charAt(i) == 'c'){
                arr[2]++;
            }
        }
        if(arr[0] < k || arr[1] < k || arr[2] < k){
            return -1;
        }
        
        int res = Integer.MAX_VALUE;
        int l = 0;
        for (int r = 0; r < s.length(); r++) {
            arr[s.charAt(r) - 'a']--;
            
            while (Math.min(Math.min(arr[0], arr[1]), arr[2]) < k) {
                arr[s.charAt(l) - 'a']++;
                l++;
            }
            res = Math.min(res, s.length() - (r - l + 1));
        }
        return res;
    }
}