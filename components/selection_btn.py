from tkinter import Frame, IntVar, Radiobutton, Tk
from tkinter.font import BOLD
from components.show_label import ShowLabel


class SelectionBtn:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(self, window: Tk, title: str, options):
        self.selectionBtnFrame = Frame(window, bg=SelectionBtn.darkBgColor)
        self.selectionBtnFrame.pack(anchor="nw", pady=(18, 5))

        self.label = ShowLabel(
            window=self.selectionBtnFrame,
            text=title,
            style=("Poppins", 12, BOLD),
            align="left",
            vAlign="nw",
            marginY=4,
        )

        self.value = IntVar()

        if options[0].isdigit():
            btnValue = int(options[0])
        else:
            btnValue = 1

        self.value.set(btnValue)

        for i in range(0, len(options), 1):
            if options[i].isdigit():
                btnValue = int(options[i])
            else:
                btnValue = i + 1
            radiobtn = Radiobutton(
                self.selectionBtnFrame,
                text=options[i],
                variable=self.value,
                value=btnValue,
                bg=SelectionBtn.darkBgColor,
                activebackground=SelectionBtn.darkBgColor,
                fg=SelectionBtn.fgColor,
                activeforeground="#fff",
                selectcolor=SelectionBtn.ligthBgColor,
            )
            radiobtn.pack(anchor="n", side="left")