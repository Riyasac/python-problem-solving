"""
Check if Two Trees are Identical


Given the roots r1 and r2 of two binary trees, determine whether they are identical.
Two trees are considered identical if they have the same structure and the same node values.

Example 1:

Input:
r1:           
    1           
   / \          
  2   3         
 /              
4 
             
r2:           
    1           
   / \          
  2   3         
 /              
4              

Output: true
Explanation: Trees are identical, having same node structure and node values.
_________________________________________________________________________________

Example 2:

Input:
r1:           
    1           
   / \          
  2   3         
 /              
4 
             
r2:           
    1           
   / \          
  2   3         
     /              
    4              

Output: false
Explanation: Trees are not identical, both have different node structure.
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_identical(r1, r2) -> bool:
    
    if r1 is None and r2 is None:
        return True
     
    if r1 is None or r2 is None:
        return False 
    
    
    if (
        r1.data == r2.data and
        is_identical(r1.left, r2.left) and
        is_identical(r1.right, r2.right)
    ):
        return True
    
    return False


if __name__ == "__main__":
    
    r1 = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
    r2 = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
    
    identical = is_identical(r1, r2)
    print("Trees are identical" if identical else "Trees are not identical")
    
    
    r1 = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3))
    r2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
    
    identical = is_identical(r1, r2)
    print("Trees are identical" if identical else "Trees are not identical")
