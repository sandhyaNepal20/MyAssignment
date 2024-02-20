
# b) Assume you were hired to create an application for an ISP, and there are n network devices, such as routers,
# that are linked together to provide internet access to users. You are given a 2D array that represents network
# connections between these network devices. write an algorithm to return impacted network devices, If there is
# a power outage on a certain device, these impacted device list assist you notify linked consumers that there is a
# power outage and it will take some time to rectify an issue.
# Input: edges= {{0,1},{0,2},{1,3},{1,6},{2,4},{4,6},{4,5},{5,7}}
# Target Device (On which power Failure occurred): 4
# Output (Impacted Device List) = {5,7}




from collections import deque,defaultdict

def get_impacted_devices(edges, target_device):
    graph = defaultdict(list)
    visited = set()
    impacted_devices = []

    # Build the adjacency list representation of the network connections
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS to find impacted devices
    queue = deque([target_device])
    visited.add(target_device)

    while queue:
        current_device = queue.popleft()

        # Traverse all connected devices
        for neighbor in graph.get(current_device, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                impacted_devices.append(neighbor)

    return impacted_devices

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 6), (2, 4), (4, 6), (4, 5), (5, 7)]
    target_device = 4
    impacted_devices = get_impacted_devices(edges, target_device)
    impacted_devices.sort()
    print("Impacted Device List:", impacted_devices)  # Output: [5, 7]from collections import deque, defaultdict

def get_impacted_devices(edges, target_device):
    graph = defaultdict(list)
    visited = set()
    impacted_devices = set()

    # Build the adjacency list representation of the network connections
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS to find impacted devices
    queue = deque([target_device])
    visited.add(target_device)

    while queue:
        current_device = queue.popleft()

        # Traverse all connected devices
        for neighbor in graph.get(current_device, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                impacted_devices.add(neighbor)

    return impacted_devices

if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (1, 6), (2, 4), (4, 6), (4, 5), (5, 7)]
    target_device = 4
    impacted_devices = get_impacted_devices(edges, target_device)
    impacted_devices = sorted(list(impacted_devices))
    print("Impacted Device List:", impacted_devices)  # Output: [5, 7]
