import json
import os
from datetime import datetime

class Note:
    def __init__(self, note_id, text, created_date):
        self.id = note_id
        self.text = text
        self.created_date = created_date

    def to_dict(self):
        return {"id": self.id, "text": self.text, "created_date": self.created_date}

class Notebook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                notes_data = json.load(file)
                return [Note(**note) for note in notes_data]
        return []

    def save_notes(self):
        with open(self.file_name, 'w') as file:
            json.dump([note.to_dict() for note in self.notes], file)

    def add_note(self, text):
        note_id = len(self.notes) + 1
        created_date = datetime.now().isoformat()
        note = Note(note_id, text, created_date)
        self.notes.append(note)
        self.save_notes()

    def show_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}, Created Date: {note.created_date}")

    def show_note_details(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            print(f"ID: {note.id}\nText: {note.text}\nCreated Date: {note.created_date}")
        else:
            print(f"No note found with ID {note_id}")

    def update_note(self, note_id, new_text):
        note = self.get_note_by_id(note_id)
        if note:
            note.text = new_text
            self.save_notes()
        else:
            print(f"No note found with ID {note_id}")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
        else:
            print(f"No note found with ID {note_id}")

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

def main():
    notebook = Notebook('notes.json')

    while True:
        print("\n1. Show All Notes")
        print("2. Show Note Details")
        print("3. Create Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            notebook.show_notes()
        elif choice == '2':
            note_id = int(input("Enter note ID: "))
            notebook.show_note_details(note_id)
        elif choice == '3':
            text = input("Enter note text: ")
            notebook.add_note(text)
        elif choice == '4':
            note_id = int(input("Enter note ID: "))
            new_text = input("Enter new note text: ")
            notebook.update_note(note_id, new_text)
        elif choice == '5':
            note_id = int(input("Enter note ID: "))
            notebook.delete_note(note_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
