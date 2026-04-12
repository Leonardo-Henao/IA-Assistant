from show_windows_response import show_response

test_data = """# IA Response Demo
This is a demo of the **Markdown support** in the `IA-Assistant`.

## Features
- Support for **Bold text**
- Support for *Italic text*
- Support for `In-line code`
- Support for # Headers

You can also have multiple styles in one line like **Bold** and *Italic* and `Code`.
"""

if __name__ == "__main__":
    show_response(test_data)
