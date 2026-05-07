class MyStack {
public:
    MyStack() {}

    vector<int> t;
    
    void push(int x) {
        t.insert(t.begin(), x);
    }
    
    int pop() {
        int tmp=t[0];
        t.erase(t.begin());
        return tmp;
    }
    
    int top() {
        return t[0];
    }
    
    bool empty() {
        return t.size()==0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */