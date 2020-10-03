n, m = map(int, input().split())
adj_list = {}
visited = [0] * (n + 1)
in_time = [0] * (n + 1)  # entry time for each node
low_time = [0] * (n + 1)  # lowest ancestor time
timer = 0


def dfs_recursive(node, parent):
    global timer

    visited[node] = 1
    if node not in adj_list:
        adj_list[node] = []

    timer += 1
    in_time[node] = timer
    low_time[node] = timer
    children = 0  # to keep track of children/subtrees of our root node

    for child in adj_list[node]:

        if child == parent:
            continue

        if visited[child]:
            low_time[node] = min(low_time[node], in_time[child])

        if visited[child] == 0:

            dfs_recursive(child, node)

            low_time[node] = min(low_time[node], low_time[child])

            # for edge node--->child, if child has a lower ancestor than its parent, that is: it is connected to the ancestor of
            # its parent node then even if remove the parent node the child node and the ancestor will still remain connected
            # that means the complete graph will remain intact and hence the parent in this case cannot be an articulation point

            if (low_time[child] >= in_time[node]) and parent != -1:
                print(f"This graph has an articulation point which is  {node}")

            # the children will keep tarck of the subtrees of root node if it is greater than 1 that means
            # that the root has more than 1 subtrees and that it can br an articulation point the child will be increased by
            # 1 after traversing one subtree first then the next subtree and so on

            children += 1

    if parent == -1 and children > 1:
        print(
            f"The root node of this graph is also an articulation point, the root is {node}"
        )


for _ in range(m):
    u, v = map(int, input().split())
    if u in adj_list:
        adj_list[u].append(v)
    if v in adj_list:
        adj_list[v].append(u)
    if u not in adj_list:
        adj_list[u] = [v]
    if v not in adj_list:
        adj_list[v] = [u]

for i in range(1, n + 1):
    if visited[i] == 0:
        # the main root node has no parent hence passing -1
        dfs_recursive(i, -1)

# print("in time", in_time)
# print("low time", low_time)
# print("visited", visited)
