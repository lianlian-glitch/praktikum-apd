# num = int("42") # 42
# name = str(123) # "123"
# data = list("abc") # ['a', 'b', 'c']
# data = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num)) # <class 'int'>

# abs(-9) # 9
# max([1, 3, 7]) # 7
# min([1, 3, 7]) # 1
# round(3.14159,2) # 3.14
# sum([1, 2, 3]) # 6

# listAngka = [1, 23, 24, 12, 214, 8, 267]

# print(len(listAngka)) # menampilkan ada berapa elemen
# print(listAngka) # menapilakan apa aja isi darii fariabel tersebut
# a = "abc"
# print(len(a))

# pilihan = input("apakah anda ingin lanjut? (ya/tidak)").lower()
# if pilihan == "ya":
#     print("terimakasih telah menggunakan program kami.")
# elif pilihan == "tidak":
#     print("program lajut.")
# else:
#     print("input salah.")


# import math
# from math import sqrt
# import math as m

# import math
# print(math.sqrt(16))
# print(math.factorial(4))


# import inquirer
# pertanyaan = [
#     inquirer.List(
#     'size',
#     message="What size do you need?",
#     choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#     ),
# ]
# # mendapatkan jawaban
# answer = inquirer.prompt(pertanyaan)
# print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
# print(answer['size']) # Ambil value dari key 'size' (Large)

# import math as m
# print(math.m(16))
# print(math.factorial(4))


#######################################################################
# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

# import random
# pilih_acak = ["pisang", "rambutan", "manggis"]
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list

# import random
# acak = "apcb"
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka

# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize

# import random
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)
# # "hoki tadi, dapat 8844. anjay"

# import random
# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kar
#############################################################################


import inquirer
pertanyaan = [
inquirer.List(
'size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
]
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size']) # Ambil value dari key 'size' (Large)