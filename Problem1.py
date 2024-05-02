# BFS-1
# Problem 1
# Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)

# Approach
# create a queue. For level order traversal, for each iteration, calculate the size of the queue. Traverse through q for range(size)
# Pop leftmost element. Add it to new list. Check if the node has left and right child. If yes, append it to queue.
# Add the list to res list. Return res list

# Time Complexity: O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            level_res = []
            for i in range(size):
                curr = q.popleft()
                level_res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_res)
        return res