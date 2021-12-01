from tkinter import Frame, Tk
from components.btn import Btn
from components.show_label import ShowLabel
from components.textfield import TextField


class InputField:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(self, window: Tk, title: str):
        self.inputFieldFrame = Frame(window, bg=InputField.darkBgColor)
        self.inputFieldFrame.pack(anchor="n")

        self.textBox = TextField(window=self.inputFieldFrame, title=title)

        self.generate = Btn(
            window=self.inputFieldFrame,
            fileName="autonew.png",
            bgColor=InputField.ligthBgColor,
            aBgColor=InputField.ligthBgColor,
            align="left",
            height=10,
        )
