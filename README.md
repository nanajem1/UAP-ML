# **Prediksi Sampah Organik dan Non-Organik untuk Optimalisasi Sistem Daur Ulang Cerdas** ♻️

![Sampah Cerdas](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Recycling_symbol.svg/1024px-Recycling_symbol.svg.png)

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
---

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
