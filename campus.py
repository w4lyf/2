def show_menu():
    print("Welcome to Campus Menu:")
    print("1. View Courses")
    print("2. View Events")
    print("3. View Facilities")
    print("4. Exit")

def view_courses():
    print("Available Courses:")
    print("1. Computer Science")
    print("2. Electrical Engineering")
    print("3. English Literature")

def view_events():
    print("Upcoming Events:")
    print("1. Seminar on Artificial Intelligence")
    print("2. Workshop on Robotics")
    print("3. Cultural Fest")

def view_facilities():
    print("Campus Facilities:")
    print("1. Library")
    print("2. Sports Complex")
    print("3. Cafeteria")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_courses()
        elif choice == '2':
            view_events()
        elif choice == '3':
            view_facilities()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")
