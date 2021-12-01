from tkinter import Frame, IntVar, Radiobutton, Tk
from components.show_label import ShowLabel


class SelectionBtn:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(self, window: Tk, title: str, options, marginY=0):
        self.selectionBtnFrame = Frame(window, bg=SelectionBtn.darkBgColor)
        self.selectionBtnFrame.pack(anchor="n", pady=marginY)

        self.label = ShowLabel(
            window=self.selectionBtnFrame,
            text=title,
            align="left",
            vAlign="n",
            marginY=5,
        )

        self.value = IntVar()
        for i in range(0, len(options), 1):
            radiobtn = Radiobutton(
                self.selectionBtnFrame,
                text=options[i],
                variable=self.value,
                value=i + 1,
                bg=SelectionBtn.darkBgColor,
                activebackground=SelectionBtn.darkBgColor,
                fg=SelectionBtn.fgColor,
                activeforeground="#fff",
                selectcolor=SelectionBtn.ligthBgColor,
            )
            radiobtn.pack(anchor="n", side="left")