"""Module which implements a note and notebook objects"""
import datetime

class Note:
    """Class for the note object"""
    last_id = 1
    def __init__(self, memo, tags=""):
        """Initialisation function"""
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        self.id = Note.last_id
        Note.last_id += 1
    def match(self, search_filter):
        """Searches for matches in the note memo or tags"""
        if search_filter in self.memo or search_filter in self.tags:
            return True

    def __str__(self):
        """Changes string representation of the note"""
        return "{0}: {1}\n{2}".format(
            self.id, self.tags, self.memo)

class Notebook:
    """Class for the notebook object"""
    def __init__(self):
        """Initialisation function"""
        self.notes = []

    def find_note(self, id):
        """Finds a note by id"""
        for note in self.notes:
            if str(note.id) == str(id):
                return note
        return None

    def new_note(self, memo, tags=""):
        """Creates a new note"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, memo, id):
        """Modifies a memo of the note with the given id"""
        note = self.find_note(id)
        if note:
            note.memo = memo
        else:
            print("There's no such note!")

    def modify_tags(self, tags, id):
        """Modifies tags of the note with the given id"""
        note = self.find_note(id)
        if note:
            note.tags = tags
        else:
            print("There's no such note!")

    def search(self, filter):
        """Searches for notes with match in memo or tags"""
        return [note for note in self.notes if note.match(filter)]
