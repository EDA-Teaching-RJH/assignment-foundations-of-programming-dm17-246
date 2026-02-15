def init_crew():
    crew_names = ["Picard", "Riker", "Kirk", "Spock", "Uhura"]
    crew_ranks = ["Commodore", "Captain", "Commander", "Lieutenant","Ensign"]
    crew_divisions = ["Command", "Operations", "Science", "Medical", "Engineering"]
    crew_ids = ["NC1001", "NC1002", "NC1003", "NC1004", "NC1005"]
    
    return crew_names, crew_ranks, crew_divisions, crew_ids


def display_crew(user):
    print("\n==============================")
    print("     FLEET MANAGEMENT SYSTEM")
    print("==============================")
    print(f"Welcome, {user}!\n")
    print("1 - View Crew")
    print("2 - Add Crew Member")
    print("3 - Remove Crew Member")
    print("4 - Analyze Crew Data")
    print("5 - Exit")
          

    option = input("Select option: ").strip()
    return option

