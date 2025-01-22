import time
import pyautogui as auto
from auto import navegador as nav
def youtube(pesquisa):
    nav('Youtube.com')
    time.sleep(3)
    for c in range(0, 4):
        auto.press('tab')
    auto.write(pesquisa)
    auto.press('enter')
