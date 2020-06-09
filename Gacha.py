import random

print('selamat datang')
dice = input('do u want to roll the dice ? (y/n)')
seed = int(input ('masukkan seed number:'))
random.seed(seed)
if dice == 'y':
    print('random:', random.randint(1,6))
else:
        print('')