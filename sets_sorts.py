def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input('enter the name')
    ninja_belt = input('what belt')
    ninja_belts[ninja_name] = ninja_belt

    another = input('input another one ? (y/n)')
    if another == 'y':
        continue
    else:
        break

belt_count(ninja_belts)
