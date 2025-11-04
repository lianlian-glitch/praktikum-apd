def penyambut():
    print("""
        =====================================================
        |                                                   |
        |          Selamat Datang di Fortal Dunia           |
        |                                                   |
        =====================================================
        """)
penyambut()

users={}

username = input("Masukkan username: ")
password = input("Masukkan password: ")
role = input("Masukkan role (admin/pengguna): ")

def data_user(username, password,role):    
    while True:               
        if role == "admin" or role == "pengguna":
            users.update({'username' : username, 
                            'password' : password,
                            'role' : role})
            print("Registrasi berhasil!")
            break
        else:
            print("Pilih role antara admin atau pengguna.")
            role = input("Masukkan role [admin/pengguna]: ")
            users.update({'role' : role})

def login_user(login=0):
    if login >= 3:
        print("Terlalu banyak percobaan. Program akan keluar.")
        exit()

    print("================= Login User =========================")
    username_in = input("Masukkan Username: ")
    password_in = input("Masukkan Password: ")
    role_in = input("Masukkan role (admin/pengguna): ")

    if username_in == username and password_in == password and role_in == "admin":
        show_menu_admin()
        return True
    elif username_in == username and password_in == password and role_in == "pengguna":
        show_menu_pengguna()
        return True
    else:
        print("Gagal login.")
        return login_user(login + 1)
    
DIMENSI = [
    "Dimensi 1",
    "Dimensi 2",
    "Dimensi 3"
]

def tampilkan():
    if DIMENSI:
        for judul, data in DIMENSI.items():
            print(f"{judul}: {data}")
    else:
        print("Tidak ada data untuk ditampilkan.")