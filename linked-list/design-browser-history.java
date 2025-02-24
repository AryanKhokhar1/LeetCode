class Node{
    Node next;
    Node prev;
    String value;
    Node(){}
    Node(String value){this.value = value; this.next = null; this.prev = null;}
    Node(String value, Node prev){this.value = value; this.next = null; this.prev = prev;}
}
class BrowserHistory {

    Node head;
    Node current_position;
    public BrowserHistory(String homepage) {
        head = new Node(homepage);
        current_position = head;
    }
    
    public void visit(String url) {
        Node node = new Node(url,current_position);
        node.prev = current_position;
        current_position.next = node;
        current_position = current_position.next;
    }
    
    public String back(int steps) {
        while(steps != 0 && current_position.prev != null){
            steps--;
            current_position = current_position.prev;
        }
        return current_position.value;
    }
    
    public String forward(int steps) {
        while(steps != 0 && current_position.next != null){
            steps--;
            current_position = current_position.next;
        }
        return current_position.value;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */