class Solution {
    int maxRow;
    int queen(boolean[][] board, int row){
        if(row == this.maxRow){
            return 1;
        }
        int time = 0;
        for(int i = 0; i<this.maxRow; i++){
            if(checkQueenPlaced(board, row , i)){
                board[row][i] = true;

                time += queen(board,row+1);

                board[row][i] = false;
            }
        }
        return time;
    }
    public int totalNQueens(int n) {
        boolean[][] board =  new boolean[n][n];
        this.maxRow = n;
        return queen(board,0);
    }
    boolean checkQueenPlaced(boolean[][] board, int row, int column){
        int tempRow = row;
        while(tempRow >= 0){
            if(board[tempRow][column]){
                return false;
            }
            tempRow--;
        }

        // Going to left Diagonal
        tempRow = row;
        int tempColumn = column;
        while(tempRow>= 0 && tempColumn >= 0){
            if(board[tempRow][tempColumn]){
                return false;
            }
            tempRow--;
            tempColumn--;
        }

        tempRow = row;
        tempColumn = column;
        while(tempRow >= 0 && tempColumn <this.maxRow){
            if(board[tempRow][tempColumn]){
                return false;
            }
            tempRow--;
            tempColumn++;
        }
        return true;
    }
}