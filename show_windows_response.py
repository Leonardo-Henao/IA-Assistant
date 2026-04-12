import subprocess
import pyperclip
from config_tkinter import *  # noqa: F403


def copy_response(event, data: str, window: MTkinter):
    pyperclip.copy(data)

    # Notification module is not used as tkinter does not allow calling methods from another module
    subprocess.run(
        [
            "notify-send",
            "-a",
            "Gemini IA",
            "IA Assistant - @lhenaoll",
            "The response was copied",
            "-t",
            "2000",
        ]
    )
    window.close_window()


def show_response(data: str):
    window = MTkinter("Response IA", 0)

    # title
    window.make_label("IA Response", tk_title_font).pack()
    window.make_label(
        "[Escape] To close windows - [Shift] + [c] To copy",
        tk_small_font,
        "center",
        True,
    ).pack()

    # frame title
    window.make_frame(20).pack()

    # text response
    window.make_scroll_text(data).pack(side="top")

    # frame ending
    window.make_frame(10).pack()

    # label ending
    window.add_bind("<Shift-C>", lambda event: copy_response(event, data, window))

    window.show_window()
