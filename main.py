from profile_manager import *
from graph_adt import *
from linked_adts import *
from user_profile import *

def main():
    manager = ProfileManager()
    
    while True:
        print("\nMenu:")
        print("1. Add Profile")
        print("2. Display Profiles")
        print("3. Connect Profiles")
        print("4. Remove Profile")
        print("5. View Profile Details")
        print("6. Friends of Friends")
        print("7. Read Profiles from CSV")
        print("8. Create User Graph")
        print("9. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            location = input("Enter location: ")
            relationship_status = input("Enter relationship status: ")
            age = int(input("Enter age: "))
            occupation = input("Enter occupation: ")
            astrological_sign = input("Enter astrological sign: ")
            status = input("Enter status (optional): ")
            manager.add_profile(name, location, relationship_status, age, occupation, astrological_sign, status)
        
        elif choice == "2":
            manager.display_profiles()
        
        elif choice == "3":
            name1 = input("Enter the first profile name: ")
            name2 = input("Enter the second profile name: ")
            manager.connect_profile(name1, name2)
        
        elif choice == "4":
            name = input("Enter name of the profile to remove: ")
            manager.remove_profile(name)
        
        elif choice == "5":
            name = input("Enter name of the profile to view: ")
            manager.display_profile_details(name)
        
        elif choice == "6":
            name = input("Enter name of the profile: ")
            friends_of_friends = manager.get_friends_of_friends(name)
            print(f"Friends of friends for {name}: {', '.join(friends_of_friends)}")
        
        elif choice == "7":
            file_path = input("Enter path to CSV file: ")
            manager.read_profiles_from_csv(file_path)
        
        elif choice == "8":
            current_user = input("Enter the current user's name: ")
            depth = int(input("Enter depth for the graph: "))
            manager.create_user_graph(current_user, depth)
        
        elif choice == "9":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
