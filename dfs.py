class Graph_dfs:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if not self.directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def depth_first_search(self, start, goals):
        visited = set()
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex in goals:
                    return path, vertex
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None, None

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path), end=' ')
        print('\nGoal: %s' % goal)
