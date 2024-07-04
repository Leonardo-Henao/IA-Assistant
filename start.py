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
_title_notification = "Gemini IA - @lhenaoll"

commands = [
    (":tre", "Translate to English"),
    (":trs", "Translate to Spanish"),
    (":hs", "Show history"),
    (":hsc", "Clear history"),
]


def use_translator(prompt: str, to_lang: str):
    tr = Translator(from_lang="es" if to_lang ==
                    "en" else "en", to_lang=to_lang)
    return tr.translate(prompt)


def use_IA(prompt: str):
    API_KEY_GEMINI = os.environ.get("GOOGLE_API_KEY")
    try:
        if API_KEY_GEMINI == None:
            return f"API_KEY_GEMINI is not defined. Result to get api key : {API_KEY_GEMINI}. Remember set you environment variable GOOGLE_API_KEY. See -> https://github.com/Leonardo-Henao/IA-Assistant?tab=readme-ov-file#all"

        subprocess.run(
            [
                "notify-send",
                "-a",
                "Gemini IA",
                _title_notification,
                "Gemini is loading a response...",
                "-t",
                "2000",
            ]
        )

        genai.configure(api_key=API_KEY_GEMINI)
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"{str(e)} \n\n api-key:{API_KEY_GEMINI}"


def handle_text(event):
    global window

    value_entry = entry_variable.get()
    window.close_window()

    if len(value_entry) == 0:
        pass
        return ""
    else:
        new_prompt = value_entry
        response = ""
        if value_entry.startswith(":tre"):
            new_prompt = value_entry.replace(":tre", "")
            response = use_translator(new_prompt, "en")

        elif value_entry.startswith(":trs"):
            new_prompt = value_entry.replace(":trs", "")
            response = use_translator(new_prompt, "es")

        elif value_entry.startswith(":hsc"):
            remove_all()  # pyright: ignore missing-parameter
            subprocess.run(
                [
                    "notify-send",
                    "-a",
                    "Gemini IA",
                    _title_notification,
                    "Historial borrado",
                    "-t",
                    "2000",
                ]
            )
            exit()

        elif value_entry.startswith(":hs"):
            result = get_all_data()  # pyright: ignore missing-parameter

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
                    t = f"{r[0]}: {r[1]}\nQ: {r[2]}\nR: {r[3]}\n\n"
                    to_show += t

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
