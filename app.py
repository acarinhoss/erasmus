from flask import Flask, request, render_template
from datetime import datetime, timedelta
from plant_data import get_suggestions

app = Flask(__name__)

# ESP32'den gelen son verileri saklamak için
esp_data = {}

@app.route('/', methods=['GET', 'POST'])
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
    global esp_data
    data = request.get_json()

    if not data:
        return {"status": "error", "message": "JSON verisi yok"}, 400

    try:
        esp_data = {
            "temperature": data["temperature"],
            "humidity": data["humidity"],
            "soil": data["soil_moisture"],
            "temp_status": "Normal" if 15 < data["temperature"] < 30 else "Uygun Değil",
            "soil_status": "Nemli" if data["soil_moisture"].lower() == "humid" else "Kuru/Normal"
        }
        print("ESP32'den veri alındı:", esp_data)
        return {"status": "ok"}
    except KeyError as e:
        return {"status": "error", "message": f"Eksik alan: {str(e)}"}, 400


if __name__ == '__main__':
    app.run(debug=True)
