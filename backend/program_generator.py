import random
# Yeni mantık modülümüzden tüm temel yapı taşlarını import ediyoruz
from workout_logic import EXERCISE_DB, GOAL_LOGIC, PROGRAM_TEMPLATES

def get_allowed_exercises(muscle_group, user_level, predicted_level):
    """
    Hibrit AI mantığını kullanarak kullanıcının seviyesine uygun egzersizleri filtreler.
    Kullanıcının beyan ettiği ve modelin tahmin ettiği seviyeyi karşılaştırır.
    """
    level_map = {"beginner": 1, "intermediate": 2, "advanced": 3}
    user_lvl = level_map.get(user_level, 1)
    predicted_lvl = level_map.get(predicted_level, 1)

    # Sanal antrenör karar verir: Daha temkinli olan seviyeyi baz al.
    # Örn: Kullanıcı "advanced" dedi ama model "beginner" bulduysa, max_level = 1 olur.
    max_level = min(user_lvl, predicted_lvl)

    allowed = []
    for ex in EXERCISE_DB.get(muscle_group, []):
        if level_map.get(ex["level"].lower(), 1) <= max_level:
            allowed.append(ex)
    return allowed

def select_template(goal, frequency):
    """Kullanıcının hedefine ve frekansına göre en uygun program şablonunu seçer."""
    # Öncelik her zaman kullanıcının seçtiği gün sayısıdır.
    if frequency == "5":
        # 5 gün için en uygun şablon "Body Part Split"tir.
        return PROGRAM_TEMPLATES["5_day_body_part"]
    if frequency == "4":
        # 4 gün için en uygun şablon "Upper/Lower"dır.
        return PROGRAM_TEMPLATES["4_day_upper_lower"]
    if frequency == "3":
        # 3 gün için en uygun şablon "Full Body"dir.
        return PROGRAM_TEMPLATES["3_day_full_body"]
    
    # Herhangi bir eşleşme olmazsa varsayılan olarak 3 günlük bir program döndür.
    return PROGRAM_TEMPLATES["3_day_full_body"]

def generate_program(goal, user_level, predicted_level, frequency):
    """
    Generates a highly personalized training program using Hybrid AI logic.
    """
    template = select_template(goal, frequency)
    logic = GOAL_LOGIC.get(goal, GOAL_LOGIC["general_health"])
    reps = logic["reps"]
    exercises_per_muscle = logic["exercises_per_muscle"]

    final_schedule = {}
    
    # Isınma ve soğumayı her zaman ekle
    warmup_exercises = random.sample(EXERCISE_DB["warmup"], 2)
    cooldown_exercises = random.sample(EXERCISE_DB["cooldown"], 2)

    day_names = list(template["schedule"].keys())
    
    for day_name, muscle_groups in template["schedule"].items():
        if "rest" in muscle_groups:
            final_schedule[day_name] = [{"name": "Rest Day", "sets": ""}]
            continue

        daily_exercises_obj = []
        for group in muscle_groups:
            allowed = get_allowed_exercises(group, user_level, predicted_level)
            
            # Bileşik ve izole hareketleri ayır
            compounds = [ex for ex in allowed if ex['type'] == 'Compound']
            isolations = [ex for ex in allowed if ex['type'] == 'Isolation']
            
            # Her kas grubu için öncelikli olarak bileşik hareket seç
            if compounds:
                daily_exercises_obj.append(random.choice(compounds))
            # Kalan yer varsa izole hareket ekle
            if isolations and len(daily_exercises_obj) < exercises_per_muscle * len(muscle_groups):
                 daily_exercises_obj.append(random.choice(isolations))

        # Tekrarları önle
        seen = set()
        unique_exercises = [ex for ex in daily_exercises_obj if not (ex['name'] in seen or seen.add(ex['name']))]
        
        # Egzersizleri formatla
        formatted_exercises = [{"name": ex['name'], "sets": reps} for ex in unique_exercises]

        # Başına ısınma, sonuna soğuma ekle
        final_schedule[day_name] = [
            {"name": "Warm-up", "sets": ", ".join(e['duration'] for e in warmup_exercises)},
            *formatted_exercises,
            {"name": "Cool-down", "sets": ", ".join(e['duration'] for e in cooldown_exercises)}
        ]

    return {
        "programName": template["name"],
        "description": template["description"],
        "schedule": final_schedule
    }
