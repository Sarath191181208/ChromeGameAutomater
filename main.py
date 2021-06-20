import pyautogui
from PIL import Image, ImageGrab
import time


def hitKey(key: str) -> None:
    pyautogui.keyDown(key)
    return


def printRange(img) -> None:
    data = img.load()
    # checking for cactus
    # i is the detection range width
    for i in range(250, 260):
        # j is length
        for j in range(460, 480):
            data[i, j] = 0
    # checking for birds
    for i in range(200, 210):
        for j in range(390, 400):
            data[i, j] = 120

    img.show()


def play(img) -> None:
    for i in range(250, 260):
        # j is length
        for j in range(460, 480):
            if img[i, j] < 100:
                hitKey('up')
                return

    for i in range(200, 210):
        for j in range(390, 400):
            if img[i, j] < 100:
                hitKey('down')
                return


if __name__ == '__main__':
    time.sleep(2)
    while True:
        play(ImageGrab.grab().convert('L').load())
#        printRange(ImageGrab.grab().convert('L'))
#       break
