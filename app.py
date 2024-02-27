import time

def select_workout(workout = None, duration = None):
    print(workout)


user_selected_workout = []

workout_options = {
    1: "push ups",
    2: "sit ups",
    3: "jumping jacks",
    4: "other"
}

# TODO read in the json instead of this
# TODO add option for user to add workouts and it write out to that json file so next time that user entered workout is an option 

print("Welcome\n")
while True:

    print("""Workout Options: \n Enter the number of the exercise you're interested in. When finished, enter "done".""")

    for index, workouts in enumerate(workout_options.values()):
        print(f"{index + 1}) {workouts.title()}")

    user_input = input("\nChoose workout: ")

    if str(user_input).lower() == 'done':
        break
    else:
        user_selected_workout.append(int(user_input))

    print("\n")

    
print("Workout")

for index, options in enumerate(user_selected_workout):
    print(f"{index + 1}) {workout_options[options].title()}")
# TODO when the output is shown, show the amount of time that exercise will be
# TODO add functionality to add the amount of time for each workout. Maybe make this into a dictionary because it might make things easier in the code below. 

print(f"\n{user_selected_workout}\n")
# print("\n\nBeginning workout")

# while True:
#     print(workout_options[user_workout])
#     time.sleep(3)

#     print(f"{workout_options[user_workout]} completed")
#     break
    
print("\n")