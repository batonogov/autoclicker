import pyautogui
import os
import time


# Полное инфо об ОС 
your_os = os.uname()
print('Ваша ОС:', your_os[0])

# Получаем разрешение экрана
screen = pyautogui.size()
print('Экран:', screen)

def start_chrome_mac():
    # Запускаем браузер с необходимой страницей
    run = 'open -a "Safari" "https://www.youtube.com/watch?v=8T9SFZDP60Q"'
    os.system(run)
    # time.sleep(5)
    # pyautogui.hotkey('ctrl', 'win', 'f')
    print('Запустил:', run)

def start_chrome_win():
    # Запускаем браузер с необходимой страницей
    run = '"start /max /b cmd /c ""C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk" -kiosk https://www.youtube.com/watch?v=8T9SFZDP60Q""'
    os.system(run)
    print('Запустил:', run)

# # Закрываем всплывающее окно восстановления
# print('Ищу крестик')
# if os.path.exists('cross.png') == True:
#     cross = pyautogui.locateCenterOnScreen('cross.png')
#     print('Файл cross.png на месте')
#     if cross != None:
#         print('Нашел крестик тут:', cross)
#         pyautogui.moveTo (cross, duration = 0)
#         pyautogui.click(button='left', clicks=1, interval=0.0)
# else:
#     print('Файл cross.png не найден!')

# # Закрываем рекламу premium
# print('Ищу кнопки')
# if os.path.exists('premium_white.png') == True:
#     premium = pyautogui.locateCenterOnScreen('premium_white.png')
#     print('premium_white =', premium)
#     if premium != None:
#         pyautogui.moveTo (premium, duration = 0)
#         pyautogui.click(button='left', clicks=1, interval=0.0)

# if os.path.exists('premium_dark.png') == True:
#     premium = pyautogui.locateCenterOnScreen('premium_dark.png')
#     print('premium_dark =', premium)
#     if premium != None:
#         pyautogui.moveTo (premium, duration = 0)
#         pyautogui.click(button='left', clicks=1, interval=0.0)

def click():
    # Передвигаем курсор в нужное место
    x1, y1 = screen[0] / 4, screen[1] / 4
    pyautogui.moveTo (x1, y1, duration = 0)
    print('Передвинул курсор:', x1, y1)

    # Двойной клик для полноэкранного режима
    pyautogui.click(button='left', clicks=2, interval=0.0)
    print('Дважды кликнул')

    # Прибавляем громкость в системе
    pyautogui.press('volumeup', presses=50) 
    # И в ютубе
    pyautogui.press('up', presses=20)

# # Убиваю хром
# print('Убиваю хром')
# # time.sleep(10)
# os.system('taskkill /F /IM chrome.exe /T')

if your_os[0] == "Darwin":
    # Запускаем браузер
    start_chrome_mac()
elif your_os[0] == "win32":
    # Запускаем браузер
    start_chrome_win()
