# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def insertBT(btreenode,val):
        if val<btreenode.val:
            if btreenode.right == None:
                btreenode.right=TreeNode(val)
            else:
                insertBT(btreenode.right,val)
        else:
            if btreenode.left == None:
                btreenode.left=TreeNode(val)
            else:
                insertBT(btreenode.left,val)
            
def preorderTraversal(node):
    print(node.val)
    if node.left!=None:
        preorderTraversal(node.left)
    
    if node.right!=None:
        preorderTraversal(node.right)
        
class Solution:
    def constructMaximumBinaryTree(nums: list[int]) -> Optional[TreeNode]:
        nums = sorted(nums,reverse = True)
        print(nums)
        a = TreeNode(nums[0])
        for i in range(1,len(nums)):
            insertBT(a,nums[i])
        return a
    a =  constructMaximumBinaryTree(nums = [3,2,1,6,0,5])
    preorderTraversal(a)