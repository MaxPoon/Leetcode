/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		if(headA==null || headB==null) return null;
		if(headA==headB) return headA;
		ListNode p = headA;
		ListNode q = headB;
		while(p.next!=null && q.next!=null){
			if(p==q) return q;
			p = p.next;
			q = q.next;
		}
		int count = 0;
		int x;
		if(p.next== null) x=0;
		else x =1;
		while(p.next!=null){
			p=p.next;
			count++;
		}
		while(q.next!=null){
			q = q.next;
			count++;
		}
		if(q!=p) return null;
		p = headA;
		q = headB;
		if(x==0){
			while(count>0){
				q = q.next;
				count--;
			}
		}else{
			while(count>0){
				p=p.next;
				count--;
			}
		}
		if(p==q) return p;
		while(p.next!=null && q.next!=null){
			if(p==q) return q;
			p = p.next;
			q = q.next;
		}
		if(p==q) return p;
		return null;
	}
}