import sys
import random

def get_number(message):
    sys.stdout.buffer.write(message.encode())
    sys.stdout.flush()
    return int(sys.stdin.buffer.readline().decode().strip())

min_number = get_number('Please input minimum number.\n')
max_number = get_number('Please input maximum number.\n')

guess_number = random.randint(min_number, max_number)

for i in range(3):
    number = get_number('Guess the number.\n')
    if number == guess_number:
        print('Correct! You win!!')
        break
else:
    print('You lose. The number is', guess_number)