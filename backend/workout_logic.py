# Bu dosya, egzersiz veritabanını ve program oluşturma mantığının temel yapı taşlarını içerir.

# Gelişmiş Egzersiz Veritabanı
EXERCISE_DB = {
    "warmup": [
        {"name": "Jumping Jacks", "duration": "60 seconds"},
        {"name": "Arm Circles", "duration": "30 seconds per direction"},
        {"name": "Leg Swings", "duration": "30 seconds per leg"},
        {"name": "Cat-Cow Stretch", "duration": "60 seconds"},
        {"name": "High Knees", "duration": "45 seconds"},
        {"name": "Butt Kicks", "duration": "45 seconds"},
        {"name": "Torso Twists", "duration": "45 seconds"},
        {"name": "Ankle Circles", "duration": "30 seconds per ankle"},
    ],
    "cooldown": [
        {"name": "Quad Stretch", "duration": "30 seconds per leg"},
        {"name": "Hamstring Stretch", "duration": "30 seconds per leg"},
        {"name": "Chest Stretch", "duration": "30 seconds"},
        {"name": "Child's Pose", "duration": "60 seconds"},
        {"name": "Triceps Stretch", "duration": "30 seconds per arm"},
        {"name": "Pigeon Pose", "duration": "45 seconds per side"},
        {"name": "Butterfly Stretch", "duration": "60 seconds"},
        {"name": "Seated Forward Fold", "duration": "60 seconds"},
    ],
    "chest": [
        {"name": "Push-ups", "type": "Compound", "level": "Beginner"},
        {"name": "Incline Push-ups", "type": "Compound", "level": "Beginner"},
        {"name": "Knee Push-ups", "type": "Compound", "level": "Beginner"},
        {"name": "Dumbbell Bench Press", "type": "Compound", "level": "Beginner"},
        {"name": "Dumbbell Flyes", "type": "Isolation", "level": "Beginner"},
        {"name": "Resistance Band Chest Press", "type": "Compound", "level": "Beginner"},
        {"name": "Machine Chest Press", "type": "Compound", "level": "Beginner"},
        
        {"name": "Incline Dumbbell Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Barbell Bench Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Cable Crossover", "type": "Isolation", "level": "Intermediate"},
        {"name": "Decline Dumbbell Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Dumbbell Pullover", "type": "Isolation", "level": "Intermediate"},
        {"name": "Incline Cable Flyes", "type": "Isolation", "level": "Intermediate"},
        
        {"name": "Chest Dips", "type": "Compound", "level": "Advanced"},
        {"name": "Incline Barbell Press", "type": "Compound", "level": "Advanced"},
        {"name": "Plyometric Push-ups", "type": "Compound", "level": "Advanced"},
        {"name": "Weighted Chest Dips", "type": "Compound", "level": "Advanced"},
        {"name": "Explosive Medicine Ball Push-ups", "type": "Compound", "level": "Advanced"},
    ],
    "back": [
        {"name": "Lat Pulldown", "type": "Compound", "level": "Beginner"},
        {"name": "Seated Cable Row", "type": "Compound", "level": "Beginner"},
        {"name": "Face Pulls", "type": "Isolation", "level": "Beginner"},
        {"name": "Superman Hold", "type": "Isolation", "level": "Beginner"},
        {"name": "Resistance Band Pull-aparts", "type": "Isolation", "level": "Beginner"},
        {"name": "Single Arm Dumbbell Row", "type": "Compound", "level": "Beginner"},

        {"name": "Bent-over Row", "type": "Compound", "level": "Intermediate"},
        {"name": "Pull-ups", "type": "Compound", "level": "Intermediate"},
        {"name": "Chin-ups", "type": "Compound", "level": "Intermediate"},
        {"name": "Inverted Rows", "type": "Compound", "level": "Intermediate"},
        {"name": "Meadows Row", "type": "Compound", "level": "Intermediate"},
        {"name": "Close-Grip Lat Pulldown", "type": "Compound", "level": "Intermediate"},

        {"name": "T-Bar Row", "type": "Compound", "level": "Advanced"},
        {"name": "Deadlift", "type": "Compound", "level": "Advanced"},
        {"name": "Rack Pulls", "type": "Compound", "level": "Advanced"},
        {"name": "Weighted Pull-ups", "type": "Compound", "level": "Advanced"},
        {"name": "Barbell Row (Heavy)", "type": "Compound", "level": "Advanced"},
        {"name": "One-Arm Dumbbell Row (Weighted)", "type": "Compound", "level": "Advanced"},
        {"name": "Reverse Grip Bent-over Row", "type": "Compound", "level": "Advanced"},
    ],
    "quads": [
        {"name": "Goblet Squat", "type": "Compound", "level": "Beginner"},
        {"name": "Leg Press", "type": "Compound", "level": "Beginner"},
        {"name": "Leg Extensions", "type": "Isolation", "level": "Beginner"},
        {"name": "Lunges", "type": "Compound", "level": "Beginner"},
        {"name": "Step-ups", "type": "Compound", "level": "Beginner"},
        {"name": "Wall Sits", "type": "Isolation", "level": "Beginner"},
        {"name": "Bodyweight Split Squats", "type": "Compound", "level": "Beginner"},

        {"name": "Barbell Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Bulgarian Split Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Front Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Walking Lunges with Dumbbells", "type": "Compound", "level": "Intermediate"},
        {"name": "Hack Squat (Machine)", "type": "Compound", "level": "Intermediate"},
        {"name": "Single-Leg Leg Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Sissy Squat", "type": "Isolation", "level": "Intermediate"},

        {"name": "Front Squat (Heavy Barbell)", "type": "Compound", "level": "Advanced"},
        {"name": "Hack Squat (Weighted)", "type": "Compound", "level": "Advanced"},
        {"name": "Pistol Squats", "type": "Compound", "level": "Advanced"},
        {"name": "Bulgarian Split Squat (Weighted)", "type": "Compound", "level": "Advanced"},
        {"name": "Overhead Squat", "type": "Compound", "level": "Advanced"},
        {"name": "Jump Squats", "type": "Compound", "level": "Advanced"},
        {"name": "Step-ups with Barbell", "type": "Compound", "level": "Advanced"}
    ],
    "hamstrings": [
        {"name": "Lying Leg Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Seated Leg Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Single-Leg Glute Bridge", "type": "Isolation", "level": "Beginner"},
        {"name": "Swiss Ball Hamstring Curl", "type": "Isolation", "level": "Beginner"},

        {"name": "Romanian Deadlift", "type": "Compound", "level": "Intermediate"},
        {"name": "Kettlebell Swings", "type": "Compound", "level": "Intermediate"},
        {"name": "Good Mornings", "type": "Compound", "level": "Intermediate"},
        {"name": "Stiff-Leg Deadlift", "type": "Compound", "level": "Intermediate"},
        {"name": "Hip Thrust with Hamstring Focus", "type": "Compound", "level": "Intermediate"},

        {"name": "Good Mornings (Heavy Barbell)", "type": "Compound", "level": "Advanced"},
        {"name": "Glute-Ham Raise", "type": "Compound", "level": "Advanced"},
        {"name": "Nordic Hamstring Curl", "type": "Isolation", "level": "Advanced"},
        {"name": "Single-Leg Romanian Deadlift (Weighted)", "type": "Compound", "level": "Advanced"},
        {"name": "Barbell Hip Thrust (Hamstring Focus)", "type": "Compound", "level": "Advanced"},
    ],
    "glutes": [
        {"name": "Glute Bridges", "type": "Isolation", "level": "Beginner"},
        {"name": "Fire Hydrants", "type": "Isolation", "level": "Beginner"},
        {"name": "Donkey Kicks", "type": "Isolation", "level": "Beginner"},
        {"name": "Clamshells", "type": "Isolation", "level": "Beginner"},
        {"name": "Bodyweight Hip Thrusts", "type": "Compound", "level": "Beginner"},

        {"name": "Cable Kickbacks", "type": "Isolation", "level": "Intermediate"},
        {"name": "Hip Thrust", "type": "Compound", "level": "Intermediate"},
        {"name": "Sumo Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Step-ups with Dumbbells", "type": "Compound", "level": "Intermediate"},
        {"name": "Bulgarian Split Squat", "type": "Compound", "level": "Intermediate"},
        {"name": "Glute Bridge March", "type": "Isolation", "level": "Intermediate"},

        {"name": "Barbell Hip Thrust", "type": "Compound", "level": "Advanced"},
        {"name": "Single-Leg Hip Thrust", "type": "Isolation", "level": "Advanced"},
        {"name": "Weighted Sumo Squat", "type": "Compound", "level": "Advanced"},
        {"name": "Romanian Deadlift", "type": "Compound", "level": "Advanced"},
        {"name": "Cable Pull-Through", "type": "Compound", "level": "Advanced"},
        {"name": "Kettlebell Swings", "type": "Compound", "level": "Advanced"},
    ],
    "calves": [
        {"name": "Standing Calf Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Seated Calf Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Donkey Calf Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Toe Walks", "type": "Isolation", "level": "Beginner"},

        {"name": "Leg Press Calf Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Single-leg Calf Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Farmer's Carry on Toes", "type": "Compound", "level": "Intermediate"},
        {"name": "Seated Single-leg Calf Raise", "type": "Isolation", "level": "Intermediate"},

        {"name": "Weighted Standing Calf Raises", "type": "Isolation", "level": "Advanced"},
        {"name": "Jumping Calf Raises", "type": "Compound", "level": "Advanced"},
        {"name": "Explosive Box Jumps", "type": "Compound", "level": "Advanced"},
        {"name": "Single-leg Weighted Calf Raises", "type": "Isolation", "level": "Advanced"},
    ],
    "shoulders": [
        {"name": "Dumbbell Overhead Press", "type": "Compound", "level": "Beginner"},
        {"name": "Seated Dumbbell Press", "type": "Compound", "level": "Beginner"},
        {"name": "Lateral Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Front Raises", "type": "Isolation", "level": "Beginner"},
        {"name": "Dumbbell Shrugs", "type": "Isolation", "level": "Beginner"},
        
        {"name": "Barbell Overhead Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Arnold Press", "type": "Compound", "level": "Intermediate"},
        {"name": "Upright Row", "type": "Compound", "level": "Intermediate"},
        {"name": "Rear Delt Flyes", "type": "Isolation", "level": "Intermediate"},
        {"name": "Face Pulls", "type": "Compound", "level": "Intermediate"},
        {"name": "Cable Lateral Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Single-Arm Dumbbell Press", "type": "Compound", "level": "Intermediate"},
        
        {"name": "Handstand Push-ups", "type": "Compound", "level": "Advanced"},
        {"name": "Barbell Push Press", "type": "Compound", "level": "Advanced"},
        {"name": "Overhead Dumbbell Carry", "type": "Compound", "level": "Advanced"},
        {"name": "Behind-the-Neck Press", "type": "Compound", "level": "Advanced"},
        {"name": "Landmine Press", "type": "Compound", "level": "Advanced"}
    ],
    "biceps": [
        {"name": "Dumbbell Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Hammer Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Concentration Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Resistance Band Curls", "type": "Isolation", "level": "Beginner"},
        {"name": "Cable Rope Hammer Curls", "type": "Isolation", "level": "Beginner"},

        {"name": "Barbell Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Preacher Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Incline Dumbbell Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Cable Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Zottman Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "Spider Curls", "type": "Isolation", "level": "Intermediate"},
        {"name": "21s (Barbell/Dumbbell)", "type": "Isolation", "level": "Intermediate"},
        {"name": "Cross-Body Hammer Curls", "type": "Isolation", "level": "Intermediate"},

        {"name": "Chin-ups (underhand grip)", "type": "Compound", "level": "Advanced"},
        {"name": "Weighted Chin-ups", "type": "Compound", "level": "Advanced"},
        {"name": "Drag Curls", "type": "Isolation", "level": "Advanced"},
        {"name": "Incline Barbell Curl", "type": "Isolation", "level": "Advanced"},
        {"name": "One-Arm Cable Curl (High Pulley)", "type": "Isolation", "level": "Advanced"},
        {"name": "Reverse Grip Barbell Curl", "type": "Isolation", "level": "Advanced"},
    ],
    "triceps": [
        {"name": "Tricep Pushdown", "type": "Isolation", "level": "Beginner"},
        {"name": "Overhead Tricep Extension", "type": "Isolation", "level": "Beginner"},
        {"name": "Tricep Dips (on bench)", "type": "Compound", "level": "Beginner"},
        {"name": "Kickbacks (Dumbbell)", "type": "Isolation", "level": "Beginner"},
        {"name": "Resistance Band Pushdowns", "type": "Isolation", "level": "Beginner"},

        {"name": "Tricep Dips (parallel bars)", "type": "Compound", "level": "Intermediate"},
        {"name": "Skull Crushers", "type": "Isolation", "level": "Intermediate"},
        {"name": "Diamond Push-ups", "type": "Compound", "level": "Intermediate"},
        {"name": "Overhead Dumbbell Press (narrow grip)", "type": "Compound", "level": "Intermediate"},
        {"name": "EZ Bar Overhead Extension", "type": "Compound", "level": "Intermediate"},
        {"name": "Close-Grip Push-ups", "type": "Compound", "level": "Intermediate"},
        
        {"name": "Close-Grip Bench Press", "type": "Compound", "level": "Advanced"},
        {"name": "JM Press", "type": "Compound", "level": "Advanced"},
        {"name": "Weighted Dips", "type": "Compound", "level": "Advanced"},
        {"name": "Floor Press (Close Grip)", "type": "Compound", "level": "Advanced"},
        {"name": "Single-Arm Dumbbell Overhead Extension", "type": "Isolation", "level": "Advanced"},
        {"name": "Cable Overhead Tricep Extension (rope)", "type": "Isolation", "level": "Advanced"},
    ],
    "abs": [
        {"name": "Crunches", "type": "Isolation", "level": "Beginner"},
        {"name": "Plank", "type": "Isolation", "level": "Beginner"},
        {"name": "Side Plank", "type": "Isolation", "level": "Beginner"},
        {"name": "Reverse Crunches", "type": "Isolation", "level": "Beginner"},
        {"name": "Heel Touches", "type": "Isolation", "level": "Beginner"},
        {"name": "Mountain Climbers", "type": "Compound", "level": "Beginner"},
        
        {"name": "Leg Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Russian Twists", "type": "Isolation", "level": "Intermediate"},
        {"name": "Hanging Knee Raises", "type": "Isolation", "level": "Intermediate"},
        {"name": "Bicycle Crunches", "type": "Compound", "level": "Intermediate"},
        {"name": "Flutter Kicks", "type": "Isolation", "level": "Intermediate"},
        {"name": "Scissor Kicks", "type": "Isolation", "level": "Intermediate"},
        {"name": "Toe Touches", "type": "Isolation", "level": "Intermediate"},
        {"name": "V-Ups", "type": "Compound", "level": "Intermediate"},
        
        {"name": "Cable Crunches", "type": "Isolation", "level": "Advanced"},
        {"name": "Ab Rollout", "type": "Compound", "level": "Advanced"},
        {"name": "Dragon Flags", "type": "Compound", "level": "Advanced"},
        {"name": "Hanging Leg Raises (Straight Legs)", "type": "Compound", "level": "Advanced"},
        {"name": "Windshield Wipers", "type": "Compound", "level": "Advanced"},
        {"name": "Decline Sit-ups (Weighted)", "type": "Compound", "level": "Advanced"},
        {"name": "Medicine Ball Slams", "type": "Compound", "level": "Advanced"},
    ]
}

# Hedeflere göre Set/Tekrar ve Egzersiz Sayısı Mantığı
GOAL_LOGIC = {
    "muscle_gain": {"reps": "4 sets x 10-12 reps", "exercises_per_muscle": 2},
    "strength": {"reps": "5 sets x 4-6 reps", "exercises_per_muscle": 1},
    "weight_loss": {"reps": "3 sets x 15-20 reps", "exercises_per_muscle": 2},
    "general_health": {"reps": "3 sets x 12-15 reps", "exercises_per_muscle": 1}
}

# Haftalık Program Şablonları (Artık daha dinamik kullanılacak)
PROGRAM_TEMPLATES = {
    "3_day_full_body": {
        "name": "3-Day Full Body Split",
        "description": "Focuses on hitting all major muscle groups three times a week.",
        "schedule": {
            "Day 1": ["chest", "back", "quads"],
            "Day 2": ["rest"],
            "Day 3": ["shoulders", "hamstrings", "biceps", "triceps"],
            "Day 4": ["rest"],
            "Day 5": ["chest", "back", "glutes", "abs"],
            "Day 6": ["rest"],
            "Day 7": ["rest"]
        }
    },
    "4_day_upper_lower": {
        "name": "4-Day Upper/Lower Split",
        "description": "Splits the body into upper and lower body workouts.",
        "schedule": {
            "Day 1": ["chest", "shoulders", "triceps"],
            "Day 2": ["quads", "hamstrings", "calves"],
            "Day 3": ["rest"],
            "Day 4": ["back", "biceps"],
            "Day 5": ["glutes", "hamstrings", "abs"],
            "Day 6": ["rest"],
            "Day 7": ["rest"]
        }
    },
    "5_day_body_part": {
        "name": "5-Day Body Part Split",
        "description": "Focuses on specific muscle groups each day for higher volume.",
        "schedule": {
            "Day 1": ["chest", "abs"],
            "Day 2": ["back"],
            "Day 3": ["quads", "hamstrings", "calves"],
            "Day 4": ["shoulders"],
            "Day 5": ["biceps", "triceps"],
            "Day 6": ["rest"],
            "Day 7": ["rest"]
        }
    }
}
