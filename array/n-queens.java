class Solution {
    int maxRow;
    List<List<String>> queen(boolean[][] board, int row, List<String> path){
        if(row == this.maxRow){
            List<List<String>> lis = new ArrayList<>();
            lis.add(new ArrayList<>(path));
            return lis;
        }
        
        List<List<String>> p = new ArrayList<>();
        for(int i = 0; i<this.maxRow; i++){
            if(checkqueen(board,row,i)){
                board[row][i] = true;
                path.add(pathAdd(i));

                p.addAll(queen(board,row+1,path));

                path.remove(path.size()-1);
                board[row][i] = false;
            }
        }
        return p;
    }
    String pathAdd(int i){
        return ".".repeat(i)+ "Q"+ ".".repeat(this.maxRow-1-i);
    }
    boolean checkqueen(boolean[][] board, int row, int column){
        int tempRow = row;
        // To Upward
        while(tempRow >= 0){
            if(board[tempRow][column]){
                return false;
            }
            tempRow--;
        }

        // Going to Left Diagonal
        tempRow = row;
        int tempColumn = column;
        while(tempRow >= 0 && tempColumn >= 0){
            if(board[tempRow][tempColumn]){
                return false;
            }
            tempRow--;
            tempColumn--;
        }

        // Going to Right Diagonal
        tempRow = row;
        tempColumn = column;
        while(tempRow >= 0 && tempColumn < this.maxRow){
            if(board[tempRow][tempColumn]){
                return false;
            }
            tempRow--;
            tempColumn++;
        }
        return true;
    }
    public List<List<String>> solveNQueens(int n) {
        boolean[][] board = new boolean[n][n];
        this.maxRow = n;
        List<String> lis = new ArrayList<>();
        return queen(board,0,lis);
    }
}