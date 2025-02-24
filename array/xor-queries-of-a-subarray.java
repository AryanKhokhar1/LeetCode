class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int[] prefix_xor = new int[arr.length+1];
        prefix_xor[0] = 0;
        for(int i = 0; i<arr.length; i++){
            prefix_xor[i+1] = prefix_xor[i] ^ arr[i];
        }

        int i = 0;
        int ar[];
        for(; i<queries.length; ){
            ar = queries[i];
            if(ar[0] == 0){
                answer[i++] = prefix_xor[ar[1]+1];
            }else{
                answer[i++] = (prefix_xor[ar[0]] ^ prefix_xor[ar[1]+1]);
            }
        }
        return answer;
    }
}