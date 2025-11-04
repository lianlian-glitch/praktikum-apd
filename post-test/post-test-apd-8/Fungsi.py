from prettytable import PrettyTable
from Data import Daftar_Lukisan, pencipta

def tampilkan_header():
    print("\n" + "=" * 40)
    print("   SISTEM MANAJEMEN KOLEKSI LUKISAN")
    print("=" * 40)

def tampilkan_info_sistem():
    print("\n--- INFORMASI SISTEM ---")
    print(f"Total Lukisan Terdaftar : {len(Daftar_Lukisan)}")
    print(f"Total Pencipta Terdaftar: {len(pencipta)}")
    print("------------------------")

def show_data():
    if not Daftar_Lukisan:
        print("Belum ada data.")
        return
    tabel = PrettyTable(["No", "Nama Lukisan"])
    for i, lukisan in enumerate(Daftar_Lukisan, start=1):
        tabel.add_row([i, lukisan])
    print(tabel)

def show_data_pencipta():
    if not pencipta:
        print("Belum ada data.")
        return
    tabel = PrettyTable(["No", "Nama Pencipta"])
    for i, nama in enumerate(pencipta, start=1):
        tabel.add_row([i, nama])
    print(tabel)

def Data_Setiap_Lukisan():
    tabel = PrettyTable(["Judul Lukisan", "Pencipta", "Tahun", "Lokasi"])
    data_detail = [
        ["Mona Lisa", "Leonardo da Vinci", "1503-1506", "Louvre, Paris"],
        ["The Last Supper", "Leonardo da Vinci", "1495-1498", "Milan, Italia"],
        ["The Starry Night", "Vincent van Gogh", "1889", "MoMA, New York"],
        ["Guernica", "Pablo Picasso", "1937", "Madrid, Spanyol"],
        ["The Persistence of Memory", "Salvador Dalí", "1931", "Milan, Italia"],
        ["Girl with a Pearl Earring", "Johannes Vermeer", "1665", "Den Haag, Belanda"],
    ]
    for data in data_detail:
        tabel.add_row(data)
    print(tabel)

def insert_data():
    nama = input("Masukkan nama lukisan baru: ")
    Daftar_Lukisan.append(nama)
    print("Lukisan berhasil ditambahkan!")

def edit_data():
    show_data()
    try:
        idx = int(input("Nomor lukisan yang ingin diubah: ")) - 1
        if 0 <= idx < len(Daftar_Lukisan):
            Daftar_Lukisan[idx] = input("Masukkan nama baru: ")
            print("Data berhasil diubah!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus angka!")

def delete_data():
    show_data()
    try:
        idx = int(input("Nomor lukisan yang ingin dihapus: ")) - 1
        if 0 <= idx < len(Daftar_Lukisan):
            Daftar_Lukisan.pop(idx)
            print("Data berhasil dihapus!")
        else:
            print("Nomor tidak valid!")
    except ValueError:
        print("Input harus angka!")

def cari_data(data_list, keyword):
    return [item for item in data_list if keyword.lower() in item.lower()]

def cari_lukisan():
    keyword = input("Masukkan kata kunci pencarian: ")
    hasil = cari_data(Daftar_Lukisan, keyword)
    if hasil:
        tabel = PrettyTable(["No", "Hasil Pencarian"])
        for i, item in enumerate(hasil, start=1):
            tabel.add_row([i, item])
        print(tabel)
    else:
        print("Tidak ada lukisan ditemukan.")
