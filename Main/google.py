import time
import pyautogui as auto
from auto import navegador as nav
def google(pesquisa):
    nav('google.com')
    time.sleep(1.5)
    auto.write(pesquisa)
    time.sleep(0.5)
    auto.press('enter')
