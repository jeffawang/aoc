from collections import defaultdict

with open("inputs/day12") as f:
    raw = f.read().splitlines()

d = defaultdict(list)

for k, v, in [line.split("-") for line in raw]:
    d[k] += [v]
    d[v] += [k]

def visit(graph, parent, visited):
    if parent == 'end':
        print("===============omg:", visited)
        return 1
    routes = 0
    for child in graph[parent]:
        print(" " * len(visited), child)
        if child == child.lower() and child in visited:
            continue
        routes += visit(graph, child, visited + [child] )
    return routes

count = visit(d, "start", ['start'])
print(count)