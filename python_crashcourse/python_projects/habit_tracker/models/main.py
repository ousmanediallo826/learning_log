from habit import *
from tracker import *
from storage import *

tracker = HabitTracker()



tracker = HabitTracker()

from tracker import HabitTracker
from habit import Habit
from storage import save_habits, load_habits

tracker = HabitTracker()

# load old habits
tracker.habit_list = load_habits()

while True:
    print("\n📊 Your Ultimate Habit Tracker 💪\n")
    add_habit = input("➕ Do you want to add a habit? (y/n): ")

    if add_habit.lower() == "y":
        name = input("📝 Habit name: ")
        category = input("📂 Habit category: ")
        frequency = input("⏱ Habit frequency: ")

        habit = Habit(name, frequency, category)
        tracker.add_habit(habit)
        save_habits(tracker)

        print(f"✅ Habit '{name}' saved successfully!")

    else:
        print("🙏 Thank you! See you tomorrow 🚀")
        break

print("\n📋 Your Habits:")
tracker.habit_lists()