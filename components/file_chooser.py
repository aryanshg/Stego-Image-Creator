from tkinter import Frame, Tk, filedialog
from tkinter.font import BOLD
from components.btn import Btn
from components.show_label import ShowLabel
from pathlib import Path


class FileChooser:
    def __init__(
        self,
        window: Tk,
        dialogTitle: str,
        title: str,
        fileTypes,
        fileImageName: str,
        marginY=0,
    ):
        self.dialogTitle = dialogTitle

        self.title = title

        self.fileTypes = fileTypes

        self.label = ShowLabel(
            window=window,
            text=title,
            style=("Poppins", 12, BOLD),
            vAlign="nw",
            marginY=marginY,
        )

        self.fileChooserFrame = Frame(
            window,
            bg="#282828",
            width=465,
            height=50,
        )
        self.fileChooserFrame.pack(anchor="n", padx=3)

        self.fileChooserFrame.pack_propagate(0)

        self.fileImage = ShowLabel(
            window=self.fileChooserFrame,
            image=fileImageName,
            bgColor="#282828",
            align="left",
            marginX=5,
        )

        self.fileFullPath = ""
        self.fileName = "No file chosen"

        self.pathLabel = ShowLabel(
            window=self.fileChooserFrame,
            text=self.fileName,
            bgColor="#282828",
            align="left",
        )

        self.clearPath = Btn(
            window=self.fileChooserFrame,
            fileName="clear.png",
            bgColor="#282828",
            aBgColor="#282828",
            align="right",
            marginX=5,
        )

        self.clearPath.btn.config(command=self.clearFileFullPath)

        self.chooser = Btn(
            window=self.fileChooserFrame,
            fileName="chooser.png",
            bgColor="#282828",
            aBgColor="#282828",
            align="right",
        )

        self.chooser.btn.config(command=self.browseFiles)

    def clearFileFullPath(self):
        self.fileFullPath = ""
        self.fileName = "No file chosen"

        self.pathLabel.label.config(text=self.fileName)

    def browseFiles(self) -> None:

        if self.fileName == "No file chosen":
            self.initialDir = str(Path.home() / "Downloads")
        else:
            self.initialDir = self.fileFullPath

        filePath = filedialog.askopenfilename(
            initialdir=self.initialDir,
            title=self.dialogTitle,
            filetypes=self.fileTypes,
        )

        if filePath == "":
            self.fileFullPath = ""
            self.fileName = "No file chosen"
        else:
            self.fileFullPath = filePath
            self.fileName = filePath.split("/")[-1]

        self.pathLabel.label.config(text=self.fileName)