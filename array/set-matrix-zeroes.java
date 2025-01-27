class Solution {
    public void setZeroes(int[][] matrix){
        HashSet<Integer> setRow = new HashSet<>();
        HashSet<Integer> setColumn = new HashSet<>();
        for(int i = 0; i<matrix.length; i++){
            for(int j = 0; j<matrix[i].length; j++){
                if(matrix[i][j] == 0){
                    setRow.add(i);
                    setColumn.add(j);
                }
            }
        }
        Iterator<Integer> row = setRow.iterator();

        // Convert targeted row's to zero
        int value;
        while(row.hasNext()){
            value = row.next();
            for(int i = 0; i<matrix[0].length; i++){
                matrix[value][i] = 0;
            }
        }

        // Convert targeted column to zero's

        Iterator<Integer> column = setColumn.iterator();

        while(column.hasNext()){
            value = column.next();
            for(int i = 0; i<matrix.length; i++){
                matrix[i][value] = 0;
            }
        }
    }
}