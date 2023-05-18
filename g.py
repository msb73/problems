import grap
ls = {'A': {'B'},
 'B': {'D', 'A', 'C'},
 'C': {'D', 'B', 'F'},
 'D': {'C', 'F'},
 'E': {'F'},
 'F': {'E', 'C'}}

class Node():
    def __init__(self, val, prev, l_node ) -> None:
        self.val = val
        self.prev = prev
        self.node = []
t = Node('A', None, None)
que = []    # A -> [B]
que.append(t)
# for _ in range(len(ls)-1):
#     for i in ls[que[num].val]:
for obj in que:
    for ele in ls[obj.val]: 
        if ele not in (i.val for i in que):
            temp_node = Node(ele, obj, None)
            que.append(temp_node)
            obj.node.append(temp_node)
            if ele == 'F':
                print('F')
                n = obj
                while n.prev:
                    print(n.val)
                    n = n.prev
                exit()
    else: continue
    break
    
            # if i == 'E':
            #     print('E')
            #     n = que[num]
            #     while n.prev:
            #         print(n.val)
            #         n = n.prev
            #     exit()
                
    


