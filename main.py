#KH main page for Word Counter
from file_utils import read_document, add_content, update, ensure_file
from time_utils import get_timestamp

def menu():
    print("\n--- Document Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")

def get_file_path(existing_file):
    if existing_path:
        return existing_path
    return input("Enter the exact ile path for your document: ").strip()

def handle_update():
    file_path = get_file_path(file_path)
    ensure_file(file_path)

    content = read_document(file_path)
    word_count = len(content.split())
    timestamp = get_timestamp()

    update(file_path, word_count, timestamp)
    print(f"document updated. word count: {word_count}")
    return file_path

def handle_view():
    file_path = get_file_path(file_path)
    try:
        content = read_document(file_path)
        print("Document content stuff:")
        print(content if content else "doc is empty")
    except FileNotFoundError:
        print("File not found, please be more smart")
    return file_path

def handle_add_content(file_path):
    file_path = get_file_path(file_path)
    print("Enter new content(press enter twice to finisj): ")

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