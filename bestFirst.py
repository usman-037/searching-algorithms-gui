class Graph_bestfs:
    def __init__(self, directed):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = set()
        if node2 not in self.graph:
            self.graph[node2] = set()

        self.graph[node1].add(node2)

        if not self.directed:
            self.graph[node2].add(node1)

    def best_first_search(self, start, goals):
        explored = set()
        queue = [(0, start)]

        while queue:
            queue.sort()
            _, current_node = queue.pop(0)

            if current_node in goals:
                return self.trace_path(start, current_node)

            if current_node not in explored:
                explored.add(current_node)

                if current_node in self.graph:
                    neighbors = self.graph[current_node]

                    for neighbor in neighbors:
                        if neighbor not in explored:
                            queue.append((0, neighbor))

        return None, None

    def trace_path(self, start, goal):
        path = [goal]
        current_node = goal

        while current_node != start:
            for node in self.graph[current_node]:
                if node in self.graph and current_node in self.graph[node]:
                    path.insert(0, node)
                    current_node = node
                    break

        return path, goal

    def print_path(self, path, goal):
        print(" -> ".join(path), end="")
        print(f" (Goal: {goal})")
