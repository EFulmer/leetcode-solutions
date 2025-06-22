/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if root == nil {
        return false
    } else if root.Val == subRoot.Val {
        if eq(root, subRoot) {
            return true
        }
    }
    return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func eq(tree1 *TreeNode, tree2 *TreeNode) bool {
    if tree1 == nil && tree2 == nil {
        return true
    } else if (tree1 == nil && tree2 != nil) || (tree1 != nil && tree2 == nil) {
        return false
    } else if (tree1.Val != tree2.Val) {
        return false
    } else {
        return eq(tree1.Left, tree2.Left) && eq (tree1.Right, tree2.Right)
    }
}
