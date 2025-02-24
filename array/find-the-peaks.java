class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        ArrayList answer = new ArrayList();
        for(int i =0, j= 2; j<mountain.length; i++,j++){
            if(mountain[i+1]>mountain[i] && mountain[i+1]>mountain[j]){
                answer.add(i+1);
            }
        }
        return answer;
    }
}