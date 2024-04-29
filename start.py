import subprocess
import webbrowser
from tkinter import StringVar

import google.generativeai as genai

from config import API_KEY_GEMINI

# from show_windows_response import show_response
from config_tkinter import *
from helpers.control_history import get_all_data, remove_all, write_in_backup
from show_windows_response import show_response

_you_name = "Leo"
_title_notification = "Gemini IA - @lhenaoll"

commands = [
    (":tre", "Translate to English"),
    (":trs", "Translate to Spanish"),
    (":hs", "Show history"),
    (":hsc", "Clear history"),
]


def handle_text(event):
    global window

    value_entry = entry_variable.get()
    window.close_window()

    if len(value_entry) == 0:
        pass
        return ""
    else:
        new_prompt = value_entry
        if value_entry.startswith(":tre"):
            new_prompt = value_entry.replace(":tre", "Traduce al ingles ")

        if value_entry.startswith(":trs"):
            new_prompt = value_entry.replace(":trs", "Traduce al español ")

        if value_entry.startswith(":hsc"):
            remove_all()
            subprocess.run(["notify-send", "-a", "Gemini IA", _title_notification, "Historial borrado", "-t", "2000"])
            exit()

        if value_entry.startswith(":hs"):
            result = get_all_data()

            if len(result) == 0:
                subprocess.run(
                    [
                        "notify-send",
                        "-a",
                        "Gemini IA",
                        _title_notification,
                        "No hay contenido en el historial",
                        "-t",
                        "2000",
                    ]
                )
            else:
                to_show = ""
                for r in result:
                    t = f"{r[0]}: {r[1]}\n{r[2]}\n\n"
                    to_show += t

                show_response(to_show)
            exit()

    subprocess.run(
        ["notify-send", "-a", "Gemini IA", _title_notification, "Gemini is loading a response...", "-t", "2000"]
    )

    genai.configure(api_key=API_KEY_GEMINI)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(new_prompt)

    result_from_response = response.text
    write_in_backup(result_from_response, new_prompt)
    show_response(result_from_response)


##########################################
#       Creating GUI with Tkinter          #
##########################################

window: MTkinter = MTkinter(f"Hi {_you_name}, I'm you assistant", 250)

# title
window.make_label(f"Hi {_you_name}, I'm you assistant \nWhat is you question in this moment?", tk_title_font).pack()

# first frame
window.make_frame(20).pack()

# entry
entry_variable = StringVar(value="", name="What is you question in this moment?")
entry_question = window.make_entry(entry_variable)
entry_question.focus()
entry_question.pack()

# second frame
window.make_frame(30).pack()

# message
message_commands = [f"{c} = {a}" for c, a in commands]

label_message = window.make_label(
    str(message_commands).replace("[", "").replace("]", "").replace("'", "").replace(",", " | "),
    tk_small_font,
    "center",
    True,
).pack()

# ending frame
window.make_frame(50).pack()

# copyright message
copy_label = window.make_label("Create by @lhenaoll", tk_small_font, "e", True)
copy_label.bind("<Button-1>", lambda event: webbrowser.open("https://leonardohenao.com"))
copy_label.pack()

window.add_bind("<Return>", handle_text)
window.show_window()
