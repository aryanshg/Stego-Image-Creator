from tkinter import Text, Tk

from components.show_label import ShowLabel


class TextField:
    def __init__(
        self,
        window: Tk,
        title: str,
        height: int = 1,
        width: int = 46,
        align: str = "left",
    ):

        self.label = ShowLabel(
            window=window,
            text=title,
            vAlign="n",
        )

        self.textBox = Text(
            window,
            height=height,
            width=width,
            font=("Poppins", 12),
        )
        self.textBox.pack(anchor="n", side=align)
