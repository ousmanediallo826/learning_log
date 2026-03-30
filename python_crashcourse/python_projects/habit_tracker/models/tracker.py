from habit import *



class HabitTracker():

    def __init__(self):
        self.habit_list = []



    def add_habit(self, habit: Habit):
        if isinstance(habit, Habit):
            self.habit_list.append(habit)
            return f"Habit {habit.name} added successfully."
        else:
            return f"ERROR: only habit instances of type Habit can be added."

    def remove_habit(self, habit: Habit):
        if isinstance(habit, Habit):
            self.habit_list.remove(habit)
            return f"Habit {habit.name} removed successfully."
        else:
            return f"ERROR: only habit instances of type Habit can be removed."

    def find_habit(self, name):
        for habit in self.habit_list:
            if habit.name == name:
                return habit
        return f"ERROR: habit {name} not found."

    def habit_lists(self):
        for habit in self.habit_list:
            print(habit)
    def summary(self):
        for habit in self.habit_list:
            status = "completed" if habit.completed() else "not completed"
            print(f"{habit.name}: {status}")




