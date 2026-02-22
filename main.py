#KH main page for Word Counter
from file_utils import read_document, add_content, update_metadata, ensure_file
from time_utils import get_timestamp
#display menu
def menu():
    print("\n--- Document Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")

#function for geting file path
def get_file_path(existing_path):
    if existing_path:
        return existing_path
    return input("Enter the exact file path for your document: ").strip()

#function for handling update
def handle_update(file_path):
    file_path = get_file_path(file_path)
    ensure_file(file_path)

    content = read_document(file_path)
    word_count = len(content.split())
    timestamp = get_timestamp()

    update_metadata(file_path, word_count, timestamp)
    print(f"Document Updated. Word Ccount: {word_count}")
    return file_path

#function for handling view
def handle_view(file_path):
    file_path = get_file_path(file_path)
    try:
        content = read_document(file_path)
        print("\nDocument content stuff:")
        print(content if content else "doc is empty")
    except FileNotFoundError:
        print("File not found, please be more smart")
    return file_path

#function for handing the add content
def handle_add_content(file_path):
    file_path = get_file_path(file_path)
    print("\nEnter new content (press enter twice to finish): ")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    new_text = "\n".join(lines)

    if new_text.strip():
        add_content(file_path, new_text)
        print("content added successfully")
    else:
        print("no content entered.")

    return file_path

#main function
def main():
    file_path = None

    while True:
        menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == '1':
            file_path = handle_update(file_path)
        elif choice == '2':
            file_path = handle_view(file_path)
        elif choice == '3':
            file_path = handle_add_content(file_path)
        elif choice == '4':
            print("Goodbye fellow human being")
            break
        else:
            print("invalid. try again.")
    
if __name__ == "__main__":
    main()