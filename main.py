import os
import tkinter.messagebox
from tkinter import Canvas, Scrollbar, Tk, Frame, font
from aes import AESEncryptor
from components.btn import Btn
from components.file_chooser import FileChooser
from components.inputfield import InputField
from components.navbar import NavBar
from components.selection_btn import SelectionBtn
from components.show_label import ShowLabel
from components.textfield import TextField
from lsb import Lsb
import time
import cv2
import utils
from skimage import metrics

darkBgColor = "#222021"
ligthBgColor = "#282828"
fgColor = "#cccccc"


def showPage(frame: Frame) -> None:
    frame.tkraise()


def encode():
    start = time.time()
    if (plainFileChooser.fileFullPath == "" and plainTextInput.getValue() == ""
        ) or (plainFileChooser.fileFullPath != ""
              and plainTextInput.getValue() != "") or (
                  plainFileChooser.fileFullPath != "" and
                  (not os.path.exists(plainFileChooser.fileFullPath))):
        tkinter.messagebox.showerror(
            title="Error!",
            message="Please choose either plain file or enter plain text.",
        )
    elif (secretKeyInput1.inputField.getValue()
          == "") or len(secretKeyInput1.inputField.getValue()
                        ) != keySizeSelection.value.get():
        tkinter.messagebox.showerror(
            title="Error!",
            message="Please enter secret key of size 16, 24 or 32 bytes.",
        )
    elif coverImageChooser.fileFullPath == "" or (not os.path.exists(
            coverImageChooser.fileFullPath)):
        tkinter.messagebox.showerror(
            title="Error!",
            message="Please choose cover image.",
        )
    else:

        aes = AESEncryptor(secretKeyInput1.inputField.getValue())

        if plainFileChooser.fileFullPath != "":
            aes.encryptFile(plainFileChooser.fileFullPath)
        else:
            hideText = "ipt$:-" + plainTextInput.getValue()
            aes.encrypt(bytes(hideText, "utf-8"))

        # -----

        lsb = Lsb()

        lsb.hide(coverImageChooser.fileFullPath, aes.cipherText)

        end = time.time()

        if lsb.errorMessage == "":
            coverImgRef = cv2.imread(coverImageChooser.fileFullPath, 1)
            stegoImgRef = cv2.imread(lsb.stegoFilePath, 1)

            mse = metrics.mean_squared_error(coverImgRef, stegoImgRef)
            psnr = metrics.peak_signal_noise_ratio(coverImgRef,
                                                   stegoImgRef,
                                                   data_range=None)

            answer = tkinter.messagebox.askokcancel(
                title="Encoding successful",
                message="Do you want to view stego object ?" +
                "\n\nEmbedding Time: " + str(round(end - start, 2)) +
                " seconds" + "\n\nMean Squared Error: " + str(round(mse, 2)) +
                "\n\nPeak Signal to Noise Ratio: " + str(round(psnr, 2)) +
                " dB",
            )

            if answer:
                os.startfile(lsb.stegoFilePath)
        else:
            tkinter.messagebox.showerror(
                title="Error!",
                message=lsb.errorMessage + "\n\nEmbedding Time: " +
                str(end - start) + " seconds",
            )


def decode():
    start = time.time()
    if stegoObjectChooser.fileFullPath == "" or (not os.path.exists(
            stegoObjectChooser.fileFullPath)):
        tkinter.messagebox.showerror(
            title="Error!",
            message="Please choose stego object.",
        )
    elif (secretKeyInput2.getValue()
          == "") or (len(secretKeyInput2.getValue()) != 16
                     and len(secretKeyInput2.getValue()) != 24
                     and len(secretKeyInput2.getValue()) != 32):
        tkinter.messagebox.showerror(
            title="Error!",
            message="Please enter secret key of size 16, 24 or 32 bytes.",
        )
    else:

        lsb = Lsb()

        lsb.reveal(stegoObjectChooser.fileFullPath)

        # -----

        if lsb.errorMessage == "":

            aes = AESEncryptor(secretKeyInput2.getValue())

            aes.decrypt(lsb.embededMessage)

            if aes.errorMessage == "":
                if str(aes.plaintext)[2:].split("$:-")[0] == "ipt":

                    end = time.time()

                    tkinter.messagebox.showinfo(
                        title="Decoding successful",
                        message="Your Decoded Message is: " +
                        str(aes.plaintext, "utf-8").split("$:-")[1] +
                        "\n\nExtraction Time: " + str(round(end - start, 2)) +
                        " seconds",
                    )
                else:
                    originalFileName = str(aes.plaintext)[2:].split("$:-")[1]

                    originalFileExtension = str(
                        aes.plaintext)[2:].split("$:-")[2]

                    newFilePath = "/".join(
                        stegoObjectChooser.fileFullPath.split("/")[0:-1]
                    ) + "/" + originalFileName + "-dec" + originalFileExtension

                    with open(newFilePath, 'wb') as f1:
                        f1.write(aes.plaintext[aes.plaintext.rfind(b'$:-') +
                                               3:])

                    end = time.time()

                    answer = tkinter.messagebox.askokcancel(
                        title="Decoding successful",
                        message="Do you want to view decoded message ?" +
                        "\n\nExtraction Time: " + str(round(end - start, 2)) +
                        " seconds",
                    )

                    if answer:
                        os.startfile(newFilePath)
            else:

                end = time.time()

                tkinter.messagebox.showerror(
                    title="Error!",
                    message=aes.errorMessage + "\n\nExtraction Time: " +
                    str(round(end - start, 2)) + " seconds",
                )
        else:

            end = time.time()

            tkinter.messagebox.showerror(
                title="Error!",
                message=lsb.errorMessage + "\n\nExtraction Time: " +
                str(round(end - start, 2)) + " seconds",
            )


root = Tk()
root.title("Stego Image Creator | Project")
root.iconbitmap(utils.resource_path("assets/images/favicon.ico"))
root.geometry("490x625")
root.minsize(490, 625)
root.configure(bg=darkBgColor)
root.resizable(False, True)

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Poppins", size=12)
root.option_add("*Font", defaultFont)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

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
    dialogTitle="Select a plain file",
    title="Choose plain file:",
    fileImageName="file.png",
    fileTypes=(("All Files", "*.*"), ),
)

# -----

ShowLabel(
    window=enBottomFrame,
    text="OR",
    style=("Poppins", 12, font.BOLD),
    vAlign="n",
    marginY=(20, 0),
)

# -----

plainTextInput = TextField(
    window=enBottomFrame,
    title="Enter plain text:",
    height=3,
    width=46,
    align="top",
)

# -----

keySizeSelection = SelectionBtn(
    window=enBottomFrame,
    title="Select key size in bytes:",
    options=["16", "24", "32"],
)

# -----

secretKeyInput1 = InputField(
    window=enBottomFrame,
    title="Enter secret key:",
    stringSize=lambda: keySizeSelection.value.get(),
)

# -----

coverImageChooser = FileChooser(
    window=enBottomFrame,
    title="Choose cover image:",
    fileImageName="image.png",
    dialogTitle="Select a cover image",
    marginY=(18, 0),
    fileTypes=(
        ("PNG", "*.png"),
        ("JPEG", "*.jpg;*.jpeg"),
    ),
)

# -----

encodeBtn = Btn(window=enBottomFrame, fileName="encode-btn.png", marginY=18)
encodeBtn.btn.config(command=encode)

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
    dialogTitle="Select a stego object",
    title="Choose stego object:",
    fileImageName="image.png",
    fileTypes=(
        ("PNG", "*.png"),
        ("JPEG", "*.jpg;*.jpeg"),
    ),
)

# -----

secretKeyInput2 = TextField(
    window=deBottomFrame,
    title="Enter secret key:",
    width=46,
    align="top",
    marginY=(18, 0),
)

# -----

decodeBtn = Btn(window=deBottomFrame, fileName="decode-btn.png", marginY=18)
decodeBtn.btn.config(command=decode)

showPage(homeFrame)
root.mainloop()
