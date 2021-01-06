import pyautogui, os, time, sys


class command:
    'Нужна ссылка которую будем открывать'
    def __init__(self, link):
        self.link = link

    def start(self, latency=30):
        'Сколько секунд подождать перед запуском?'
        # Инфо об ОС 
        your_os = sys.platform
        print('Ваша ОС:', your_os)

        print('Жду %s секунд' % latency)
        time.sleep(latency)

        if your_os == "darwin":
            # Запускаем браузер с переданной ссылкой
            command = 'open %s' % self.link
            os.system(command)
            print('Запустил:', command)

        elif your_os == "win32":
            FirefoxPortable = 'FirefoxPortable/FirefoxPortable.exe'

            # Запускаем браузер с переданной ссылкой
            if os.path.exists(FirefoxPortable) == True:
                command = '"start /max /b cmd /c "FirefoxPortable\FirefoxPortable.exe -kiosk %s""' % self.link
            else:
                command = '"start /max /b %s""' % self.link

            os.system(command)
            print('Запустил:', command)

        else:
            print('Операционная система %s не поддерживается' % your_os)

    def click(self, latency=60):
        'Сколько секунд подождать перед запуском?'

        # Получаем разрешение экрана
        screen = pyautogui.size()
        print('Экран:', screen)

        print('Жду %s секунд' % latency)
        time.sleep(latency)

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

link = 'https://www.youtube.com/watch?v=8T9SFZDP60Q'
command(link).start()
command(link).click()
