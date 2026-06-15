# basic text editor system 

# Memento
class Memento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


# Originator
class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def get_content(self):
        return self._content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()


# Caretaker
class History:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def save(self, memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()  # important!

    def undo(self, editor: TextEditor):
        if not self._undo_stack:
            return

        # move current state to redo
        self._redo_stack.append(editor.save())

        # restore previous
        memento = self._undo_stack.pop()
        editor.restore(memento)

    def redo(self, editor: TextEditor):
        if not self._redo_stack:
            return

        # move current to undo
        self._undo_stack.append(editor.save())

        # restore redo state
        memento = self._redo_stack.pop()
        editor.restore(memento)


# Client Code
if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello ")
    history.save(editor.save())

    editor.write("World")
    history.save(editor.save())

    editor.write("!!!")

    print(editor.get_content())  # Hello World!!!

    history.undo(editor)
    print(editor.get_content())  # Hello World

    history.undo(editor)
    print(editor.get_content())  # Hello 

    history.redo(editor)
    print(editor.get_content())  # Hello World
