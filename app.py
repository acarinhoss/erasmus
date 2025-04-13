from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from plant_data import plant_dict, temperature_ranges

app = Flask(__name__)

# Son alınan ESP verilerini saklamak için değişken
latest_esp_data = {}

# 🧠 Bitki öneri sistemi
def suggest_plants(temp, soil_status, season):
    matched_range = None
    for key, (min_val, max_val) in temperature_ranges.items():
        if min_val <= temp <= max_val:
            matched_range = key
            break

    suggested = []

    # Sıcaklık bazlı öneri
    if matched_range and matched_range in plant_dict['temperature']:
        suggested += plant_dict['temperature'][matched_range].get(season, [])

    # Toprak nemi bazlı öneri
    if soil_status in plant_dict['humidity']:
        suggested += plant_dict['humidity'][soil_status].get(season, [])

    # Yinelenenleri kaldır
    unique_plants = list({p[0]: p for p in suggested}.values())

    return [
        {"name": p[0], "watering": p[1], "growth": p[2]}
        for p in unique_plants
    ]

# 📅 Sulama takvimi oluşturma
def create_schedule(start_date, watering_freq, duration_days):
    schedule = []
    freq_map = {
        "Once a week": 7,
        "Twice a week": 3,
        "Three times a week": 2
    }

    days_between = freq_map.get(watering_freq, 7)
    date = datetime.strptime(start_date, "%Y-%m-%d")

    while duration_days > 0:
        schedule.append(date.strftime("%d %B %Y"))
        date += timedelta(days=days_between)
        duration_days -= days_between

    return schedule

# 🌐 Ana sayfa - hem form hem de esp verilerini göster
@app.route('/', methods=['GET', 'POST'])
def index():
    suggested_plants = []
    schedule = []
    global latest_esp_data

    if request.method == 'POST':
        temp = float(request.form['temperature'])
        soil_status = request.form['soil_status']
        season = request.form['season']
        start_date = request.form['start_date']

        suggested_plants = suggest_plants(temp, soil_status, season)

        if suggested_plants:
            first = suggested_plants[0]
            schedule = create_schedule(start_date, first["watering"], int(first["growth"].split()[0]))

    return render_template("index.html",
                           suggested_plants=suggested_plants,
                           schedule=schedule,
                           esp_data=latest_esp_data)

# 📡 ESP32 veri gönderme endpoint'i
@app.route('/data', methods=['POST'])
def receive_esp_data():
    global latest_esp_data
    data = request.get_json()

    if not data:
        return jsonify({"error": "Veri alınamadı"}), 400

    try:
        latest_esp_data = {
            "temperature": data['temperature'],
            "humidity": data['humidity'],
            "soil": data['soil_moisture'],
            "temp_status": classify_temp(data['temperature']),
            "soil_status": data['soil_moisture']
        }
        return jsonify({"status": "Veri başarıyla alındı"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🌡️ Sıcaklık durumu sınıflandırması
def classify_temp(temp):
    if temp < 10:
        return "Soğuk"
    elif 10 <= temp <= 30:
        return "Normal"
    else:
        return "Sıcak"

if __name__ == '__main__':
    app.run(debug=True)
