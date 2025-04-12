from flask import Flask, render_template, request

app = Flask(__name__)

# plant_dict ve temperature_ranges verilerini buraya ekliyoruz
plant_dict = {
    "temperature": {
        "0-10": {
            "spring": [("lettuce", "Once a week", "30 days")],
            "summer": [],
            "autumn": [],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days")]
        },
        "10-20": {
            "spring": [("potato", "Twice a week", "90 days"), ("cabbage", "Once a week", "60 days"), ("lettuce", "Once a week", "30 days"), ("carrot", "Once a week", "75 days")],
            "summer": [("broccoli", "Once a week", "70 days"), ("cauliflower", "Once a week", "70 days"), ("lettuce", "Once a week", "30 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("cabbage", "Once a week", "60 days"), ("lettuce", "Once a week", "30 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days")]
        },
        "15-25": {
            "spring": [("onion", "Once a week", "90 days"), ("cucumber", "Twice a week", "50 days"), ("pepper", "Twice a week", "70 days")],
            "summer": [("eggplant", "Twice a week", "80 days"), ("cucumber", "Twice a week", "50 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("cauliflower", "Once a week", "70 days"), ("onion", "Once a week", "90 days"), ("grape", "Once a week", "120 days"), ("apple", "Once a week", "365 days"), ("pear", "Once a week", "365 days"), ("cherry", "Once a week", "120 days")],
            "winter": [("cabbage", "Once a week", "60 days"), ("leek", "Once a week", "90 days")]
        },
        "15-30": {
            "spring": [("tomato", "Twice a week", "70 days"), ("watermelon", "Twice a week", "90 days")],
            "summer": [("pepper", "Twice a week", "70 days"), ("tomato", "Twice a week", "70 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days")]
        },
        "20-30": {
            "spring": [("eggplant", "Twice a week", "80 days"), ("tomato", "Twice a week", "70 days"), ("watermelon", "Twice a week", "90 days")],
            "summer": [("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("onion", "Once a week", "90 days"), ("plum", "Once a week", "120 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days")]
        },
        "31-40": {
            "spring": [],
            "summer": [],
            "autumn": [],
            "winter": []
        }
    },
    "humidity": {
        "dry": {
            "spring": [("tomato", "Twice a week", "70 days"), ("pepper", "Twice a week", "70 days")],
            "summer": [("eggplant", "Twice a week", "80 days"), ("cucumber", "Twice a week", "50 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days")]
        },
        "normal": {
            "spring": [("strawberry", "Twice a week", "30 days"), ("watermelon", "Twice a week", "90 days")],
            "summer": [("pepper", "Twice a week", "70 days"), ("tomato", "Twice a week", "70 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days")]
        },
        "humid": {
            "spring": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days")],
            "summer": [("broccoli", "Once a week", "70 days"), ("cauliflower", "Once a week", "70 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("leek", "Once a week", "90 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days")]
        }
    }
}

temperature_ranges = {
    "0-10": (0, 10),
    "10-20": (10, 20),
    "15-25": (15, 25),
    "15-30": (15, 30),
    "20-30": (20, 30),
    "31-40": (31, 40)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest_plants():
    # Kullanıcıdan gelen veriler
    temperature = float(request.form['temperature'])
    soil_moisture = request.form['soil_moisture']
    season = request.form['season']
    
    # Sıcaklık aralığını belirleme
    temperature_range = None
    for temp_range in temperature_ranges:
        min_temp, max_temp = temperature_ranges[temp_range]
        if min_temp <= temperature <= max_temp:
            temperature_range = temp_range
            break
    
    # Sıcaklık aralığına göre bitkileri alıyoruz
    if temperature_range:
        plants = plant_dict['temperature'][temperature_range][season]
    else:
        plants = []

    # Nem durumuna göre bitkileri filtreleme
    if soil_moisture in plant_dict['humidity']:
        humidity_plants = plant_dict['humidity'][soil_moisture][season]
        plants = list(set(plants) & set(humidity_plants))

    # Bitkileri formatlı şekilde hazırlıyoruz
    plant_suggestions = [(plant[0], plant[1], plant[2]) for plant in plants]

    return render_template('index.html', suggestions=plant_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
