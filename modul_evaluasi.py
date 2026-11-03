def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Menghitung persentase kehadiran."""
    persentase = (hadir / total_pertemuan) * 100
    return persentase
 
 
def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Menghitung nilai akhir: Tugas 20%, UCP 1 40%, UCP 2 40%."""
    nilai_akhir = (tugas * 0.2) + (ucp1 * 0.4) + (ucp2 * 0.4)
    return nilai_akhir
 
 
def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Menentukan status kelayakan asisten laboratorium."""
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran di bawah 75%)"
    elif nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi Syarat)"
    else:
        return "DITOLAK (Nilai Akhir Kurang)"
 