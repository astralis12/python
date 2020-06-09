# murid = {}

# def biodata(): 
#     nama = input('apakah nama dia:')
#     usia = input('berapa umur anda:')
#     rumah = input('dimana anda tinggal:')

#     return nama, usia, rumah

# def vertikal(students):
#     for student in students:
#         for key, value in student.items():
#             print(key, value)

# while True:
#     murid = {}
#     nama, usia, rumah = biodata()
#     murid['nama'] : nama
#     murid['usia'] : usia
#     murid['rumah'] : rumah

#     student.append(murid)
#     #print(student)

#     lagi = input('mau nambah lagi atau kgk ? (y/n)')
#     if lagi == 'y':
#         continue
#     else:
#         break

# vertikal(student)
def ninja_info(dictionary):
    for key, val in dictionary.items():
        print(f'i am {key} and i am a {val} belt')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter belt color :')
    ninja_belts[ninja_name] = ninja_belt
    
    another = input('do you want to add some more ? (y/n)')
    if another == 'y':
        continue
    else:
        break
    
ninja_info(ninja_belts)