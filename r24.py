import pyautogui, os, time, sys


# Полное инфо об ОС 
your_os = sys.platform
print('Ваша ОС:', your_os)

# Получаем разрешение экрана
screen = pyautogui.size()
print('Экран:', screen)

class start:
    'Нужна ссылка которую будем открывать'
    def __init__(self, link):
        self.link = link

    def mac(self):
        'Открою ссылку в браузере'
        # Запускаем браузер с переданной ссылкой
        command = 'open %s' % self.link
        os.system(command)
        # time.sleep(5)
        # pyautogui.hotkey('ctrl', 'win', 'f')
        print('Запустил:', command)

    def win(self):
        'Открою ссылку в брвузере'
        # Запускаем браузер с переданной ссылкой
        FirefoxPortable = 'FirefoxPortable/FirefoxPortable.exe'
        if os.path.exists(FirefoxPortable) == True:
            command = '"start /max /b cmd /c "FirefoxPortable\FirefoxPortable.exe -kiosk %s""' % self.link
            run = os.system(command)
        else:
            command = '"start /max /b %s""' % self.link
            run = os.system(command)
        print('Запустил:', command)

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

if your_os == "darwin":
    # Передаем ссылку
    link = 'https://www.youtube.com/watch?v=8T9SFZDP60Q'
    # Запускаем браузер
    start(link).mac()
    time.sleep(10)
    click()
elif your_os == "win32":
    time.sleep(30)
    # Передаем ссылку
    link = 'https://www.youtube.com/watch?v=8T9SFZDP60Q'
    # Запускаем браузер
    start(link).win()
    time.sleep(90)
    click()
