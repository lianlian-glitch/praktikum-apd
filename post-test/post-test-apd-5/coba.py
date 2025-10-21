status = input ("pengguna/admin: ")
if status == "pengguna":
    print("Menu")
    print("1 Menampilkan buah")
    print("2 Data-data buah")
    Menu = int(input("pilih menu: "))
    if Menu == 1:
        print("Menampilkan buah")
        daftar = ["Anggur", "Apel", "Mangga", "Pir"]
        print(f"1. {daftar[0]}")
        print(f"2. {daftar[1]}")
        print(f"3. {daftar[2]}")
        print(f"4. {daftar[3]}")
    elif Menu == 2:
        print ("Data-data buah") 
        data = ["Anggur", "Apel", "Mangga", "Pir"]
        print(f"1. {data[0]}")
        print(f"2. {data[1]}")
        print(f"3. {data[2]}")
        print(f"4, {data[3]}")
        buah = input("pilih buah: ")
        if buah == "Anggur":
            print("Anggur")
            print("Nama ilmiah: Vitis vinifera")
            print("Asal: timur tengah/sekitar laut kaspia")
            print("Kandungan nutrisi: Air, serat, vitamin c, kalium, resveratrol")
            print("Manfaat: menjaga jantung, tekanan darah, kulit, dan daya ingat")
            print("Jnid dan varietas: merah, hujau, hitam, tanpa biji")
            print("Fakta unik: buah tertua dibudidayakan manusia dan kaya antioksida")
        elif buah == "Apel":
            print("apel")
            print("Nama ilmiah: Malus domestica")
            print("Asal buah: Berasal dari asia tengah. khususnya wilayah kazakhstaan, dan kini kini di budidayakan di seluruh dunia")
            print("Kandungan nutrisi: mrengandung vitamin C, vitamin  A, serat, air, antioksida, serta mineral seprti kalium")
            print("Manfaat kesehatan: membantu menjaga kesehatan jantung, menurunkan resiko diabetes, melancarkan pencernaan") 
            print("Jenis dan varietas: Red deliclous, grany smith")
            print("fakta unik: Mengapung di air karena banyak udara")   
        elif buah == "Mangga":
            print("Mangga")
            print("Nama ilmiah: Mangifera indica")
            print("Asal buah: India dan asia tengah")
            print("Kandungan nurtisi: vitamin A,C,E,serat,kalium,dan antioksida")
            print("Manfaat kesehatan: Menjaga imun, baik untuk kulit dan mata, melancarkan pencernaan, menurunkan kolestrol")
            print("Jenis dan varietas: Arumanis, manalagi, manalagi, golek")
            print("Fakta unik: disebut raja buah tropis dan termasuk buah nasional india")
        elif buah == "Pir":
            print("Pir")
            print("Nama ilmiah: Pyrus communis")
            print("Asal buah: Eropa timur dan asia barat")
            print("Kandungan nutrusi: Air,serat,vitami c,k,kalium")
            print("Manfaat kesehatan: melancarkan pencernaan, menjaga jantung, meningkatkan imun, bantu turunkan berat badan")
            print("Jenis dan varietas: Bartlett,anjou,bosc,nashi")
            print("fakta unik: Matang setelah dipetik dan berair lembut saat dimakan")
        else:
            ()
    else:
        ()
elif status == "admin":
    print("=== menu ===")
    print("1. menu")