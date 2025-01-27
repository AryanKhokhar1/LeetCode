class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> answer = new ArrayList<>();

        Set<Integer> minElementRow = new HashSet<>();
        Set<Integer> maxElementColumn = new HashSet<>();
        
        for(int row = 0; row<matrix.length; row++){
            int min = Integer.MAX_VALUE;
            for(int i = 0; i<matrix[0].length; i++){
                min = Math.min(min,matrix[row][i]);
            }
            // System.out.println(min);
            minElementRow.add(min);
        }
        // System.out.println(minElementRow);

        for(int column = 0; column<matrix[0].length; column++){
            int max = Integer.MIN_VALUE;
            for(int row = 0; row<matrix.length; row++){
                max = Math.max(max,matrix[row][column]);
            }
            maxElementColumn.add(max);
        }

        for(int ele: minElementRow){
            if(maxElementColumn.contains(ele)){
                answer.add(ele);
            }
        }
        return answer;
    }
}