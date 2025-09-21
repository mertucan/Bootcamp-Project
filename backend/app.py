from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import json
import numpy as np # Numpy'yi içe aktar

# Yeni program oluşturucu "beynimizi" import ediyoruz
from program_generator import generate_program

app = Flask(__name__)
# Frontend'in çalıştığı porttan gelen tüm isteklere izin veriyoruz
# Debugging için ayarı daha esnek hale getiriyoruz
CORS(app)

# ML Modelini ve Scaler'ı yükle
try:
    model = joblib.load('ml_artifacts/activity_model.pkl')
    scaler = joblib.load('ml_artifacts/scaler.pkl')
except FileNotFoundError:
    print("Model veya scaler dosyaları bulunamadı. Lütfen 'model_builder.py' script'ini çalıştırdığınızdan emin olun.")
    model = None
    scaler = None

# Veri setlerini ve raporları yükle
try:
    # Analiz için gerekli tüm veri setlerini yükle
    activity_df = pd.read_csv('../data/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')
    sleep_df = pd.read_csv('../data/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv')
    heartrate_df = pd.read_csv('../data/mturkfitbit_export_4.12.16-5.12.16/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv')

    with open('ml_artifacts/classification_report.json', 'r') as f:
        classification_report_data = json.load(f)
    with open('ml_artifacts/model_accuracy.json', 'r') as f:
        accuracy_data = json.load(f)
except FileNotFoundError:
    print("Rapor veya veri set dosyaları bulunamadı. Lütfen 'model_builder.py' script'ini çalıştırdığınızdan ve veri setinin doğru yolda olduğundan emin olun.")
    activity_df, sleep_df, heartrate_df = None, None, None
    classification_report_data, accuracy_data = None, None

def calculate_stress_score(user_id):
    """Kalp atış hızı değişkenliğine dayalı bir stres skoru hesaplar."""
    if heartrate_df is None: return 0
    user_hr = heartrate_df[heartrate_df['Id'] == user_id]['Value']
    if len(user_hr) < 2: return 50 # Yetersiz veri için varsayılan
    
    # Kalp atış hızının standart sapmasını kullanarak bir stres metriği oluştur
    hr_std_dev = user_hr.std()
    # Tersine çevirerek daha yüksek std dev'nin daha düşük stres (daha iyi değişkenlik) anlamına gelmesini sağla
    # Sonucu 0-100 aralığına normalize et (bu basit bir normalizasyondur)
    stress_score = max(0, 100 - (hr_std_dev * 2)) 
    return round(stress_score, 2)

@app.route('/get-random-activity', methods=['GET'])
def get_random_activity():
    if activity_df is None:
        return jsonify({"error": "Activity data not loaded"}), 500
    
    # Veri setinden rastgele bir satır seç
    random_row = activity_df.sample(n=1).iloc[0]
    
    # Gerekli sütunları seç ve JSON olarak döndür
    activity_data = {
        "TotalSteps": int(random_row['TotalSteps']),
        "TotalDistance": float(random_row['TotalDistance']),
        "VeryActiveMinutes": int(random_row['VeryActiveMinutes']),
        "FairlyActiveMinutes": int(random_row['FairlyActiveMinutes']),
        "LightlyActiveMinutes": int(random_row['LightlyActiveMinutes']),
        "SedentaryMinutes": int(random_row['SedentaryMinutes']),
        "Calories": int(random_row['Calories'])
    }
    
    return jsonify(activity_data)

def get_user_sleep_data(user_id):
    """Kullanıcının uyku verilerini alır ve bir kalite skoru hesaplar."""
    if sleep_df is None: return {"quality_score": 0, "total_minutes_asleep": 0}
    user_sleep = sleep_df[sleep_df['Id'] == user_id]
    if user_sleep.empty: return {"quality_score": 0, "total_minutes_asleep": 0}
    
    # En son uyku kaydını al
    latest_sleep = user_sleep.iloc[-1]
    total_minutes_asleep = int(latest_sleep['TotalMinutesAsleep'])  # int64'den int'e dönüştür
    total_time_in_bed = int(latest_sleep['TotalTimeInBed'])        # int64'den int'e dönüştür
    
    # Uyku Verimliliği = (Uyunan Süre / Yatakta Kalınan Süre) * 100
    efficiency = (total_minutes_asleep / total_time_in_bed) * 100 if total_time_in_bed > 0 else 0
    
    return {
        "quality_score": round(efficiency, 2),
        "total_minutes_asleep": total_minutes_asleep
    }

@app.route('/predict-level', methods=['POST'])
def predict_level_endpoint():
    if not model or not scaler:
        return jsonify({"error": "ML Model not loaded"}), 500
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input for level prediction"}), 400

    # Gelen veriyi modelin beklediği formata dönüştür
    features = ['TotalSteps', 'TotalDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']
    try:
        user_df = pd.DataFrame([data], columns=features)
        user_data_scaled = scaler.transform(user_df)
    except Exception as e:
        return jsonify({"error": f"Error processing data for ML model: {e}"}), 400

    # Aktivite seviyesini tahmin et
    prediction = model.predict(user_data_scaled)[0]

    # Modelin Türkçe çıktısını, frontend'in beklediği İngilizce değere çevir
    level_map = {
        "Düşük Aktif": "beginner",
        "Orta Aktif": "intermediate",
        "Yüksek Aktif": "advanced"
    }
    predicted_level = level_map.get(prediction, "beginner")
    
    return jsonify({"predictedLevel": predicted_level})

@app.route('/activity-analysis', methods=['POST'])
def activity_analysis_endpoint():
    if not all([model, scaler, classification_report_data, accuracy_data, activity_df is not None]):
        return jsonify({"error": "Model, rapor dosyaları veya aktivite veri seti yüklenemedi"}), 500
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input for analysis"}), 400

    # Örnek bir kullanıcı ID'si al (gerçek bir sistemde bu, oturumdan gelir)
    sample_user_id = 1503960366 

    features = ['TotalSteps', 'TotalDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories']
    try:
        user_df = pd.DataFrame([data], columns=features)
        user_data_scaled = scaler.transform(user_df)
    except Exception as e:
        return jsonify({"error": f"Error processing data for ML model: {e}"}), 400

    # Seviyeyi tahmin et
    prediction = model.predict(user_data_scaled)[0]
    level_map = {"Düşük Aktif": "Beginner", "Orta Aktif": "Intermediate", "Yüksek Aktif": "Advanced"}
    predicted_level = level_map.get(prediction, "Beginner")

    # Yeni skorları ve verileri hesapla
    stress_score = calculate_stress_score(sample_user_id)
    sleep_data = get_user_sleep_data(sample_user_id)

    # model_builder.py'den gelen modelin test doğruluğunu ve raporunu ekle
    analysis_result = {
        "predictedLevel": predicted_level,
        "modelAccuracy": accuracy_data['accuracy'],
        "classificationReport": classification_report_data,
        "userData": data,
        "sleepData": sleep_data,
        "stressScore": stress_score,
    }
    
    return jsonify(analysis_result)


@app.route('/generate-program', methods=['POST'])
def generate_program_endpoint():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Frontend'den gelen 4 anahtar kelime
    goal = data.get('goal')
    user_level = data.get('level') # Kullanıcının seçtiği
    frequency = data.get('frequency')
    predicted_level = data.get('predictedLevel') # Frontend'in gönderdiği tahmin edilen seviye

    if not all([goal, user_level, frequency, predicted_level]):
        return jsonify({"error": "Missing one or more required fields"}), 400

    # AI modülümüzü yeni 4 parametre ile çağır
    program = generate_program(goal, user_level, predicted_level, frequency)

    if "error" in program:
        return jsonify(program), 400

    return jsonify(program)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
