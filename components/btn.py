from tkinter import Button, PhotoImage, Tk
import utils


class Btn:
    def __init__(
        self,
        window: Tk,
        fileName: str,
        bgColor: str = "#222021",
        aBgColor: str = "#222021",
        height: int = 0,
        isExpanded: bool = False,
        fillBy: str = 'none',
        align: str = "top",
        vAlign: str = "center",
        marginX=0,
        marginY=0,
    ):
        self.btnImg = PhotoImage(file=utils.resource_path(f"assets/images/{fileName}"))
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
            padx=marginX,
            pady=marginY,
        )
