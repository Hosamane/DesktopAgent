from pywinauto import Desktop


def safe_type(target_window_title, text):

    try:

        window = Desktop(
            backend="uia"
        ).window(
            title=target_window_title
        )

        window.wait("ready", timeout=5)

        edit = window.child_window(
            control_type="Edit"
        )

        edit.set_edit_text(text)

        return True

    except Exception as e:

        print(
            f"Typing failed: {e}"
        )

        return False