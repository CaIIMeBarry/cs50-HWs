import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    available_fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        # Select a random font from the list of available fonts
        font_name = random.choice(available_fonts)
        figlet.setFont(font=font_name)

    elif len(sys.argv) == 3:
        if (sys.argv[1] not in ['-f', '--font']) or (sys.argv[2] not in available_fonts):
            print("Invalid usage")
            sys.exit(1)  # Exit with a non-zero status code to indicate an error

        font_name = sys.argv[2]
        figlet.setFont(font=font_name)
    else:
        print("Invalid usage")
        sys.exit(1) # Exit with an error

    user_text = input()
    print(figlet.renderText(user_text))


if __name__ == "__main__":
    main()
