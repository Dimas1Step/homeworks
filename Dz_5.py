import colorama

from colorama import Fore, Back, Style
# функція Fore робить текст іншого кольору
# функція Back замальовую задній фон та по бажанню пише на ньому текст який був заданий у попередній функції Fore


print(Fore.LIGHTBLUE_EX)
print(Back.YELLOW + 'the upper part of the flag of Ukraine')
print(Fore.LIGHTYELLOW_EX)
print(Back.BLUE + 'the lower part of the flag of Ukraine')
print(Fore.GREEN)