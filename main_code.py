
def menu():
    file_name =  input(f"Enter your data file path: ").strip() or "docuement.txt"
    load_doc(file_name)
    while True:
        print("--- Document Word Count Updater ---")
        print("1. Update document info")
        print("2. View document")
        print("3. Add content to document")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1" and file_name == "":
                file_name =  input(f"Enter your data file path: ").strip() or "document.csv"
        elif choice == "1":
             pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
