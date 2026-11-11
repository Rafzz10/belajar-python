from pathlib import Path


NAMA_FILE = "data.txt"


def tulis_file(data):
    if not data.strip():
        print("Catatan tidak boleh kosong!\n")
        return
    with open(NAMA_FILE, "a", encoding="utf-8") as f:
        f.write(f"{data}\n")
    print("Catatan ditambahkan ✓\n")


def baca_file():
    try:
        with open(NAMA_FILE, "r", encoding="utf-8") as f:
            list_baris = f.readlines()
    except FileNotFoundError:
        list_baris = []

    if not list_baris:
        print("Belum ada catatan!\n")
        return

    print("\nDaftar catatan:")
    for i, baris in enumerate(list_baris, start=1):
        print(f"{i}. {baris.strip()}")
    print()


def hapus_file():
    p = Path(NAMA_FILE)
    if not p.exists():
        print("Belum ada catatan!\n")
        return

    while True:
        konfirmasi = input("Konfirmasi hapus (y/n): ").strip().lower()
        if konfirmasi == "y":
            p.unlink()
            print("Catatan berhasil dihapus ✓\n")
            return
        elif konfirmasi == "n":
            print("Hapus catatan dibatalkan!\n")
            return
        else:
            print("Pilih y/n!\n")


def main():
    while True:
        print("=== Catatan Harian CLI ===")
        print("1. Tambah catatan")
        print("2. Lihat semua catatan")
        print("3. Hapus semua catatan")
        print("4. Keluar\n")

        pilihan = input("Input pilihan (1/2/3/4): ")

        if pilihan == "1":
            data = input("\nMasukkan catatan: ")
            tulis_file(data)
        elif pilihan == "2":
            baca_file()
        elif pilihan == "3":
            hapus_file()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia!\n")


if __name__ == "__main__":
    main()