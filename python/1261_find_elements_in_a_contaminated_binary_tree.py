# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        clean_root = self.__clean_tree(root)
        self.root = clean_root

    def __clean_tree(self, root: Optional[TreeNode], val: Optional[int]=0):
        if root is None:
            return root

        if root.val == -1:
            clean_val = val
        else:
            clean_val = root.val
        root.val = clean_val

        if root.left is not None:
            clean_left_val = 2 * clean_val + 1
            self.__clean_tree(root=root.left, val=clean_left_val)
        if root.right is not None:
            clean_right_val = 2 * clean_val + 2
            self.__clean_tree(root=root.right, val=clean_right_val)
        return root

    def find(self, target: int) -> bool:
        return self.__find(self.root, target)

    def __find(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        elif target < root.val:
            return False
        elif target == root.val:
            return True
        else:
            return self.__find(root.left, target) or \
                self.__find(root.right, target)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
