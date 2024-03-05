class GraphBidirectionalBFS:
    def __init__(self, graph):
        self.graph = graph

    def add_edge(self, u, v):
        self.graph.add_edge(u, v)

    def bidirectional_search(self, start, goal):
        forward_visited = set()
        backward_visited = set()
        forward_queue = [start]
        backward_queue = [goal]
        forward_visited.add(start)
        backward_visited.add(goal)
        forward_path_dict = {start: None}
        backward_path_dict = {goal: None}

        while forward_queue and backward_queue:
            forward_vertex = forward_queue.pop(0)
            backward_vertex = backward_queue.pop(0)

            if forward_vertex in backward_visited:
                # Intersection point found
                intersection = forward_vertex
                forward_path = self.reconstruct_path(forward_path_dict, intersection)
                backward_path = self.reconstruct_path(backward_path_dict, intersection)[::-1]
                return forward_path + backward_path

            for neighbor in self.get_neighbors(forward_vertex):
                if neighbor not in forward_visited:
                    forward_visited.add(neighbor)
                    forward_queue.append(neighbor)
                    forward_path_dict[neighbor] = forward_vertex

            for neighbor in self.get_neighbors(backward_vertex):
                if neighbor not in backward_visited:
                    backward_visited.add(neighbor)
                    backward_queue.append(neighbor)
                    backward_path_dict[neighbor] = backward_vertex

        return []  # If no path is found

    def reconstruct_path(self, path_dict, intersection):
        path = [intersection]
        while path_dict[intersection] is not None:
            intersection = path_dict[intersection]
            path.insert(0, intersection)
        return path

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            return {}
