from tkinter import Canvas, IntVar, Radiobutton, Scrollbar, StringVar, Tk, Frame, font, filedialog
import string
import random
from components.btn import Btn
from components.file_chooser import FileChooser
from components.inputfield import InputField
from components.navbar import NavBar
from components.selection_btn import SelectionBtn
from components.show_label import ShowLabel
from components.textfield import TextField

darkBgColor = "#222021"
ligthBgColor = "#282828"
fgColor = "#cccccc"


def showPage(frame: Frame) -> None:
    frame.tkraise()


def browseFiles() -> str:
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a plain file",
        filetypes=(("Text files", "*.txt*"), ("all files", "*.*")),
    )


def randomKey():
    # t3.delete(0, "end")
    secretKey = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=16))
    print(secretKey)
    # t3.insert(0, secretKey)


root = Tk()
root.title("Stego Image Creator | Project")
root.iconbitmap("assets/images/favicon.ico")
root.geometry("515x650")
root.minsize(515, 650)
root.configure(bg=darkBgColor)
root.resizable(False, True)
root.state("zoomed")

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Poppins", size=15)
root.option_add("*Font", defaultFont)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

plainFilePath = "C:/Users/Aryansh/Desktop/file-to-encrypt.txt"
plainText = StringVar()
keySize = IntVar()
secretKey = StringVar()
coverFilePath = "C:/Users/Aryansh/Desktop/cover-image.png"
stegoObjectPath = "C:/Users/Aryansh/Desktop/cover-image.png"
originalMessageType = IntVar()
originalFileExtension = StringVar()

homeFrame = Frame(root)
encodeFrame = Frame(root)
decodeFrame = Frame(root)

for frame in (homeFrame, encodeFrame, decodeFrame):
    frame.grid(row=0, column=0, sticky="nsew")

# ================================================================== HOME ==================================================================
encodeOpBtn = Btn(
    window=homeFrame,
    fileName="encode.png",
    isExpanded=True,
    fillBy="both",
)
encodeOpBtn.btn.config(command=lambda: showPage(encodeFrame))

decodeOpBtn = Btn(
    window=homeFrame,
    fileName="decode.png",
    isExpanded=True,
    fillBy="both",
)
decodeOpBtn.btn.config(command=lambda: showPage(decodeFrame))

# ================================================================== ENCODE ==================================================================
enBottomScroller = Scrollbar(encodeFrame)
enBottomScroller.pack(side="right", fill="y")

enTopFrame = Frame(encodeFrame, bg=darkBgColor)
enTopFrame.pack(fill="x")

enBottomMainFrame = Frame(encodeFrame)
enBottomMainFrame.pack(expand=True, fill="both")

enBottomCanvas = Canvas(
    enBottomMainFrame,
    bg=darkBgColor,
    bd=0,
    highlightthickness=0,
)
enBottomCanvas.pack(expand=True, fill="both")
enBottomCanvas.config(yscrollcommand=enBottomScroller.set)
enBottomCanvas.bind(
    "<Configure>",
    lambda e: enBottomCanvas.config(scrollregion=enBottomCanvas.bbox("all"), ),
)

enBottomScroller.config(command=enBottomCanvas.yview)

enBottomFrame = Frame(enBottomCanvas, bg=darkBgColor)
enBottomCanvas.create_window((0, 0), window=enBottomFrame, anchor="nw")

# ------- encode top frame -------

navbar1 = NavBar(window=enTopFrame, title="Encode")
navbar1.back.btn.config(command=lambda: showPage(homeFrame))

# ------- encode bottom frame -------

plainFileChooser = FileChooser(
    window=enBottomFrame,
    title="Choose plain file:",
    fileImageName="file.png",
    filePath=plainFilePath,
)
# plainFileChooser.clearPath.btn.config(command=browseFiles)
plainFileChooser.chooser.btn.config(command=browseFiles)

# -----

l1 = ShowLabel(
    window=enBottomFrame,
    text="OR",
    style=("Poppins", 15, font.BOLD),
    vAlign="n",
    marginY=(15, 0),
)

# -----

plainTextInput = TextField(
    window=enBottomFrame,
    title="Enter plain text:",
    height=3,
    width=49,
    align="top",
)

# -----

keySizeSelection1 = SelectionBtn(
    window=enBottomFrame,
    title="Select key size in bytes:",
    options=["16", "24", "32"],
)

# -----

secretKeyInput1 = InputField(window=enBottomFrame, title="Enter secret key:")

# -----

coverImageChooser = FileChooser(
    window=enBottomFrame,
    title="Choose cover image:",
    fileImageName="image.png",
    filePath=coverFilePath,
)
# coverImageChooser.clearPath.btn.config(command=browseFiles)
coverImageChooser.chooser.btn.config(command=browseFiles)

# -----

encodeBtn = Btn(
    window=enBottomFrame,
    fileName="encode-btn.png",
    vpad=15,
)

# ================================================================== DECODE ==================================================================
deBottomScroller = Scrollbar(decodeFrame)
deBottomScroller.pack(side="right", fill="y")

deTopFrame = Frame(decodeFrame, bg=darkBgColor)
deTopFrame.pack(fill="x")

deBottomMainFrame = Frame(decodeFrame)
deBottomMainFrame.pack(expand=True, fill="both")

deBottomCanvas = Canvas(
    deBottomMainFrame,
    bg=darkBgColor,
    bd=0,
    highlightthickness=0,
)
deBottomCanvas.pack(expand=True, fill="both")
deBottomCanvas.config(yscrollcommand=deBottomScroller.set)
deBottomCanvas.bind(
    "<Configure>",
    lambda e: deBottomCanvas.config(scrollregion=deBottomCanvas.bbox("all"), ),
)

deBottomScroller.config(command=deBottomCanvas.yview)

deBottomFrame = Frame(deBottomCanvas, bg=darkBgColor)
deBottomCanvas.create_window((0, 0), window=deBottomFrame, anchor="nw")

# ------- decode top frame -------

navbar2 = NavBar(window=deTopFrame, title="Decode")
navbar2.back.btn.config(command=lambda: showPage(homeFrame))

# ------- decode bottom frame -------

stegoObjectChooser = FileChooser(
    window=deBottomFrame,
    title="Choose stego object:",
    fileImageName="file.png",
    filePath=plainFilePath,
)
# stegoObjectChooser.clearPath.btn.config(command=browseFiles)
stegoObjectChooser.chooser.btn.config(command=browseFiles)

# -----

keySizeSelection2 = SelectionBtn(
    window=deBottomFrame,
    title="Select key size in bytes:",
    options=["16", "24", "32"],
    marginY=(10, 0),
)

# -----

secretKeyInput2 = InputField(window=deBottomFrame, title="Enter secret key:")

# -----

cipherFormatSelection = SelectionBtn(
    window=deBottomFrame,
    title="Select original message format:",
    options=["Text", "File"],
)

# -----

originalFileType = TextField(
    window=deBottomFrame,
    title="Enter original file extension:",
    width=49,
    align="top",
)

# -----

decodeBtn = Btn(
    window=deBottomFrame,
    fileName="decode-btn.png",
    vpad=15,
)

showPage(homeFrame)
root.mainloop()
