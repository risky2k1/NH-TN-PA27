import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dancing_fan():
    frames = [
        "      o/\n     /| \n     / \ ",
        "      o\n     /|>\n     / \ ",
        "     \o\n      |\n     / \ ",
        "      o\n     <|\n     / \ "
    ]

    try:
        while True:
            for frame in frames:
                clear_screen()
                print(frame)
                time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nMúa quạt dừng lại!")

dancing_fan()