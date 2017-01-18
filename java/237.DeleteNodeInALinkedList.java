/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
	public void deleteNode(ListNode node) {
		ListNode currentNode = node;
		ListNode prevNode = node;
		while(currentNode.next != null){
			currentNode.val = currentNode.next.val;
			prevNode = currentNode;
			currentNode = currentNode.next;
		}
		prevNode.next = null;
	}
}