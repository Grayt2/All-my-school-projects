#https://github.com/lucars1
#⠀     ⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢰⣿⡿⠗⠀⠠⠄⡀⠀⠀⠀⠀
#⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⠈⠑⢶⣶⡄
#⢀⣶⣦⣸⠀⢼⣟⡇⠀⠀⢀⣀⠀⠘⡿⠃
#⠀⢿⣿⣿⣄⠒⠀⠠⢶⡂⢫⣿⢇⢀⠃⠀
#⠀⠈⠻⣿⣿⣿⣶⣤⣀⣀⣀⣂⡠⠊⠀⠀
#⠀⠀⠀⠃⠀⠀⠉⠙⠛⠿⣿⣿⣧⠀⠀⠀
#⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀
#⠀⠀⠀⣷⣄⡀⠀⠀⠀⢀⣴⡟⠿⠃⠀⠀
#⠀⠀⠀⢻⣿⣿⠉⠉⢹⣿⣿⠁⠀⠀⠀⠀
#⠀⠀⠀ ⠉⠁⠀⠀⠀⠉⠁⠀⠀⠀
import winsound
import random

ran = random.randint(1, 10)
int(ran)
for i in range(0, 10):
    #print(ran) # remover first '#' if you want to see the number!
    guess = int(input('what is your guess?: '))
    int(guess)
    if ran != guess:
        winsound.PlaySound('check-mark_oPG7Xo5.wav', winsound.SND_FILENAME)
        print('WRONG')
    if guess == ran:
        print('waza you did it!')
        exit()
    