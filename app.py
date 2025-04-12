from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
from plant_data import plant_dict, temperature_ranges

app = Flask(__name__)

# ESP'den gelen veriyi burada tutacağız (geçici)
esp_data = {
    "temperature": None,
    "humidity": None,
    "soil": None,
    "timestamp": None
}

# Ana sayfa (veri ve giriş formu)
@app.route("/", methods=["GET", "POST"])
def index():
    global esp_data

    if request.method == "POST":
        season = request.form["season"]
        temp = float(request.form["temperature"])
        humidity = request.form["humidity"]

        # Sıcaklık aralığını bul
        selected_range = None
        for label, (low, high) in temperature_ranges.items():
            if low <= temp <= high:
                selected_range = label
                break

        suggested_plants = []

        if selected_range:
            suggested_plants = plant_dict["temperature"].get(selected_range, {}).get(season, [])
            if not suggested_plants:
                suggested_plants = plant_dict["humidity"].get(humidity, {}).get(season, [])

        return render_template("results.html", 
                               plants=suggested_plants, 
                               temp=temp, 
                               humidity=humidity, 
                               season=season,
                               esp_data=esp_data)

    return render_template("index.html", esp_data=esp_data)

# ESP32 veri gönderimi için endpoint
@app.route("/update", methods=["POST"])
def update_data():
    global esp_data

    try:
        # Örnek veri: 'T:23.5,H:55,S:650,TS:Normal,SS:Normal'
        raw_data = request.data.decode("utf-8")
        print(f"Gelen veri: {raw_data}")
        values = raw_data.split(",")

        temp = float(values[0].split(":")[1])
        humidity = int(values[1].split(":")[1])
        soil = int(values[2].split(":")[1])

        esp_data = {
            "temperature": temp,
            "humidity": humidity,
            "soil": soil,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return "Data updated successfully", 200

    except Exception as e:
        return f"Error: {e}", 400


# Bitki seçildikten sonra takvim sayfası
@app.route("/calendar", methods=["POST"])
def calendar():
    plant = request.form["plant"]
    frequency = request.form["frequency"]
    duration = int(request.form["duration"].replace(" days", ""))

    interval = 7 if "Once" in frequency else 3
    today = datetime.today()
    calendar_data = []

    for i in range(0, duration, interval):
        day = today + timedelta(days=i)
        calendar_data.append(day.strftime("%Y-%m-%d"))

    return render_template("calendar.html", plant=plant, frequency=frequency, calendar=calendar_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
