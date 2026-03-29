import uuid
import datetime

generated_habit = []

def generate_id():
    habit = f"HA{uuid.uuid4().hex[8].upper()}"
    if habit not in generated_habit:
        generated_habit.append(habit)
        print("Habit id generated")
        return habit
    else:
        print("Habit id already generated")
        return generate_id()

def timeStamp():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


id = generate_id()
print(id)
