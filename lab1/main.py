import Tasks.task1 as t1

def run():
    # load data to be used by all classes
    message = "\n\nCZ3005 Lab 1 Project Menu\n\n\
    Presets - Start Node: 1, End Node: 50, Energy Budget: 287932 == \n\
    1) UCS: Shortest Distance without Energy Constraint\n\
    2) \n\
    3) \n\
    4) Quit\n"
    while True:
        print(message)
        choice_str = input("Enter your choice: ").strip()
        try:
            choice = int(choice_str)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if choice == 1:
            print("You chose UCS: Shortest Distance without Energy Constraint")
            t1.run_ucs()
            input("Press [Enter] to continue...")
            continue
        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter 1 or 4.")




if __name__ == "__main__":
    run()
