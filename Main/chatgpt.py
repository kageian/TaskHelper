import pyautogui as auto
import time
from auto import navegador as nav
def chatgpt(pesquisa):
    nav('chatgpt.com')
    time.sleep(2)
    auto.write(pesquisa)
    time.sleep(0.5)
    auto.press('enter')
