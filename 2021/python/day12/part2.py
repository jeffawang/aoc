from collections import defaultdict

with open("inputs/day12") as f:
    raw = f.read().splitlines()

d = defaultdict(list)

for k, v, in [line.split("-") for line in raw]:
    d[k] += [v]
    d[v] += [k]

for k in d:
    d[k] = list(set(d[k]))

def visit(graph, parent, visited, part1=False):
    if parent == 'end':
        return 1
    routes = 0
    for child in graph[parent]:
        a = dict(visited)
        if child == child.lower():
            if child == 'start' or part1 and child in visited:
                continue
            a[child] = a.get(child, 0) + 1
        routes += visit(graph, child, a, part1 or child in visited)
    return routes

count = visit(d, "start", {})
print(count)