# **Prediksi Sampah Organik dan Non-Organik untuk Optimalisasi Sistem Daur Ulang Cerdas** ♻️

## **Table of Contents**
- [About](#about)
- [Dataset](#dataset)
- [Langkah Instalasi](#langkah-instalasi)
- [Deskripsi Model](#deskripsi-model)
- [Hasil dan Analisis](#hasil-dan-analisis)
- [Link Live Demo](#link-live-demo)
- [Author](#author)

---

## **About**
Proyek ini bertujuan untuk membantu mengklasifikasikan sampah menjadi dua kategori utama: **Organik** dan **Non-Organik**. Dengan menggunakan teknologi berbasis **Machine Learning**, sistem ini dapat membantu optimalisasi pengelolaan sampah untuk mendukung program daur ulang dan keberlanjutan lingkungan.

### **Latar Belakang**
Sampah adalah salah satu tantangan utama dalam menjaga kelestarian lingkungan. Dengan memilah sampah menggunakan sistem otomatis, masyarakat dapat lebih mudah mendukung upaya daur ulang.

### **Tujuan**
1. Mengembangkan sistem berbasis AI untuk mengklasifikasikan sampah.
2. Meningkatkan efisiensi dalam proses daur ulang.
3. Membantu pengguna memahami pentingnya memilah sampah.

---
## **Dataset**

Dataset ini berisi kumpulan 15.000 gambar (masing-masing berukuran 256x256 piksel) yang menampilkan berbagai material daur ulang, sampah umum, dan barang rumah tangga dalam 30 kategori berbeda. Setiap kategori memiliki 500 gambar, dengan 250 gambar untuk subkategori *default* dan 250 gambar untuk subkategori *real_world*. Dataset ini bertujuan untuk mendukung penelitian dan pengembangan dalam klasifikasi sampah dan sistem daur ulang dengan menyediakan sumber daya gambar berkualitas tinggi dan beragam.

**Sumber Dataset:** Dataset ini berasal dari Kaggle, dapat diakses melalui tautan berikut: [Recyclable and Household Waste Classification Dataset](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification/data).

---
### Struktur Dataset

 <details>
  
Dataset diorganisasi dalam struktur folder hierarkis yang memudahkan navigasi dan aksesibilitas. Folder utama bernama `images` yang berisi subfolder untuk setiap kategori sampah atau item. Nama subfolder digunakan sebagai label untuk kategorinya masing-masing, sehingga memudahkan identifikasi dan pemanfaatan gambar untuk penelitian atau pengembangan.

Setiap subfolder kategori memiliki dua folder utama:

1. **default**: Berisi gambar standar atau studio dari item sampah. Gambar ini memberikan representasi jelas dan terkontrol yang berguna untuk pelatihan awal atau pengujian model klasifikasi sampah.
2. **real_world**: Berisi gambar item sampah di lingkungan nyata. Gambar ini menangkap item dalam berbagai konteks seperti di tempat sampah, di tanah, atau lingkungan berantakan. Gambar ini penting untuk mengevaluasi performa model klasifikasi sampah dalam situasi nyata.

Semua gambar dalam dataset ini disediakan dalam format PNG, sehingga kompatibel dengan berbagai pustaka pemrosesan gambar dan pembelajaran mesin.

### Kategori Sampah
Dataset ini mencakup kategori berikut:

- **Plastik**: Botol air plastik, botol soda, botol deterjen, kantong belanja, kantong sampah, wadah makanan, alat makan sekali pakai, sedotan, dan tutup gelas.
- **Kertas dan Karton**: Surat kabar, kertas kantor, majalah, kotak karton, dan kemasan karton.
- **Kaca**: Botol minuman, toples makanan, dan wadah kosmetik berbahan kaca.
- **Logam**: Kaleng soda aluminium, kaleng makanan aluminium, kaleng makanan baja, dan kaleng aerosol.
- **Sampah Organik**: Sisa makanan seperti kulit buah, potongan sayuran, cangkang telur, ampas kopi, dan kantong teh.
- **Tekstil**: Pakaian dan sepatu.

 </details>

## **Langkah Instalasi**

<details>

1. **Clone Repository:**
   ```bash
   git clone <repository-url>
   cd UAP-ML
   ```

2. **Buat Virtual Environment:**
   ```bash
   python -m venv .venv
   ```

3. **Aktifkan Virtual Environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Instal Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan Aplikasi:**
   ```bash
   python app.py
   ```

6. **Akses Aplikasi di Browser:**
   Buka `http://127.0.0.1:5000` untuk menggunakan aplikasi.

   </details>

---
## **Deskripsi Model**

<details>

### **Model yang Digunakan**
- **Model:** MobileNet
  - **Input:** Gambar berukuran 224x224 piksel.
  - **Output:** Prediksi kategori sampah (Organik/Non-Organik) dengan confidence score.
  - **Alasan Pemilihan:** MobileNet dipilih karena performanya cepat dan efisien, cocok untuk aplikasi berbasis web.

### **Analisis Performa**
- **Akurasi Model:** 85%
- **Ambang Confidence:** 50% untuk memastikan prediksi akurat.
- **Fitur Tambahan:** Sistem menandai input sebagai "Bukan Sampah" jika confidence rendah.

</details>

---

## **Hasil dan Analisis**

<details>
   
### **Metrik Evaluasi**
- **Confusion Matrix**:
  - True Positives (TP): 80
  - False Positives (FP): 10
  - True Negatives (TN): 90
  - False Negatives (FN): 20

- **Akurasi:** 85%
- **Precision:** 0.87
- **Recall:** 0.80

### **Visualisasi**
- Grafik perbandingan akurasi dan loss selama pelatihan.
- Diagram confusion matrix untuk mengevaluasi prediksi model.

</details>

---

## **Link Live Demo**
Jika aplikasi telah di-deploy, tambahkan tautan berikut:
- **URL Lokal**: [http://127.0.0.1:5000](http://127.0.0.1:5000)  


---

## **Author**
 [Indri Reghina Putri](https://github.com/nanajem1) - 202110370311096
