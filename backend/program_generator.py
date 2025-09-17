import random

# Gelişmiş Egzersiz Veritabanı: Her egzersiz bir obje olarak tanımlandı.
# type: 'Compound' (Bileşik), 'Isolation' (İzole)
# level: 'Beginner', 'Intermediate', 'Advanced'
EXERCISE_DB = {
    "chest": [
        {"name": "Push-ups", "type": "Compound", "level": "Beginner"},
        {"name": "Dumbbell Bench Press", "type": "Compound", "level": "Beginner"},
        {"name": "Barbell Bench Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Incline Dumbbell Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Dumbbell Flyes", "type": "Isolation", "level": "Beginner"},
        {"name": "Cable Crossover", "type": "Isolation", "level": "Intermediate"},
        {"name": "Chest Dips", "type": "Compound", "level": "Advanced"},
    ],
    "back": [
        {"name": "Lat Pulldown", "type": "Compound", "level": "Beginner"},
        {"name": "Seated Cable Row", "type": "Compound", "level": "Beginner"},
        {"name": "Bent-over Row", "type": "Compound", "level": "Intermediate"},
        {"name": "Pull-ups", "type": "Compound", "level": "Intermediate"},
        {"name": "T-Bar Row", "type": "Compound", "level": "Advanced"},
        {"name": "Deadlift", "type": "Compound", "level": "Advanced"},
        {"name": "Face Pulls", "type": "Isolation", "level": "Beginner"},
    ],
    "quads": [
        {"name": "Goblet Squat", "type": "Compound", "level": "Beginner"},
        {"name": "Leg Press", "type": "Compound", "level": "Beginner"},
        {"name": "Leg Extensions", "type": "Isolation", "level": "Beginner"},
        {"name": "Barbell Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Front Squat", "type": "Compound", "level": "Advanced"},
    ],
    "hamstrings": [
        {"name": "Leg Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Romanian Deadlift", "type": "Compound", "level": "Intermediate"},
        {"name": "Good Mornings", "type": "Compound", "level": "Advanced"},
    ],
    "glutes": [
        {"name": "Glute Bridges", "type": "Isolation", "level": "Beginner"},
        {"name": "Cable Kickbacks", "type": "Isolation", "level": "Intermediate"},
        {"name": "Hip Thrust", "type": "Compound", "level": "Intermediate"},
    ],
    "calves": [
        {"name": "Calf Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Seated Calf Raises", "type": "Isolation", "level": "Beginner"},
    ],
    "shoulders": [
        {"name": "Dumbbell Overhead Press", "type": "Compound", "level": "Beginner"},
        {"name": "Lateral Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Barbell Overhead Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Arnold Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Front Raises", "type": "Isolation", "level": "Beginner"},
    ],
    "biceps": [
        {"name": "Dumbbell Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Hammer Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Barbell Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Preacher Curls", "type": "Isolation", "level": "Intermediate"},
    ],
    "triceps": [
        {"name": "Tricep Pushdown", "type": "Isolation", "level": "Beginner"},
        {"name": "Overhead Tricep Extension", "type": "Isolation", "level": "Beginner"},
        {"name": "Tricep Dips", "type": "Compound", "level": "Intermediate"},
        {"name": "Skull Crushers", "type": "Isolation", "level": "Intermediate"},
    ],
    "abs": [
        {"name": "Crunches", "type": "Isolation", "level": "Beginner"},
        {"name": "Plank", "type": "Isolation", "level": "Beginner"},
        {"name": "Leg Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Russian Twists", "type": "Isolation", "level": "Intermediate"},
        {"name": "Cable Crunches", "type": "Isolation", "level": "Advanced"},
    ]
}

REP_SCHEMES = {
    "muscle_gain": "4 sets x 10-12 reps",
    "strength": "5 sets x 4-6 reps",
    "weight_loss": "3 sets x 15-20 reps",
    "general_health": "3 sets x 12-15 reps"
}

PROGRAM_SPLITS = {
    # ... (Splits can remain the same or be updated too) ...
    "3": {
        "name": "Full Body Workout",
        "description": "A program that works all major muscle groups in each session.",
        "schedule": {
            "Monday": ["chest", "back", "quads"],
            "Tuesday": ["rest"],
            "Wednesday": ["shoulders", "hamstrings", "biceps", "triceps"],
            "Thursday": ["rest"],
            "Friday": ["chest", "back", "glutes", "abs"],
            "Saturday": ["rest"],
            "Sunday": ["rest"]
        }
    },
    "4": {
        "name": "Upper/Lower Body Split",
        "description": "A popular program that separates training into upper and lower body days.",
        "schedule": {
            "Monday": ["chest", "shoulders", "triceps"], # Upper
            "Tuesday": ["quads", "hamstrings", "calves"], # Lower
            "Wednesday": ["rest"],
            "Thursday": ["back", "biceps"], # Upper
            "Friday": ["glutes", "hamstrings", "abs"], # Lower
            "Saturday": ["rest"],
            "Sunday": ["rest"]
        }
    },
    "5": {
        "name": "Body Part Split (Bro Split)",
        "description": "An advanced program focusing on one or two muscle groups per day.",
        "schedule": {
            "Monday": ["chest", "abs"],
            "Tuesday": ["back"],
            "Wednesday": ["quads", "hamstrings", "calves"],
            "Thursday": ["shoulders"],
            "Friday": ["biceps", "triceps"],
            "Saturday": ["rest"],
            "Sunday": ["rest"]
        }
    }
}

def get_allowed_exercises(muscle_group, level):
    """Kullanıcının seviyesine uygun egzersizleri filtreler."""
    level_map = {
        "beginner": 1,
        "intermediate": 2,
        "advanced": 3
    }
    user_level = level_map.get(level, 1)
    
    allowed = []
    for ex in EXERCISE_DB.get(muscle_group, []):
        if level_map.get(ex["level"], 1) <= user_level:
            allowed.append(ex)
    return allowed

def generate_program(goal, level, frequency, duration):
    """
    Generates a personalized training program based on user inputs.
    """
    if frequency not in PROGRAM_SPLITS:
        return {"error": "Invalid frequency selection"}

    split = PROGRAM_SPLITS[frequency]
    reps = REP_SCHEMES.get(goal, "3 sets x 12 reps")
    
    total_exercises_per_session = 3
    if duration == "45":
        total_exercises_per_session = 4
    elif duration == "60":
        total_exercises_per_session = 5

    final_schedule = {}
    for day, muscle_groups in split["schedule"].items():
        if "rest" in muscle_groups:
            final_schedule[day] = [{"name": "Rest Day", "sets": ""}]
            continue
            
        daily_exercises_obj = []
        # Her kas grubu için izin verilen egzersizleri topla
        for group in muscle_groups:
            allowed = get_allowed_exercises(group, level)
            daily_exercises_obj.extend(allowed)

        # Egzersizleri karıştır ve yinelenenleri kaldır
        random.shuffle(daily_exercises_obj)
        seen = set()
        unique_exercises = []
        for ex in daily_exercises_obj:
            if ex['name'] not in seen:
                unique_exercises.append(ex)
                seen.add(ex['name'])

        # Önce Compound, sonra Isolation hareketlerini sırala
        sorted_exercises = sorted(unique_exercises, key=lambda x: x['type'] != 'Compound')
        
        # Gerekli sayıda egzersiz seç
        chosen_exercises = sorted_exercises[:total_exercises_per_session]

        final_schedule[day] = [{"name": ex['name'], "sets": reps} for ex in chosen_exercises]

    return {
        "programName": split["name"],
        "description": split["description"],
        "schedule": final_schedule
    }
