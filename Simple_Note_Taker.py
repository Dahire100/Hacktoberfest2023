def create_note():
    note_title = input("Enter the note title: ")
    note_content = input("Enter the note content: ")
    with open("notes.txt", "a") as file:
        file.write(f"Title: {note_title}\n")
        file.write(f"Content: {note_content}\n\n")
    print("Note created successfully!\n")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            print(notes)
    except FileNotFoundError:
        print("No notes found.")

while True:
    print("Note-Making Application")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
