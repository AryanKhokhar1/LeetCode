class Solution {
    public int minimumPushes(String word) {
        int [] map = new int [26];

        for(int i=0; i<word.length(); i++){
            map[word.charAt(i) - 'a']++;
        }

        Arrays.sort(map);
        int i=25;
        int count=0;
        int cost=1;
        int sum=0;
        while(i>=0 && map[i] != 0){
            sum += (cost*map[i]);
            count++;
            if(count == 8){
                cost++;
                count = 0;
            }
            i--;
        }

        return sum;
    }
}