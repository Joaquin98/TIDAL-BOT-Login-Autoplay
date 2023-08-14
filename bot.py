import pyautogui
import os
import pyperclip
import time


class Bot:

    user = ""
    password = ""
    IMAGES_FOLDER = '/Images/Login/'

    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
        pyautogui.PAUSE = 0.2

    def image(self, name):
        return self.IMAGES_FOLDER + name

    def start_browser(self):
        os.system(
            'C:\Program^ Files\Google\Chrome\Application\chrome.exe "https://listen.tidal.com/login?autoredirect=true&lang=es" --profile-directory="aaa" ')
        time.sleep(4)
    # screenWidth, screenHeight = pyautogui.size()
    # currentMouseX, currentMouseY = pyautogui.position()

    def login(self):
        button = list(pyautogui.locateAllOnScreen(self.image('button.png')))
        print(button)
        pyautogui.moveTo(self.image('button.png'))
        pyautogui.click(self.image('button.png'))
        user1, user2 = self.user.split('@')
        pyautogui.write(user1, interval=0.25)
        pyperclip.copy('@')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(user2, interval=0.25)
        pyautogui.moveTo(self.image('continue.png'))
        pyautogui.click()
        try:
            pyautogui.moveTo(self.image('password.png'))
            pyautogui.click()
        except Exception:
            try:
                pyautogui.moveTo(self.image('pass2.png'))
                pyautogui.click()
            except Exception:
                pyautogui.moveTo(self.image('pass3.png'))
                pyautogui.click()

        pyautogui.write(self.password, interval=0.25)
        pyautogui.moveTo(self.image('enter.png'))
        pyautogui.click()

# https://pyautogui.readthedocs.io/en/latest/quickstart.html


# start Chrome 'https://listen.tidal.com/login?autoredirect=true&lang=es'


bot = Bot("gitrejamla@gufum.com", "hellsaus1")
bot.start_browser()
bot.login()
