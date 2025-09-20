# FitBit Coach: AI-Powered Personal Fitness Koçu

FitBit Coach'a hoş geldiniz! Bu akıllı web uygulaması, kişisel fitness asistanınız olmak üzere tasarlanmıştır. Proje, Fitbit verilerinize dayanarak size özel antrenman programları sunmak, fiziksel aktivitenizi, uyku düzeninizi ve stres seviyenizi derinlemesine analiz etmek için makine öğrenmesi ve kural tabanlı bir uzman sistem kullanır.

## 🚀 Teknoloji Yığını

-   **Frontend:** React, Vite, Tailwind CSS, Recharts, Axios
-   **Backend:** Flask, Pandas, Scikit-learn, Joblib
-   **Veri Kaynağı:** Kaggle'dan [Fitbit Fitness Tracker Veri Seti](https://www.kaggle.com/datasets/arashnic/fitbit)

## 🤖 Öne Çıkan Yapay Zeka Özellikleri

Bu proje, son derece kişiselleştirilmiş ve akıllı bir kullanıcı deneyimi sunmak için hibrit bir yapay zeka yaklaşımını benimser.

### 1. Intelligent Program Generator (Expert System)

Uygulamanın kalbi, bir uzman sistem olarak çalışan yapay zeka destekli bir antrenman planlayıcısıdır. Statik antrenman planları sunmak yerine, birkaç ana faktöre dayanarak haftalık bir programı dinamik olarak oluşturur:

-   **Kullanıcının Fitness Hedefi:** (Kas Kazanımı, Kilo Kaybı, Güç, Genel Sağlık)
-   **Antrenman Sıklığı:** (Haftada 3, 4 veya 5 gün)
-   **Hybrid AI Level Assessment:** Benzersiz bir güvenlik ve kişiselleştirme özelliği. Sistem, hem **kullanıcının kendi bildirdiği fitness seviyesini** hem de makine öğrenmesi modelimiz tarafından **tahmin edilen fitness seviyesini** dikkate alır. Yapay zeka "koçu" daha sonra bu iki seviyeden *daha düşük* olanına uygun egzersizleri dikkatli bir şekilde seçerek programın hem etkili hem de güvenli olmasını sağlar.
-   **Dinamik Egzersiz Seçimi:** Sistem, kullanıcının hedefine göre bileşik hareketlere öncelik veren ve izolasyon egzersizleri ekleyen zengin bir egzersiz veritabanı kullanır. Ayrıca her antrenman günü için otomatik olarak ısınma ve soğuma rutinleri içerir.

### 2. Comprehensive Activity Analysis (`My Activity` Sayfası)

Bu sayfa, veri analizi ve makine öğrenmesi ile desteklenen, kullanıcının sağlığı hakkında derinlemesine bilgiler sunan kişisel bir sağlık panosu olarak hizmet vermektedir.

-   **Fitness Level Prediction:**
    -   **Model:** Denetimli bir makine öğrenmesi algoritması olan **K-Nearest Neighbors (KNN) Classifier** kullanıyoruz.
    -   **Süreç:** Model, günlük aktivite metriklerindeki (Toplam Adım, Aktif Dakikalar, Yakılan Kalori vb.) kalıpları tanımak için Fitbit veri seti üzerinde eğitilmiştir. Sayfayı ziyaret ettiğinizde, örnek verileriniz modele beslenir ve model, aktivite profilinizin "Başlangıç", "Orta Düzey" veya "İleri Düzey" bir fitness seviyesiyle uyumlu olup olmadığını tahmin eder. Modelin doğruluğu, güvenilirliği sağlamak için sağlam bir **5-fold Cross-Validation** yöntemi kullanılarak değerlendirilir.

-   **Sleep Quality Score:** Bu skor (0-100), **uyku verimliliğine** (sleep efficiency) dayanarak hesaplanır: `UykudaGeçenToplamDakika`'nın `YataktaGeçenToplamSüre`'ye oranı. Daha yüksek bir skor, daha dinlendirici ve verimli bir uykuya işaret eder.

-   **Estimated Stress Score:** Bu skor (0-100), kullanıcının saniye saniye kalp atış hızı verilerinden **Heart Rate Variability (HRV)** analiz edilerek tahmin edilir. Genellikle, daha yüksek değişkenlik (kalp atış hızında daha yüksek bir standart sapma), daha düşük stres ve daha iyi toparlanma ile ilişkilidir. Skor, kolayca anlaşılabilir olması için normalize edilmiştir.

## ⚙️ Başlarken: Kurulum ve Çalıştırma

Projeyi yerel makinenizde kurmak ve çalıştırmak için bu adımları izleyin.

### Ön Gereksinimler

-   [Node.js](https://nodejs.org/) (v18 veya üstü önerilir)
-   [Python](https://www.python.org/) (v3.9 veya üstü önerilir) & Pip
-   Bir Kaggle hesabı ve API anahtarı.

### 1. Kaggle API Kurulumu

Gerekli veri setini indirmek için bir Kaggle API anahtarına ihtiyacınız var.

1.  Kaggle hesap ayarlarınıza gidin (`https://www.kaggle.com/<KullanıcıAdınız>/account`).
2.  "Create New API Token"a tıklayın. Bu, bir `kaggle.json` dosyası indirecektir.
3.  Bu dosyayı uygun dizine yerleştirin:
    -   **Windows:** `C:\Users\<KullanıcıAdınız>\.kaggle\`
    -   **macOS/Linux:** `~/.kaggle/`
    *(Eğer `.kaggle` klasörü mevcut değilse oluşturmanız gerekebilir)*.

### 2. Backend Kurulumu

1.  Terminalinizde **projenin kök dizinine** gidin.

2.  **Python bağımlılıklarını yükleyin:**
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Veri setini indirin:**
    Bu proje, Kaggle'daki Fitbit veri setini kullanır.
    ```bash
    # Not: PowerShell'de bu komutları tek tek çalıştırmanız gerekebilir.
    kaggle datasets download -d arashnic/fitbit -p data/ --unzip
    ```
    Bu komut, veri setini `/data` klasörüne indirip sıkıştırılmış dosyaları çıkaracaktır.

4.  **Build the AI Model:**
    Sunucuyu başlatmadan önce model oluşturma betiğini çalıştırmalısınız. Bu, verileri analiz edecek, KNN modelini ve ölçekleyiciyi (scaler) eğitecek ve gerekli yapay zeka dosyalarını kaydedecektir.
    ```bash
    python backend/model_builder.py
    ```
    Bu komut, `/backend` içinde bir `ml_artifacts` klasörü oluşturacaktır.

5.  **Flask Sunucusunu Çalıştırın:**
    Backend klasörüne gidin ve uygulamayı çalıştırın.
    ```bash
    cd backend
    python app.py
    ```
    Backend sunucusu şimdi `http://localhost:5000` adresinde çalışıyor olacak.

### 3. Frontend Kurulumu

1.  **Yeni bir terminal açın** ve projenin kök dizinine gidin.

2.  **Frontend klasörüne gidin ve Node.js bağımlılıklarını yükleyin:**
    ```bash
    cd frontend
    npm install
    ```

3.  **Frontend Geliştirme Sunucusunu Çalıştırın:**
    ```bash
    npm run dev
    ```
    React uygulaması şimdi `http://localhost:5173` adresinde çalışıyor olacak.

### 4. Kurulum Tamamlandı!

FitBit Coach'u kullanmaya başlamak için tarayıcınızda `http://localhost:5173` adresini açın.
