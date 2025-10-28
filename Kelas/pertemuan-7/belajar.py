# def nama():
#     print("Hallo guys, namaku Lilly")
# def perkalian():
#     Y = 10*7
#     print(Y)
# def  tambah():
#     X =5+5
#     print(X)
# nama()
# nama()
# tambah()
# tambah()
# perkalian()

# Contoh Program mengembalikan hasil fungsi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# print ("Luas persegi :", luas_persegi(8))

# # membuat variabel global
# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     #satu
#     Nama = "Informatika"
#     Mata_Kuliah = "Logika Informatika"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
#     # mengakses variabel global
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()

# def faktorial(n):
#     # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
#     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# # Fungsi untuk menampilkan semua data
# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks, "|", film[indeks])
#     print(show_data)

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# #Pembuatan Fungsi Dengan Parameter
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas persegi panjang adalah ", luas)

# #Pemanggilan Fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 5)

# # rumus: sisi x sisi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)

# luas_persegi(4)
# volume_persegi(6)


def salam():
    print("""
        =======================================================
        | Selamat Datang di Manajemen Data Webtoon Indonesia  |
        |               Silahkan Registrasi!                  |
        =======================================================
        """)
salam()

users={}

username = input("Masukkan username: ")
password = input("Masukkan password: ")
role = input("Masukkan role (admin/pengguna): ")

def data_user(username, password,role):    
    while True:               
        if role == "admin" or role == "pengguna":
            users.update({'username' : username, 
                            'password' : password,
                            'role' : role})
            print("Registrasi berhasil!")
            break
        else:
            print("Pilih role antara admin atau pengguna.")
            role = input("Masukkan role [admin/pengguna]: ")
            users.update({'role' : role})

def login_user(login=0):
    if login >= 3:
        print("Terlalu banyak percobaan. Program akan keluar.")
        exit()

    print("================= Login User =========================")
    username_in = input("Masukkan Username: ")
    password_in = input("Masukkan Password: ")
    role_in = input("Masukkan role (admin/pengguna): ")

    if username_in == username and password_in == password and role_in == "admin":
        show_menu_admin()
        return True
    elif username_in == username and password_in == password and role_in == "pengguna":
        show_menu_pengguna()
        return True
    else:
        print("Gagal login.")
        return login_user(login + 1)

komik_webtoon = {}

def tambah_data():
    judul = input("Judul Webtoon: ")
    pembaca = input("Jumlah Pembaca: ")
    genre = input("Genre: ")
    rating = input("Rating: ")
    komik_webtoon[judul] = {
            'Pembaca': pembaca,
            'Genre': genre,
            'Rating': rating
            }          

def tampil_data():
    if komik_webtoon:
        for judul, data in komik_webtoon.items():
            print(f"{judul}: {data}")
    else:
        print("Tidak ada data untuk ditampilkan.")

def update_data():
    judul_lama = input("Judul Webtoon lama: ")
    if judul_lama in komik_webtoon:
        pembaca_baru = input("Masukkan jumlah pembaca baru: ")
        genre_baru = input("Masukkan genre baru: ")
        rating_baru = input("Masukkan rating baru: ")
        komik_webtoon[judul_lama] = {
                'Pembaca': pembaca_baru,
                'Genre': genre_baru,
                'Rating': rating_baru
                }
        print(f"Data {judul_lama} berhasil diubah.")
    else:
        print("Data tidak valid.")
                

def hapus_data():
    judul_hapus = input("Masukkan judul yang ingin dihapus: ")
    if judul_hapus in komik_webtoon:
        komik_webtoon.pop(judul_hapus)
        print(f"Data {judul_hapus} berhasil dihapus.")
    else:
        print("Data tidak valid.")

def end_data():
    print("Terima kasih telah mengunjungi Manajemen Data Komik Webtoon Indonesia")
    exit()


def show_menu_admin():     
    print("""
        ==================================================
        [      MANAJEMEN DATA KOMIK WEBTOON INDONESIA     ]
        ==================================================
        [1. TAMBAH DATA                                   ]
        [2. TAMPILKAN DATA                                ]
        [3. UBAH DATA                                     ]
        [4. HAPUS DATA                                    ]
        [5. KELUAR                                        ]
        ===================================================
            """)
    while True:
        try:
            pilihan = int(input("PILIH: "))        
            if pilihan == 1:
                    tambah_data()
            elif pilihan == 2:
                    tampil_data()
            elif pilihan == 3:
                    update_data()
            elif pilihan == 4:
                    hapus_data()
            elif pilihan == 5:
                end_data()
        except ValueError:
            print("Pilihan tidak valid. Pilih angka 1/2/3/4/5")


def show_menu_pengguna(): 
    print("""
        ==================================================
        [      MANAJEMEN DATA KOMIK WEBTOON INDONESIA     ]
        ==================================================
        [1. TAMBAH DATA                                   ]
        [2. TAMPILKAN DATA                                ]
        [3. UBAH DATA                                     ]
        [4. HAPUS DATA                                    ]
        [5. KELUAR                                        ]
        ===================================================
            """)
    while True:
        try:
            pilihan = int(input("PILIH: "))        
            if pilihan == 1:    
                tambah_data()
            elif pilihan == 2:
                tampil_data()
            elif pilihan == 3:
                update_data()
            elif pilihan == 4:
                end_data()
        except ValueError:
            print("Pilihan tidak valid. Pilih angka 1/2/3/4/5")

while True:
    data_user(username, password,role)
    login_user()