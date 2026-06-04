from pywinauto import Application

text = """
Title: Test

Hello from pywinauto
"""

app = Application(backend="uia").connect(
    title_re=".*Notepad"
)

window = app.top_window()

window.set_focus()

window.child_window(
    control_type="Edit"
).set_edit_text(text)

print("Text written successfully")