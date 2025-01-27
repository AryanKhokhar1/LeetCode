class Solution {
    public int subtractProductAndSum(int n) {
        int lett;
        int summ = 0;
        int mult = 1;
        while(n != 0){
            lett = n%10;
            summ += lett;
            mult *= lett;
            n = n/10;
        }
        return (mult-summ);
    }
}