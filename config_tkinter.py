from tkinter import INSERT, Entry, Frame, Label, StringVar, Tk, scrolledtext

tk_title_font = ("Poppins", "14", "bold")
tk_normal_font = ("Poppins", "12")
tk_small_font = ("Poppins", "8")


class MTkinter:
    _tk_background = "#313131"
    _tk_font_color = "#fff"
    _tk_font_secondary = "#999999"
    _tk_width = 600

    _global_config = [
        {"background": _tk_background, "foreground": _tk_font_color}]
    _input_config = [
        {
            "background": _tk_background,
            "foreground": _tk_font_color,
            "selectbackground": "red",
            "selectforeground": "white",
            "highlightthickness": 1,
            "borderwidth": 0,
            "highlightcolor": "white",
        }
    ]

    def __init__(self, title: str, height: int = 150):
        self.window = Tk()
        self.window.title = title  # pyright: ignore
        self.window.configure(
            bg=self._tk_background, width=self._tk_width, height=height, padx=30, pady=10)
        self.window.pack_propagate(False)

        self.window.bind("<Escape>", self.close_window)

    def show_window(self):
        self.window.mainloop()

    def close_window(self, event: any = None):  # pyright: ignore
        self.window.destroy()

    def make_frame(self, height: int = 10):
        return Frame(self.window, height=height, background=self._tk_background)

    def make_label(self, data: str, type: tuple, anchor: str = "sw", secondary: bool = False):
        lb = Label(self.window, text=data, font=type)
        lb.configure(
            anchor=anchor,  # pyright: ignore
            justify="left",
            width=90,
            wraplength=self._tk_width,
            *self._global_config,
            foreground="#999999" if secondary else "white",
        )
        return lb

    def make_entry(self, txt_var: StringVar):
        entry: Entry = Entry(self.window, textvariable=txt_var)
        entry.configure(
            *self._input_config,
            width=self._tk_width,
            font=tk_normal_font,  # pyright: ignore
            insertbackground=self._tk_font_secondary,
            insertontime=50,
        )
        return entry

    def make_scroll_text(self, data: str):
        _height = self.get_height_response(len(data))
        self.window.config(height=_height)

        scrolltext: scrolledtext.ScrolledText = scrolledtext.ScrolledText(
            self.window)
        scrolltext.configure(
            bg=self._tk_background,
            fg=self._tk_font_secondary,
            font=tk_normal_font,  # pyright: ignore
            wrap="word",
            highlightthickness=0,
            borderwidth=0,
            padx=2,
            selectbackground="red",
            selectforeground="white",
        )
        scrolltext.insert(
            INSERT,
            data,
        )
        return scrolltext

    def add_bind(self, key: str, func):
        self.window.bind(key, func)

    def get_height_response(self, length: int):
        n_length = int(length / 2)

        if n_length <= 300:
            return 300
        elif n_length > 300 and n_length < 900:
            return 400
        else:
            return 600
