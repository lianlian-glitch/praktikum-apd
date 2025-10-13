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

    print("===PILIHAN===")
    print("1. Menambahkan lukisan baru")
    print("2. Daftar Lukiksan")
    print("3. Edit data Lukisan")
    print("4. Hapus Koleksi Lukisan")
    print("5. keluar dari program")
    pilihan = int(input("input pilihan: "))
    if pilihan == 1:
        print("menambahkan lukisan")
        daftar =  ["Mona Lisa", "The Last Supper", "The Starry Night", "Guernica", "The Persistence of Memory ", "Girl with a Pearl Earring "]
        #daftar_lukisan = [["Mona Lisa", "The Last Supper", "The Starry Night"], ["Guernica", "The Persistence of Memory", "Girl with a Pearl Earring "]]
        print("===daftar Lukisan===")
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
        print(f"5. {daftar[4]}")
        print(f"6. {daftar[5]}")
        elemen = input("Masukkan elemen: ")
        daftar.append(elemen)
        print("===daftar Lukisan===")
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
        print(f"5. {daftar[4]}")
        print(f"6. {daftar[5]}")
        print(f"7. {daftar[6]}")

    elif pilihan == 2:
        daftar = [
            ["Mona Lisa", "The Last Supper", "The Starry Night"],
            ["Guernica", "The Persistence of Memory", "Girl with a Pearl Earring"]
        ]
        print(f"1. {daftar[0][0]}")
        print(f"2. {daftar[0][1]}")
        print(f"3. {daftar[0][2]}")
        print(f"4. {daftar[1][0]}")
        print(f"5. {daftar[1][1]}")
        print(f"6. {daftar[1][2]}")
        pilihan = int(input("lukisan: "))
        if pilihan == 1:
            print("===Lukisan Mona Lisa===")
            print("pewncipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).")
            print("Tahun Pembuatan: Sekitar 1503-1506, meskipun Leonardo terus menyempurnakannya hingga kematiannya pada 1519.")
            print("Lokasi Saat Ini: Museum Louvre, Paris, Prancis. Dipajang di ruangan khusus sejak 1914, dengan pengamanan ketat (kaca anti-peluru dan pelindung dari suhu/kelembaban).")
            print("Umur Saat Ini: Sekitar 518-521 tahun (per 2024).")

        elif pilihan ==2:
            print("===Lukisan The Last Supper===")
            print("Pencipta: Leonardo da Vinci, seniman, ilmuwan, dan arsitek Renaissance Italia (1452-1519).")
            print("Tahun Pembuatan: 1495-1498. Leonardo menerima komisi dari Duke of Milan, Ludovico Sforza, untuk melukis dinding ruang makan (refektori) biara Santa Maria delle Grazie.")
            print("Lokasi Saat Ini: Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia. Dilindungi oleh UNESCO sebagai Situs Warisan Dunia sejak 1980. Pengunjung dibatasi (maksimal 40 orang per 15 menit) untuk menjaga kondisi.")
            print("Umur Saat Ini: Sekitar 526-529 tahun (per 2024).")

        elif pilihan == 3:
            print("=== Lukisan The Starry Night===")
            print("Seniman: Vincent van Gogh (1853-1890).")
            print("Tahun pembuatan: 1889.")
            print("Lokasi Saat Ini: Disimpan di Museum of Modern Art (MoMA), New York, AS, sejak 1941. Diakuisisi melalui donasi dari keluarga Lillie P. Bliss.")
            print("umur saat ini: 135 tahun (per 2024)")

        elif pilihan == 4:
            print("===Lukisan Guernica===")
            print("Seniman: Pablo Picasso (1881-1973), pelukis Spanyol yang menjadi tokoh utama Cubism dan seni modern.")
            print("Tahun pembuatan: 1937. Dibuat dalam waktu singkat (sekitar 35 hari) di studio Picasso di Paris, mulai Mei 1937, setelah ia mendengar berita pemboman Guernica (kota Basque, Spanyol) oleh pasukan Nazi Jerman dan fasis Italia pada 26 April 1937.")
            print("lokasi saat ini: Disimpan di Museo Nacional Centro de Arte Reina Sofía, Madrid, Spanyol, sejak 1981. Ini adalah museum seni modern nasional Spanyol, di mana Guernica menjadi karya utama.")
            print("umur saat ini: 87 tahun (per 2024)")

        elif pilihan == 5:
            print("===The Persistence of Memory===")
            print("Seniman: Salvador Dalí (1904-1989)")
            print("Tahun pembuatan: 1931. Dibuat selama musim panas di Port Lligat, Costa Brava, Spanyol, di rumah Dalí.")
            print("lokasi: Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia. Dilindungi oleh UNESCO sebagai Situs Warisan Dunia sejak 1980.")
            print("umur saat ini: 93 tahun (per 2024)")

        elif pilihan == 6:
            print("=== Lukisan Girl with a Pearl Earring===")
            print("seniman: Johannes Vermeer (1632-1675)")
            print("Tahun pembuatan: Sekitar 1665 (diperkirakan antara 1662-1665, karena tidak ada catatan pasti).")
            print("lokasi: Disimpan di Mauritshuis, museum seni di The Hague (Den Haag), Belanda, sejak 1902.")
            print("umur saat ini: 359 tahun (per 2024)")

        else:
            print("input salah. Error!")

    elif pilihan == 3:
        daftar =  ["Mona Lisa", "The Last Supper", "The Starry Night", "Guernica", "The Persistence of Memory", "Girl with a Pearl Earring"]
        print("Edit data Lukisan")
        print("===daftar Lukisan===")
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
        print(f"5. {daftar[4]}")
        print(f"6. {daftar[5]}")
        pilihan = int(input("lukisan: "))
        if pilihan == 1:
            print("===Data Lukisan Mona Lisa===")
            Update = input("edit/ubah/hapus): ")
            if Update == "edit":
                Data_ML = ["pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).", "Tahun Pembuatan: Sekitar 1503-1506.", "Umur Saat Ini: Sekitar 518-521 tahun (per 2024)."]
                print(f"1. {Data_ML[0]}")
                print(f"2. {Data_ML[1]}")
                print(f"3. {Data_ML[2]}")
                elemen = input("Masukkan Data: ")
                Data_ML.append(elemen)
                print(f"1. {Data_ML[0]}")
                print(f"2. {Data_ML[1]}")
                print(f"3. {Data_ML[2]}")
                print(f"4. {Data_ML[3]}")
            elif Update == "ubah":
                Data_ML = ["pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).", "Tahun Pembuatan: Sekitar 1503-1506.", "Umur Saat Ini: Sekitar 518-521 tahun (per 2024)."]
                print(Data_ML)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_ML[baris] = ubah
                print(Data_ML)
            elif Update == "hapus":
                Data_ML = ['pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).', 'Tahun Pembuatan: Sekitar 1503-1506.', 'Umur Saat Ini: Sekitar 518-521 tahun (per 2024).']
                print(Data_ML)
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_ML[hapus]
                print(Data_ML)
            else:
                ()

        elif pilihan ==2:
            print("===Lukisan The Last Supper===")
            Update = input("edit/hapus): ")
            if pilihan == "edit":
                Data_TLS = ["Pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).", "Tahun Pembuatan: 1495-1498.", "Umur Saat Ini: Sekitar 526-529 tahun (per 2024)."]
                print(f"1. {Data_TLS[0]}")
                print(f"2. {Data_TLS[1]}")
                print(f"3. {Data_TLS[2]}")
                elemen = input("Masukkan Data: ")
                Data_TLS.append(elemen)
                print(f"1. {Data_TLS[0]}")
                print(f"2. {Data_TLS[1]}")
                print(f"3. {Data_TLS[2]}")
                print(f"4. {Data_TLS[3]}")
            elif Update == "ubah":
                Data_TLS = ["Pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).", "Tahun Pembuatan: 1495-1498.", "Umur Saat Ini: Sekitar 526-529 tahun (per 2024)."]
                print(Data_TLS)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_TLS[baris] = ubah
                print(Data_TLS)
            elif Update == "hapus":
                Data_TLS = ['Pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).', 'Tahun Pembuatan: 1495-1498.', 'Umur Saat Ini: Sekitar 526-529 tahun (per 2024).']
                print(Data_TLS)
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_TLS[hapus]
                print(Data_TLS)
            else:
                ()

        elif pilihan == 3:
            print("=== Lukisan The Starry Night===")
            Update = input("edit/ganti/hapus): ")
            if Update == "edit":
                Data_TSN = ["Seniman: Vincent van Gogh (1853-1890).", "Tahun pembuatan: 1889.", "umur saat ini: 135 tahun (per 2024)"]
                print(f"1. {Data_TSN[0]}")
                print(f"2. {Data_TSN[1]}")
                print(f"3. {Data_TSN[2]}")
                elemen = input("Masukkan Data: ")
                Data_TSN.append(elemen)
                print(f"1. {Data_TSN[0]}")
                print(f"2. {Data_TSN[1]}")
                print(f"3. {Data_TSN[2]}")
                print(f"4. {Data_TSN[3]}")
            elif Update == "ubah":
                Data_TSN = ["Seniman: Vincent van Gogh (1853-1890).", "Tahun pembuatan: 1889.", "umur saat ini: 135 tahun (per 2024)"]
                print(Data_TSN)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_TSN[baris] = ubah
                print(Data_TSN)
            elif Update == "hapus":
                Data_TSN = ['Seniman: Vincent van Gogh (1853-1890).', 'Tahun pembuatan: 1889.', 'umur saat ini: 135 tahun (per 2024)']
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_TSN[hapus]
                print(Data_TSN)
            else:
                ()

        elif pilihan == 4:
            print("===Lukisan Guernica===")
            Update = input("edit/ganti/hapus): ")
            if pilihan == "edit":
                Data_Guernica = ["Seniman: Pablo Picasso (1881-1973).", "Tahun pembuatan: 1937.", "umur saat ini: 87 tahun (per 2024)"]
                print(f"1. {Data_Guernica[0]}")
                print(f"2. {Data_Guernica[1]}")
                print(f"3. {Data_Guernica[2]}")
                elemen = input("Masukkan Data: ")
                Data_Guernica.append(elemen)
                print(f"1. {Data_Guernica[0]}")
                print(f"2. {Data_Guernica[1]}")
                print(f"3. {Data_Guernica[2]}")
                print(f"4. {Data_Guernica[3]}")
            elif Update == "ubah":
                Data_Guernica = ["Seniman: Pablo Picasso (1881-1973).", "Tahun pembuatan: 1937.", "umur saat ini: 87 tahun (per 2024)"]
                print(Data_Guernica)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_Guernica[baris] = ubah
                print(Data_Guernica)
            elif Update == "hapus":
                Data_Guernica = ['Seniman: Pablo Picasso (1881-1973).', 'Tahun pembuatan: 1937.', 'umur saat ini: 87 tahun (per 2024)']
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_Guernica[hapus]
                print(Data_Guernica)
            else:
                ()

        elif pilihan == 5:
            print("===The Persistence of Memory===")
            Update = input("edit/ganti/hapus): ")
            if pilihan == "edit":
                Data_TPOM = ["Seniman: Salvador Dalí (1904-1989)", "Tahun pembuatan: 1931.", "umur saat ini: 93 tahun (per 2024)"]
                print(f"1. {Data_TPOM[0]}")
                print(f"2. {Data_TPOM[1]}")
                print(f"3. {Data_TPOM[2]}")
                elemen = input("Masukkan Data: ")
                Data_TPOM.append(elemen)
                print(f"1. {Data_TPOM[0]}")
                print(f"2. {Data_TPOM[1]}")
                print(f"3. {Data_TPOM[2]}")
                print(f"4. {Data_TPOM[3]}")
            elif Update == "ubah":
                Data_TPOM = ["Seniman: Salvador Dalí (1904-1989)", "Tahun pembuatan: 1931.", "umur saat ini: 93 tahun (per 2024)"]
                print(Data_TPOM)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_TPOM[baris] = ubah
                print(Data_TPOM)
            elif Update == "hapus":
                Data_TPOM = ['Seniman: Salvador Dalí (1904-1989)', 'Tahun pembuatan: 1931.', 'umur saat ini: 93 tahun (per 2024)']
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_TPOM[hapus]
                print(Data_TPOM)
            else:
                ()


        elif pilihan == 6:
            print("=== Lukisan Girl with a Pearl Earring===")
            Update = input("edit/ganti/hapus): ")
            if pilihan == "edit":
                Data_GWAPE = ["seniman: Johannes Vermeer (1632-1675)", "Tahun pembuatan: sekitar 1662-1665, karena tidak ada catatan pasti.", "umur saat ini: 359 tahun (per 2024)"]
                print(f"1. {Data_GWAPE[0]}")
                print(f"2. {Data_GWAPE[1]}")
                print(f"3. {Data_GWAPE[2]}")
                elemen = input("Masukkan Data: ")
                Data_GWAPE.append(elemen)
                print(f"1. {Data_GWAPE[0]}")
                print(f"2. {Data_GWAPE[1]}")
                print(f"3. {Data_GWAPE[2]}")
                print(f"4. {Data_GWAPE[3]}")
            elif Update == "ubah":
                Data_GWAPE = ["Seniman: Salvador Dalí (1904-1989)", "Tahun pembuatan: 1931.", "umur saat ini: 93 tahun (per 2024)"]
                print(Data_GWAPE)
                baris = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                ubah = input("ubah: ")
                Data_GWAPE[baris] = ubah
                print(Data_GWAPE)
            elif Update == "hapus":
                Data_GWAPE = ['Seniman: Salvador Dalí (1904-1989)', 'Tahun pembuatan: 1931.', 'umur saat ini: 93 tahun (per 2024)']
                hapus = int(input("masukkan angkka dari 0 sampai 2 untuk di hapus: "))
                del Data_GWAPE[hapus]
                print(Data_GWAPE)
            else:
                ()

    elif pilihan == 4:
        print("===Hapus Koleksi Lukisan===")
        daftar =  ["Mona Lisa", "The Last Supper", "The Starry Night", "Guernica", "The Persistence of Memory", "Girl with a Pearl Earring"]
        print("===daftar Lukisan===")
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
        print(f"5. {daftar[4]}")
        print(f"6. {daftar[5]}")
        hapus = int(input("lukisan yang mana yang akan anda hapus: "))
        del daftar[hapus]
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
        print(f"5. {daftar[4]}")
    elif pilihan == 5:
        print("===keluar dari progra===")
    else:
        ()

elif status == "pengguna":
    nama = input("masukkan nama anda: ")
    print("===PILIHAN===")
    print("1. Tampilkan Semua Lukisan")
    print("2. Tampilkan Lukisan berdasarkan Pencipta nya")
    pilihan = int(input("masuk ke pilihan: "))
    if pilihan == 1:
        lukisan = [
            ["Mona Lisa", "The Last Supper", "The Starry Night"],
            ["Guernica", "The Persistence of Memory", "Girl with a Pearl Earring"]
        ]
        print("===daftar Lukisan===")
        print(f"1. {lukisan[0][0]}")
        print(f"2. {lukisan[0][1]}")
        print(f"3. {lukisan[0][2]}")
        print(f"4. {lukisan[1][0]}")
        print(f"5. {lukisan[1][1]}")
        print(f"6. {lukisan[1][2]}")
        
    elif pilihan == 2:
        pencipta = ("Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Salvador Dalí", "Johannes Vermeer")
        print("===daftar Pelukis===")
        print(f"1. {pencipta[0]}")
        print(f"2. {pencipta[1]}")
        print(f"3. {pencipta[2]}")
        print(f"4. {pencipta[3]}")
        print(f"5. {pencipta[4]}")
        lihat = int(input("siapa yang ingin ada lihat? "))
        if lihat == 1:
            print("~~Leonardo da Vinci~~")
            print("1. Mona Lisa ")
            print("2. The Last Supper ")
            info = int(input("lihat data penting lukisan, lukisan 1 atau 2? "))
            if info == 1:
                print("=== Lukisan Mona Lisa ===")
                print("pencipta: Leonardo da Vinci, seniman Renaissance Italia (1452-1519).")
                print("Tahun Pembuatan: Sekitar 1503-1506, meskipun Leonardo terus menyempurnakannya hingga kematiannya pada 1519.")
                print("Lokasi Saat Ini: Museum Louvre, Paris, Prancis. Dipajang di ruangan khusus sejak 1914, dengan pengamanan ketat (kaca anti-peluru dan pelindung dari suhu/kelembaban).")
                print("Umur Saat Ini: Sekitar 518-521 tahun (per 2024).")
            elif info == 2:
                print("===Lukisan The Last Supper===")
                print("Pencipta: Leonardo da Vinci, seniman, ilmuwan, dan arsitek Renaissance Italia (1452-1519).")
                print("Tahun Pembuatan: 1495-1498. Leonardo menerima komisi dari Duke of Milan, Ludovico Sforza, untuk melukis dinding ruang makan (refektori) biara Santa Maria delle Grazie.")
                print("Lokasi Saat Ini: Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia. Dilindungi oleh UNESCO sebagai Situs Warisan Dunia sejak 1980. Pengunjung dibatasi (maksimal 40 orang per 15 menit) untuk menjaga kondisi.")
                print("Umur Saat Ini: Sekitar 526-529 tahun (per 2024).")
            elif not info:
                print("eror!")
            else:
                ()

        elif lihat == 2:
            print("~~Vincent van Gogh~~")
            print("Lukisan The Starry Night")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                print("=== Lukisan The Starry Night ===")
                print("Seniman: Vincent van Gogh (1853-1890).")
                print("Tahun pembuatan: 1889.")
                print("Lokasi Saat Ini: Disimpan di Museum of Modern Art (MoMA), New York, AS, sejak 1941. Diakuisisi melalui donasi dari keluarga Lillie P. Bliss.")
                print("umur saat ini: 135 tahun (per 2024)")
            elif info == "tidak":
                print("program berhenti")
            elif not info:
                print("eror!")
            else:
                ()

        elif lihat == 3:
            print("~~Pablo Picasso~~")
            print("Lukisan Guernica")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                print("Seniman: Pablo Picasso (1881-1973), pelukis Spanyol yang menjadi tokoh utama Cubism dan seni modern.")
                print("Tahun pembuatan: 1937. Dibuat dalam waktu singkat (sekitar 35 hari) di studio Picasso di Paris, mulai Mei 1937, setelah ia mendengar berita pemboman Guernica (kota Basque, Spanyol) oleh pasukan Nazi Jerman dan fasis Italia pada 26 April 1937.")
                print("lokasi saat ini: Disimpan di Museo Nacional Centro de Arte Reina Sofía, Madrid, Spanyol, sejak 1981. Ini adalah museum seni modern nasional Spanyol, di mana Guernica menjadi karya utama.")
                print("umur saat ini: 87 tahun (per 2024)")
            elif info == "tidak":
                print("program berhenti")
            elif not info:
                print("eror!")
            else:
                ()

        elif lihat == 4:
            print("~~Salvador Dalí~~")
            print("Lukisan The Persistence of Memory")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                print("=== Lukisan The Persistence of Memory ===")
                print("Seniman: Salvador Dalí (1904-1989)")
                print("Tahun pembuatan: 1931. Dibuat selama musim panas di Port Lligat, Costa Brava, Spanyol, di rumah Dalí.")
                print("lokasi: Masih di dinding refektori biara Santa Maria delle Grazie, Milan, Italia. Dilindungi oleh UNESCO sebagai Situs Warisan Dunia sejak 1980.")
                print("umur saat ini: 93 tahun (per 2024)")
            elif info == "tidak":
                print("program berhenti")
            elif not info:
                print("eror!")
            else:
                ()
        
        elif lihat == 5:
            print("~~Johannes Vermeer~~")
            print("== Girl with a Pearl Earring ==")
            info = int(input("lihat data penting lukisan? ya/tidah: "))
            if info == "ya":
                print("seniman: Johannes Vermeer (1632-1675)")
                print("Tahun pembuatan: Sekitar 1665 (diperkirakan antara 1662-1665, karena tidak ada catatan pasti).")
                print("lokasi: Disimpan di Mauritshuis, museum seni di The Hague (Den Haag), Belanda, sejak 1902.")
                print("umur saat ini: 359 tahun (per 2024)")
            elif info == "tidak":
                print("program berhenti")
            elif not info:
                print("eror!")
            else:
                ()
        else:
            ()
    else:
        ()
else:
    ()