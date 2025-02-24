class Solution {
    int number = 0;
    public int numberOfSteps(int num) {
        // if(num == 0){
        //     return this.number;
        // }

        if(num%2 != 0 && num != 0){
            this.number++;
            numberOfSteps(num-1);
        }else if(num%2 == 0 && num != 0){
            this.number++;
            numberOfSteps(num/2);
        }
        return this.number;
    }
}