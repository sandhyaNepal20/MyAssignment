
# b) Assume you were hired to create an application for an ISP, and there are n network devices, such as routers,
# that are linked together to provide internet access to users. You are given a 2D array that represents network
# connections between these network devices. write an algorithm to return impacted network devices, If there is
# a power outage on a certain device, these impacted device list assist you notify linked consumers that there is a
# power outage and it will take some time to rectify an issue.
# Input: edges= {{0,1},{0,2},{1,3},{1,6},{2,4},{4,6},{4,5},{5,7}}
# Target Device (On which power Failure occurred): 4
# Output (Impacted Device List) = {5,7}




from collections import defaultdict

def find_nodes_with_only_target_as_parent(edges, target):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        in_degree[to_node] += 1

    result = []
    dfs(graph, in_degree, target, target, result)
    return result

def dfs(graph, in_degree, node, target, result):
    if in_degree.get(node, 0) == 1 and node != target:
        result.append(node)

    for child in graph.get(node, []):
        dfs(graph, in_degree, child, target, result)

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 6), (2, 4), (4, 6), (4, 5), (5, 7)]
    target = 4
    unique_parents = find_nodes_with_only_target_as_parent(edges, target)
    print(f"Nodes whose only parent is {target}: {{", end="")
    print(", ".join(map(str, unique_parents)), end="")
    print("}")


