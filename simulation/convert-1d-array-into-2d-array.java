class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int[][] arr = new int[m][n];
        int index = 0;
        for(int row = 0; row<m; row++){
            for(int column = 0; column<n; column++){
                if(index<original.length){
                    arr[row][column] = original[index++];
                }else{
                    return new int[0][0];
                }
            }
        }
        // System.out.println(index);
        if(index != original.length){
            return new int[0][0];
        }
        return arr;
    }
}