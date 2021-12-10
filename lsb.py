import numpy as np
from PIL import Image


class LSBEmbedding:
    def __init__(self) -> None:
        self.errorMessage = ""

    def embedMsg(self, fileName: str, message: bytes) -> None:
        print("image processing started")

        img = Image.open(fileName, 'r')

        print("image opened")

        width, height = img.size

        print("got image size")

        array = np.array(list(img.getdata()))

        print("got image pixel list")

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4
        total_pixels = array.size // n

        print("image processing done")

        message += b"$t3g0"
        b_message = ''
        for i in message:
            b_message += ''.join(bin(i)[2:])
            b_message += ''.join('00101100')
            b_message += ''.join('01001110')
            b_message += ''.join('01110011')

        req_pixels = len(b_message)

        print("message processing done")

        if req_pixels > total_pixels:
            self.errorMessage = "Error! Total pixels available is insufficient to store the secret message, need larger file."

        else:
            index = 0
            for p in range(total_pixels):
                for q in range(0, 3):
                    if index < req_pixels:
                        array[p][q] = int(
                            bin(array[p][q])[2:9] + b_message[index],
                            2,
                        )
                        index += 1
            print("lsb replacement done")

            array = array.reshape(height, width, n)
            enc_img = Image.fromarray(array.astype('uint8'), img.mode)

            print("new message embedding in image done")

            self.stegoFilePath = fileName.split(
                ".")[0] + "-enc." + fileName.split(".")[1]

            enc_img.save(self.stegoFilePath)

            print("encode image save")

    def extractMsg(self, fileName: str) -> None:
        print("image processing started")

        img = Image.open(fileName, 'r')

        print("image opened")

        array = np.array(list(img.getdata()))

        print("got image pixel list")

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        print("image processing done")

        hidden_bits = ""

        for p in range(total_pixels):
            for q in range(0, 3):
                hidden_bits += (bin(array[p][q])[2:][-1])

        print("hidden bit string extraction from lsb done")

        hidden_bits = [
            hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)
        ]

        print("convertion of hidden bit string into 8 bits arr done")

        message = ""

        for i in range(len(hidden_bits)):
            if message[-5:] == "$t3g0":
                break
            else:
                message += chr(int(hidden_bits[i], 2))

        print("convert of 8 bits arr into string message done")

        if "$t3g0" in message:
            self.embededMessage = bytes(message[2:], 'utf-8')
            self.embededMessage = bytes(message[:-5], 'utf-8')
        else:
            self.errorMessage = "No Hidden Message Found"