import java.util.*;
public class MinStack {

	/** initialize your data structure here. */
	Stack<Integer> st, minValues;
	public MinStack() {
		st = new Stack();
		minValues = new Stack();
		
	}
	
	public void push(int x) {
		if (minValues.empty() || x <= minValues.peek())  minValues.push(new Integer(x));
		st.push(new Integer(x));
	}
	
	public void pop() {
		Integer x = st.pop();
		if (x.equals(minValues.peek())) x = minValues.pop();
	}
	
	public int top() {
		return st.peek();
	}
	
	public int getMin() {
		return minValues.peek();
	}
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */