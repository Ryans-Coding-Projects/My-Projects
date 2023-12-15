def generate_workout():
    workout_choice = int(input("1. Full Body\n2. Chest\n3. Legs\n4. Biceps\n5. Triceps\n6. Back\n7. Abs\n\nWhich would you like to workout?: "))
    workout_time = int(input("1. 1 Hour\n2. 30 Minutes\n3. 15 Minutes\n\nHow much time do you have to workout?: "))

    print("\nWorkout Generated\n")

    if workout_choice == 1:
        if workout_time == 1:
            print("Full Body 1-Hour Workout:")
            print("- Warm-up: 10 minutes of light cardio")
            print("- Squats: 4 sets of 12 reps")
            print("- Push-ups: 3 sets of 15 reps")
            print("- Deadlifts: 3 sets of 10 reps")
        elif workout_time == 2:
            print("Full Body 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Lunges: 3 sets of 10 reps each leg")
            print("  - Plank: 3 sets of 30 seconds")
            print("- Circuit 2:")
            print("  - Dumbbell Rows: 3 sets of 12 reps each arm")
            print("  - Mountain Climbers: 3 sets of 20 reps")
        elif workout_time == 3:
            print("Full Body 15-Minute Workout:")
            print("- Tabata Workout:")
            print("  - Jump Squats: 4 minutes (20 seconds on, 10 seconds rest)")
            print("  - Push-ups: 4 minutes (20 seconds on, 10 seconds rest)")
        else:
            print("Invalid time selection for Full Body workout")

    elif workout_choice == 2:
        if workout_time == 1:
            print("Chest 1-Hour Workout:")
            print("- Warm-up: 10 minutes of skipping")
            print("- Bench Press: 4 sets of 10 reps")
            print("- Dumbbell Flyes: 3 sets of 12 reps")
        elif workout_time == 2:
            print("Chest 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Push-ups: 3 sets of 15 reps")
            print("  - Chest Dips: 3 sets of 10 reps")
        elif workout_time == 3:
            print("Chest 15-Minute Workout:")
            print("- Quick Chest Routine:")
            print("  - Push-ups: 3 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Chest workout")

    elif workout_choice == 3:
        if workout_time == 1:
            print("Legs 1-Hour Workout:")
            print("- Warm-up: 10 minutes of cycling")
            print("- Squats: 5 sets of 10 reps")
            print("- Lunges: 4 sets of 12 reps each leg")
        elif workout_time == 2:
            print("Legs 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Squats: 3 sets of 12 reps")
            print("  - Calf Raises: 3 sets of 15 reps")
        elif workout_time == 3:
            print("Legs 15-Minute Workout:")
            print("- Quick Leg Routine:")
            print("  - Jump Squats: 2 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Legs workout")

    elif workout_choice == 4:
        if workout_time == 1:
            print("Biceps 1-Hour Workout:")
            print("- Warm-up: 10 minutes of skipping")
            print("- Barbell Curls: 4 sets of 12 reps")
            print("- Hammer Curls: 3 sets of 15 reps")
        elif workout_time == 2:
            print("Biceps 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Dumbbell Curls: 3 sets of 12 reps")
            print("  - Chin-ups: 3 sets of 8 reps")
        elif workout_time == 3:
            print("Biceps 15-Minute Workout:")
            print("- Quick Biceps Routine:")
            print("  - Alternating Dumbbell Curls: 2 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Biceps workout")

    elif workout_choice == 5:
        if workout_time == 1:
            print("Triceps 1-Hour Workout:")
            print("- Warm-up: 10 minutes of rowing")
            print("- Tricep Dips: 4 sets of 12 reps")
            print("- Overhead Tricep Extension: 3 sets of 15 reps")
        elif workout_time == 2:
            print("Triceps 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Tricep Pushdowns: 3 sets of 12 reps")
            print("  - Close-Grip Bench Press: 3 sets of 10 reps")
        elif workout_time == 3:
            print("Triceps 15-Minute Workout:")
            print("- Quick Triceps Routine:")
            print("  - Diamond Push-ups: 2 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Triceps workout")

    elif workout_choice == 6:
        if workout_time == 1:
            print("Back 1-Hour Workout:")
            print("- Warm-up: 10 minutes of rowing")
            print("- Deadlifts: 4 sets of 8 reps")
            print("- Pull-ups: 3 sets of 10 reps")
        elif workout_time == 2:
            print("Back 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Lat Pulldowns: 3 sets of 12 reps")
            print("  - Bent-Over Rows: 3 sets of 10 reps")
        elif workout_time == 3:
            print("Back 15-Minute Workout:")
            print("- Quick Back Routine:")
            print("  - Superman: 2 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Back workout")

    elif workout_choice == 7:
        if workout_time == 1:
            print("Abs 1-Hour Workout:")
            print("- Warm-up: 10 minutes of core activation exercises")
            print("- Plank variations: 4 sets of 45 seconds")
            print("- Russian Twists: 3 sets of 20 reps")
        elif workout_time == 2:
            print("Abs 30-Minute Workout:")
            print("- Circuit 1:")
            print("  - Bicycle Crunches: 3 sets of 15 reps each side")
            print("  - Leg Raises: 3 sets of 12 reps")
        elif workout_time == 3:
            print("Abs 15-Minute Workout:")
            print("- Quick Abs Routine:")
            print("  - Sit-ups: 2 minutes (as many reps as possible)")
        else:
            print("Invalid time selection for Abs workout")

generate_workout()
