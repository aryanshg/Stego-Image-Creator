from tkinter import Label, PhotoImage, Tk


class ShowLabel:
    darkBgColor = "#222021"
    ligthBgColor = "#282828"
    fgColor = "#cccccc"

    def __init__(
        self,
        window: Tk,
        image: str = "",
        bgColor: str = "#222021",
        style=("Poppins", 12),
        text: str = "",
        align: str = "top",
        vAlign: str = "center",
        marginX=0,
        marginY=0,
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
        self.label.pack(
            side=align,
            anchor=vAlign,
            padx=marginX,
            pady=marginY,
        )
