class Solution {
    private List<TreeNode> res = new ArrayList<>();
    private boolean[] toDelete = new boolean[1001];

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        for (int val : to_delete) {
            toDelete[val] = true;
        }
        dfs(root, true);
        return res;
    }

    private TreeNode dfs(TreeNode root, boolean addThisNode) {
        if (root == null) return null;
        boolean addNextNode = toDelete[root.val];
        root.left = dfs(root.left, addNextNode);
        root.right = dfs(root.right, addNextNode);

        if (!addNextNode && addThisNode) {
            res.add(root);
        } 

        return addNextNode ? null : root;
    }
}