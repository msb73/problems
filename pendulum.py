import ast
graph = {
    1: {},
    2: {1,4},
    3: {2},
    4: {3}
}
s = '1.{},2.{},3.{1,2}'
s = s.replace('.',':')
graph = ast.literal_eval('{' + s + '}')
n_nodes = len(graph)
path_lens = [-1]*n_nodes
visited = [0]*n_nodes
graph1 = {}
for i in graph.keys():
    graph1[i] = {j for j in graph.keys() if i in graph[j]}
print(graph1)
def find_path_len(_node):
    if visited[_node]==0:
        visited[_node] = 1
    else:
        print("error")
        quit()
    if path_lens[_node] != -1:
        return path_lens[_node]
    if graph[_node+1] == {}:
        path_lens[_node] = 0
        return 0
    else:
        dists = []
        for _pred in graph[_node+1]:
            dists.append(find_path_len(_pred-1) + 1)
        path_lens[_node] = max(dists)
        return path_lens[_node]
        
for _node in range(n_nodes):
    visited = [0]*n_nodes
    find_path_len(_node)

print(max(path_lens))
    