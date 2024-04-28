import subprocess
from tkinter import INSERT, Frame, Label, Tk, scrolledtext

import pyperclip

window = Tk()

_background = "#313131"
_font_color = "#fff"
_width = 650

_title_font = ("Poppins", "14", "bold")
_normal_font = ("Poppins", "12")
_small_font = ("Poppins", "7")


def close_windows(event):
    window.destroy()


def make_label(data: str, type: tuple, anchor: Label.anchor = "sw"):
    lb = Label(window, text=data, bg=_background, fg=_font_color, font=type)
    lb.configure(anchor=anchor, width=90, wraplength=700)
    return lb


def make_frame(height: int = 10):
    return Frame(window, height=height, bg=_background)


def get_height_response(length: int):

    n_length = int(length / 2)

    if n_length > 30:
        return 13
    if n_length < 4:
        return 4

    return n_length


def copy_response(event, data: str):
    pyperclip.copy(data)

    # No se utiliza el modulo de notificación ya que tkinter no permite llamar métodos de otro modulo
    subprocess.run(["notify-send", "-a", "Gemini IA", "Gemini IA - @lhenaoll", "The response was copied", "-t", "2000"])
    window.destroy()


def show_response(data: str):
    window.title = "Response IA"
    window.minsize(_width, 0)
    window.configure(bg=_background, width=_width)

    label_title = make_label("IA Response", _title_font)
    label_title.grid(column=0, padx=10)

    frame_1 = make_frame()
    frame_1.grid()

    _height = get_height_response(len(data.splitlines()))

    text_response = scrolledtext.ScrolledText(window)
    text_response.configure(
        height=_height,
        bg=_background,
        fg="#999999",
        font=_normal_font,
        highlightthickness=0,
        borderwidth=0,
        padx=2,
        selectbackground="red",
        selectforeground="white",
    )
    text_response.insert(
        INSERT,
        data,
    )
    text_response.grid()

    frame_ending = make_frame(30)
    frame_ending.grid()

    label_info = make_label("[Escape] To close windows - [c] To copy", _small_font, "center")
    label_info.grid()

    window.bind("<Escape>", close_windows)
    window.bind("<Key-c>", lambda event: copy_response(event, data))

    window.mainloop()
