import random, string
from tkinter import Frame, Tk
from components.btn import Btn
from components.textfield import TextField


class InputField:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(self, window: Tk, title: str, stringSize: int):

        self.stringSize = stringSize

        self.inputFieldFrame = Frame(window, bg=InputField.darkBgColor)
        self.inputFieldFrame.pack(anchor="nw")

        self.inputField = TextField(
            window=self.inputFieldFrame,
            title=title,
            marginX=(3, 0),
        )

        self.generate = Btn(
            window=self.inputFieldFrame,
            fileName="autonew.png",
            bgColor=InputField.ligthBgColor,
            aBgColor=InputField.ligthBgColor,
            align="left",
            height=32,
        )

        self.generate.btn.config(command=self.randomKey)

    def randomKey(self):
        self.inputField.textBox.delete(1.0, "end")
        secretKey = "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=self.stringSize(),
            ), )
        self.inputField.textBox.insert(1.0, secretKey)
