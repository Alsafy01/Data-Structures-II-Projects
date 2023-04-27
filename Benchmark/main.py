from AppOpener import open, close
import pyautogui
import time


def detect_image(image):
    while True:
        try:
            location = pyautogui.locateOnScreen(image)
            return
        except Exception as e:
            pass



def bechmark(app_name):

    match app_name:
        case "whatsapp":
            image = "img.png"
        case "teams":
            image = "img.png"
        case "chrome":
            image = "img.png"
        case "edge":
            image = "img.png"
        case "netbeans":
            image = "img.png"

    open(app_name)
    start = time.time()
    detect_image(image)
    end = time.time()
    close(app_name)

    return end - start


print(bechmark("whatsapp"))