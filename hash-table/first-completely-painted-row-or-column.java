class Solution {
    
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] arr1 = new int[n];
        int[] arr2 = new int[m];

        HashMap<Integer, int[]> map = new HashMap<>();
        for(int i = 0; i<mat.length; i++){
            for(int j = 0; j<mat[0].length; j++){
                map.put(mat[i][j],new int[]{i,j});
            }
        }

        for(int x = 0; x< arr.length; x++){
            int value = arr[x];
            int[] position = map.get(value);
            arr1[position[1]]++;
            arr2[position[0]]++;
            if(arr1[position[1]] == m || arr2[position[0]] == n){
                return x;
            }
        }
        return -1;
    }
}