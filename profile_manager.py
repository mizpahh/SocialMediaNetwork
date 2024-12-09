# mizpah:
# from graph_adt import *
# class ProfileManager:
#     def __init__(self):
#         self.graph = Undirected_graph()# The graph to store profiles
#     def add_profile(self,name, location, relationshiop_status, age, occupation, astrological_sign, status=""):
#         # Check if the profile already exists in the graph
#         #U should you contain function for this
        



#         #Create a new userProfile and add to the graph
#         #Add the profile name as a vertex in the graph (add_vertex)
#         #Attach the UserProfile object to the vertex (get_vertex)
#         pass
    
#     def get_profile(self,name):
#         #check is that name contain in graph 
#         #if yes return it
#         pass

#     def remove_profile(self,name):
#         #check is the name contain in graph
#         #if yes remove it from all connected profiles (I add remove_neighbor in class vertex already)
#         pass

#     def connect_profile(self, name1, name2, weight=0):
#         # check if 2 namw are in graph
#         # then use add_edge
#         pass
    
#     def display_profiles(self):
#         #
#         pass
    
#     def display_profile_details(self, name):
#         pass
    
#     def get_friends_of_friends(self, name):
#         #check if name in graph
#         #then use get_vertex and get_connection to get friend
#         # use set to store friends of friends to not let duplicate
#         #use get_vertex and get_connection to get friends of friend again 
#         #then add into the set
#         # return list set after completed
#         pass
    
#     def read_profiles_from_csv(self, file_path):
#         pass
    
#     def create_user_graph(self, current_user,depth = 1):
#         pass

from graph_adt import *
from user_profile import *
class ProfileManager:
    def __init__(self):
        self.graph = Undirected_graph()  # The graph to store profiles

    def add_profile(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        # Check if the profile already exists in the graph
        if self.graph.contains(name):
            print(f"Profile for {name} already exists.")
            return

        # Create a new UserProfile and add it to the graph
        new_profile = UserProfile(name, location, relationship_status, age, occupation, astrological_sign, status)
        self.graph.add_vertex(name)
        self.graph.get_vertex(name).data = new_profile
        print(f"Profile for {name} added successfully.")

    def get_profile(self, name):
        # Check if the name exists in the graph
        if self.graph.contains(name):
            return self.graph.get_vertex(name).data
        print(f"Profile for {name} not found.")
        return None

    def remove_profile(self, name):
        # Check if the name exists in the graph
        if not self.graph.contains(name):
            print(f"Profile for {name} does not exist.")
            return

        # Remove the profile from all connected profiles
        for neighbor in self.graph.get_vertex(name).get_connections():
            neighbor.remove_neighbor(name)

        # Remove the vertex from the graph
        self.graph.remove_vertex(name)
        print(f"Profile for {name} removed successfully.")

    def connect_profile(self, name1, name2, weight=0):
        # Check if both names exist in the graph
        if not (self.graph.contains(name1) and self.graph.contains(name2)):
            print("One or both profiles do not exist.")
            return

        # Use add_edge to connect the profiles
        self.graph.add_edge(name1, name2, weight)
        print(f"{name1} and {name2} are now connected.")

    def display_profiles(self):
        # Display all profile names in the graph
        for vertex in self.graph.get_vertices():
            print(vertex)

    def display_profile_details(self, name):
        # Display the details of a specific profile
        profile = self.get_profile(name)
        if profile:
            profile.print_details()

    def get_friends_of_friends(self, name):
        # Check if the name exists in the graph
        if not self.graph.contains(name):
            print(f"Profile for {name} not found.")
            return []

        # Get direct friends
        direct_friends = self.graph.get_vertex(name).get_connections()
        friends_of_friends = set()

        # Get friends of friends
        for friend in direct_friends:
            friend_vertex=self.graph.get_vertex(friend)
            if friend_vertex:
                fof_connections = friend_vertex.get_connections()
                friends_of_friends.update(fof_connections)

        # Exclude the original user and direct friends
        friends_of_friends.discard(name)
        friends_of_friends -= set(direct_friends)

        return list(friends_of_friends)

    def read_profiles_from_csv(self, file_path):
        import csv
        try:
            with open(file_path, "r") as csv_file:
                reader = csv.DictReader(csv_file)
                
                # First, add all profiles to the graph
                for row in reader:
                    self.add_profile(
                        name=row["name"],
                        location=row["location"],
                        relationship_status=row["relationship_status"],
                        age=int(row["age"]),
                        occupation=row["occupation"],
                        astrological_sign=row["astrological_sign"],
                        status=row.get("status", "")
                    )

                # Reset file pointer to re-read for connections
                csv_file.seek(0)
                next(reader)  # Skip the header row

                # Then, add connections
                for row in reader:
                    if "friends" in row and row["friends"]:
                        for friend in row["friends"].split("|"):  # Use "|" as delimiter
                            self.connect_profile(row["name"], friend.strip())

                print("Profiles loaded successfully from CSV.")
        except Exception as e:
            print(f"Error reading profiles from CSV: {e}")

    def create_user_graph(self, current_user, depth=1):
        import graphviz

        if not self.graph.contains(current_user):
            print(f"Profile for {current_user} not found.")
            return

        graph = graphviz.Graph(format="png")
        visited = set()
        queue = LinkedQueue()

        queue.enqueue((current_user, 0))
        visited.add(current_user)

        while not queue.is_empty():
            user, current_depth = queue.dequeue()
            if current_depth < depth:
                connections = self.graph.get_vertex(user).get_connections()
                for connection in connections:
                    if connection not in visited:
                        visited.add(connection)
                        queue.enqueue((connection, current_depth + 1))

                    graph.edge(user, connection)

        output_path = graph.render(filename="user_network")
        print(f"Graph saved to {output_path}.")

