from more_itertools import value_chain


class TreeNode:
    def __init__(self, value, left, right) -> None:
        self.value = value
        self.left = left
        self.right = right
class Tree:
    def __init__(self, value :int) -> None:
        self.compare = 1e-20
    def InsertNode(self, node,value):
        if value > node.value:
            if node.right:
                return self.InsertNode(node.right,value)
            node.right = TreeNode(value, None, None)  
        else:
            if node.left:
                return self.InsertNode(node.left,value)
            node.left = TreeNode(value, None, None)
            
    def printTreeDFS(self, node):
        if node.left:
            self.printTreeDFS(node.left)
        print(node.value)
        if node.right:
            self.printTreeDFS(node.right)
            

    def printTreeBFS(self,root):
        queue = [root]
        rear = 0   # ince while add
        front = 0  # while sub
        while True:
            if queue[front].left:
                queue.append(queue[front].left)
                rear +=1
            if queue[front].right:
                queue.append(queue[front].right)
                rear +=1
            print(queue[front].value)
            front +=1
            if rear < front:
                break

#at line 11
# System.out.println(input_from_question.toUpperCase());

# # at line 13
# System.out.println(input_from_question.toLowerCase());

    
#                       5
#             4                  6
#         3        3.5                   7
1 2 3 4 5
1 4 3  2 5
1 3 2 5 4

            
root = TreeNode(5, None, None)
t1 = Tree(4)
t1.InsertNode(root, 4)
t1.InsertNode(root, 6)
t1.InsertNode(root, 7)
t1.InsertNode(root, 3)
t1.InsertNode(root, 4.5)

# mastane hazaro hai