# hai:
from linked_adts import *

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbor = LinkedDictionary()  # Use LinkedDictionary instead of a regular dictionary

    def add_neighbor(self, nbr, weight=0):
        """Add a connection to this vertex."""
        self.neighbor.add(nbr, weight)


    def remove_neighbor(self,nbr,):
        """Remove a connection to the given neighbor."""
        if self.neighbor.get_value(nbr):
            self.neighbor.remove(nbr)


            
    def get_connection(self):
        """Return all neighbors (keys in LinkedDictionary)."""
        return self.neighbor.get_keys()

    def get_id(self):
        """Return the ID of this vertex."""
        return self.key

    def get_weight(self, nbr):
        """Return the weight of the edge to the specified neighbor."""
        return self.neighbor.get_value(nbr)

class Undirected_graph:
    def __init__(self):
        self.vertices = LinkedDictionary()
        self.edge_count = 0 # number of friend


    def add_vertex(self, key):
        """
        Adds a new vertex to the graph with the given key.
        If the vertex already exists, it does nothing.
        """
        if not self.vertices.get_value(key):
            # Create a new Vertex object and add it to the vertices dictionary
            new_vertex = Vertex(key)
            self.vertices.add(key, new_vertex)


    def get_vertex(self,key):
        return self.vertices.get_value(key)
    
    def add_edge(self, from_key, to_key, weight=0):
        
        from_vertex=self.get_vertex(from_key)
        to_vertex=self.get_vertex(to_key)
        if(from_vertex and to_vertex):
            from_vertex.add_neighbor(to_key, weight)
            to_vertex.add_neighbor(from_key, weight)
            self.edge_count+=1

    def get_vertices(self):
        return self.vertices.get_keys()

    def contains(self,key):
        if ( self.vertices.get_value(key)):
            return True
        return False

    def clear (self):
        self.vertices = LinkedDictionary()  # Reinitialize the LinkedDictionary
        self.edge_count = 0  # Reset the edge count

    def is_empty(self):
        if (self.vertices.get_keys()):
            return False
        return True

    def size(self):
        return len(self.get_vertices())

    def get_edges(self):
        edges = set()  # Use a set to avoid duplicate edges

        for vertex_key in self.vertices.get_keys():
            vertex = self.get_vertex(vertex_key)  # Retrieve the vertex object

            for neighbor_key in vertex.get_connection():
                weight = vertex.get_weight(neighbor_key)  # Retrieve the weight of the edge
                # Create an edge tuple in sorted order to avoid duplicates
                edge = (min(vertex_key, neighbor_key), max(vertex_key, neighbor_key), weight)
                edges.add(edge)  # Add the edge to the set

        return list(edges)  # Convert the set to a list and return



    def bfs(self,start):
        vertex_queue = LinkedQueue()  # Initialize the queue for BFS
        visited = {key: False for key in self.vertices.get_keys()}  # Use a dictionary to track visited vertices
        result=[]
        visited[start] = True  # Mark the starting vertex as visited
        vertex_queue.enqueue(start)  # Enqueue the starting vertex
        while vertex_queue.is_empty() != True :
            curr_vertex= vertex_queue.dequeue()
            result.append(curr_vertex)
            v=self.get_vertex(curr_vertex)
            neighbors=v.get_connection()
            for i in neighbors:
                if visited[i] ==False:
                    visited[i]=True
                    vertex_queue.enqueue(i)
        return result



    def dfs(self,start):
        stack=[]
        visited = {key: False for key in self.vertices.get_keys()}
        result=[]
        stack.append(start)# Add the starting vertex to the stack
        while (len(stack)):
            curr_vertex=stack.pop()# Pop the top vertex from the stack 
            if not visited[curr_vertex]: #If it hasn't been visited 
                visited[curr_vertex]= True# mark it visited
                result.append(curr_vertex) # add it to the result
                #push univisted vertex into stack
                neighbors = self.get_vertex(curr_vertex).get_connection()
                for neighbor in neighbors:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return result