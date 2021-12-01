from tkinter import Button, PhotoImage, Tk


class Btn:
    def __init__(
        self,
        window: Tk,
        fileName: str,
        isExpanded: bool = False,
        fillBy: str = 'none',
        align: str = "top",
        vAlign: str = "center",
        hpad: int = 5,
        vpad: int = 10,
        bgColor: str = "#222021",
        aBgColor: str = "#222021",
        height: int = 0,
    ):
        self.btnImg = PhotoImage(file=f"assets/images/{fileName}")
        if height != 0:
            self.btn = Button(
                window,
                image=self.btnImg,
                bg=bgColor,
                activebackground=aBgColor,
                borderwidth=0,
                height=height,
            )
        else:
            self.btn = Button(
                window,
                image=self.btnImg,
                bg=bgColor,
                activebackground=aBgColor,
                borderwidth=0,
            )
        self.btn.pack(
            expand=isExpanded,
            fill=fillBy,
            side=align,
            anchor=vAlign,
            ipadx=hpad,
            ipady=vpad,
        )
