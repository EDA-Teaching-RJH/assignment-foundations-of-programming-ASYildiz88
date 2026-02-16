# fleet_manager.py
# Part B - Modular version

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    divisions = ["Command", "Command", "Operations", "Security", "Sciences"]
    ids = ["001", "002", "003", "004", "005"]

    return names, ranks, divisions, ids


def main():
    names, ranks, divisions, ids = init_database()

    print("Fleet system started.")
    print("Crew count:", len(names))


if __name__ == "__main__":
    main()
