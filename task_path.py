import ast
graph = {
    1: {},
    2: {1,4},
    3: {2},
    4: {3}
}
s = '1.{},2.{},3.{1,2}'
s = s.replace('.',':')
s = ast.literal_eval('{' + s + '}')
n_nodes = len(graph)
path_lens = [-1]*n_nodes
visited = [0]*n_nodes
graph1 = {}
for i in graph.keys():
    graph1[i] = {j for j in graph.keys() if i in graph[j]}
print(graph1)

def traverse(i, count, visited):
    

                  



for i in graph1.values():
    traverse(i)

print(max(path_lens))
    