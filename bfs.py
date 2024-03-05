from collections import deque

class Graph_bfs:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, source, destination):
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]
        if not self.directed:
            if destination in self.graph:
                self.graph[destination].append(source)
            else:
                self.graph[destination] = [source]

    def breadth_first_search(self, start, goals):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            node, path = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node in goals:
                return path, node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None, None

    @staticmethod
    def print_path(traced_path, goal):
        print(traced_path)
        print(f'Goal node: {goal}')
