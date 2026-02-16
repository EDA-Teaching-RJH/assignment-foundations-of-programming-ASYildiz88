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

def main():
    names, ranks, divisions, ids = init_database()

    while True:
        choice = display_menu()

        if choice == "1":
            print("Roster feature not added yet.")
        elif choice == "2":
            print("Add feature not added yet.")
        elif choice == "3":
            print("Remove feature not added yet.")
        elif choice == "4":
            print("Update feature not added yet.")
        elif choice == "5":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
