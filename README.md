# **Prediksi Sampah Organik dan Non-Organik untuk Optimalisasi Sistem Daur Ulang Cerdas** ♻️

## **Table of Contents**
- [About](#about)
- [Dataset](#dataset)
- [Langkah Instalasi](#langkah-instalasi)
- [Deskripsi Model](#deskripsi-model)
- [Hasil dan Analisis](#hasil-dan-analisis)
- [Link Live Demo](#link-live-demo)
- [Tampilan Lokal Web Deployment](#tampilam-lokal-web-deployment)
- [Author](#author)

---

## **About**
Sampah adalah salah satu tantangan utama dalam menjaga kelestarian lingkungan. Dengan memilah sampah menggunakan sistem otomatis, masyarakat dapat lebih mudah mendukung upaya daur ulang.
Proyek ini bertujuan untuk membantu mengklasifikasikan sampah menjadi dua kategori utama: **Organik** dan **Non-Organik**. Dengan menggunakan teknologi berbasis **Machine Learning**, sistem ini dapat membantu optimalisasi pengelolaan sampah untuk mendukung program daur ulang dan keberlanjutan lingkungan.

### **Tujuan**
1. Mengembangkan sistem berbasis AI untuk mengklasifikasikan sampah.
2. Meningkatkan efisiensi dalam proses daur ulang.
3. Membantu pengguna memahami pentingnya memilah sampah.

---
## **Dataset**

Dataset ini berisi kumpulan 15.000 gambar (masing-masing berukuran 256x256 piksel) yang menampilkan berbagai material daur ulang, sampah umum, dan barang rumah tangga dalam 30 kategori berbeda. Setiap kategori memiliki 500 gambar, dengan 250 gambar untuk subkategori *default* dan 250 gambar untuk subkategori *real_world*. Dataset ini bertujuan untuk mendukung penelitian dan pengembangan dalam klasifikasi sampah dan sistem daur ulang dengan menyediakan sumber daya gambar berkualitas tinggi dan beragam.

**Sumber Dataset:** Dataset ini berasal dari Kaggle, dapat diakses melalui tautan berikut: [Recyclable and Household Waste Classification Dataset](https://www.kaggle.com/datasets/alistairking/recyclable-and-household-waste-classification/data).

## Struktur Dataset

 <details>
  
Dataset diorganisasi dalam struktur folder hierarkis yang memudahkan navigasi dan aksesibilitas. Folder utama bernama `images` yang berisi subfolder untuk setiap kategori sampah atau item. Nama subfolder digunakan sebagai label untuk kategorinya masing-masing, sehingga memudahkan identifikasi dan pemanfaatan gambar untuk penelitian atau pengembangan.

Setiap subfolder kategori memiliki dua folder utama:

1. **default**: Berisi gambar standar atau studio dari item sampah. Gambar ini memberikan representasi jelas dan terkontrol yang berguna untuk pelatihan awal atau pengujian model klasifikasi sampah.
2. **real_world**: Berisi gambar item sampah di lingkungan nyata. Gambar ini menangkap item dalam berbagai konteks seperti di tempat sampah, di tanah, atau lingkungan berantakan. Gambar ini penting untuk mengevaluasi performa model klasifikasi sampah dalam situasi nyata.

Dengan 30  kategori yang masing masing dibagi ke dalam tiga subset: train (70%), validation (15%), dan test (15%) untuk memastikan model dapat dilatih, divalidasi, dan diuji dengan baik

### Kategori Sampah
Dataset ini mencakup kategori berikut:

- **Plastik**: Botol air plastik, botol soda, botol deterjen, kantong belanja, kantong sampah, wadah makanan, alat makan sekali pakai, sedotan, dan tutup gelas.
- **Kertas dan Karton**: Surat kabar, kertas kantor, majalah, kotak karton, dan kemasan karton.
- **Kaca**: Botol minuman, toples makanan, dan wadah kosmetik berbahan kaca.
- **Logam**: Kaleng soda aluminium, kaleng makanan aluminium, kaleng makanan baja, dan kaleng aerosol.
- **Sampah Organik**: Sisa makanan seperti kulit buah, potongan sayuran, cangkang telur, ampas kopi, dan kantong teh.
- **Tekstil**: Pakaian dan sepatu.

 </details>
 
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
   Buka `http://127.0.0.1:8000` untuk menggunakan aplikasi.

   </details>

---
## **Deskripsi Model**

Proyek ini mengimplementasikan model deep learning untuk mengklasifikasikan sampah ke dalam **30 kategori** menggunakan transfer learning dengan arsitektur MobileNet. Dataset diorganisasi ke dalam tiga subset: **70% untuk training**, **15% untuk validasi**, dan **15% untuk pengujian**.


 <details>

- **Base Model**: MobileNet (weights = "imagenet", input shape = (224, 224, 3))
- **Layer Tambahan**:
  - GlobalAveragePooling2D
  - Batch Normalization
  - Dense Layers dengan aktivasi ReLU
  - Dropout Layers untuk mencegah overfitting
  - Dense Layer terakhir dengan aktivasi Softmax untuk 30 kelas keluaran
- **Total Parameter**:
  - Trainable: **561.37 K**
  - Non-Trainable: **2.31 M**

### Preprocessing Data
1. **Augmentasi Data (Training)**:
   - Rescaling (1/255)
   - Rotasi acak, pergeseran, shear, dan zoom
   - Flip horizontal
2. **Preprocessing untuk Validasi dan Pengujian**:
   - Rescaling (1/255)

Generator data digunakan untuk memuat dan memproses gambar secara dinamis selama pelatihan dan evaluasi.

### Konfigurasi Pelatihan
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy
- **Epochs**: 30
- **Batch Size**: 32
- **Ukuran Input Gambar**: 224 x 224 x 3

 </details>

---

## **Hasil dan Analisis**

Model ini mencapai metrik performa berikut pada data pengujian:
- **Akurasi**: **81.13%**
- **Loss**: **0.59**

Model dapat dilihat di Google Colab melalui link berikut:
[Model Klasifikasi](https://colab.research.google.com/drive/1eeZcsnz0NKTCcBmzubqCg1r2wRiq0kCl?authuser=0#scrollTo=JAVez2ZIt2qb)


<details>
   
### Laporan Klasifikasi (Data Pengujian)

| Nama Kategori                  | Precision | Recall | F1-Score | Support |
|--------------------------------|-----------|--------|----------|---------|
| aerosol_cans                   | 0.79      | 0.77   | 0.78     | 71      |
| aluminum_food_cans             | 0.48      | 0.48   | 0.48     | 71      |
| aluminum_soda_cans             | 0.77      | 0.80   | 0.79     | 71      |
| cardboard_boxes                | 0.58      | 0.63   | 0.61     | 71      |
| cardboard_packaging            | 0.51      | 0.49   | 0.50     | 71      |
| clothing                       | 0.74      | 0.72   | 0.73     | 71      |
| coffee_grounds                 | 0.91      | 0.86   | 0.88     | 71      |
| disposable_plastic_cutlery     | 0.97      | 0.90   | 0.93     | 71      |
| eggshells                      | 0.82      | 0.96   | 0.88     | 71      |
| food_waste                     | 0.80      | 0.93   | 0.86     | 71      |
| glass_beverage_bottles         | 0.77      | 0.79   | 0.78     | 71      |
| glass_cosmetic_containers      | 0.74      | 0.92   | 0.82     | 71      |
| glass_food_jars                | 0.93      | 0.75   | 0.83     | 71      |
| magazines                      | 0.85      | 0.90   | 0.88     | 71      |
| newspaper                      | 0.89      | 0.77   | 0.83     | 71      |
| office_paper                   | 0.48      | 0.66   | 0.56     | 71      |
| paper_cups                     | 0.77      | 0.85   | 0.81     | 71      |
| plastic_cup_lids               | 0.79      | 0.77   | 0.78     | 71      |
| plastic_detergent_bottles      | 0.91      | 0.87   | 0.89     | 71      |
| plastic_food_containers        | 0.93      | 0.58   | 0.71     | 71      |
| plastic_shopping_bags          | 0.69      | 0.79   | 0.74     | 71      |
| plastic_soda_bottles           | 0.74      | 0.83   | 0.78     | 71      |
| plastic_straws                 | 0.98      | 0.76   | 0.86     | 71      |
| plastic_trash_bags             | 0.94      | 0.69   | 0.80     | 71      |
| plastic_water_bottles          | 0.75      | 0.62   | 0.68     | 71      |
| shoes                          | 0.87      | 0.94   | 0.91     | 71      |
| steel_food_cans                | 0.51      | 0.52   | 0.52     | 71      |
| styrofoam_cups                 | 0.96      | 0.77   | 0.86     | 71      |
| styrofoam_food_containers      | 0.84      | 0.93   | 0.88     | 71      |
| tea_bags                       | 0.73      | 0.79   | 0.76     | 71      |

| **Akurasi Keseluruhan**        |           |        | **0.77** | **2130** |
| **Rata-rata Makro**            | **0.78**  | **0.77** | **0.77** | **2130** |
| **Rata-rata Tertimbang**       | **0.78**  | **0.77** | **0.77** | **2130** |


### Fitur Utama
- Transfer learning dengan MobileNet untuk ekstraksi fitur
- Augmentasi data untuk meningkatkan generalisasi model
- Klasifikasi multi-kelas untuk 30 kategori sampah




</details>

---

## **Link Live Demo**
- **URL Lokal**: [http://127.0.0.1:8000](http://127.0.0.1:8000)  


---
## **Tampilan Lokal Web Deployment**

### HomePage

![Home Page](https://github.com/nanajem1/UAP-ML/blob/main/static/images/homepage.jpg)

### Tampilan Prediction Result

![Hasil Prediksi](https://github.com/nanajem1/UAP-ML/blob/main/static/images/predick.jpg)

---

## **Author**
 [Indri Reghina Putri](https://github.com/nanajem1) - 202110370311096
