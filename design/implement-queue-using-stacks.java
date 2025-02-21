class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;
    public MyQueue() {
        this.stack1 = new Stack<>();
        this.stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        if(empty()){
            return -1;
        }
        while(!stack1.empty()){
            stack2.push(stack1.pop());
        }
        int val = stack2.pop();
        while(!stack2.empty()){
            stack1.push(stack2.pop());
        }
        return val;
    }
    
    public int peek() {
        if(empty()){
            return -1;
        }else{
            while(!stack1.empty()){
                stack2.push(stack1.pop());
            }
            int val = stack2.peek();
            while(!stack2.empty()){
                stack1.push(stack2.pop());
            }
            return val;
        }
    }
    
    public boolean empty() {
        if(stack1.size() == 0){
            return true;
        }
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */