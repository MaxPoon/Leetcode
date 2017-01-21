/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
	public ListNode oddEvenList(ListNode head) {
		if(head==null || head.next==null) return head;
		ListNode odd = head, even = head.next, second = head.next;
		while(even!=null && even.next!=null){
			ListNode nextOdd = even.next;
			ListNode nextEven = nextOdd.next;
			odd.next = nextOdd;
			even.next = nextEven;
			odd = nextOdd;
			even = nextEven;
		}
		odd.next = second;
		return head;
	}
}