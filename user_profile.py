class UserProfile:
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        self.name=name
        self.location=location
        self.relationship_status= relationship_status
        self.age=age
        self.occupation=occupation
        self.astrological_sign=astrological_sign
        self.status=status
        self.friends = []

    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location

    def get_age(self):
        return self.age
    
    def get_occupation(self):
        return self.occupation
    
    def get_astrological_sign(self):
        return self.astrological_sign
    
    def get_status(self):
        return self.status
    
    def set_status(self,status):
        self.status=status

    def get_friends(self):
        return self.friends

    def add_friend(self, friend_profile):
        if friend_profile not in self.friends:
            self.friends.append(friend_profile)
        else:
            print("This user is already your friend")

    def remove_friend(self,friend_profile):
        if friend_profile in self.friends:
            self.friends.remove(friend_profile)
        else:
            print("This user is not your friend, can not be removed")
    
    
    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Relationship Status: {self.relationship_status}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")
        print(f"Astrological Sign: {self.astrological_sign}")
        print(f"Status: {self.status}")
        print(f"Friends: {[friend.name for friend in self.friends]}")
