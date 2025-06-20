import os
import subprocess
import webbrowser
from tkinter import StringVar

import google.generativeai as genai
from translate import Translator

from config_tkinter import *
from helpers.control_history import get_all_data, remove_all, write_in_backup
from show_windows_response import show_response

_you_name = "Leo"
_title_notification = "IA Assistant - @lhenaoll"
_sep = "++++++++++++++++++++++++++++++++++++++++++++"


commands = [
    (":et", "Translate to English"),
    (":st", "Translate to Spanish"),
    (":sh", "Show history"),
    (":ch", "Clear history"),
]


def send_notification(message: str):
    subprocess.run(
        [
            "notify-send",
            "-a",
            "Gemini IA",
            _title_notification,
            message,
            "-t",
            "2000",
        ]
    )


def use_translator(prompt: str, to_lang: str):
    tr = Translator(from_lang="es" if to_lang ==
                    "en" else "en", to_lang=to_lang)
    return tr.translate(prompt)


def use_IA(prompt: str):
    API_KEY_GEMINI = os.environ.get("GOOGLE_API_KEY")
    try:
        if API_KEY_GEMINI is None:

            return f"API_KEY_GEMINI is not defined. Result to get api key : {API_KEY_GEMINI}. Remember set you environment variable GOOGLE_API_KEY. See -> https://github.com/Leonardo-Henao/IA-Assistant?tab=readme-ov-file#all"

        send_notification("Gemini is loading a response...")

        genai.configure(api_key=API_KEY_GEMINI)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"{str(e)} \n\n api-key:{API_KEY_GEMINI}"


def handle_text(event):
    global window

    value_entry = entry_variable.get()
    window.close_window()

    if len(value_entry) == 0:
        return ""
    else:
        new_prompt = value_entry
        response = ""
        if value_entry.startswith(":et"):
            new_prompt = value_entry.replace(":et", "")
            response = use_translator(new_prompt, "en")

        elif value_entry.startswith(":st"):
            new_prompt = value_entry.replace(":st", "")
            response = use_translator(new_prompt, "es")

        elif value_entry.startswith(":ch"):
            remove_all()  # pyright: ignore missing-parameter
            send_notification("History deleted")
            exit()

        elif value_entry.startswith(":sh"):
            result = get_all_data()  # pyright: ignore missing-parameter

            if len(result) == 0:
                send_notification("No content in history")
            else:
                to_show = ""
                for r in result:
                    row = f"{r[0]}: {r[1]}\nQ: {r[2]}\nR: {r[3]}\n\n"
                    to_show += f"{_sep} \n{row}"

                show_response(to_show)
            exit()

        else:
            response = use_IA(new_prompt)

    write_in_backup(response, new_prompt)  # pyright: ignore missing-parameter
    show_response(response)


##########################################
#       Creating GUI with Tkinter        #
##########################################
window: MTkinter = MTkinter(f"Hi {_you_name}, I'm you assistant", 250)

# title
window.make_label(
    f"Hi {_you_name}, I'm you assistant \nWhat is you question in this moment?",
    tk_title_font,
).pack()

# first frame
window.make_frame(20).pack()

# entry
entry_variable = StringVar(
    value="", name="What is you question in this moment?")
entry_question = window.make_entry(entry_variable)
entry_question.focus()
entry_question.pack()

# second frame
window.make_frame(30).pack()

# message
message_commands = [f"{c} = {a}" for c, a in commands]

label_message = window.make_label(
    str(message_commands)
    .replace("[", "")
    .replace("]", "")
    .replace("'", "")
    .replace(",", " | "),
    tk_small_font,
    "center",
    True,
).pack()

# ending frame
window.make_frame(50).pack()

# copyright message
copy_label = window.make_label("Create by @lhenaoll", tk_small_font, "e", True)
copy_label.bind(
    "<Button-1>", lambda event: webbrowser.open("https://leonardohenao.com"))
copy_label.pack()

window.add_bind("<Return>", handle_text)
window.show_window()
