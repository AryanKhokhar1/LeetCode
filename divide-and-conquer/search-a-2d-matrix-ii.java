class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int i = 0; i<matrix.length && matrix[i][0] <= target ; i++){
            for(int ele: matrix[i]){
                if(ele == target){
                    return true;
                }else if(ele > target){
                    break;
                }
            }
        }
        return false;
    }
}