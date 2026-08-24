# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # If array is empty
        if not nums:
            return None

        # Find middle index
        mid = len(nums) // 2

        # Middle element becomes root
        root = TreeNode(nums[mid])

        # Left side becomes left subtree
        root.left = self.sortedArrayToBST(nums[:mid])

        # Right side becomes right subtree
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root