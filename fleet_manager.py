# fleet_manager.py
# Part B - Modular version

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["001", "002", "003", "004", "005"]

    return names, ranks, divisions, ids

def display_menu(current_user):
    print("\n--- FLEET MANAGER ---")
    print("Logged in as:", current_user)
    print("1. Display Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    choice = input("Select option: ").strip()
    return choice

def add_member(names, ranks, divisions, ids):
    new_id = input("Enter ID: ").strip()

    if new_id in ids:
        print("ID already exists.")
        return

    new_name = input("Enter full name: ").strip()
    new_rank = input("Enter rank: ").strip()

    valid_ranks = ["Captain", "Commander", "Lt. Commander",
                   "Lieutenant", "Ensign"]

    if new_rank not in valid_ranks:
        print("Invalid rank.")
        return

    new_div = input("Enter division: ").strip()

    valid_divisions = ["Command", "Operations", "Security", "Sciences"]

    if new_div not in valid_divisions:
        print("Invalid division.")
        return

    names.append(new_name)
    ranks.append(new_rank)
    divisions.append(new_div)
    ids.append(new_id)

    print("Crew member added.")

def display_roster(names, ranks, divisions, ids):
    print("\n=== CREW ROSTER ===")
    print(f"{'ID':<6} {'NAME':<15} {'RANK':<13} {'DIVISION':<10}")
    print("-" * 50)

    for i in range(len(names)):
        print(f"{ids[i]:<6} {names[i]:<15} {ranks[i]:<13} {divisions[i]:<10}")

def remove_member(names, ranks, divisions, ids):
    target_id = input("Enter ID to remove: ").strip()

    if target_id not in ids:
        print("ID not found.")
        return

    index = ids.index(target_id)

    names.pop(index)
    ranks.pop(index)
    divisions.pop(index)
    ids.pop(index)

    print("Crew member removed.")

def update_rank(names, ranks, ids):
    target_id = input("Enter ID to update: ").strip()

    if target_id not in ids:
        print("ID not found.")
        return

    index = ids.index(target_id)
    print("Current:", names[index], "-", ranks[index])

    new_rank = input("Enter new rank: ").strip()

    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    if new_rank not in valid_ranks:
        print("Invalid rank.")
        return

    ranks[index] = new_rank
    print("Rank updated.")

def search_crew(names, ranks, divisions, ids):
    term = input("Search name: ").strip().lower()
    found = False

    for i in range(len(names)):
        if term in names[i].lower():
            print(ids[i], "-", names[i], "-", ranks[i], "-", divisions[i])
            found = True

    if not found:
        print("No matches.")

def filter_by_division(names, divisions):
    div = input("Division (Command/Operations/Security/Sciences): ").strip()

    if div not in ["Command", "Operations", "Security", "Sciences"]:
        print("Invalid division.")
        return

    found = False
    for i in range(len(names)):
        if divisions[i] == div:
            print(names[i], "-", divisions[i])
            found = True

    if not found:
        print("No crew in that division.")

def calculate_payroll(ranks):
    total = 0

    for rank in ranks:
        if rank == "Captain":
            total += 1000
        elif rank == "Commander":
            total += 800
        elif rank == "Lt. Commander":
            total += 600
        elif rank == "Lieutenant":
            total += 400
        elif rank == "Ensign":
            total += 200
        else:
            total += 300  # default for unknown ranks

    print("Total payroll cost:", total)

def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1

    print("Captain/Commander count:", count)

def main():
    names, ranks, divisions, ids = init_database()
    current_user = input("Enter your full name: ").strip()

    while True:
        choice = display_menu(current_user)

        if choice == "1":
            display_roster(names, ranks, divisions, ids)
        elif choice == "2":
            add_member(names, ranks, divisions, ids)
        elif choice == "3":
            remove_member(names, ranks, divisions, ids)  
        elif choice == "4":
            update_rank(names, ranks, ids)      
        elif choice == "5":
            search_crew(names, ranks, divisions, ids)
        elif choice == "6":
            filter_by_division(names, divisions)
        elif choice == "7":
            calculate_payroll(ranks)
        elif choice == "8":
            count_officers(ranks)
        elif choice == "9":
            print("Exiting system.")
            break
       
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
