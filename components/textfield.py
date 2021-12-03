from tkinter import Text, Tk
from tkinter.font import BOLD

from components.show_label import ShowLabel


class TextField:
    def __init__(
        self,
        window: Tk,
        title: str,
        height: int = 1,
        width: int = 44,
        align: str = "left",
        marginX=0,
        marginY=0,
    ):

        self.label = ShowLabel(
            window=window,
            text=title,
            vAlign="nw",
            style=("Poppins", 12, BOLD),
            marginY=marginY,
        )

        self.textBox = Text(
            window,
            height=height,
            width=width,
        )
        self.textBox.pack(anchor="n", side=align, padx=marginX)

    def getValue(self) -> str:
        return self.textBox.get(1.0, "end-1c")
