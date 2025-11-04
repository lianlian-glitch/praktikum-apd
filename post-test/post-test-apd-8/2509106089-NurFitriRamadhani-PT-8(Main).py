from LoginNMenu import login_admin, menu_pengguna
from Fungsi import tampilkan_header

print("Manajemen Koleksi Lukisan")
print("~program dimulai~")

status = input("Login sebagai (admin/pengguna): ").lower()

if status == "admin":
    login_admin()
elif status == "pengguna":
    tampilkan_header()
    menu_pengguna()
else:
    print("Status tidak valid! Pilih 'admin' atau 'pengguna'.")
