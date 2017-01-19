/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
	public ListNode sortList(ListNode head) {
		if(head==null || head.next==null) return head;
		ListNode mid = getMidNode(head);
		ListNode right = sortList(mid.next);
		mid.next = null;
		ListNode left = sortList(head);
		return merge(left,right);
	}
	
	public ListNode getMidNode(ListNode head){
		ListNode fast = head.next, slow = head;
		while(fast!=null && fast.next != null){
			fast = fast.next.next;
			slow = slow.next;
		}
		return slow;
	}
	
	public ListNode merge(ListNode head1, ListNode head2){
		ListNode node1 = head1;
		ListNode node2 = head2;
		ListNode head = new ListNode(0);
		ListNode node = head;
		while(node1!=null && node2!=null){
			if(node1.val>node2.val) {
				node.next = node2;
				node2 = node2.next;
			}else{
				node.next = node1;
				node1 = node1.next;
			}
			node = node.next;
		}
		if(node1!=null) node.next = node1;
		if(node2!=null) node.next = node2;
		return head.next;
	}
}