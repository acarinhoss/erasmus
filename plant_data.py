# plant_data.py

plant_dict = {
    "temperature": {
        "0-10": {
            "spring": [("lettuce", "Once a week", "30 days"), ("spinach", "Once a week", "40 days"), 
                      ("cabbage", "Once a week", "60 days"), ("radish", "Once a week", "25 days")],
            "summer": [("lettuce", "Once a week", "30 days"), ("arugula", "Once a week", "25 days")],
            "autumn": [("cabbage", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"), 
                      ("radish", "Once a week", "25 days")],
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
            "spring": [("watermelon", "Twice a week", "90 days"), ("melon", "Twice a week", "80 days"),
                      ("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days")],
            "summer": [("tomato", "Three times a week", "70 days"), ("eggplant", "Three times a week", "80 days"),
                      ("pepper", "Three times a week", "70 days"), ("watermelon", "Three times a week", "90 days")],
            "autumn": [("eggplant", "Twice a week", "80 days"), ("pepper", "Twice a week", "70 days")],
            "winter": [("heat-resistant spinach", "Once a week", "40 days")]
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

# 🌱 Ana öneri fonksiyonu
def get_suggestions(temp, soil_status, season):
    temp_key = None
    for key, (min_t, max_t) in temperature_ranges.items():
        if min_t <= temp <= max_t:
            temp_key = key
            break

    if not temp_key:
        return []  # Sıcaklık aralığına uyan bitki yok

    suggestions = []

    # Sıcaklığa göre öneriler
    if temp_key in plant_dict["temperature"]:
        temp_plants = plant_dict["temperature"][temp_key].get(season.lower(), [])
        for plant in temp_plants:
            suggestions.append({
                "name": plant[0],
                "watering": plant[1],
                "growth_time": plant[2],
                "based_on": "temperature"
            })

    # Nem durumuna göre öneriler
    if soil_status.lower() in plant_dict["humidity"]:
        humidity_plants = plant_dict["humidity"][soil_status.lower()].get(season.lower(), [])
        for plant in humidity_plants:
            suggestions.append({
                "name": plant[0],
                "watering": plant[1],
                "growth_time": plant[2],
                "based_on": "humidity"
            })

    return suggestions
