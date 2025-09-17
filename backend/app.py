from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import json

# Yeni program oluşturucu "beynimizi" import ediyoruz
from program_generator import generate_program

app = Flask(__name__)
# Frontend'in çalıştığı porttan gelen tüm isteklere izin veriyoruz
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# ML Modelini ve Scaler'ı yükle
try:
    model = joblib.load('ml_artifacts/activity_model.pkl')
    scaler = joblib.load('ml_artifacts/scaler.pkl')
except FileNotFoundError:
    print("Model veya scaler dosyaları bulunamadı. Lütfen 'model_builder.py' script'ini çalıştırdığınızdan emin olun.")
    model = None
    scaler = None

# Raporları ve doğruluğu başlangıçta yükle
try:
    with open('ml_artifacts/classification_report.json', 'r') as f:
        classification_report_data = json.load(f)
    with open('ml_artifacts/model_accuracy.json', 'r') as f:
        accuracy_data = json.load(f)
except FileNotFoundError:
    print("Rapor dosyaları bulunamadı. Lütfen 'model_builder.py' script'ini çalıştırın.")
    classification_report_data = None
    accuracy_data = None

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
    if not model or not scaler or not classification_report_data or not accuracy_data:
        return jsonify({"error": "Model veya rapor dosyaları yüklenemedi"}), 500
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input for analysis"}), 400

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

    # model_builder.py'den gelen modelin test doğruluğunu ve raporunu ekle
    analysis_result = {
        "predictedLevel": predicted_level,
        "modelAccuracy": accuracy_data['accuracy'],
        "classificationReport": classification_report_data,
        "userData": data
    }
    
    return jsonify(analysis_result)


@app.route('/generate-program', methods=['POST'])
def generate_program_endpoint():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Frontend'den gelen 4 anahtar kelime
    goal = data.get('goal')
    level = data.get('level')
    frequency = data.get('frequency')
    duration = data.get('duration')

    if not all([goal, level, frequency, duration]):
        return jsonify({"error": "Missing one or more required fields"}), 400

    # AI modülümüzü çağır
    program = generate_program(goal, level, frequency, duration)

    if "error" in program:
        return jsonify(program), 400

    return jsonify(program)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
