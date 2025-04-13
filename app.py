from flask import Flask, request, render_template, jsonify
import traceback
from datetime import datetime, timedelta
from plant_data import get_suggestions

app = Flask(__name__)

# ESP32'den gelen son verileri saklamak için
esp_data = {}

@app.route('/', methods=['GET'])
def index():
    global esp_data
    print(esp_data)
    return render_template('index.html',
                           esp_data=esp_data
                          )
@app.route('/suggest', methods=['POST'])
def suggest_plants():
    global esp_data
    # Kullanıcıdan gelen veriler
    temperature = float(request.form['temperature'])
    soil_moisture = request.form['soil_status']
    season = request.form['season']
    date = request.form['start_date']
    print(temperature,soil_moisture,season,date) 

    plant_suggestions = get_suggestions(temperature, soil_moisture, season)

    return render_template('index.html', suggested_plants=plant_suggestions, start_date=date, esp_data=esp_data)

@app.route('/data', methods=['POST'])
def receive_data():
    try:
        global esp_data
        data = request.get_json(force=True)  # JSON verisi zorla çözülür
        print("Gelen veri:", data)
        
        esp_data = data

        print(esp_data)
        return jsonify({"status": "success"})

    except Exception as e:
        print("Hata oluştu:", e)
        traceback.print_exc()  # Hatanın detaylarını terminale yaz
        return jsonify({"status": "error", "message": str(e)}), 500
