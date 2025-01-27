class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> set2 = new HashSet<>();
        int[] answer = new int[A.length];

        for(int i = 0; i<A.length; i++){
            set1.add(A[i]);
            set2.add(B[i]);

            int intersectionSize = 0;
            for (int element : set1) {
                if (set2.contains(element)) {
                intersectionSize++;
                }
            }
            answer[i] = intersectionSize;
        }
        return answer;
    }
}