import pyautogui
import os
import pyperclip
import time


class Bot:

    user = ""
    password = ""
    IMAGES_FOLDER = './Images/Login/'
    DEBUG = True

    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
        pyautogui.PAUSE = 0.2

    def image(self, name):
        return self.IMAGES_FOLDER + name

    def info(self, data):
        if self.DEBUG:
            print(data)

    def start_browser(self):
        os.system(
            'C:\Program^ Files\Google\Chrome\Application\chrome.exe "https://listen.tidal.com/login?autoredirect=true&lang=es" --profile-directory="aaa" ')
        time.sleep(4)

    def complete_user(self):

        screenWidth, screenHeight = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()

        image = ''

        image = 'user_not_clicked.png'
        if len(list(pyautogui.locateAllOnScreen(self.image(image)))):
            self.info(image)
        else:
            image = 'user_clicked.png'
            pyautogui.locateAllOnScreen(self.image(image))
            self.info(image)

        self.info(self.image(image))
        pyautogui.moveTo(self.image(image))
        # pyautogui.click(self.image(image))
        user1, user2 = self.user.split('@')
        pyautogui.write(user1, interval=0.25)
        pyperclip.copy('@')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(user2, interval=0.25)

        pyautogui.moveTo(self.image('continue.png'))
        pyautogui.click()

    def complete_password(self):
        try:
            pyautogui.moveTo(self.image('password_not_clicked.png'))
            pyautogui.click()
        except Exception:
            try:
                pyautogui.moveTo(self.image('password_clicked.png'))
                pyautogui.click()
            except Exception:
                pyautogui.moveTo(self.image('password_clicked_bar.png'))
                pyautogui.click()

        pyautogui.write(self.password, interval=0.25)
        pyautogui.moveTo(self.image('enter.png'))
        pyautogui.click()

    def login(self):

        self.complete_user()
        self.complete_password()


# https://pyautogui.readthedocs.io/en/latest/quickstart.html


# start Chrome 'https://listen.tidal.com/login?autoredirect=true&lang=es'

bot = Bot("gitrejamla@gufum.com", "hellsaus1")
bot.start_browser()
bot.login()
