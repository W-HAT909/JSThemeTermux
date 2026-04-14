# AUTHOR       : SadBit08
# TOOL NAME    : JSTheme
# ABOUT TOOL   : Termux JakartaSecTeam Theme
# CODE EDITORS : Nano, Micro, NeoVim
# LANGUANGE    : Python3
# VERSION      : Python 3.13.13
# PLATFORMS    : Termux(Terminal Linux)
# CODED IN TIME: Selasa, 14 - April - 2026 | J.S.T SAD THEME
import os
import sys
import time
import shutil
import pyfiglet
import subprocess
from datetime import datetime
from rich import box
from rich.text import Text
from rich.align import Align
from rich.style import Style
from rich.panel import Panel
from rich.console import Console


# CONSOLE DEFINITION
console = Console()


# TERMINAL COLUMN
column = os.get_terminal_size().columns


# ANSII ESCAPE BOLD COLORS
BLACK = "\033[1;30m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"


# CLEAN TERMINAL SCREEN
def clear():
    os.system("clear")
    

# TIME NOW
def today():
    time_now = datetime.now()
    date = f"{time_now.strftime('%A, %d - %Y | %I:%M:%S.%p')}"
    return date


# DISPLAY FEATURES
class SetDisplay:
    @staticmethod
    def ShowImage(img: str):
        os.system(f"catimg {img}")

    @staticmethod
    def ShowFiglet(text: str):
        text_figlet = pyfiglet.figlet_format(text, font="ansi_shadow").rstrip()
        return text_figlet

    @staticmethod
    def ShowBorderText(text: str, font_style: str = "none", color_text: str = "none", border_color: str = "none"):
        border = Panel(
            Align.center(Text(f"{text}", style=f"{font_style} {color_text}")),
            width=column,
            border_style=border_color, box=box.DOUBLE_EDGE,
        )
        BorderText = Align.center(border)
        console.print(BorderText)

    @staticmethod
    def ShowBorderFiglet(text: str, title: str = "", subtitle: str = "", color_text: str = "bold green", border_color: str = "bold white", color_title: str = "bold green", color_subtitle: str = "bold green", font_style: str = None):
        if color_text and font_style is None:
            font_style = color_text

        border = Panel(
            Align.center(Text(f"{text}", style=f"{font_style} {color_text}")),
            width=column,
            border_style=border_color, box=box.DOUBLE_EDGE,
            title=f"[{color_title}]{title}[/{color_title}]",
            subtitle=f"[{color_subtitle}]{subtitle}[/{color_subtitle}]"
        )
        BorderText = Align(border)
        console.print(BorderText)

    @staticmethod
    def ShowLoad():
        width = shutil.get_terminal_size().columns - 10

        total = 100

        for i in range(total + 1):
            filled = int(width * i / total)
            bar = f"{GREEN}█" * filled + "-" * (width - filled)
            percent = f"{i}%"

            sys.stdout.write(f"\r[{bar}] {percent}")
            sys.stdout.flush()
            time.sleep(0.02)

        print()


# SHOW THEME
def display_theme():
    clear()
    SetDisplay.ShowImage("~/../usr/etc/JSTheme/logo/JakartaSecTeam.jpg")
    figlet = SetDisplay.ShowFiglet("J.S.T")
    SetDisplay.ShowBorderFiglet(figlet, "JakartaSecTeam", "DARK THEME", "bold red", "bold blue", "bold purple", "bold black on cyan")
    SetDisplay.ShowBorderText('"Kami JakartaSecTeam, kami selalu di sini, kami selalu ada, kami selalu memperbaiki, untuk kebebasan, keadilan, kemanusiaan."', "italic", "bold green", "bold red1")
    now = today()
    SetDisplay.ShowBorderText(now, "underline", "bold white", "bold orange1")
    SetDisplay.ShowBorderText("Selamat datang di terminal linux, Anda adalah anonymous!", "bold", "green1", "pale_turquoise1")


# MAIN PROGRAM
def main():
    clear()
    text = SetDisplay.ShowFiglet("WAIT")
    console.print(Align.center(Text(text, style="bold yellow")))
    SetDisplay.ShowLoad()
    display_theme()


# RUN MAIN PROGRAM
if __name__ == "__main__":
    main()






