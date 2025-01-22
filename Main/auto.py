import pyautogui as auto
import time
def navegador (url):
    auto.press('win')
    time.sleep(1.5)
    auto.write('opera')
    time.sleep(0.5)
    auto.press('enter')
    time.sleep(1.5)
    auto.write(url)
    time.sleep(0.5)
    auto.press('enter')
