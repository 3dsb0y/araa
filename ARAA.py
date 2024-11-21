from pydirectinput import keyUp, keyDown, press, write, leftClick, position
from colorama import init, Fore, Style
from shutil import get_terminal_size
from random import randint, choice
from urllib.request import urlopen
from datetime import datetime
from ctypes import windll
from time import sleep
from json import load

class ARAA:
    def __init__(self):
        self.ver = "1.9"
        self.config = None
        self.actions_map = {
            "spin_camera": [self.rand_1, self.rand_2],
            "jumps": self.rand_3,
            "clicking": self.rand_4,
            "move_around": [self.rand_5, self.rand_11],
            "writing": self.rand_6,
            "emotes": [self.rand_7, self.rand_8, self.rand_9],
            "chat_commands": [self.rand_10, self.rand_13,],
            "check_menu": self.rand_12,
        }
        self.title = f"ARAA (Adaptive Randomized Anti-AFK), version {self.ver}"
        init(autoreset=True)  # colorama fix

    def set_console_title(self, title):
        windll.kernel32.SetConsoleTitleW(title)
    
    def load_config(self):
        try:
            with open('araa_config.json') as f:
                self.config = load(f)
                self.print_centered(f"Конфиг загружен!", Fore.LIGHTGREEN_EX)
        except FileNotFoundError:
            self.print_centered(f"Конфиг не найден! Выход!", Fore.RED)
            sleep(2)
            exit()

    def get_remote_version(self):
        url = "http://raw.githubusercontent.com/nwsynx/araa/main/ver.txt"
        try:
            with urlopen(url) as response:
                return response.read().decode('utf-8').strip()
        except Exception as e:
            self.print_centered(f"Ошибка при получении версии: {e}", Fore.RED)
            return "Ошибка при получении версии"

    def check_version(self):
        remote_version = self.get_remote_version()
        if remote_version:
            if self.ver == remote_version:
                self.print_centered(f"Используется последняя версия: {self.ver}", Fore.GREEN)
                print("\n")
            else:
                self.print_centered(f"У вас устаревшая версия {self.ver}. Актуальная версия: {remote_version}\n\n\n", Fore.RED)
                print("\n")

    def betterprint(self, text):
        print(f"{datetime.now().strftime('%H:%M:%S')} [{Fore.GREEN}*{Fore.WHITE}]: {text}")

    def updprint(self, text, end=False):
        color = Fore.GREEN if end else Fore.YELLOW
        print(f"\r{datetime.now().strftime('%H:%M:%S')} [{color}*{Fore.WHITE}]: {text}", end="", flush=True)

    def print_centered(self, text, color=Fore.WHITE):
        terminal_width, _ = get_terminal_size()
        print(color + text.center(terminal_width) + Style.RESET_ALL)

    def random_string(self, length):
        letters = self.config["option_settings"]["writing"]["strings"]
        return ''.join(choice(letters) for _ in range(length))

    def execute_random_action(self):
        available_actions = []

        options = self.config["options_mode"]
        for action, enabled in options.items():
            if enabled:
                if isinstance(self.actions_map[action], list):
                    available_actions.extend(self.actions_map[action])
                else:
                    available_actions.append(self.actions_map[action])

        if not available_actions:
            self.betterprint("Нет доступных действий в конфиге.")
            return

        action = choice(available_actions)
        if callable(action):
            action()
        else:
            self.betterprint("Выбранное действие не может быть выполнено.")

    # 

    def rand_1(self):
        a = randint(self.config["option_settings"]["spin_camera"]["minimum"], self.config["option_settings"]["spin_camera"]["maximum"])
        self.betterprint(f"Кручу камеру влево {a} секунд")
        keyDown('left')
        sleep(a)
        keyUp('left')

    def rand_2(self):
        a = randint(self.config["option_settings"]["spin_camera"]["minimum"], self.config["option_settings"]["spin_camera"]["maximum"])
        self.betterprint(f"Кручу камеру вправо {a} секунд")
        keyDown('right')
        sleep(a)
        keyUp('right')

    def rand_3(self):
        jumps = randint(self.config["option_settings"]["jumps"]["minimum"], self.config["option_settings"]["jumps"]["maximum"])
        self.betterprint(f"Прыгаю {jumps} раз")
        while jumps > 0:
            jumps -= 1
            sleep(1)
            press('space', interval=self.config["option_settings"]["jumps"]["interval"])
        
    def rand_4(self):
        a = randint(self.config["option_settings"]["clicking"]["minimum"], self.config["option_settings"]["clicking"]["maximum"])
        self.betterprint(f"Нажимаю {a} раз")
        while a > 0:
            a -= 1
            sleep(randint(0, 2))
            leftClick(interval=self.config["option_settings"]["clicking"]["interval"], duration=self.config["option_settings"]["clicking"]["duration"])

    def rand_5(self):
        self.betterprint("Двигаюсь по сторонам слегка")
        press("a")
        sleep(0.2)
        press("d")
    
    def rand_6(self):
        a = self.random_string(randint(8, 24))
        self.betterprint(f"Печатаю {a}")
        write(a, interval=self.config["option_settings"]["writing"]["interval"])
    
    def rand_7(self):
        self.betterprint(f"Танцую dance2")
        write("/")
        sleep(0.67)
        write('/e dance2')
        sleep(1.7)
        press('enter')
    
    def rand_8(self):
        self.betterprint(f"Танцую dance")
        write("/")
        sleep(0.67)
        write('/e dance')
        sleep(1.7)
        press('enter')
    
    def rand_9(self):
        self.betterprint(f"Показываю жест wave")
        write("/")
        sleep(0.67)
        write('/e wave')
        sleep(1.7)
        press('enter')
    
    def rand_10(self):
        self.betterprint(f"Чищю чат")
        write("/")
        sleep(0.67)
        write('/clear')
        sleep(1.7)
        press('enter')
    
    def rand_11(self):
        self.betterprint("Двигаюсь вперед-назад")
        press("w")
        sleep(0.2)
        press("s")
    
    def rand_12(self):
        self.betterprint("Посмотрю меню")
        press("escape")
        sleep(2)
        press("escape")
    
    def rand_13(self):
        self.betterprint("Напишу /help")
        write(f"/")
        sleep(1.5)
        write(f"/help {self.random_string(16)}")
        sleep(1.5)
        press("enter")

    def premain(self): # cringe
        self.set_console_title(self.title)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.print_centered("_____________________________ ")
        self.print_centered("___    |__  __ \__    |__    |")
        self.print_centered("__  /| |_  /_/ /_  /| |_  /| |")
        self.print_centered("_  ___ |  _, _/_  ___ |  ___ |")
        self.print_centered("/_/  |_/_/ |_| /_/  |_/_/  |_|")
        self.print_centered("Adaptive Randomized Anti-AFK\n")
        self.print_centered("by nwsynx (funpay: xGerman)")
        self.print_centered("Данная программа не подлежит будущей перепродажи!", Fore.RED)
        self.print_centered("Если вы купили эту программу не у xGerman - Возвращайте деньги!", Fore.RED)
        print("\n")
        self.load_config()
        print("\n")
        self.check_version()
        print("\n")
        self.main()

    def main(self):
        try:
            for remaining_time in range(5, 0, -1):
                self.updprint(f"Начну работу через {remaining_time} секунд")
                sleep(1)
            self.updprint("Начинаю работу                                           ", True)  # чтобы не слиплись буквы
            print()

            while True:
                self.set_console_title(self.title+" | Status: Working")
                self.execute_random_action()

                sleep_time = randint(self.config["sleep_minimum"], self.config["sleep_maximum"])
                self.set_console_title(self.title + " | Status: Sleeping")

                for remaining_time in range(sleep_time, 0, -1):
                    self.updprint(f"Сплю {remaining_time} секунд           ")
                    sleep(1)

                self.updprint("Проснулся                  ", True)
                print()
                self.set_console_title(self.title + " | Status: Woke up")

        except KeyboardInterrupt:
            print()  # Fix
            self.print_centered("Работа приостановлена, нажмите Enter чтобы продолжить.")
            input()
            self.main()

if __name__ == "__main__":
    araa = ARAA()
    araa.premain()
