from collections import deque, defaultdict


def read_graph(filename):
    graph = defaultdict(list)
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        root = int(lines[0])
        lines = lines[1:]
        for line in lines:
            if line:
                parts = line.split(",")
                node = int(parts[0])
                neighbor = int(parts[1])
                graph[node].append(neighbor)

    return root, graph


def find_min_depth(root, graph):
    if root is None:
        return 0

    visited = set()
    queue = deque([(root, 1)])

    while queue:
        node, depth = queue.popleft()
        visited.add(node)

        if node not in graph:
            return depth

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))

    return 0


root, graph = read_graph("input.txt")


min_depth = find_min_depth(root, graph)

with open("output.txt", "w") as file:
    file.write(str(min_depth))
