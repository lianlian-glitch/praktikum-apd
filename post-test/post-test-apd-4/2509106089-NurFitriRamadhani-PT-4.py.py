sofa = 500000
MejaBelajar = 250000
RakLemari = 150000

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



print("Menampilkan piliha:")
print("opsi 1. Sofa dengan Harga per unit Rp500.000")
print("opsi 2. Meja Belajar dengan Harga per unit Rp250.000")
print("opsi 3. Rak lemari dengan Harga per unit Rp150.000")
print("opsi 4. keluar dari program")
opsi = int(input("input opis anda: "))
if opsi == 1:
    print("1. Sofa dengan Harga per unit Rp500.000")
    unit = int(input("berapa unit yang anda butuhkan? "))
    totalBayar =  0
    for i in range (unit):
        totalBayar += sofa
        totalBayar = sofa*unit
        if totalBayar >= 700000:
            potongan = totalBayar*0.20
            totalAkhir = totalBayar-potongan
            print(f"anda mendapatkan diskon 20% menjadi Rp{totalAkhir}")
    else:
        print()
    totalBayar = sofa*unit
    print(f"total biaya yang harus anda bayar adalah Rp{totalBayar}")
elif opsi == 2:
    print("2. Meja Belajar dengan Harga per unit Rp250.000")
    unit = int(input("berapa unit yang anda butuhkan? "))
    for i in range (unit):
        totalBayar = MejaBelajar*unit
        print(f"total biaya yang harus anda bayar adalah Rp{totalBayar}")
        if totalBayar >= 500000 and totalBayar <= 700000:
            potongan = totalBayar*0.08
            totalAkhir = totalBayar-potongan
            print(f"anda mendapatkan diskon 8% menjadi Rp{totalAkhir}")
    else:
        print()
    totalBayar = MejaBelajar*unit
    print(f"total biaya yang harus anda bayar adalah Rp{totalBayar}")
elif opsi == 3:
    print("3. Rak lemari dengan Harga per unit Rp150.000")
    unit = int(input("berapa unit yang anda butuhkan? "))
    for i in range (unit):
        totalBayar = MejaBelajar*unit
        print(f"total biaya yang harus anda bayar adalah Rp{totalBayar}")
        if totalBayar >= 150000 and totalBayar <= 500000:
            print("dan juga anda mendapatkan Kitchen Set")
    else:
        print()
    totalBayar = MejaBelajar*unit
    print(f"total biaya yang harus anda bayar adalah Rp{totalBayar}")
elif opsi == 4:
    print("keluar dari program")
else:
    print("Error: Input bukan angka bulat yang valid")