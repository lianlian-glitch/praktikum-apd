from Fungsi import tampilkan_header, tampilkan_info_sistem, show_data, show_data_pencipta, Data_Setiap_Lukisan, cari_lukisan, insert_data, edit_data, delete_data

def login_admin():
    nama_admin = "Nur Fitri Ramadhani"
    password_admin = "2509106089"
    percobaan = 3

    while percobaan > 0:
        nama = input("Nama: ")
        password = input("Password: ")
        if nama == nama_admin and password == password_admin:
            print("Login berhasil sebagai admin!\n")
            menu_admin()
            return
        else:
            percobaan -= 1
            print(f"Login gagal! Sisa percobaan: {percobaan}")
    print("Login gagal setelah 3 kali percobaan. Program dihentikan.")

def menu_admin():
    while True:
        tampilkan_header()
        print("\n----------- MENU ADMIN ----------")
        print("[1] Tampilkan Daftar Lukisan")
        print("[2] Tambah Lukisan")
        print("[3] Ubah Lukisan")
        print("[4] Hapus Lukisan")
        print("[5] Tampilkan Daftar Pencipta")
        print("[6] Tampilkan Data Lukisan")
        print("[7] Cari Lukisan")
        print("[8] Info Sistem")
        print("[9] Keluar")
        menu = input("PILIH MENU > ")

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
            break
        else:
            print("Pilihan tidak valid!")

def menu_pengguna():
    while True:
        print("\n----------- MENU PENGGUNA ----------")
        print("[1] Tampilkan Daftar Lukisan")
        print("[2] Tampilkan Daftar Pencipta")
        print("[3] Tampilkan Data Lukisan")
        print("[4] Info Sistem")
        print("[5] Keluar")
        menu = input("PILIH MENU > ")

        if menu == "1":
            show_data()
        elif menu == "2":
            show_data_pencipta()
        elif menu == "3":
            Data_Setiap_Lukisan()
        elif menu == "4":
            tampilkan_info_sistem()
        elif menu == "5":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid!")
