import array

from AppOpener import open, close
import pyautogui
import time


def detect_image(image):
    while True:
        try:
            location = pyautogui.locateOnScreen(image)
            if(location != None):
                print(location)
                return
        except Exception as e:
            pass


def benchmark(app_name):
    a = []
    match app_name:
        case "whatsapp":
            image = "whatsapp.png"
        case "onenote":
            image = "onenote.png"
        case "discord":
            image = "discord.png"
        case "excel":
            image = "excel.png"
        case "codeblocks":
            image = "codeblocks.png"
    for i in range(0, 5):
        open(app_name)
        start = time.time()
        detect_image(image)
        end = time.time()
        close(app_name)
        time.sleep(1)
        a.append(end - start)
    return a


apps = ["whatsapp", "codeblocks", "excel", "onenote", "discord"]
a = []
for j in apps:
    a.append(benchmark(j))

for i in range(0, 5):
    print(f"{apps[i]} time = {a[i]}")
