#%% [markdown]
#```
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#```
# %%
from typing import *
from collections import deque
root = [3,9,20,None ,None ,15,7]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# %%
def maxDepth(root: TreeNode) -> int:
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        cur_root = queue.popleft()
        if cur_root.left:
            print(cur_root.left)
maxDepth(root)
# %%
