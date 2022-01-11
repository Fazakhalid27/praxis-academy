#3.1.1

#operasi matematika 
print(7 + 8)
print((50 + 5*6)/4)
print(90 / 9)

#operasi matematika tambahan
print(40 / 5)
print(97 // 4)
print(57 % 4)
print(7 + 9 * 2)

#pangkat
print(99 ** 2)

#penggunaan variable
width = 3 #penggunaan tanda (=) untuk memberikan value kepada variable.
height = 9
print(width * height)

#3.1.2

#penggunaan string
print('doesn\'t') #tanda \' digunakan utk memisahkan ('') utk string dengan tanda petik dalam kalimat
print("doesn't") #utk doble quotes tidak perlu menggunakan (\)

print('"Yes," they said')
print("\"Yes,\" they said")

s = 'orang pertama. \norang kedua'
print(s)

print(r'halo\semua\nama\saya\annie')

print("""nama = yusuf
kelas = 12
kota = Jakarta""")

#penggabungan string
print("cho" + "erry")

#penggandaan string
print(5*'kakakuk')

print("halo ini andien dan semua yang ada disini adalah temanku"
" yaitu rasha, irlan, fia dan indira")

#penggabungan variabel dengan string

kata_1 = "cho"
print(kata_1 + "erry")

#index

word = "ular"
print(word[3])
print(word[-1])
print(word[1:])
print(word[:3])
print('o'+word[1:])
print(len(word))

#3.1.3

#list

bola = [1, 2, 3, 4, 5]
print(bola)

#merubah nilai dalam list, menambah nilai, menghapus
bola[3] = 8
print(bola)
bola.append(9)
print(bola)
bola[2:4] = []
print(bola)

