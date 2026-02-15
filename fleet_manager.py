def init_database():
    crew_names = ["Garrovick", "Kirk", "Spock", "Uhura", "Keenser"]
    crew_ranks = ["Commodore", "Captain", "Commander", "Lieutenant","Ensign"]
    crew_divisions = ["Command", "Science", "Engineering", "Operations", "Medical"]
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

def display_roster(crew_names, crew_ranks, crew_divisions, crew_ids):
    print("\nCurrent Crew Roster:")
    if len(crew_names) == 0:
        print("No crew members found.")
        return
    for i in range(len(crew_names)):
        print(f"{crew_names[i]} - {crew_ranks[i]} - {crew_divisions[i]} - {crew_ids[i]}")


def search_crew(crew_names, crew_ranks, crew_divisions, crew_ids):
    keyword = input("Keyword to search: ").strip().capitalize()
    if keyword not in crew_names:
        print("Crew member not found.")
        return

    idx = crew_names.index(keyword)
    print(f"Name: {crew_names[idx]}")
    print(f"Rank: {crew_ranks[idx]}")
    print(f"Division: {crew_divisions[idx]}")
    print(f"Crew ID: {crew_ids[idx]}")

def filter_by_division(crew_names, crew_ranks, crew_divisions, crew_ids):
    division = input("Division to filter by: ").strip().capitalize()
    if division not in ["Command", "Operations", "Science", "Medical", "Engineering"]:
        print("Invalid division.")
        return

    print(f"\nCrew members in {division} Division:")
    found = False
    for i in range(len(crew_names)):
        if crew_divisions[i] == division:
            print(f"{crew_names[i]} - {crew_ranks[i]} - {crew_ids[i]}")
            found = True
    if not found:
        print("No crew members found in this division.")

def calculate_payroll(crew_names, crew_ranks, crew_divisions, crew_ids):
    rank_salaries = {
        "Commodore": 1000,
        "Captain": 900,
        "Commander": 800,
        "Lieutenant": 700,
        "Ensign": 600
    }
    total_payroll = 0
    for rank in crew_ranks:
        total_payroll += rank_salaries.get(rank, 0)
    print(f"Total Payroll: ${total_payroll}")

def count_officers(crew_ranks):
    high_ranking = ["Commodore", "Captain", "Commander"]
    count = sum(1 for rank in crew_ranks if rank in high_ranking)
    print(f"High ranking officers: {count}")

def main():
    crew_names, crew_ranks, crew_divisions, crew_ids = init_database()
    user = input("Enter your name: ").strip().capitalize()

    while True:
        option = display_menu(user)

        if option == "1":
            display_roster(crew_names, crew_ranks, crew_divisions, crew_ids)
        elif option == "2":
            add_member(crew_names, crew_ranks, crew_divisions, crew_ids)
        elif option == "3":
            remove_member(crew_names, crew_ranks, crew_divisions, crew_ids)
        elif option == "4":
            count_officers(crew_ranks)
        elif option == "5":
            print("Exiting Fleet Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()