class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        
        HashMap<Integer,String> person = new HashMap<>();
        for(int i = 0; i<names.length; i++){
            person.put(heights[i],names[i]);
        }
        Arrays.sort(heights);
        String[] ans = new String[names.length];
        int a = 0;
        for(int i = names.length -1; i>= 0; i--){
            ans[a++] = person.get(heights[i]);
        }
        return ans;
    }
}