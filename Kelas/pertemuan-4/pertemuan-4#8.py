angka = [2, 5, 8, 12, 15, 7, 20]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        break

    print("\nProgram selesai.")