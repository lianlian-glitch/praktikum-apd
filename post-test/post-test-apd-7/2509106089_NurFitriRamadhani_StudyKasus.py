# Evet Gebyar Informatika mengadakan bebrrapacabang lomba
lomba = []
peserta_lomba = []

def show_data():
    if len(lomba) <= 0:
        print("Belum ada data.")
    else:
        print("cabang lomba")
        for indeks in range(len(lomba)):
            print(indeks, "|", lomba[indeks])

# Fungsi untuk menambah data
def insert_data():
    lomba_baru = input("daftarkan lomba: ")
    lomba.append(lomba_baru)
    print("lomba berhasil ditambahkan.")

# Fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan namba lomba yang ingin diubah: "))
    if indeks >= len(lomba) or indeks < 0:
        print("input salah.")
    else:
        judul_baru = input("lomba baru: ")
        lomba[indeks] = judul_baru
        print("lomba berhasil diubah!")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan nama lomba: "))
    if indeks >= len(lomba) or indeks < 0:
        print("nomor lomba salah.")
    else:
        lomba.remove(lomba[indeks])
        print("Daftar lomba berhasil dihapus!")

# Fungsi untuk menambah data peserta
def insert_data_peserta():
    peserta_baru = input("daftarkan nama peserta: ")
    peserta_lomba.append(peserta_baru)
    print("lomba berhasil ditambahkan.")

# Memperlihatkan peserta lomba
def show_data_peserta():
    if len(peserta_lomba) <= 0:
        print("Belum ada data.")
    else:
        print("Nama peserta Lomba")
        for indeks in range(len(peserta_lomba)):
            print(indeks, "|", peserta_lomba[indeks])

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Menambahkan peserta lomba")
    print("[6] Show Data peserta")
    print("[7] Exit")
    menu = input("PILIH MENU > ")
    print("\n")

    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        insert_data_peserta()
    elif menu == "6":
        show_data_peserta()
    elif menu == "7":
        print("Keluar dari program...")
        exit()
    else:
        print("Salah pilih!")

# Program utama (loop menu)
while True:
    show_menu()
