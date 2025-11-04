print("Manajemen Koleksi Lukisan")
print("~program di mulai~")
# VARIABEL GLOBAL
total_lukisan = 0
total_pencipta = 0
status_login = False
# Fungsi dengan parameter
def cari_data(data_list, keyword):
    try:
        hasil = []
        keyword_lower = keyword.lower()
        for item in data_list:
            if keyword_lower in item.lower():
                hasil.append(item)
        return hasil
    except AttributeError:
        print("Atribut tidak ditemukan!")
        return []
    
# Daftar lukisan
Daftar_Luksian = [
    "Mona Lisa",
    "The Last Supper",
    "The Starry Night",
    "Guernica",
    "The Persistence of Memory",
    "Girl with a Pearl Earring",
]
# Daftar pencipta
pencipta = [
    "Leonardo da Vinci",
    "Vincent van Gogh",
    "Pablo Picasso",
    "Salvador Dalí",
    "Johannes Vermeer",
]

# Fungsi tanpa parameter
def tampilkan_header():
    try:
        print("\n" + "=" * 50)
        print("   SISTEM MANAJEMEN KOLEKSI LUKISAN")
        print("=" * 50)
        return True
    except:
        return False

# informasi sistem
def tampilkan_info_sistem():
    global total_lukisan, total_pencipta, status_login
    print("\n--- INFORMASI SISTEM ---")
    print(f"Status Login: {'Berhasil' if status_login else 'Belum Login'}")
    print(f"Total Lukisan Terdaftar: {total_lukisan}")
    print(f"Total Pencipta Terdaftar: {total_pencipta}")
    print("------------------------")

# Perlihatkan Daftar pencipta
def show_data_pencipta():
    try:
        ada_data = len(pencipta) > 0
        if not ada_data:
            print("Belum ada data.")
        else:
            print("Daftar pencipta luksan")
            for indeks in range(len(pencipta)):
                print(indeks, "|", pencipta[indeks])
    except TypeError:
        print("Tipe data tidak sesuai!")

# Perlihatkan Daftar Lukisan
def show_data():
    try:
        ada_data = len(Daftar_Luksian) > 0
        
        if not ada_data:
            print("Belum ada data.")
        else:
            print("Daftar luksan")
            for indeks in range(len(Daftar_Luksian)):
                    print(indeks, "|", Daftar_Luksian[indeks])
    except TypeError:
        print("Tipe data tidak sesuai!")

# Menampilkan Data Lukisan
def Data_Setiap_Lukisan():
    try:
        Data_ML = [
            "Lukisan                 : Lukisan Mona Lisa",
            "pencipta                : Leonardo da Vinci",
            "Tahun Pembuatan         : Sekitar 1503-1506, meskipun Leonardo terus menyempurnakannya hingga kematiannya pada 1519.",
            "Lokasi lukisan saat ini : Museum Louvre, Paris, Prancis.",
            "Umur lukisan Saat Ini   : Umur Saat Ini: Sekitar 518-521 tahun (per 2024)."
        ]
        def show_data_ML():
            try:
                if len(Data_ML) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_ML)):
                        print(indeks, "|", Data_ML[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_ML())
        # Data Lukisan The Last Supper
        Data_TLS = [
            "lukisan                 : Lukisan The Last Suppe",
            "Pencipta                : Leonardo da Vinci",
            "Tahun Pembuatan         : Tahun 1495-1498.",
            "Lokasi lukisan Saat Ini : Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
            "Umur lukisan Saat Ini   : Sekitar 526-529 tahun (per 2024)."
        ]
        def show_data_TLS():
            try:
                if len(Data_TLS) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_TLS)):
                        print(indeks, "|", Data_TLS[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_TLS())
        # Data Luksian The Starry Night
        Data_TSN = [
            "Lukisan                 : Lukisan The Starry Night",
            "Pencipta                : Vincent van Gogh",
            "Tahun Pembuatan         : Tahun 1889.",
            "Lokasi lukisan saat ini : Disimpan di Museum of Modern Art (MoMA), New York, AS, sejak 1941.",
            "Umur lukisan saat ini   : 135 tahun (per 2024)."    
        ]
        def show_data_TSN():
            try:
                if len(Data_TSN) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_TSN)):
                        print(indeks, "|", Data_TSN[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_TSN())
        # Data Lukisan Guernica
        Data_G = [
            "Lukisan                 : Lukisan Guernica",
            "Pencipta                : Pablo Picasso",
            "Tahun Pembuatan         : Tahun 1937.",
            "Lokasi lukisan saat ini : Disimpan di Museo Nacional Centro de Arte Reina Sofía, Madrid, Spanyol, sejak 1981.",
            "Umur lukisan saat ini   : 87 tahun (per 2024)."
        ]
        def show_data_G():
            try:
                if len(Data_G) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_G)):
                        print(indeks, "|", Data_G[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_G())
        # Data Luksan The Persistence of Memory
        Data_TPOM = [
            "Lukisan                 : The Persistence of Memory",
            "Pencipta                : Salvador Dalí",
            "Tahun Pembuatan         : Tahun 1931.",
            "Lokasi lukisan saat ini : Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
            "Umur lukisan saat ini   : 93 tahun (per 2024)."
        ]
        def show_data_TPOM():
            try:
                if len(Data_TPOM) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_TPOM)):
                        print(indeks, "|", Data_TPOM[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_TPOM())
        # Data Luksian Girl with a Pearl Earring
        Data_GWAPE = [
            "Lukisan                 : Lukisan Girl with a Pearl Earring",
            "Pencipta                : Johannes Vermeer",
            "Tahun Pembuatan         : Sekitar tahun 1665 (diperkirakan antara 1662-1665, karena tidak ada catatan pasti).",
            "Lokasi lukisan saat ini : Disimpan di Mauritshuis, museum seni di The Hague (Den Haag), Belanda.",
            "Umur lukisan saat ini   : 359 tahun (per 2024)."
        ]
        def show_data_GWAPE():
            try:
                if len(Data_GWAPE) <= 0:
                    print("Belum ada data.")
                else:
                    print("Data lukisan")
                    for indeks in range(len(Data_GWAPE)):
                        print(indeks, "|", Data_GWAPE[indeks])
            except TypeError:
                print("Tipe data tidak sesuai!")
        print(show_data_GWAPE())
    except NameError:
        print("Variabel tidak ditemukan!")

try:
    status = input("pengguna/admin: ")
    if status == "admin":
        nama = "Nur Fitri Ramadhani"
        password = 2509106089
        login = 3
        while (login <= 3): 
            try:
                nama = input("Nama: ")
                try:
                    password = int(input("Password: "))
                except ValueError:
                    print("Password harus berupa angka!")
                    login -= 1
                    if login > 0:
                        print(f"Login gagal! Sisa percobaan {login}")
                    continue
                if nama == "Nur Fitri Ramadhani" and password == 2509106089:
                    print("login berhasil")
                    status_login = True
                    break
                else:
                    login -= 1
                    if login > 0:
                        print(f"login gagal! sisa percobaan {login}")
                    else:
                        print("login gagal setelah 3 kali percobaan. program dihentikan")
                        break
            except NameError:
                print("NameError: Variabel tidak ditemukan!")
                break
        if login == 0:
            print("akses di tolak. silakan coba lagi nanti")
            exit()
        # Update variabel global
        total_lukisan = len(Daftar_Luksian)
        total_pencipta = len(pencipta)
        # Fungsi untuk menambah data
        def insert_data():
            global total_lukisan
            try:
                Daftar_baru = input("daftarkan lukisan: ")
                Daftar_Luksian.append(Daftar_baru)
                total_lukisan = len(Daftar_Luksian)
                print("daftar lukisan berhasil ditambahkan.")
            except TypeError:
                print("Tipe data tidak sesuai!")
        # Fungsi untuk mengedit data
        def edit_data():
            try:
                show_data()
                try:
                    indeks = int(input("Inputkan nomor luksan yang ingin diubah: "))
                    indeks_valid = 0 <= indeks < len(Daftar_Luksian)
                except ValueError:
                    print("Input harus berupa angka!")
                    return
                if not indeks_valid:
                    print("input salah.")
                else:
                    judul_baru = input("lukisan baru: ")
                    Daftar_Luksian[indeks] = judul_baru
                    print("daftar lukisan berhasil diubah!")
            except TypeError:
                print("Tipe data tidak sesuai!")
        # Fungsi untuk menghapus data
        def delete_data():
            global total_lukisan
            try:
                show_data()
                try:
                    indeks = int(input("Inputkan nomor daftar luksian yang ingin dihapus: "))
                    indeks_valid = 0 <= indeks < len(Daftar_Luksian)
                except ValueError:
                    print("Input harus berupa angka!")
                    return
                if not indeks_valid:
                    print("nomor daftar salah.")
                else:
                    Daftar_Luksian.remove(Daftar_Luksian[indeks])
                    total_lukisan = len(Daftar_Luksian)
                    print("Daftar luksan berhasil dihapus.")
            except ValueError:
                print("Item tidak ditemukan dalam list!")
        # Fungsi pencarian lukisan
        def cari_lukisan():
            try:
                keyword = input("Masukkan kata kunci pencarian: ")
                hasil = cari_data(Daftar_Luksian, keyword)
                if len(hasil) > 0:
                    print(f"\nDitemukan {len(hasil)} lukisan:")
                    for idx, lukisan in enumerate(hasil):
                        print(f"{idx}. {lukisan}")
                else:
                    print("Tidak ada lukisan yang ditemukan.")
            except:
                print("Terjadi kesalahan saat pencarian!")
        # Fungsi untuk menampilkan menu
        def show_menu():
            try:
                tampilkan_header()
                print("\n----------- MENU ----------")
                print("[1] Tampilkan Daftar Lukisan")
                print("[2] Tamabah Daftar Lukisan")
                print("[3] Ubah Daftar Lukisan")
                print("[4] Hapus Daftar Lukisan")
                print("[5] Tamplkan daftar pencipta")
                print("[6] Perlihatkan Semua Data Lukisan")
                print("[7] Cari Lukisan")
                print("[8] Info Sistem")
                print("[9] Exit")
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
                    show_data_pencipta()
                elif menu == "6":
                    Data_Setiap_Lukisan()
                elif menu == "7":
                    cari_lukisan()
                elif menu == "8":
                    tampilkan_info_sistem()
                elif menu == "9":
                    print("Keluar dari program...")
                    exit()
                else:
                    print("Salah pilih!")
            except NameError:
                print(" Variabel tidak ditemukan!")
        # Program utama (loop menu)
        while True:
            try:
                show_menu()
            except KeyboardInterrupt:
                print("\nProgram dihentikan.")
                break
    elif status == "pengguna":
        # Update variabel global
        total_lukisan = len(Daftar_Luksian)
        total_pencipta = len(pencipta)
        # Fungsi untuk menampilkan menu
        def show_menu():
            try:
                tampilkan_header()
                print("\n----------- MENU ----------")
                print("[1] Perlihatkan Daftar Lukisan")
                print("[2] Tampilkan Daftar Pencita")
                print("[3] Tampilkan Data Luksan")
                print("[4] Info Sistem")
                print("[5] Exit")
                menu = input("PILIH MENU > ")
                print("\n")
                if menu == "1":
                    show_data()
                elif menu == "2":
                    show_data_pencipta()
                elif menu == "3":
                    Data_Setiap_Lukisan()
                elif menu == "4":
                    tampilkan_info_sistem()
                elif menu == "5":
                    print("Keluar dari program")
                    exit()
                else:
                    print("Salah pilih!")
            except NameError:
                print("Variabel tidak ditemukan!")
        # Program utama (loop menu)
        while True:
            try:
                show_menu()
            except KeyboardInterrupt:
                print("\nProgram dihentikan.")
                break
    else:
        print("Status tidak valid! Pilih 'admin' atau 'pengguna'.")
except TypeError:
    print("Tipe data tidak sesuai!")
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")