import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import classification_report
import joblib
import json
import numpy as np

# Veri setini yükle
try:
    # Veri setinin yolu, projenin kök dizinine göre ayarlandı.
    df = pd.read_csv('../data/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')
except FileNotFoundError:
    print("Hata: 'dailyActivity_merged.csv' dosyası doğru yolda bulunamadı. Lütfen dosya yolunu kontrol edin.")
    exit()

# Kullanıcıların ortalama aktivite metriklerini hesapla
user_avg_metrics = df.groupby('Id').agg({
    'TotalSteps': 'mean',
    'TotalDistance': 'mean',
    'VeryActiveMinutes': 'mean',
    'FairlyActiveMinutes': 'mean',
    'LightlyActiveMinutes': 'mean',
    'SedentaryMinutes': 'mean',
    'Calories': 'mean'
}).reset_index()

# Aktivite seviyelerini belirlemek için bir metrik oluşturalım
# Örneğin, Çok Aktif ve Orta Aktif dakikaların toplamına göre bir skor
user_avg_metrics['ActivityScore'] = user_avg_metrics['VeryActiveMinutes'] + user_avg_metrics['FairlyActiveMinutes'] * 0.5

# Aktivite seviyelerini segmentlere ayırma (Düşük, Orta, Yüksek)
# Bu eşik değerleri veri setinin dağılımına göre ayarlanabilir
bins = [0, 30, 60, user_avg_metrics['ActivityScore'].max()]
labels = ['Low Activity', 'Medium Activity', 'High Activity']
user_avg_metrics['ActivityLevel'] = pd.cut(user_avg_metrics['ActivityScore'], bins=bins, labels=labels, include_lowest=True)

# Model için özellikleri (X) ve hedefi (y) belirle
features = ['TotalSteps', 'TotalDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']
target = 'ActivityLevel'

X = user_avg_metrics[features]
y = user_avg_metrics[target].dropna() # Etiketi olmayan verileri temizle
X = X.loc[y.index] # Etiketleri temizlenmiş X'i ayarla

# Veriyi ölçeklendir (tüm veri seti üzerinde)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- YENİ KISIM: Çapraz Doğrulama ile Değerlendirme ---
knn = KNeighborsClassifier(n_neighbors=3)

# 5-katlı çapraz doğrulama ile ortalama doğruluk skorunu hesapla
# cv=5, veri setini 5 parçaya böler
accuracies = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
avg_accuracy = np.mean(accuracies)

print(f"Çapraz Doğrulama Doğruluk Skorları: {accuracies}")
print(f"Ortalama Doğruluk: {avg_accuracy:.2f}")

# Çapraz doğrulama ile her veri noktası için tahminler üret
y_pred_cv = cross_val_predict(knn, X_scaled, y, cv=5)

# Yeni tahminlere göre sınıflandırma raporunu oluştur
report = classification_report(y, y_pred_cv, output_dict=True)
print("\nÇapraz Doğrulama Sınıflandırma Raporu:")
print(classification_report(y, y_pred_cv))

# --- Kaydetme ---
# Nihai modeli TÜM veri seti üzerinde yeniden eğit (en iyi pratik)
knn.fit(X_scaled, y)
joblib.dump(knn, 'ml_artifacts/activity_model.pkl')
joblib.dump(scaler, 'ml_artifacts/scaler.pkl')

# Yeni, daha güvenilir raporu ve doğruluğu kaydet
with open('ml_artifacts/classification_report.json', 'w') as f:
    json.dump(report, f, indent=4)
with open('ml_artifacts/model_accuracy.json', 'w') as f:
    json.dump({'accuracy': avg_accuracy}, f, indent=4)

print("\nModel, scaler ve daha güvenilir raporlar 'ml_artifacts' klasörüne başarıyla kaydedildi.")

# Örnek bir program önerme fonksiyonu
def recommend_program(user_data):
    """
    Kullanıcı verilerine göre egzersiz programı önerir.
    user_data: Kullanıcının özelliklerini içeren bir pandas DataFrame.
    """
    model = joblib.load('activity_model.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # Gelen veriyi ölçeklendir
    user_data_scaled = scaler.transform(user_data)
    
    # Kullanıcının aktivite seviyesini tahmin et
    prediction = model.predict(user_data_scaled)[0]
    
    # Tahmine göre program öner
    if prediction == 'Low Activity':
        return {
            "level": "Low Activity",
            "program": "Hafif Tempo Yürüyüş (Haftada 3 gün, 30 dk) ve Esneme Hareketleri."
        }
    elif prediction == 'Medium Activity':
        return {
            "level": "Medium Activity",
            "program": "Tempolu Koşu veya Bisiklet (Haftada 3-4 gün, 45 dk) ve Temel Vücut Ağırlığı Egzersizleri."
        }
    elif prediction == 'High Activity':
        return {
            "level": "High Activity",
            "program": "Yüksek Yoğunluklu Interval Antrenman (HIIT) (Haftada 2 gün) ve Ağırlık Antrenmanı (Haftada 2-3 gün)."
        }
    else:
        return {
            "level": "Bilinmiyor",
            "program": "Lütfen daha fazla veri sağlayın."
        }

# Örnek kullanım
if __name__ == '__main__':
    # Test için bir kullanıcı verisi oluşturalım (X_test'ten bir örnek alalım)
    sample_user_data = pd.DataFrame(X.iloc[0:1])
    
    recommendation = recommend_program(sample_user_data)
    print("\n--- Örnek Program Önerisi ---")
    print(f"Tahmin Edilen Aktivite Seviyesi: {recommendation['level']}")
    print(f"Önerilen Program: {recommendation['program']}")
