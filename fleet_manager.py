# fleet_manager.py
# Part B - Modular version

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["001", "002", "003", "004", "005"]

    return names, ranks, divisions, ids

def display_menu():
    print("\n--- FLEET MANAGER ---")
    print("1. Display Roster")
    print("2. Add Member")
    print("3. Remove Member")
    print("4. Update Rank")
    print("5. Exit")
    return input("Select option: ").strip()

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

def main():
    names, ranks, divisions, ids = init_database()

    while True:
        choice = display_menu()

        if choice == "1":
            display_roster(names, ranks, divisions, ids)
        elif choice == "2":
            add_member(names, ranks, divisions, ids)
        elif choice == "3":
            remove_member(names, ranks, divisions, ids)  
        elif choice == "4":
            print("Update feature not added yet.")
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
