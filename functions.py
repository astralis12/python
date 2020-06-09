# def area(radius) :
#    return(3.142 * radius * radius)

# def vol(area,length) :
#    print(area * length)

# radius = int(input('masukkan angka nya :'))
# length = int(input('enter a length:'))

# vol(area(radius),length)


# def awal():
#    print('compute pay')
#    print('====')

# #def tanya():
#    nama = input('siapakah nama pegawai')
# jam = int(input('berapa jam kerja'))
#    biaya = int(input('berapa biaya per jam'))

#    return nama, jam ,biaya

# def compute_pay(jam, biaya):
#    if jam > 10:
#        return jam * biaya + 100
#    else :
#        return jam * biaya 
    
# def run():
#    awal()
#    nama, jam, biaya = tanya()
#    gaji = compute_pay(jam, biaya)
#     print(f"{nama} bekerja selama {jam} jam dan mendapatkan gaji {gaji} ")

# run()

# def halo():
#    global nama
#    nama = 'edu'
#    print(f"halo {nama}")

# halo()
# print(f"halo {nama}")


# def greet(name = 'ryu', time = 'morning'):
#     print(f'good {time} {name}, fuck u')

# # x = input('ur name:')
# # y = input('what time:')

# greet('jame')

# def area(radius):
#     return 3.142 * radius * radius

# def volume(area, length):
#     print(area * length)


# radius = int(input("radius :"))
# length = int(input('length :'))




# volume(area(radius), length)

def area(radius):
    return (3.14 * radius * radius)

def vol(area, length):
    print(area * length)

radius = int(input('berapa radius nya :'))
length = int(input("length :"))


vol(area(radius), length)