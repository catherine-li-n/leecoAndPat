# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if not root:
			return []
		results = []
		cur = [root]
		next = []
		while cur or next:
			result = []
			for p in cur:
				result.append(p.val)
				if p.left:
					next.append(p.left)
				if p.right:
					next.append(p.right)
			results.append(result)
			cur = next
			next = []
		return results




