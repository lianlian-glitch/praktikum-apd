nim = 2509106089
nama = "Nur Fitri Ramadhani"
ukt = 6000000

nama = input("masukkan nama: ")
nim = int(input("input NIM: "))

if nama == "Nur Fitri Ramadhani" and nim == 2509106089:
    print("piliha:")
    print("1. lunas (sekali bayar)")
    print("2. cicilann 2x per Semester")
    print("3. cicilan 4x per Semester")
    print("4. cicilann 6x per Semester")
    pilihan = int(input("input pilihan: "))
    if pilihan == 1:
        TotalBayar = ukt+(ukt*0.01)
        print(f"Rp{TotalBayar}")
    elif pilihan == 2:
        TotalBayar = ukt+(ukt*0.05)
        cicilan = TotalBayar/2
        print(f"Total yang harus di bayar Rp{TotalBayar}")
        print(f"Cicilan yang harus di bayar dalam 2x per semester Rp{cicilan}")
    elif pilihan == 3:
        TotalBayar = ukt+(ukt*0.08)
        cicilan = TotalBayar/4
        print(f"Total yang harus di bayar Rp{TotalBayar}")
        print(f"Cicilan yang harus di bayar dalam 4x per semester Rp{cicilan}")
    elif pilihan == 4:
        TotalBayar = ukt+(ukt*0.12)
        cicilan = TotalBayar/6
        print(f"Total yang harus di bayar Rp{TotalBayar}")
        print(f"Cicilan yang harus di bayar dalam 6x per semester Rp{cicilan}")
    else:
        print("output tidak valid")
else:
    print("gagal login")