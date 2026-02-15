def init_database():
    crew_names = ["Picard", "Riker", "Kirk", "Spock", "Uhura"]
    crew_ranks = ["Commodore", "Captain", "Commander", "Lieutenant","Ensign"]
    crew_divisions = ["Command", "Operations", "Science", "Medical", "Engineering"]
    crew_ids = ["NC1001", "NC1002", "NC1003", "NC1004", "NC1005"]
    
    return crew_names, crew_ranks, crew_divisions, crew_ids


def display_menu(user):
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


def add_member(crew_names, crew_ranks, crew_divisions, crew_ids):
    name = input("Name: ").strip().capitalize()
    rank = input("Rank: ").strip().capitalize()
    division = input("Division: ").strip().capitalize()
    crew_id = input("Crew ID: ").strip().upper()

    if rank not in ["Commodore", "Captain", "Commander", "Lieutenant", "Ensign"]:
        print("Invalid rank. Crew member not added.")
        return
    if division not in ["Command", "Operations", "Science", "Medical", "Engineering"]:
        print("Invalid division. Crew member not added.")
        return
    if name in crew_names:
        print("Crew member already exists. Not added.")
        return
    if crew_id in crew_ids:
        print("Crew ID already exists. Not added.")
        return

    crew_names.append(name)
    crew_ranks.append(rank)
    crew_divisions.append(division)
    crew_ids.append(crew_id)
    print("Crew member added.")

def remove_member(crew_names, crew_ranks, crew_divisions, crew_ids):
    ID = input("ID to remove: ").strip().upper()
    if ID not in crew_ids:
        print("Crew member not found. No changes made.")
        return

    idx = crew_ids.index(ID)
    crew_names.pop(idx)
    crew_ranks.pop(idx)
    crew_divisions.pop(idx)
    crew_ids.pop(idx)
    print("Crew member removed.", remove_member.__name__)


def update_rank(crew_names, crew_ranks, crew_divisions, crew_ids):
    ID = input("ID to update: ").strip().upper()
    if ID not in crew_ids:
        print("Crew member not found. No changes made.")
        return

    idx = crew_ids.index(ID)
    print(f"Current Rank: {crew_ranks[idx]}")
    new_rank = input("New Rank: ").strip().capitalize()
    if new_rank not in ["Commodore", "Captain", "Commander", "Lieutenant", "Ensign"]:
        print("Invalid rank. No changes made.")
        return

    crew_ranks[idx] = new_rank
    print("Crew member rank updated.", update_rank.__name__)