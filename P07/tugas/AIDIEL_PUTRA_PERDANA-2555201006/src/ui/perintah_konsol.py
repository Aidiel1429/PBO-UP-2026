from src.model.daftar_harga import DaftarHarga


class PerintahKonsol:
    """Penerjemah perintah konsol untuk daftar harga alat."""

    BANTUAN: str = (
        "Perintah tersedia: bantuan, ?, daftar <hari>, "
        "harga <kode> <hari>, termurah <hari>"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def _harga_satu_alat(self, kode: str, hari: int) -> str:
        for nama, biaya in self._daftar.biaya_semua(hari):
            if nama.upper().startswith(f"[{kode}]") or kode in nama.upper():
                return f"{nama}, {hari} hari: Rp{biaya:,}".replace(",", ".")
        return f"Alat berkode {kode} tidak ada dalam daftar."

    def jalankan(self, perintah: str) -> str:
        match perintah.strip().lower().split():
            case []:
                return "Perintah kosong. Ketik 'bantuan'."
            case ["bantuan"] | ["?"]:
                return PerintahKonsol.BANTUAN
            case ["daftar", hari] if hari.isdigit():
                jumlah_hari = int(hari)
                baris = [
                    f"- {nama}: Rp{biaya:,}".replace(",", ".")
                    for nama, biaya in self._daftar.biaya_semua(jumlah_hari)
                ]
                return "\n".join(baris)
            case ["harga", kode, hari] if hari.isdigit():
                return self._harga_satu_alat(kode.upper(), int(hari))
            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                return f"Termurah untuk {hari} hari: {alat.nama}"
            case [perintah_pertama, *_]:
                return f"Perintah '{perintah_pertama}' tidak dikenal."
        return "Perintah tidak dikenali."