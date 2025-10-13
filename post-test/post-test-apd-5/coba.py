status = input ("pengguna/admin: ")
if status == "pengguna":
    print("Menu ")
    print("Menampilkan buah")
    print("Data-Data buah")
    Menu = int(input("pilih menu"))
    if Menu == 1:
        print("Menampilkan buah")
        daftar = ["Anggur", "Apel", "Mangga", "Pir", "Nenas", "Jeruk"]
        print(daftar[0])
        print(daftar[1])
        print(daftar[2])
        print(daftar[3])
        print(daftar[4])
        print(daftar[5])
    elif Menu == 2: