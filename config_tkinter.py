from tkinter import Entry, Frame, Label, StringVar, Tk, scrolledtext

tk_title_font = ("Poppins", "14", "bold")
tk_normal_font = ("Poppins", "12")
tk_small_font = ("Poppins", "8")
tk_bold_font = ("Poppins", "12", "bold")
tk_italic_font = ("Poppins", "12", "italic")
tk_code_font = ("Courier New", "11")
tk_h1_font = ("Poppins", "16", "bold")
tk_h2_font = ("Poppins", "14", "bold")


class MTkinter:
    _tk_background = "#313131"
    _tk_font_color = "#fff"
    _tk_font_secondary = "#999999"
    _tk_width = 600

    _global_config = [{"background": _tk_background, "foreground": _tk_font_color}]
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
            bg=self._tk_background,
            width=self._tk_width,
            height=height,
            padx=30,
            pady=10,
        )
        self.window.pack_propagate(False)

        self.window.bind("<Escape>", self.close_window)

    def show_window(self):
        self.window.mainloop()

    def close_window(self, event: any = None):  # pyright: ignore
        self.window.destroy()

    def make_frame(self, height: int = 10):
        return Frame(self.window, height=height, background=self._tk_background)

    def make_label(
        self, data: str, type: tuple, anchor: str = "sw", secondary: bool = False
    ):
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

        scrolltext: scrolledtext.ScrolledText = scrolledtext.ScrolledText(self.window)
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
        self._render_markdown(scrolltext, data)
        return scrolltext

    def _render_markdown(self, widget, data: str):
        import re

        widget.config(state="normal")
        widget.delete("1.0", "end")

        # Configure tags
        widget.tag_configure("bold", font=tk_bold_font)
        widget.tag_configure("italic", font=tk_italic_font)
        widget.tag_configure(
            "code", font=tk_code_font, background="#444444", foreground="#eee"
        )
        widget.tag_configure("h1", font=tk_h1_font, foreground="white")
        widget.tag_configure("h2", font=tk_h2_font, foreground="white")

        lines = data.split("\n")
        for i, line in enumerate(lines):
            # Header 1
            if line.startswith("# "):
                widget.insert("end", line[2:] + "\n", "h1")
                continue
            # Header 2
            elif line.startswith("## "):
                widget.insert("end", line[3:] + "\n", "h2")
                continue

            # Inline parsing
            pattern = re.compile(r"(\*\*.*?\*\*|\*.*?\*|`.*?`)")
            parts = pattern.split(line)

            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    widget.insert("end", part[2:-2], "bold")
                elif part.startswith("*") and part.endswith("*"):
                    widget.insert("end", part[1:-1], "italic")
                elif part.startswith("`") and part.endswith("`"):
                    widget.insert("end", part[1:-1], "code")
                else:
                    widget.insert("end", part)

            if i < len(lines) - 1:
                widget.insert("end", "\n")

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
