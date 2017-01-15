/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
	public TreeNode invertTree(TreeNode root) {
		if(root==null) return root;
		TreeNode tmp = invertTree(root.left);
		root.left = invertTree(root.right);
		root.right = tmp;
		return root;
	}
}