print("masukkan Nama lengkap")
nama = input("masukkan nama: ")

print("masukkan NIM anda")
nim = int(input("input NIM: "))

print("masukkan harga")
harga = int(input("masukkan harga makanan: "))

pajakPecelLele = harga*0.05
pajakMieAyam = harga*0.08
pajakNasiPadang = harga*0.10
totalHargaPecel = harga+pajakPecelLele
totalHargaMie = harga+pajakMieAyam
totalHargaNasi = harga+pajakNasiPadang
print(f"{nama} dengan nim {nim} ingin membeli makanan dengan seharga Rp{harga}") 
print(f"jika dia membeli Pecel Lele maka biaya pesanan anda RP{totalHargaPecel} setelah mendapat pajak 5%")
print(f"jika dia membeli Mie Ayam maka biaya pesanan anda RP{totalHargaMie} setelah mendapat pajak 8%")
print(f"jika dia membeli Nasi Padang maka biaya pesanan anda RP{totalHargaNasi} setelah mendapat pajak 10%")