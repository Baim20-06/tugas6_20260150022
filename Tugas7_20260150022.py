import modul_evaluasi
 
 
def input_angka_valid(prompt, min_val, max_val):
    """Meminta input angka dan mengulang sampai valid (anti-crash)."""
    while True:
        try:
            angka = float(input(prompt))
            if angka < min_val or angka > max_val:
                print(f"Warning: Angka harus di antara {min_val} sampai {max_val}!")
            else:
                return angka
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf/teks!")
 
 
def proses_kelayakan():
    """Meminta data aslab, lalu menampilkan hasil evaluasi."""
    print("\n--- Input Data Calon Asisten Lab ---")
    nama = input("Nama                 : ")
    nim = input("NIM                  : ")
    hadir = input_angka_valid("Jumlah kehadiran (0-14): ", 0, 14)
    tugas = input_angka_valid("Nilai Tugas (0-100)    : ", 0, 100)
    ucp1 = input_angka_valid("Nilai UCP 1 (0-100)   : ", 0, 100)
    ucp2 = input_angka_valid("Nilai UCP 2 (0-100)   : ", 0, 100)
 
    # Panggil fungsi dari modul
    persentase = modul_evaluasi.hitung_persentase_presensi(hadir)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)
 
    # Tampilkan hasil
    print("\n" + "=" * 40)
    print("      HASIL EVALUASI ASLAB AI")
    print("=" * 40)
    print(f"Nama               : {nama}")
    print(f"NIM                : {nim}")
    print(f"Kehadiran          : {hadir:.0f}/14 ({persentase:.2f}%)")
    print(f"Nilai Akhir        : {nilai_akhir:.2f}")
    print(f"Status             : {status}")
    print("=" * 40)
 
 
def main():
    while True:
        print("\n===== SISTEM EVALUASI ASLAB AI =====")
        print("1. Hitung Kelayakan")
        print("2. Keluar")
 
        try:
            pilihan = int(input("Pilih menu (1/2): "))
            if pilihan == 1:
                proses_kelayakan()
            elif pilihan == 2:
                print("Terima kasih, program selesai.")
                break
            else:
                print("Warning: Pilihan hanya 1 atau 2!")
        except ValueError:
            print("Error: Input menu harus berupa angka!")
 
 
main()
 