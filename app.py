from flask import Flask, request, render_template, jsonify
from datetime import datetime, timedelta
from plant_data import get_suggestions

app = Flask(__name__)

# ESP32'den gelen son verileri saklamak için
esp_data = {}

@app.route('/', methods=['GET'])
def index():
    global esp_data
    suggested_plants = None
    schedule = None

    if request.method == 'POST':
        # Web formundan gelen verileri al
        temperature = float(request.form.get('temperature'))
        soil_status = request.form.get('soil_status')
        season = request.form.get('season')
        start_date_str = request.form.get('start_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')

        # Bitki önerilerini al
        suggested_plants = get_suggestions(temperature, soil_status, season)

        # Sulama takvimi oluştur
        schedule = []
        for plant in suggested_plants:
            days = plant["watering"]
            growth_days = plant["growth"]
            for day in range(0, growth_days, days):
                watering_day = start_date + timedelta(days=day)
                schedule.append(f"{plant['name']}: {watering_day.strftime('%d.%m.%Y')}")

    return render_template('index.html',
                           esp_data=esp_data,
                           suggested_plants=suggested_plants,
                           schedule=schedule)


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Gelen veri:", data)

    temperature = data['temperature']
    humidity = data['humidity']
    # ESP32 'soil_moisture' gönderiyor, bunu 'soil_status' olarak kullan
    soil_status = data['soil_moisture'].lower()

    plant_suggestions = get_suggestions(temperature, humidity, soil_status)
    print("Önerilen bitkiler:", plant_suggestions)

    return jsonify({"status": "success", "suggestions": plant_suggestions})
