# plant_data.py

plant_dict = {
    "temperature": {
        "0-10": {
            "spring": [("lettuce", "Once a week", "30 days"), ("spinach", "Once a week", "40 days"), 
                      ("cabbage", "Once a week", "60 days"), ("radish", "Once a week", "25 days"),
                      ("peas", "Once a week", "65 days"), ("kale", "Once a week", "55 days")],
            "summer": [("lettuce", "Once a week", "30 days"), ("arugula", "Once a week", "25 days"),
                      ("pak choi", "Once a week", "45 days")],
            "autumn": [("cabbage", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"), 
                      ("radish", "Once a week", "25 days"), ("turnip", "Once a week", "60 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days"),
                      ("Brussels sprouts", "Once a week", "100 days")]
        },
        "10-15": {
            "spring": [("potato", "Twice a week", "90 days"), ("cabbage", "Once a week", "60 days"),
                      ("lettuce", "Once a week", "30 days"), ("carrot", "Once a week", "75 days"),
                      ("beet", "Once a week", "60 days")],
            "summer": [("broccoli", "Once a week", "70 days"), ("cauliflower", "Once a week", "70 days"),
                      ("lettuce", "Once a week", "30 days"), ("green beans", "Twice a week", "55 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("cabbage", "Once a week", "60 days"),
                      ("lettuce", "Once a week", "30 days"), ("spinach", "Once a week", "40 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days"),
                      ("leek", "Once a week", "120 days")]
        },
        "15-20": {
            "spring": [("potato", "Twice a week", "90 days"), ("cabbage", "Once a week", "60 days"),
                      ("lettuce", "Once a week", "30 days"), ("carrot", "Once a week", "75 days"),
                      ("green beans", "Twice a week", "55 days"), ("cucumber", "Twice a week", "50 days")],
            "summer": [("broccoli", "Once a week", "70 days"), ("cauliflower", "Once a week", "70 days"),
                      ("lettuce", "Once a week", "30 days"), ("zucchini", "Twice a week", "50 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("cauliflower", "Once a week", "70 days"),
                      ("lettuce", "Once a week", "30 days"), ("broccoli", "Once a week", "70 days")],
            "winter": [("cabbage", "Once a week", "60 days"), ("leek", "Once a week", "90 days"),
                      ("spinach", "Once a week", "40 days")]
        },
        "20-25": {
            "spring": [("tomato", "Twice a week", "70 days"), ("cucumber", "Twice a week", "50 days"),
                      ("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days"),
                      ("green beans", "Twice a week", "55 days"), ("strawberry", "Twice a week", "30 days"),
                      ("corn", "Twice a week", "80 days"), ("zucchini", "Twice a week", "50 days"),
                      ("basil", "Twice a week", "30 days"), ("melon", "Twice a week", "80 days")],
            "summer": [("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days"),
                      ("tomato", "Twice a week", "70 days"), ("cucumber", "Twice a week", "50 days"),
                      ("okra", "Twice a week", "60 days"), ("corn", "Twice a week", "80 days"),
                      ("sweet potato", "Once a week", "120 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days"),
                      ("broccoli", "Once a week", "70 days"), ("lettuce", "Once a week", "30 days"),
                      ("spinach", "Once a week", "40 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"),
                      ("arugula", "Once a week", "25 days"), ("cilantro", "Once a week", "30 days")]
        },
        "25-30": {
            "spring": [("tomato", "Twice a week", "70 days"), ("watermelon", "Twice a week", "90 days"),
                      ("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days"),
                      ("sweet corn", "Twice a week", "80 days"), ("okra", "Twice a week", "60 days"),
                      ("cantaloupe", "Twice a week", "85 days")],
            "summer": [("pepper", "Three times a week", "70 days"), ("eggplant", "Three times a week", "80 days"),
                      ("tomato", "Three times a week", "70 days"), ("okra", "Twice a week", "60 days"),
                      ("sweet potato", "Once a week", "120 days"), ("watermelon", "Three times a week", "90 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("onion", "Once a week", "90 days"),
                      ("sweet potato", "Once a week", "120 days"), ("grape", "Once a week", "120 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"),
                      ("mustard greens", "Once a week", "45 days")]
        },
        "30-35": {
            "spring": [("watermelon", "Twice a week", "90 days"), ("melon", "Twice a week", "80 days"),
                      ("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days"),
                      ("okra", "Twice a week", "60 days"), ("sweet potato", "Once a week", "120 days")],
            "summer": [("tomato", "Three times a week", "70 days"), ("eggplant", "Three times a week", "80 days"),
                      ("pepper", "Three times a week", "70 days"), ("watermelon", "Three times a week", "90 days"),
                      ("okra", "Three times a week", "60 days"), ("sweet potato", "Once a week", "120 days")],
            "autumn": [("eggplant", "Twice a week", "80 days"), ("pepper", "Twice a week", "70 days"),
                      ("okra", "Twice a week", "60 days"), ("sweet potato", "Once a week", "120 days")],
            "winter": [("heat-resistant spinach", "Once a week", "40 days"), ("heat-resistant lettuce", "Once a week", "30 days")]
        },
        "35-40": {
            "spring": [("watermelon", "Three times a week", "90 days"), ("heat-resistant melon", "Three times a week", "80 days"),
                      ("heat-resistant pepper", "Three times a week", "70 days"), ("heat-resistant eggplant", "Three times a week", "80 days")],
            "summer": [("heat-resistant tomato", "Three times a week", "70 days"), ("heat-resistant eggplant", "Three times a week", "80 days"),
                      ("heat-resistant pepper", "Three times a week", "70 days"), ("heat-resistant watermelon", "Three times a week", "90 days"),
                      ("okra", "Three times a week", "60 days")],
            "autumn": [("heat-resistant eggplant", "Twice a week", "80 days"), ("heat-resistant pepper", "Twice a week", "70 days"),
                      ("okra", "Twice a week", "60 days")],
            "winter": [("heat-resistant spinach", "Once a week", "40 days"), ("heat-resistant lettuce", "Once a week", "30 days")]
        }
    },
    "humidity": {
        "dry": {
            "spring": [("tomato", "Twice a week", "70 days"), ("pepper", "Twice a week", "70 days"),
                      ("sage", "Once a week", "90 days"), ("thyme", "Once a week", "90 days"),
                      ("rosemary", "Once a week", "90 days"), ("lavender", "Once a week", "90 days")],
            "summer": [("eggplant", "Twice a week", "80 days"), ("cucumber", "Twice a week", "50 days"),
                      ("watermelon", "Twice a week", "90 days"), ("thyme", "Once a week", "90 days"),
                      ("sage", "Once a week", "90 days"), ("oregano", "Once a week", "90 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days"),
                      ("onion", "Once a week", "90 days"), ("garlic", "Once a week", "120 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days"),
                      ("rosemary", "Once a week", "90 days"), ("thyme", "Once a week", "90 days")]
        },
        "normal": {
            "spring": [("strawberry", "Twice a week", "30 days"), ("watermelon", "Twice a week", "90 days"),
                      ("tomato", "Twice a week", "70 days"), ("cucumber", "Twice a week", "50 days"),
                      ("pepper", "Twice a week", "70 days"), ("eggplant", "Twice a week", "80 days"),
                      ("lettuce", "Once a week", "30 days"), ("carrot", "Once a week", "75 days"),
                      ("radish", "Once a week", "25 days"), ("onion", "Once a week", "90 days"),
                      ("potato", "Twice a week", "90 days"), ("cabbage", "Once a week", "60 days"),
                      ("corn", "Twice a week", "80 days"), ("green beans", "Twice a week", "55 days"),
                      ("peas", "Once a week", "65 days"), ("beet", "Once a week", "60 days"),
                      ("zucchini", "Twice a week", "50 days"), ("cilantro", "Once a week", "30 days"),
                      ("basil", "Twice a week", "30 days"), ("parsley", "Once a week", "70 days")],
            "summer": [("pepper", "Twice a week", "70 days"), ("tomato", "Twice a week", "70 days"),
                      ("eggplant", "Twice a week", "80 days"), ("cucumber", "Twice a week", "50 days"),
                      ("watermelon", "Twice a week", "90 days"), ("cantaloupe", "Twice a week", "85 days"),
                      ("corn", "Twice a week", "80 days"), ("okra", "Twice a week", "60 days"),
                      ("green beans", "Twice a week", "55 days"), ("zucchini", "Twice a week", "50 days"),
                      ("summer squash", "Twice a week", "50 days"), ("basil", "Twice a week", "30 days")],
            "autumn": [("cauliflower", "Once a week", "70 days"), ("carrot", "Once a week", "75 days"),
                      ("cabbage", "Once a week", "60 days"), ("broccoli", "Once a week", "70 days"),
                      ("lettuce", "Once a week", "30 days"), ("spinach", "Once a week", "40 days"),
                      ("kale", "Once a week", "60 days"), ("onion", "Once a week", "90 days"),
                      ("garlic", "Once a week", "120 days"), ("turnip", "Once a week", "60 days"),
                      ("radish", "Once a week", "25 days"), ("arugula", "Once a week", "25 days")],
            "winter": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"),
                      ("lettuce", "Once a week", "30 days"), ("arugula", "Once a week", "25 days"),
                      ("onion", "Once a week", "90 days"), ("garlic", "Once a week", "120 days"),
                      ("leek", "Once a week", "90 days"), ("celery", "Once a week", "90 days"),
                      ("carrot", "Once a week", "75 days"), ("radish", "Once a week", "25 days")]
        },
        "humid": {
            "spring": [("kale", "Once a week", "60 days"), ("spinach", "Once a week", "40 days"),
                      ("cabbage", "Once a week", "60 days"), ("lettuce", "Once a week", "30 days"),
                      ("green onion", "Once a week", "60 days"), ("taro", "Once a week", "150 days"),
                      ("rice", "Three times a week", "120 days")],
            "summer": [("broccoli", "Once a week", "70 days"), ("cauliflower", "Once a week", "70 days"),
                      ("cabbage", "Once a week", "60 days"), ("wasabi", "Once a week", "180 days"),
                      ("taro", "Once a week", "150 days"), ("watercress", "Twice a week", "50 days"),
                      ("rice", "Three times a week", "120 days")],
            "autumn": [("carrot", "Once a week", "75 days"), ("leek", "Once a week", "90 days"),
                      ("taro", "Once a week", "150 days"), ("cabbage", "Once a week", "60 days"),
                      ("cauliflower", "Once a week", "70 days"), ("broccoli", "Once a week", "70 days")],
            "winter": [("celery", "Once a week", "90 days"), ("garlic", "Once a week", "120 days"),
                      ("leek", "Once a week", "90 days"), ("kale", "Once a week", "60 days"),
                      ("cabbage", "Once a week", "60 days"), ("lettuce", "Once a week", "30 days")]
        }
    }
}


# 🌱 Ana öneri fonksiyonu
def get_suggestions(temperature, soil_moisture, season):
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

    return plant_suggestions
