
class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

print(TextColors.RED + "This is red text." + TextColors.RESET)
print(TextColors.GREEN + "This is green text." + TextColors.RESET)
print(TextColors.BLUE + "This is red text." + TextColors.RESET)
print(TextColors.MAGENTA + "This is green text." + TextColors.RESET)
print(TextColors.CYAN + "This is red text." + TextColors.RESET)
print(TextColors.YELLOW + "This is yellow text." + TextColors.RESET)