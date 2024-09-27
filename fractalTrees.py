import os
import math
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_tree(x, y, length, angle, depth):
    if depth == 0:
        return

    x_end = x + int(math.cos(math.radians(angle)) * length)
    y_end = y + int(math.sin(math.radians(angle)) * length)

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(int(length)):
        x_current = x + int(math.cos(math.radians(angle)) * i)
        y_current = y + int(math.sin(math.radians(angle)) * i)
        print('\033[92m*\033[0m', end='')
        time.sleep(0.005)
    print()
    draw_tree(x_end, y_end, length*0.7, angle-20, depth-1)
    draw_tree(x_end, y_end, length*0.7, angle+20, depth-1)

def main():
    clear_screen()
    width, height = os.get_terminal_size()
    trunk_length = height // 2
    draw_tree(width // 2, 0, trunk_length, 90, 8)

if __name__ == "__main__":
    main()
