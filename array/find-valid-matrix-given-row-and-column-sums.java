class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int[][] answer = new int[rowSum.length][colSum.length];
        for(int i = 0; i<colSum.length; i++){
            for(int j = 0; j<rowSum.length; j++){
                int interSection = Math.min(rowSum[j],colSum[i]);
                answer[j][i] = interSection;
                rowSum[j] -= interSection;
                colSum[i] -= interSection;
            }
        }
        return answer;
    }
}