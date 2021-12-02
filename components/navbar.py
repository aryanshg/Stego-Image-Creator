from tkinter import Tk
from components.btn import Btn
from tkinter.font import BOLD
from components.show_label import ShowLabel


class NavBar:
    def __init__(self, window: Tk, title: str):
        self.back = Btn(
            window=window,
            fileName="back.png",
            align="left",
            vAlign="n",
            marginY=10,
        )

        self.title = ShowLabel(
            window=window,
            text=title,
            align="left",
            vAlign="n",
            style=("Poppins", 12, BOLD),
            marginY=10,
        )
