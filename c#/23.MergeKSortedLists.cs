/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MergeKLists(ListNode[] lists) {
        if (lists == null || lists.Length == 0)
            return null;
        return MergeKLists(lists, 0, lists.Length-1);
    }
    
    private ListNode MergeKLists(ListNode[] lists, int start, int end) {
        if (end == start)
            return lists[start];
        if (end - start == 1)
            return MergeTwoLists(lists[start], lists[end]);
        int mid = (end + start)/2;
        return MergeTwoLists(MergeKLists(lists, start, mid), MergeKLists(lists, mid+1, end));
    }
    
    private ListNode MergeTwoLists(ListNode listNode1, ListNode listNode2) {
        if (listNode1 == null)
            return listNode2;
        if (listNode2 == null)
            return listNode1;
        ListNode node, head, next1, next2;
        if (listNode2.val < listNode1.val)
        {
            node = listNode2;
            head = listNode2;
            next1 = listNode1;
            next2 = listNode2.next;
        }
        else
        {
            node = listNode1;
            head = listNode1;
            next1 = listNode1.next;
            next2 = listNode2;
        }
        while (next1 != null && next2 != null)
        {
            if (next1.val < next2.val)
            {
                node.next = next1;
                node = next1;
                next1 = next1.next;
            }
            else
            {
                node.next = next2;
                node = next2;
                next2 = next2.next;
            }
        }
        if (next1 != null)
            node.next = next1;
        else
            node.next = next2;
        return head;
    }
}
