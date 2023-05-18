class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def preorder(node, inner_ls):
    if node:
        inner_ls.append(node.val)
    if node.left:
        preorder(node.left, inner_ls)
    if node.right:
        preorder(node.right, inner_ls)
    return inner_ls
class Solution:
    def generateTrees(self, n: int) :
        def dfs(left, right):
            if left > right: return [None]
            if left == right: 
                print(f' left {left}')
                return [TreeNode(left)]
            ans = []
            for root in range(left, right+1):
                # print(f' NEW ITER {root}')
                # print(f' left    left = {left}    right = {root-1}')
                leftNodes = dfs(left, root - 1)
                print(f'leftnode = {[i.val for i in  leftNodes if i]}')
                # print(f' right   left = {root+1}    right = {right}')
                rightNodes = dfs(root+1, right)
                print(f'rightnode = {[i.val for i in rightNodes  if i]}')
                print('\n\n')
                for leftNode in leftNodes:
                    # if leftNode:
                    # 	print(f'leftNOne {leftNode.val}')
                    # else:
                    #     # print(f'leftNOne {leftNode}')
                    #     pass
                    # print(f'root = {root}')
                    for rightNode in rightNodes:
                        # if rightNode:
                        #     print(f'rightNone {rightNode.val}')
                        # else:
                        # 	# print(f'rightNOne {rightNode}')
                        #     pass
                        
                        rootNode = TreeNode(root, leftNode, rightNode)
                        # print(preorder(rootNode, []))
                        # print(id(rootNode))
                        # print('\n\n')
                        ans.append(rootNode)
            return ans
        
        return dfs(1, n)
obj1 = Solution()
s = obj1.generateTrees(3)
# print(s)
for i in s:
	# print(preorder(i, []))
    print(id(i))