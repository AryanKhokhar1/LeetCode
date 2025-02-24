class Solution {
    public static int[][] spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        
        int i = 1;
        // int[][] answer = new int[rows][cols];
        int[][] ans = new int[rows*cols][2];
        int val = 1;
        int index = 0;
        // answer[rStart][cStart] = 1;
        while(val<= rows*cols){
            for(int c = 0; c<i;){
                if((rStart>= 0 && rStart<rows) && (cStart>= 0 && cStart<cols)){
                    // answer[rStart][cStart] = val++;
                    val++;
                    ans[index++] = new int[]{rStart,cStart};

                }
                if(i%2 == 1){
                    cStart++;
                }else{
                    cStart--;
                }
                c++;
            }
            for(int r = 0;r<i;){
                if((rStart>= 0 && rStart<rows) && (cStart>= 0 && cStart<cols)){
                    // answer[rStart][cStart] = val++;
                    val++;
                    ans[index++] = new int[]{rStart,cStart};
                }
                if(i%2 == 1){
                    rStart++;
                }else{
                    rStart--;
                }
                r++;
            }
            i++;
        }
        return ans;
    }
}