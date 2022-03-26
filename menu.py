"""Module which implements a notebook menu"""
import sys
from notebook import Note, Notebook


class Menu:
    """Class for the menu object"""
    def __init__(self):
        """Initialisation function"""
        self.notebook = Notebook()
        self.choices = {
                             "1": self.show_notes,
                             "2": self.search_notes,
                             "3": self.add_note,
                             "4": self.modify_note,
                             "5": self.quit
                             }

    def display_menu(self):
        """Function for displaying menu"""
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
            """)

    def run(self):
        """Starts a main program cycle"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """Shows all notes or a given list of notes if provided"""
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note)

    def search_notes(self):
        """Search for notes by filter"""
        notes = self.notebook.search(input("Enter a search filter"))
        self.show_notes(notes)

    def add_note(self):
        """Adds a new note"""
        self.notebook.new_note(input("Enter a memo: "))
        print("Your note has been added.")

    def modify_note(self):
        """Modifies existing note"""
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        """Quits the program"""
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()

