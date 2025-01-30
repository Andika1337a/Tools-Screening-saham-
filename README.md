# Tools-Screening-saham-
Tools Screening saham By Andika1337

Berikut adalah contoh sederhana script Python untuk melakukan auto-screening saham menggunakan library `yfinance` untuk mengambil data saham dan `pandas` untuk analisis data. Script ini akan melakukan screening berdasarkan beberapa kriteria seperti P/E Ratio, Dividend Yield, dan Market Cap.

### Prasyarat:
1. Install library yang diperlukan:
   pip install yfinance pandas

Penjelasan:
1. Library `yfinance`: Digunakan untuk mengambil data saham dari Yahoo Finance.
2. Kriteria Screening**:
   - P/E Ratio**: Harga saham dibagi dengan earnings per share (EPS). Biasanya, P/E rendah dianggap undervalued.
   - Dividend Yield: Dividen per saham dibagi dengan harga saham. Yield tinggi menarik bagi investor yang mencari pendapatan.
   - Market Cap: Kapitalisasi pasar, menunjukkan ukuran perusahaan.
3. Hasil: Script akan menampilkan saham yang memenuhi kriteria.

Catatan:
- Anda bisa menyesuaikan ticker saham (misalnya, saham IDX berakhiran `.JK`).
- Kriteria screening bisa disesuaikan sesuai kebutuhan.
- Pastikan koneksi internet stabil karena script mengambil data secara real-time.

Jika Anda ingin menambahkan fitur atau kriteria lain, silakan modifikasi script sesuai kebutuhan!
