import json
import os
from habit import Habit

DATA_DIR = './data'
FILE_PATH = os.path.join(DATA_DIR, 'habits.json')


def save_habits(tracker):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(FILE_PATH, 'w') as f:
        json.dump(
            tracker.habit_list,
            f,
            default=lambda obj: obj.to_dict(),
            indent=4
        )


def load_habits():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, 'r') as f:
        data = json.load(f)

    return [Habit.from_dict(h) for h in data]