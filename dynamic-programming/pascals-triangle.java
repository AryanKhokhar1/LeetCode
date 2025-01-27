class Solution {
    public List<List<Integer>> generate(int numRows) {
        //   [1]
        //  [1, 1]
        // [1, 2, 1]

        List<List<Integer>> pascal = new ArrayList<>();

        if(numRows == 1){
            List<Integer> pascal1 = new ArrayList<>();
            pascal1.add(1);
            pascal.add(pascal1);
        }else if(numRows == 2){
            List<Integer> pascal1 = new ArrayList<>();
            pascal1.add(1);
            pascal.add(pascal1);
            List<Integer> pascal2 = new ArrayList<>();
            pascal2.add(1);
            pascal2.add(1);
            pascal.add(pascal2);
        }else{
            List<Integer> pascal1 = new ArrayList<>();
            pascal1.add(1);
            pascal.add(pascal1);
            List<Integer> pascal2 = new ArrayList<>();
            pascal2.add(1);
            pascal2.add(1);
            pascal.add(pascal2);

            for(int i = 3 ; i<= numRows; i++){
                List<Integer> subpascal = new ArrayList<>();
                subpascal.add(1);
                    for(int a = 0, b= 1; b<pascal.get(i-2).size(); a++, b++ ){
                        subpascal.add(pascal.get(i-2).get(a)+pascal.get(i-2).get(b));
                    }
                subpascal.add(1);
                pascal.add(subpascal);
            }
        }
        return pascal;
    }
}