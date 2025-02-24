class Solution {
    public void rotate(int[][] matrix) {
        
        int n = matrix.length;
        int[][] newMatrix = new int[n][n];
        for(int row  = 0; row<n; row++){
            for(int column = 0; column<n; column++){
                newMatrix[column][(n-1)-row] = matrix[row][column];
            }
        }
        for(int row  = 0; row<n; row++){
            for(int column = 0; column<n; column++){
                matrix[row][column] = newMatrix[row][column];
            }
        }
        
    }
}