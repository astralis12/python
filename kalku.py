number1 = int(input('masukkan angka pertama'))
number2 = int(input('masukkan angka kedua'))
angka1 = number1
angka2 = number2
print('angka pertama adalah', angka1)
print('angka kedua adalah', angka2)
print('operasi perkalian dengan angka 1' )
print('operasi pembagian dengan angka 2')
print('operasi pertambahan dengan angka 3')
print('operasi pengurangan dengan angka 4')

#cek lagi ini
operasi = int(input('operasi yang dipilih dalam angka'))

if operasi == 1:
    hasil = (number1 * number2)
    print(hasil)
elif operasi == 2:
    hasil = (number1 / number2)
    print(hasil)
elif operasi == 3:
    hasil = (number1 + number2)
    print(hasil)
#cek lagi ini
elif operasi == 4:
    hasil = (number1 - number2)
    print(hasil)

