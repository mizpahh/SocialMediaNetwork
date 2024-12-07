from linked_adts import LinkedQueue

class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = {}     # Dictionary to store neighboring verticies & weight

    def add_neighbor(self, nbr, weight = 0):
        self.neighbors[nbr] = weight

    def get_connection(self):
        return self.neighbors.keys()

    def get_id(self):
        return self.key

    def get_weight(self, nbr):
        self.connections.get(nbr, None)

class Undirected_graph:
    def __init__(self):
        self.verticies = {}     # Dictionary to store verticies and their keys

    def add_vertex(self,key):
        #self.key=key
        if key not in self.verticies:
            self.verticies[key] = Vertex(key)

    def get_vertex(self,key):
        return self.verticies.get(key, None)
    
    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(from_key)
        if to_key not in self.verticies:
            self.add_vertex(to_key)
        self.vertitcies[from_key].add_neighbor(self.verticies[to_key], weight)
        self.vertitcies[to_key].add_neighbor(self.verticies[from_key], weight)

    def get_vertices(self):
        return list(self.verticies.keys())

    def contains(self,key):
        return key in self.verticies

    def clear (self):
        self.verticies.clear()

    def is_empty(self):
        return len(self.verticies) == 0

    def size(self):
        return len(self.verticies)

    def get_edges(self):
        edges = []
        for vertex in self.verticies.values():
            for neighbor in vertex.get_connections():
                if (neighbor.get_id(), vertex.get_id()) not in edges:       # <- make sure that edges are not duplicated
                    edges.append((vertex.get_id(), neighbor.get_id()))
        return edges

    def bfs(self,start):
        if start not in self.verticies:
            return[]
        
        visited = []        # list for visited vertecies
        queue = LinkedQueue()       # queue for BFS traversal
        queue.enqueue(start)

        while not queue.is_empty():
            current_key = queue.dequeue()
            if current_key not in visited:
                visited.append(current_key)
                current_vertex = self.get_vertex(current_key)
                for neighbor in current_vertex.get_connections():
                    if neighbor.get_id() not in visited:
                        queue.enqueue(neighbor.get_id())
        return visited

    def dfs(self,start):
        if start not in self.verticies:
            return []
        
        visited = []        # same thing, visited vertecies
        stack = [start]     # stack for DFS traversal

        while stack: 
            current_key = stack.pop()
            if current_key not in visited:
                visited.append(current_key)
                current_vertex = self.get_vertex(current_key)
                for neighbor in current_vertex.get_connections():
                    if neighbor.get_id() not in visited:
                        stack.append(neighbor.get_id())

        return visited
    