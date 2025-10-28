print("Manajemen Koleksi Lukisan")
print("~program di mulai~")
status = input("pengguna/admin: ")
if status == "admin":
    nama = "Nur Fitri Ramadhani"
    password = 2509106089
    login = 3
    while (login <= 3): 
        nama = input("Nama: ")
        password  = int(input("pasword: "))
        if nama == "Nur Fitri Ramadhani" and password == 2509106089:
            print("login berhasil")
            break
        else:
            login -= 1
            if login >= 0:
                print(f"login gagal! sisa percobaan {login}")

            else:
                print("login gagal setelah 3 kali percobaan. program dihentikan")
                break
        if not login:
            print("akses di tolak. silakan coba lagi nanti")
            exit()
    else:
        print("Akses ditolak. Silakan coba lagi nanti")

    pilihan = {
        "1" : "=== Pilihan Menu ===",
        "2" : "Melihat Daftar Lukisan",
        "3" : "Tambah Daftar Lukisan",
        "4" : "Hapus Daftar Lukisan",
        "5" : "Ubah Daftar Lukisan",
        "6" : "Lihat Data Lukisan",
        "7" : "keluar dari program"
    }
    print(pilihan["1"])
    print(f"1. {pilihan["2"]}")
    print(f"2. {pilihan["3"]}")
    print(f"3. {pilihan["4"]}")
    print(f"4. {pilihan["5"]}")
    print(f"5. {pilihan["6"]}")
    print(f"6. {pilihan["7"]}")
    print(" ")
    pilihan = int(input("input pilihan: "))
    if pilihan == 1:
        #Melihat Daftar Lukisan
        Daftar_lukisan = {
            "daftar" : "=== Daftar Lukisan ===",
            "lukisan1" : "Mona Lisa",
            "lukisan2" : "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print(Daftar_lukisan["daftar"])
        print(f"1. Lukisan {Daftar_lukisan["lukisan1"]}")
        print(f"2. lukisan {Daftar_lukisan["lukisan2"]}")
        print(f"3. lukisan {Daftar_lukisan["lukisan3"]}")
        print(f"4. lukisan {Daftar_lukisan["lukisan4"]}")
        print(f"5. lukisan {Daftar_lukisan["lukisan5"]}")
        print(f"6. lukisan {Daftar_lukisan["lukisan6"]}")

    elif pilihan == 2:
        #Tambah Daftar Lukisan
        Daftar_lukisan = {
            "lukisan1" : "Mona Lisa",
            "lukisan2" :  "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print("=== Daftar Lukisan ===")
        print(Daftar_lukisan)
        key = (input("masukkan key: "))
        lukisan = input("masukkan data lukisan: ")
        Daftar_lukisan.update({key : lukisan})
        print(Daftar_lukisan)

    elif pilihan == 3:
        #Hapus Daftar Lukisan
        Daftar_lukisan = {
            "lukisan1" : "Mona Lisa",
            "lukisan2" :  "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print("=== Daftar Lukisan ===")
        print(Daftar_lukisan)
        hapus = input("masukkan KEY data yang ingin di hapus: ")
        del Daftar_lukisan[hapus]
        print("=== Daftar Lukisan ===")
        print(Daftar_lukisan)
        print("")

    elif pilihan == 4:
        #Ubah Daftar Lukisan
        Daftar_lukisan = {
            "lukisan1" : "Mona Lisa",
            "lukisan2" : "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print("=== Daftar Lukisan ===")
        print(Daftar_lukisan)
        key = input("masukkan KEY yang sama dengan yang ingin di ubah: ")
        data = input("masukkan data lukisan yang ingin di ubah: ")
        Daftar_lukisan[key] = data
        print(Daftar_lukisan)

    elif pilihan == 5:
        #Lihat Data Lukisan
        Daftar_lukisan = {
            "daftar" : "=== Daftar Lukisan ===",
            "lukisan1" : "Mona Lisa",
            "lukisan2" : "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print(Daftar_lukisan["daftar"])
        print(f"1. Lukisan {Daftar_lukisan["lukisan1"]}")
        print(f"2. lukisan {Daftar_lukisan["lukisan2"]}")
        print(f"3. lukisan {Daftar_lukisan["lukisan3"]}")
        print(f"4. lukisan {Daftar_lukisan["lukisan4"]}")
        print(f"5. lukisan {Daftar_lukisan["lukisan5"]}")
        print(f"6. lukisan {Daftar_lukisan["lukisan6"]}")
        print(" ")
        print("ingin melihat data luksan?")
        YaAtauTidak = input("ya/tidak? ")
        if YaAtauTidak == "ya":
            pilihan = int(input("pilih lukisan 1 sampai 6: "))
            if pilihan == 1:
                Data_Lukisan = {
                    "pencipta" : "Leonardo da Vinci",
                    "Tahun Pembuatan" : "Sekitar 1503-1506, meskipun Leonardo terus menyempurnakannya hingga kematiannya pada 1519.",
                    "Lokasi lukisan saat ini" : "Museum Louvre, Paris, Prancis.",
                    "Umur lukisan Saat Ini" : "Umur Saat Ini: Sekitar 518-521 tahun (per 2024)."
                }
                print("=== Lukisan Mona Lisa ===")
                print(f"pencipta                : {Data_Lukisan["pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan Saat Ini   : {Data_Lukisan["Umur lukisan Saat Ini"]}")
            elif pilihan == 2:
                Data_Lukisan = {
                    "Pencipta" : "Leonardo da Vinci",
                    "Tahun Pembuatan" : "Tahun 1495-1498.",
                    "Lokasi lukisan Saat Ini" : "Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
                    "Umur lukisan Saat Ini" : "Sekitar 526-529 tahun (per 2024)."
                }
                print("=== Lukisan The Last Supper ===")
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan Saat Ini"]}")
                print(f"Umur lukisan Saat Ini   : {Data_Lukisan["Umur lukisan Saat Ini"]}")
                
            elif pilihan == 3:
                Data_Lukisan = {
                    "Pencipta" : "Vincent van Gogh",
                    "Tahun Pembuatan" : "Tahun 1889.",
                    "Lokasi lukisan saat ini" : "Disimpan di Museum of Modern Art (MoMA), New York, AS, sejak 1941.",
                    "Umur lukisan saat ini" : "135 tahun (per 2024)."
                }
                print("=== Lukisan The Starry Night ===")
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")

            elif pilihan == 4:
                Data_Lukisan = {
                    "Pencipta" : "Pablo Picasso",
                    "Tahun Pembuatan" : "Tahun 1937.",
                    "Lokasi lukisan saat ini" : "Disimpan di Museo Nacional Centro de Arte Reina Sofía, Madrid, Spanyol, sejak 1981.",
                    "Umur lukisan saat ini" : "87 tahun (per 2024)."
                }
                print("===Lukisan Guernica ===")
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")

            elif pilihan == 5:
                Data_Lukisan = {
                    "Pencipta" : "Salvador Dalí",
                    "Tahun Pembuatan" : "Tahun 1931.",
                    "Lokasi lukisan saat ini" : "Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
                    "Umur lukisan saat ini" : "93 tahun (per 2024)."
                }
                print("=== The Persistence of Memory ===")
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")

            elif pilihan == 6:
                Data_Lukisan = {
                    "Pencipta" : "Johannes Vermeer",
                    "Tahun Pembuatan" : "Sekitar tahun 1665 (diperkirakan antara 1662-1665, karena tidak ada catatan pasti).",
                    "Lokasi lukisan saat ini" : "Disimpan di Mauritshuis, museum seni di The Hague (Den Haag), Belanda.",
                    "Umur lukisan saat ini" : "359 tahun (per 2024)."
                }
                print("=== Girl with a Pearl Earring ===")
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")
            else:
                print("input salah. Error!")
        elif YaAtauTidak == "tidak":
            print("=== Keluar Dari Program ===")
        else:
            print("kesalahan terjadi saat memasukkan pilihan. ERROR!")
    elif pilihan == 6:
        print("=== Keluar Dari Program ===")
    else:
        print("kesalahan terjadi saat memasukkan pilihan. ERROR!")

elif status == "pengguna":
    nama = input("masukkan nama anda: ")
    pilihan = {
        "nama" : "=== PILIHAN ===",
        "1" : "Tampilkan Semua Lukisan",
        "2" : "Tampilkan Lukisan berdasarkan Pencipta nya"
    }
    print(pilihan["nama"])
    print(f"1. {pilihan["1"]}")
    print(f"2. {pilihan["2"]}")

    pilihan = int(input("masuk ke pilihan 1/2: "))
    if pilihan == 1:
        Daftar_lukisan = {
            "daftar" : "=== Daftar Lukisan ===",
            "lukisan1" : "Mona Lisa",
            "lukisan2" :  "The Last Supper",
            "lukisan3" : "The Starry Night",
            "lukisan4" : "Guernica",
            "lukisan5" : "The Persistence of Memory",
            "lukisan6" : "Girl with a Pearl Earring"
        }
        print(Daftar_lukisan["daftar"])
        print(f"1. Lukisan {Daftar_lukisan["lukisan1"]}")
        print(f"2. lukisan {Daftar_lukisan["lukisan2"]}")
        print(f"3. lukisan {Daftar_lukisan["lukisan3"]}")
        print(f"4. lukisan {Daftar_lukisan["lukisan4"]}")
        print(f"5. lukisan {Daftar_lukisan["lukisan5"]}")
        print(f"6. lukisan {Daftar_lukisan["lukisan6"]}")
        
    elif pilihan == 2:
        Daftar_lukisan = {
            "daftar" : "=== Daftar Pencipta ===",
            "lukisan1" : "Leonardo da Vinci",
            "lukisan2" :  "Vincent van Gogh",
            "lukisan3" : "Pablo Picasso",
            "lukisan4" : "Salvador Dalí",
            "lukisan5" : "Johannes Vermeer"
        }
        print(Daftar_lukisan["daftar"])
        print(f"1. Lukisan {Daftar_lukisan["lukisan1"]}")
        print(f"2. lukisan {Daftar_lukisan["lukisan2"]}")
        print(f"3. lukisan {Daftar_lukisan["lukisan3"]}")
        print(f"4. lukisan {Daftar_lukisan["lukisan4"]}")
        print(f"5. lukisan {Daftar_lukisan["lukisan5"]}")

        lihat = int(input("siapa yang ingin ada lihat? "))
        if lihat == 1:
            karya = {
                "pencipta" : "~~Leonardo da Vinci~~",
                "1" : "Lukisan Mona Lisa",
                "2" : "Lukisan The Last Supper"
            }
            print(karya["pencipta"])
            print(f"1. {karya["1"]}")
            print(f"2. {karya["2"]}")

            info = int(input("lihat data penting lukisan, lukisan 1 atau 2? "))
            if info == 1:
                Data_Lukisan = {
                    "Lukisan" : "=== Lukisan Mona Lisa ===",
                    "pencipta" : "Leonardo da Vinci",
                    "Tahun Pembuatan" : "Sekitar 1503-1506, meskipun Leonardo terus menyempurnakannya hingga kematiannya pada 1519.",
                    "Lokasi lukisan saat ini" : "Museum Louvre, Paris, Prancis.",
                    "Umur lukisan Saat Ini" : "Umur Saat Ini: Sekitar 518-521 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan Saat Ini   : {Data_Lukisan["Umur lukisan Saat Ini"]}")
            elif info == 2:
                Data_Lukisan = {
                    "lukisan" : "=== Lukisan The Last Supper ===",
                    "Pencipta" : "Leonardo da Vinci",
                    "Tahun Pembuatan" : "Tahun 1495-1498.",
                    "Lokasi lukisan Saat Ini" : "Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
                    "Umur lukisan Saat Ini" : "Sekitar 526-529 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan Saat Ini   : {Data_Lukisan["Umur lukisan Saat Ini"]}")
            else:
                print("kesalahan terjadi saat memasukkan pilihan. ERROR!")

        elif lihat == 2:
            print("~~Vincent van Gogh~~")
            print("Lukisan The Starry Night")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                Data_Lukisan = {
                    "Lukisan" : "=== Lukisan The Starry Night ===",
                    "Pencipta" : "Vincent van Gogh",
                    "Tahun Pembuatan" : "Tahun 1889.",
                    "Lokasi lukisan saat ini" : "Disimpan di Museum of Modern Art (MoMA), New York, AS, sejak 1941.",
                    "Umur lukisan saat ini" : "135 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")
            elif info == "tidak":
                print("program berhenti")
            else:
                print("kesalahan terjadi saat memasukkan pilihan. ERROR!")

        elif lihat == 3:
            print("~~Pablo Picasso~~")
            print("Lukisan Guernica")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                Data_Lukisan = {
                    "Lukisan" : "===Lukisan Guernica ===",
                    "Pencipta" : "Pablo Picasso",
                    "Tahun Pembuatan" : "Tahun 1937.",
                    "Lokasi lukisan saat ini" : "Disimpan di Museo Nacional Centro de Arte Reina Sofía, Madrid, Spanyol, sejak 1981.",
                    "Umur lukisan saat ini" : "87 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")
            elif info == "tidak":
                print("program berhenti")
            else:
                print("kesalahan terjadi saat memasukkan pilihan. ERROR!")

        elif lihat == 4:
            print("~~Salvador Dalí~~")
            print("Lukisan The Persistence of Memory")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                Data_Lukisan = {
                    "Lukisan" : "=== The Persistence of Memory ===",
                    "Pencipta" : "Salvador Dalí",
                    "Tahun Pembuatan" : "Tahun 1931.",
                    "Lokasi lukisan saat ini" : "Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia.",
                    "Umur lukisan saat ini" : "93 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")
            elif info == "tidak":
                print("program berhenti")
            else:
                print("kesalahan terjadi saat memasukkan pilihan. ERROR!")
        
        elif lihat == 5:
            print("~~Johannes Vermeer~~")
            print("Lukisan Girl with a Pearl Earring")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                Data_Lukisan = {
                    "Lukisan" : "=== Lukisan Girl with a Pearl Earring ===",
                    "Pencipta" : "Johannes Vermeer",
                    "Tahun Pembuatan" : "Sekitar tahun 1665 (diperkirakan antara 1662-1665, karena tidak ada catatan pasti).",
                    "Lokasi lukisan saat ini" : "Disimpan di Mauritshuis, museum seni di The Hague (Den Haag), Belanda.",
                    "Umur lukisan saat ini" : "359 tahun (per 2024)."
                }
                print(Data_Lukisan["Lukisan"])
                print(f"Pencipta                : {Data_Lukisan["Pencipta"]}")
                print(f"Tahun Pembuatan         : {Data_Lukisan["Tahun Pembuatan"]}")
                print(f"Lokasi lukisan saat ini : {Data_Lukisan["Lokasi lukisan saat ini"]}")
                print(f"Umur lukisan saat ini   : {Data_Lukisan["Umur lukisan saat ini"]}")
            elif info == "tidak":
                print("program berhenti")
            else:
                print("kesalahan terjadi saat memasukkan pilihan. ERROR!")
        else:
            print("kesalahan terjadi saat memasukkan pilihan. ERROR!")
    else:
        print("ERROR! Keluar dari program.")
else:
    print("ERROR!")