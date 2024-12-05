class UserProfile:
    def __init__(self, name, location, relationship_status, age, occupation, astrological_sign, status=""):
        self.name=name
        self.location=location
        self.relationship_status= relationship_status
        self.age=age
        self.occupation=occupation
        self.astrological_sign=astrological_sign
        self.status=status

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
        pass

    def add_friend(self, friend_profile):
        pass

    def remove_friend(self,friend_profile):
        pass

    def print_details(self):
        pass
