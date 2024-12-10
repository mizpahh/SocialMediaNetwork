# Mizpah:
# Import necessary modules
from graph_adt import * 
from user_profile import * 

class ProfileManager:
    def __init__(self):
        # Initialize an undirected graph to store user profiles
        self.graph = Undirected_graph()

    def add_profile(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        """
        Adds a new profile to the graph if it doesn't already exist.
        Each profile is stored as a vertex in the graph.
        """
        # Check if a profile with the same name already exists
        if self.graph.contains(name):
            print(f"Profile for {name} already exists.")
            return

        # Create a new UserProfile object and add it as a vertex
        new_profile = UserProfile(name, location, relationship_status, age, occupation, astrological_sign, status)
        self.graph.add_vertex(name)  # Add a vertex for the profile name
        self.graph.get_vertex(name).data = new_profile  # Attach profile data to the vertex
        print(f"Profile for {name} added successfully.")

    def get_profile(self, name):
        """
        Retrieves the profile data for a given name.
        Returns the UserProfile object if it exists, otherwise None.
        """
        if self.graph.contains(name):
            return self.graph.get_vertex(name).data
        print(f"Profile for {name} not found.")
        return None

    def remove_profile(self, name):
        """
        Removes a profile from the graph and all its connections.
        """
        # Check if the profile exists
        if not self.graph.contains(name):
            print(f"Profile for {name} does not exist.")
            return

        # Remove connections to the profile
        for neighbor in self.graph.get_vertex(name).get_connections():
            neighbor.remove_neighbor(name)

        # Remove the profile vertex from the graph
        self.graph.remove_vertex(name)
        print(f"Profile for {name} removed successfully.")

    def connect_profile(self, name1, name2, weight=0):
        """
        Connects two profiles in the graph by creating an edge between them.
        """
        # Ensure both profiles exist
        if not (self.graph.contains(name1) and self.graph.contains(name2)):
            print("One or both profiles do not exist.")
            return

        # Add an edge between the two profiles
        self.graph.add_edge(name1, name2, weight)
        print(f"{name1} and {name2} are now connected.")

    def display_profiles(self):
        """
        Displays all profile names stored in the graph.
        """
        for vertex in self.graph.get_vertices():
            print(vertex)

    def display_profile_details(self, name):
        """
        Displays the details of a specific profile.
        """
        profile = self.get_profile(name)
        if profile:
            profile.print_details()

    def get_friends_of_friends(self, name):
        """
        Retrieves a list of friends of friends (2nd-degree connections) for a given profile.
        """
        # Check if the profile exists
        if not self.graph.contains(name):
            print(f"Profile for {name} not found.")
            return []

        # Retrieve direct friends
        direct_friends = self.graph.get_vertex(name).get_connections()
        friends_of_friends = set()

        # Collect friends of friends
        for friend in direct_friends:
            friend_vertex = self.graph.get_vertex(friend)
            if friend_vertex:
                fof_connections = friend_vertex.get_connections()
                friends_of_friends.update(fof_connections)

        # Remove the original profile and its direct friends from the list
        friends_of_friends.discard(name)
        friends_of_friends -= set(direct_friends)

        return list(friends_of_friends)

    def read_profiles_from_csv(self, file_path):
        """
        Reads profile data and connections from a CSV file and populates the graph.
        """
        import csv
        try:
            with open(file_path, "r") as csv_file:
                reader = csv.DictReader(csv_file)

                # First pass: Add all profiles
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

                # Second pass: Add connections between profiles
                for row in reader:
                    if "friends" in row and row["friends"]:
                        for friend in row["friends"].split("|"):  # Use "|" as delimiter for friends
                            self.connect_profile(row["name"], friend.strip())

                print("Profiles loaded successfully from CSV.")
        except Exception as e:
            print(f"Error reading profiles from CSV: {e}")

    def create_user_graph(self, current_user, depth=1):
        """
        Creates and visualizes a graph of a user's network up to a specified depth.
        """
        import graphviz

        # Check if the user's profile exists
        if not self.graph.contains(current_user):
            print(f"Profile for {current_user} not found.")
            return

        graph = graphviz.Graph(format="png")  # Initialize a graphviz graph
        visited = set()  # Track visited profiles
        queue = LinkedQueue()  # Initialize a queue for breadth-first traversal

        queue.enqueue((current_user, 0))  # Enqueue the starting profile with depth 0
        visited.add(current_user)

        while not queue.is_empty():
            user, current_depth = queue.dequeue()
            if current_depth < depth:  # Limit traversal depth
                connections = self.graph.get_vertex(user).get_connections()
                for connection in connections:
                    if connection not in visited:  # Avoid revisiting profiles
                        visited.add(connection)
                        queue.enqueue((connection, current_depth + 1))

                    # Add an edge to the graph
                    graph.edge(user, connection)

        # Render and save the graph visualization
        output_path = graph.render(filename="user_network")
        print(f"Graph saved to {output_path}.")
