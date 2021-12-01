from tkinter import Frame, Tk
from tkinter.constants import NORMAL, UNDERLINE
from components.btn import Btn
from components.show_label import ShowLabel


class FileChooser:
    def __init__(
        self,
        window: Tk,
        title: str,
        fileImageName: str,
        filePath: str,
    ):
        self.label = ShowLabel(
            window=window,
            text=title,
            vAlign="n",
        )

        self.fileChooserFrame = Frame(window, bg="#282828")
        self.fileChooserFrame.pack(anchor="n", padx=5)

        self.fileImage = ShowLabel(
            window=self.fileChooserFrame,
            image=fileImageName,
            bgColor="#282828",
            align="left",
            marginY=10,
        )

        self.fileFullPath = filePath
        self.pathLabel = ShowLabel(
            window=self.fileChooserFrame,
            text=self.fileFullPath,
            align="left",
            style=("Poppins", 12, NORMAL, UNDERLINE),
            bgColor="#282828",
            marginY=10,
        )

        self.clearPath = Btn(
            window=self.fileChooserFrame,
            fileName="clear.png",
            align="left",
            bgColor="#282828",
            aBgColor="#282828",
        )

        self.chooser = Btn(
            window=self.fileChooserFrame,
            fileName="chooser.png",
            align="left",
            bgColor="#282828",
            aBgColor="#282828",
        )
