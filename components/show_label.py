from tkinter import Label, PhotoImage, Tk


class ShowLabel:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(
            self,
            window: Tk,
            text: str = "",
            image: str = "",
            align: str = "top",
            vAlign: str = "center",
            marginX=5,
            marginY=0,
            style=("Poppins", 14),
            bgColor: str = "#222021",
    ):
        if image != "":
            self.labelImg = PhotoImage(file=f"assets/images/{image}")
            self.label = Label(
                window,
                image=self.labelImg,
                bg=bgColor,
                fg=ShowLabel.fgColor,
                font=style,
            )
        else:
            self.label = Label(
                window,
                text=text,
                bg=bgColor,
                fg=ShowLabel.fgColor,
                font=style,
                wraplength=400,
            )
        self.label.pack(side=align, anchor=vAlign, padx=marginX, pady=marginY)
