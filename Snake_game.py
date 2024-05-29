import os
import time
import random

# Setările inițiale ale jocului
width, height = 40, 20
snake = [(5, 5)]
direction = (0, 1)  # Inițial șarpele merge spre dreapta
food = (random.randint(1, height - 2), random.randint(1, width - 2))
score = 0

def print_board():
    os.system('cls')  # Curăță ecranul
    for i in range(height):
        for j in range(width):
            if (i, j) == food:
                print('*', end='')
            elif (i, j) in snake:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(f'Score: {score}')

def move_snake():
    global food, score
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Verificare coliziune cu marginea sau corpul șarpelui
    if (new_head[0] in [0, height-1] or
        new_head[1] in [0, width-1] or
        new_head in snake[1:]):
        return False

    # Verificare dacă a mâncat mâncarea
    if new_head == food:
        score += 1
        food = (random.randint(1, height - 2), random.randint(1, width - 2))
    else:
        snake.pop()

    return True

def change_direction(new_direction):
    global direction
    # Evităm întoarcerea în direcția opusă
    if (new_direction[0] * -1, new_direction[1] * -1) != direction:
        direction = new_direction

def get_key():
       # Citirea comenzilor de la utilizator
    try:
        import msvcrt  # Pentru Windows
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
    except ImportError:
        import sys, termios, tty  # Pentru Unix
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None

# Bucla principală a jocului
while True:
    print_board()
    time.sleep(0.1)

    key = get_key()
    
    if key == 'w':
        change_direction((-1, 0))  # Sus
    elif key == 's':
        change_direction((1, 0))  # Jos
    elif key == 'a':
        change_direction((0, -1))  # Stânga
    elif key == 'd':
        change_direction((0, 1))  # Dreapta

    if not move_snake():
         break

print("Game Over! Final score:", score)