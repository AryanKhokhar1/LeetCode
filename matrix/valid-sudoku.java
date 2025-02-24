class Solution {
    public boolean isValidSudoku(char[][] board) {
        // column wise
        for(int i = 0; i<9; i++){
            HashMap<Character,Integer> map1 = new HashMap<>();
            HashMap<Character,Integer> map2 = new HashMap<>();
            for(int j = 0; j<9; j++){
                if(map1.get(board[i][j]) == null || board[i][j] == '.'){
                    map1.put(board[i][j],1);
                }else{
                    return false;
                }
                if(map2.get(board[j][i]) == null || board[j][i] == '.'){
                    map2.put(board[j][i],1);
                }else{
                    return false;
                }
            }
        }
        for(int a = 0, b = 0; a<9 && b<9;){
            HashMap<Character, Integer> map = new HashMap<>();
            for(int i = a; i<a+3; i++){
                for(int j = b; j<b+3; j++){
                    if(map.get(board[i][j]) == null || board[i][j] == '.'){
                        map.put(board[i][j], 1);
                    }else{
                        return false;
                    }
                }
            }
            if(b+3 == 9){
                b = 0;
                a += 3;
            }else{
                b += 3;
            }
        }

        return true;

    }
}