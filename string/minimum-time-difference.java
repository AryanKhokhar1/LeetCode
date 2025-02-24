class Solution {
    private static int difference(String a, String b){
        int difmin1 = (Integer.valueOf(a.substring(0,2)) - Integer.valueOf(b.substring(0,2)))*60 + (Integer.valueOf(a.substring(3,5)) - Integer.valueOf(b.substring(3,5)));
        
        int difmin2 = (Integer.valueOf(b.substring(0,2)) - Integer.valueOf(a.substring(0,2)))*60 + (Integer.valueOf(b.substring(3,5)) - Integer.valueOf(a.substring(3,5)));

        if(difmin1 < 0){
            difmin1 = 1440 + difmin1;
        }
        if(difmin2<0){
            difmin2 = 1440 + difmin2;
        }
        return Math.min(difmin1,difmin2);

    }
    public int findMinDifference(List<String> timePoints) {
        
        int ans = Integer.MAX_VALUE;
        Collections.sort(timePoints);
        for(int i = 1; i<timePoints.size(); i++){
            ans = Math.min(ans,difference(timePoints.get(i-1), timePoints.get(i)));
            if(ans == 0){
                return ans;
            }
        }
        ans = Math.min(ans,difference(timePoints.get(0), timePoints.get(timePoints.size()-1)));

        return ans;
    }
}