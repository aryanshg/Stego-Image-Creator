from PIL import Image
from struct import pack


class Lsb:
    def __init__(self) -> None:
        self.errorMessage = ""

    def hide(self, fileName: str, message: bytes) -> None:
        messageLength = len(message)
        if messageLength == 0:
            self.errorMessage = "Message length is zero."
        else:
            img = Image.open(fileName)
            if img.mode not in ["RGB", "RGBA"]:
                self.errorMessage = "Not a RGB image."
            else:
                imgCopy = img.copy()
                width, height = img.size
                index = 0

                message += b'$t3g0'
                # message string to binary string
                messageBits = "".join([bin(i)[2:].zfill(8) for i in message])
                messageBitsLength = len(messageBits)

                noOfPixels = width * height

                if messageBitsLength > noOfPixels * 3:
                    self.errorMessage = "The message you want to hide is too long."
                else:
                    for row in range(height):
                        for col in range(width):
                            if index + 3 <= messageBitsLength:

                                # Get the colour component.
                                pixel = img.getpixel((col, row))
                                r = pixel[0]
                                g = pixel[1]
                                b = pixel[2]

                                # Change the Least Significant Bit of each colour component.
                                r = int(bin(r)[:-1] + messageBits[index], 2)
                                g = int(
                                    bin(g)[:-1] + messageBits[index + 1], 2)
                                b = int(
                                    bin(b)[:-1] + messageBits[index + 2], 2)

                                # Save the new pixel
                                if img.mode == "RGBA":
                                    imgCopy.putpixel((col, row),
                                                     (r, g, b, pixel[3]))
                                else:
                                    imgCopy.putpixel((col, row), (r, g, b))

                                index += 3
                            else:
                                break

                    img.close()

                    self.stegoFilePath = fileName.split(
                        ".")[0] + "-enc." + fileName.split(".")[1]

                    imgCopy.save(self.stegoFilePath)

    def reveal(self, fileName: str) -> None:
        img = Image.open(fileName)
        if img.mode not in ["RGB", "RGBA"]:
            self.errorMessage = "Not a RGB image."
        else:
            width, height = img.size
            hiddenBits = ""
            self.isSecretMsgExist = False

            for row in range(height):
                for col in range(width):
                    # pixel = [r, g, b] or [r,g,b,a]
                    pixel = img.getpixel((col, row))

                    if img.mode == "RGBA":
                        pixel = pixel[:3]  # ignore the alpha

                    for color in pixel:
                        hiddenBits += bin(color)[-1]

                    if len(hiddenBits) % 8 == 0:
                        # hidden bits string to 8 bit string list
                        hiddenBitsList = [
                            hiddenBits[i:i + 8]
                            for i in range(0, len(hiddenBits), 8)
                        ]

                        self.embededMessage = b''
                        self.isSecretMsgExist = False

                        for i in hiddenBitsList:
                            if self.embededMessage[-5:] == b'$t3g0':
                                self.isSecretMsgExist = True
                                break
                            else:
                                self.embededMessage += pack('B', int(i, 2))

                    if self.isSecretMsgExist:
                        break

                if self.isSecretMsgExist:
                    break

            img.close()

            if not self.isSecretMsgExist:
                self.errorMessage = "No Hidden Message Found"
            else:
                self.embededMessage = self.embededMessage[:-5]
