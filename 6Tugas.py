class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    def __init__(self, nama, nim, jurusan, ipk=0.0):
        # Instance attributes
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def perkenalan_diri(self):
        print(f"Halo, nama saya {self.nama}, NIM {self.nim}, "
              f"jurusan {self.jurusan} di {Mahasiswa.universitas}. "
              f"IPK saya {self.ipk:.2f}.")

    def update_ipk(self, ipk_baru):
        print(f"IPK {self.nama} diperbarui dari {self.ipk:.2f} menjadi {ipk_baru:.2f}")
        self.ipk = ipk_baru

    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# ===== Instansiasi 3 object dengan data berbeda =====
mhs1 = Mahasiswa("Andi Pratama", "2024001", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Siti Rahma", "2024002", "Teknik Informatika", 3.20)
mhs3 = Mahasiswa("Budi Santoso", "2024003", "Teknik Informatika")  # IPK default 0.0

daftar_mhs = [mhs1, mhs2, mhs3]

# ===== Demonstrasi semua method =====
print("=== PERKENALAN DIRI ===")
for m in daftar_mhs:
    m.perkenalan_diri()

print("\n=== UPDATE IPK ===")
mhs3.update_ipk(2.60)
mhs2.update_ipk(3.55)

print("\n=== PREDIKAT KELULUSAN ===")
for m in daftar_mhs:
    print(f"{m.nama} (IPK {m.ipk:.2f}) -> {m.predikat_kelulusan()}")

print("\n=== CLASS ATTRIBUTE ===")
print("Universitas:", Mahasiswa.universitas)