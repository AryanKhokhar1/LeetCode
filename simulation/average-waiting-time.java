class Solution {
    
    public double averageWaitingTime(int[][] customers) {
        long timetaken = 0;
        long lastime = 0;
        for(int i = 0; i<customers.length; i++){
            if(lastime < customers[i][0]){
                timetaken += customers[i][1];
                lastime = customers[i][0] + customers[i][1];
            }else{
                lastime += customers[i][1];
                timetaken += lastime - customers[i][0];
            }
        }
        return (double) timetaken/customers.length;
    }
}