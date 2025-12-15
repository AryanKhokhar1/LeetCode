class Solution {
    public int fib(int n) {
        int a = 0;
        int b = 1;
        int c;
        if(n <= 1){
            if(n == 0){
                return a;
            }else{
                return b;
            }
        }
        for(int i = 1; i<n; i++){
            c = b;
            b = b+a;
            a = c;
        }
        return b;
    }
}