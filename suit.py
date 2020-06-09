import random
print('selamat datang di game suit')
print('pemain 2 adalah komputer')
computerChoice = ['batu','gunting','kertas']
def play(pilihan1, pilihan2):
    if (pilihan1 == pilihan2):
        print('seri, coba lagi lagi lha')
    elif pilihan1 == 'batu' != pilihan2 == 'kertas':
        print('kalah sama pc !')
    elif (pilihan1 == 'batu') != (pilihan2 == 'gunting'):
        print('mantap !')
    elif (pilihan1 == 'kertas') != (pilihan2 == 'gunting'):
        print('kalah sama pc !')
    elif (pilihan1 == 'kertas') != (pilihan2 == 'batu'):
        print('mantap !')
    elif (pilihan1 == 'gunting') != (pilihan2 == 'kertas'):
        print('kalah sama pc !')
    elif (pilihan1 == 'gunting') != (pilihan2 == 'batu'):
        print('mantap !')
    else:
        print('end')
computerChoice = random.choice(computerChoice)
pilihan2 = input('batu/gunting/kertas :')
pilihan2.upper()
play(pilihan2, computerChoice)
print(computerChoice)

