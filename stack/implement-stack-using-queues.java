class MyStack {
    private Queue<Integer> queue1;
    private Queue<Integer> queue2;
    public MyStack() {
        this.queue1 = new LinkedList<>();
        this.queue2 = new LinkedList<>();
    }
    
    public void push(int x) {
        this.queue1.add(x);
    }
    
    public int pop() {
        if(empty()){
            return -1;
        }
        int q1s = this.queue1.size();
        for(int i = 1; i<q1s; i++){
            this.queue2.add(this.queue1.remove());
        }
        int val = this.queue1.remove();
        this.queue1 = this.queue2;
        // this.queue2.clear();
        return val;
    }
    
    public int top() {
        if(empty()){
            return -1;
        }
        int q1s = this.queue1.size();
        for(int i =1; i<q1s; i++){
            this.queue2.add(this.queue1.remove());
        }
        int val = this.queue1.remove();
        this.queue2.add(val);
        this.queue1 = this.queue2;
        // this.queue2.clear();
        return val;
    }
    
    public boolean empty() {
        return queue1.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */