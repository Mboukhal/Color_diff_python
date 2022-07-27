
"""
Colors class:reset all colors with colors.reset; two
sub classes fg for foreground
and bg for background; use as colors.subclass.colorname.
i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
underline, reverse, strike through,
and invisible work with the main class i.e. colors.bold
"""

class colors:

    NC = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'
 
    class fg:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHTGREY = '\033[37m'
        DARKGREY = '\033[90m'
        LIGHTRED = '\033[91m'
        LIGHTGREEN = '\033[92m'
        YELLOW = '\033[93m'
        LIGHTBLUE = '\033[94m'
        PINK = '\033[95m'
        LIGHTCYAN = '\033[96m'

    class bg:
        BLACK = '\033[40m'
        RED = '\033[41m'
        GREEN = '\033[42m'
        ORANGE = '\033[43m'
        BLUE = '\033[44m'
        PURPLE = '\033[45m'
        CYAN = '\033[46m'
        LIGHTGREY = '\033[47m'
 
# print(colors.bg.green, "SKk", colors.fg.red, "Amartya")
# print(colors.bg.lightgrey, "SKk", colors.fg.red,