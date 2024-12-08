from graph_adt import *
class ProfileManager:
    def __init__(self):
        self.graph = Undirected_graph()# The graph to store profiles
    def add_profile(self,name, location, relationshiop_status, age, occupation, astrological_sign, status=""):
        # Check if the profile already exists in the graph
        #U should you contain function for this



        #Create a new userProfile and add to the graph
        #Add the profile name as a vertex in the graph (add_vertex)
        #Attach the UserProfile object to the vertex (get_vertex)
        pass
    
    def get_profile(self,name):
        #check is that name contain in graph 
        #if yes return it
        pass

    def remove_profile(self,name):
        #check is the name contain in graph
        #if yes remove it from all connected profiles (I add remove_neighbor in class vertex already)
        pass

    def connect_profile(self, name1, name2, weight=0):
        # check if 2 namw are in graph
        # then use add_edge
        pass
    
    def display_profiles(self):
        #
        pass
    
    def display_profile_details(self, name):
        pass
    
    def get_friends_of_friends(self, name):
        #check if name in graph
        #then use get_vertex and get_connection to get friend
        # use set to store friends of friends to not let duplicate
        #use get_vertex and get_connection to get friends of friend again 
        #then add into the set
        # return list set after completed
        pass
    
    def read_profiles_from_csv(self, file_path):
        pass
    
    def create_user_graph(self, current_user,depth = 1):
        pass
