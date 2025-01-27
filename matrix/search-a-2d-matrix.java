class Solution {

    int findPosition(int[][] matrix ,int first, int last, int target){
        int mid = first+ (last - first)/2;
        if(first > last){
            return -1;
        }

        if(matrix[mid/matrix[0].length][mid%matrix[0].length] == target){
            return mid;
        }else if(matrix[mid/matrix[0].length][mid%matrix[0].length]>target){
            return findPosition(matrix,first,mid-1,target);
        }else{
            return findPosition(matrix,mid+1,last,target);
        }
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        
        return findPosition(matrix,0,(matrix.length*matrix[0].length)-1,target) != -1;

    }
}